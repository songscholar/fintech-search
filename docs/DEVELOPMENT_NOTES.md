# 开发心得

## 概述

本文档记录 USES Indexer 项目开发过程中的经验教训、技术决策和实践总结。

---

## 1. 解析层开发心得

### 1.1 DSL 解析的挑战

**问题**：UFT/USES DSL 不是标准编程语言，语法特殊。

**解决方案**：
- 先解析 XML 外壳
- 再解析 CDATA 中的 DSL 代码
- 最后提取结构化语句流

**经验**：
- 不要试图一次性完成完整解析，先产出扁平语句流
- 保留原始文本（`raw` 字段），便于后续处理
- 识别语法边界比精确解析更重要

### 1.2 语句流设计

```python
# 扁平语句流结构
class CodeStatement:
    kind: str          # action/call/control/assignment/raw
    line_start: int
    line_end: int
    raw: str           # 原始文本
    tag: str           # 子类型
    name: str          # 名称
    condition: str     # 条件
    target: str        # 目标
    reads_json: list   # 读取的变量
    writes_json: list  # 写入的变量
```

**经验**：
- 扁平结构比嵌套 AST 更容易处理
- 保留足够上下文，后续可以组装
- 字段设计要兼顾查询和存储

---

## 2. 索引层开发心得

### 2.1 SQLite 设计

**关键决策**：使用 WAL 模式提升并发性能

```python
SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;
"""
```

**经验**：
- 建表时考虑查询模式，按需建索引
- FTS5 和普通表分离，便于独立优化
- 向量数据单独存储，避免影响主查询

### 2.2 语义块切分

**原则**：
- 按控制流边界切分
- 保持语义完整
- 控制单块大小

```python
# 块切分策略
def split_into_chunks(statements):
    chunks = []
    current_chunk = []

    for stmt in statements:
        # 遇到控制流关键字或语句数过多时开启新块
        if is_control_flow_start(stmt) or len(current_chunk) > 50:
            if current_chunk:
                chunks.append(build_chunk(current_chunk))
            current_chunk = []

        current_chunk.append(stmt)

    return chunks
```

### 2.3 向量兼容性校验

**问题**：不同 embedding 模型产生的向量不兼容，混合使用会导致错误召回。

**解决方案**：

```python
def query_index(query, embedder):
    # 校验向量空间兼容性
    stored_config = get_vector_config(db)
    current_config = embedder.config

    if stored_config != current_config:
        # 自动降级，跳过向量召回
        disable_vector_retrieval()
        log_warning("Vector space mismatch, falling back to FTS only")
```

**经验**：
- 建库时记录向量配置元数据
- 查询时强制校验
- 不兼容时自动降级，而非报错

---

## 3. 检索层开发心得

### 3.1 混合检索策略

**设计**：

```python
def hybrid_retrieve(query, limit):
    # 1. FTS 精确召回
    fts_results = fts_search(query, limit * 2)

    # 2. 向量语义召回
    vector_results = vector_search(query, limit * 2)

    # 3. LIKE 兜底
    like_results = like_search(query, limit)

    # 4. 合并去重
    merged = merge_results(fts_results, vector_results, like_results)

    # 5. 重排序
    reranked = rerank(merged, query)

    return reranked[:limit]
```

**经验**：
- 多源召回比单一源更可靠
- 重排序是关键，能显著提升质量
- 向量召回是补充，不是替代

### 3.2 意图感知重排

**问题**：不同类型的问题需要不同的排序策略。

**解决方案**：

```python
def intent_aware_rerank(results, query):
    intent = detect_intent(query)  # table_read / table_write / call_chain / failure

    if intent == "table_write":
        # 提升 SQL 块、写表边的权重
        boost_by_type(results, ["writes_table", "sql_block"], 2.0)

    elif intent == "failure":
        # 提升异常处理块的权重
        boost_by_type(results, ["exception_block", "failure_handler"], 3.0)

    elif intent == "call_chain":
        # 提升调用链相关
        boost_by_type(results, ["calls_procedure", "incoming_callers"], 2.5)

    return results
```

**经验**：
- 简单规则比复杂 ML 模型更可控
- 意图识别不需要精确，模糊匹配即可
- 权重调优需要通过评测数据迭代

### 3.3 动态 SQL 恢复

**问题**：很多 SQL 是通过字符串变量动态拼接的。

**解决方案**：

```python
def recover_dynamic_sql(statements):
    # 追踪最近一次对 @sql_str 的赋值
    sql_vars = {}

    for stmt in statements:
        if is_assignment(stmt) and stmt.target.startswith("@sql"):
            sql_vars[stmt.target] = stmt.raw

        # 检查是否有 sprintf/hs_snprintf 调用
        if is_sprintf_call(stmt):
            reconstructed = reconstruct_sql(sql_vars, stmt)
            if reconstructed:
                stmt.alias_sql = reconstructed

    return statements
```

**经验**：
- 不需要 100% 恢复，70% 就有价值
- 启发式规则足够，无需完整数据流分析
- 优先处理常见模式

---

## 4. 评测层开发心得

### 4.1 评测框架设计

**核心指标**：

```python
class RetrievalEvaluator:
    def evaluate(self, db_path, cases):
        results = []

        for case in cases:
            hits = query_index(case.question, k=10)

            # pass@k：前 k 个结果是否命中期望项
            pass_at_k = compute_pass_at_k(hits, case.expected, k)

            # expectation_recall：期望项被召回的比例
            recall = compute_expectation_recall(hits, case.expected)

            results.append({
                "question": case.question,
                "pass_at_k": pass_at_k,
                "expectation_recall": recall,
                "first_relevant_rank": find_first_relevant(hits, case.expected)
            })

        return aggregate(results)
```

**经验**：
- pass@k 是最直观的指标
- expectation_recall 反映召回完整性
- 保留未命中的期望项，便于分析

### 4.2 A/B 测试

```python
def compare_eval(before_report, after_report):
    improvements = []
    regressions = []

    for case_id in before_report.cases:
        before = before_report[case_id]
        after = after_report[case_id]

        if after.score > before.score:
            improvements.append(case_id)
        elif after.score < before.score:
            regressions.append(case_id)

    return {
        "improved_count": len(improvements),
        "regressed_count": len(regressions),
        "improvements": improvements,
        "regressions": regressions
    }
```

**经验**：
- 评测必须可重复、可对比
- 保留 baseline，持续对比
- 关注 regression 比关注 improvement 更重要

---

## 5. 集成层开发心得

### 5.1 MCP 服务设计

**Stdio vs HTTP**：
- Stdio 更适合本地工具集成
- HTTP 更适合网络化服务

**工具暴露策略**：

```python
TOOLS = [
    {
        "name": "db_summary",
        "description": "获取数据库索引摘要",
        "handler": handle_db_summary
    },
    {
        "name": "query_codebase",
        "description": "语义检索代码库",
        "handler": handle_query
    },
    {
        "name": "assemble_evidence",
        "description": "组装证据上下文",
        "handler": handle_assemble_evidence
    },
    {
        "name": "ask_codebase",
        "description": "生成问答包",
        "handler": handle_ask
    },
    {
        "name": "answer_codebase",
        "description": "生成最终回答",
        "handler": handle_answer
    }
]
```

**经验**：
- 工具粒度要适中，太细则调用繁琐，太粗则不够灵活
- 每个工具都要有清晰的输入输出契约
- 错误处理要做好，工具不能随意崩溃

### 5.2 Codex 集成

**技能定义**：

```markdown
# SKILL.md

## 触发条件
- 用户询问代码相关问题
- 需要检索代码库

## 工具调用
- 优先使用 MCP 工具
- MCP 不可用时使用 HTTP API

## 输出格式
- 返回证据来源
- 返回文件路径和行号
- 标注不确定性
```

**经验**：
- 技能描述要清晰，明确何时触发
- 做好 fallback 策略
- 返回结果要可追溯

---

## 6. 性能优化心得

### 6.1 建库性能

**策略**：
- 分批提交事务
- 向量批量生成
- 断点续传支持

```python
def build_index(source_root, db_path, resume=False):
    if resume:
        # 跳过已有数据
        skip_existing(db_path)

    # 分批处理
    for batch in parse_files(source_root, batch_size=100):
        insert_batch(batch)

        # 每批提交，异常后可以从断点恢复
        conn.commit()
```

### 6.2 查询性能

**策略**：
- 索引优化
- 限制返回数量
- 向量缓存

```python
# 创建索引
CREATE INDEX IF NOT EXISTS idx_procedures_name ON procedures(name);
CREATE INDEX IF NOT EXISTS idx_edges_type ON edges(edge_type);
CREATE INDEX IF NOT EXISTS idx_chunks_type ON chunks(chunk_type);

# FTS 优化
CREATE VIRTUAL TABLE procedures_fts USING fts5(name, chinese_name, content=procedures);
```

---

## 7. 测试心得

### 7.1 测试策略

**单元测试**：
- 解析器输出结构
- 索引写入正确性
- 检索排序逻辑

**集成测试**：
- 端到端检索流程
- API 接口
- MCP 工具调用

```python
def test_build_index_creates_sqlite_tables():
    indexer = SQLiteIndexer()
    indexer.build_index(test_db, test_source)

    # 验证表存在
    tables = get_table_names(test_db)
    assert "files" in tables
    assert "procedures" in tables
    assert "chunks" in tables
```

**经验**：
- 核心逻辑必须有测试覆盖
- 集成测试验证完整链路
- 使用真实数据样本测试

---

## 8. 常见问题与解决方案

### 8.1 内存占用过高

**问题**：大文件集合建库时内存溢出

**解决**：
- 流式处理，边读边写
- 分批提交
- 及时释放大对象

### 8.2 向量召回质量差

**问题**：本地哈希向量召回效果不佳

**解决**：
- 切换到真实 embedding
- 调整切块策略
- 增强重排序权重

### 8.3 检索结果不相关

**问题**：语义检索召回无关结果

**解决**：
- 检查 embedding 维度是否一致
- 增强 FTS 权重
- 添加更多同义词到词典

---

## 9. 开发流程建议

1. **先跑通基本流程**：解析 -> 索引 -> 检索 -> 输出
2. **用小数据集验证**：避免在大数据集上反复调试
3. **建立评测闭环**：每次优化都用数据验证效果
4. **渐进式开发**：先实现核心功能，再逐步完善边缘情况
5. **保持代码简洁**：不过度设计，为未来重构留空间

---

## 10. 总结

| 阶段 | 核心经验 |
|-----|---------|
| 解析 | 扁平语句流优先，保留原始文本 |
| 索引 | 分批提交，兼容校验 |
| 检索 | 混合召回，意图重排 |
| 评测 | 量化指标，持续对比 |
| 集成 | 工具化，MCP 优先 |
| 性能 | 按需优化，渐进改进 |

**核心理念**：
- 简单优先，不过度设计
- 数据驱动，用评测指导优化
- 模块化设计，保留扩展空间
# USES Indexer

`uses-indexer` 是一个面向 USES/UFT DSL 代码库的本地索引器项目骨架。

当前阶段优先完成两件事：

1. 把 XML 外壳 + `CDATA` DSL 代码体稳定解析出来。
2. 把解析结果沉淀成可以继续扩展为索引的结构化数据。

这不是最终版索引器，而是整个项目的第一阶段基础设施。我们先保证“看得懂代码库”，再继续做“能高质量回答问题”。

## 当前已实现

- 解析 `LF / LS / AF / RS` 文件
- 提取文件级元数据
- 提取 `histories / inputParameters / outputParameters / internalParams`
- 提取代码体中的：
  - 注释
  - DSL 动作语句
  - 过程调用
  - `if / else if / else / while / switch`
  - `break / continue / goto`
  - 标签
  - 通用原始代码语句
- 抽取语句中的变量引用与简单写入变量
- 提供 CLI 入口，可对单文件或目录进行解析并输出 JSON
- 已在完整目录 `/Users/songzuoqiang/Documents/agent/code/uses_codes` 上完成一次全量扫描验证

## 当前验证结果

基于完整代码目录的当前扫描结果：

- 文件总数：`2564`
- `Function`：`1858`
- `Service`：`703`
- `FactorService`：`3`
- 语句统计：
  - `action`: `18140`
  - `call`: `8085`
  - `control`: `21326`
  - `assignment`: `16406`
  - `comment`: `33196`

完整扫描输出已保存到：

- [examples/uses_codes_summary.json](/Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_summary.json)

## 目录结构

```text
docs/
  ARCHITECTURE.md
  WORKLOG.md
examples/
src/uses_indexer/
  __init__.py
  __main__.py
  cli.py
  models.py
  parser.py
tests/
```

## 快速开始

安装：

```bash
cd /Users/songzuoqiang/Documents/agent/condex/codes
python3 -m pip install -e .
```

解析单文件：

```bash
python3 -m uses_indexer parse-file \
  /Users/songzuoqiang/Documents/agent/code/uses_codes/uftbusiness/customization/sesextmgt/LF_SESEXTMGR_BJSREALTIME_QRY.uftfunction
```

扫描目录并输出摘要：

```bash
python3 -m uses_indexer scan-dir \
  /Users/songzuoqiang/Documents/agent/code/uses_codes \
  --limit 20 \
  --output /Users/songzuoqiang/Documents/agent/condex/codes/examples/uses_codes_summary.json
```

## 下一步

- 增加更稳定的块级 AST
- 补齐事务块、异常块、SQL 块的配对关系
- 把解析结果写入 SQLite
- 增加调用关系、表访问关系、错误码关系索引
- 增加混合检索层

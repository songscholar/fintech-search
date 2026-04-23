# 索引内容不完整问题复盘

## 问题现象

在使用索引回答问题时，出现过两类“看起来不完整”的情况。

### 1. 表结构索引字段信息不完整

查询 `uses_entrust` 表结构时，索引可以返回：

- 表名
- 中文名
- object_id
- 表空间
- 字段名
- 索引字段

但字段的中文名、数据类型、字典类型大量为空。

这导致回答只能给出字段列表，无法说明：

- `fund_account` 是资产账户。
- `entrust_no` 是委托编号。
- `position_str` 的拼接规则。
- 字段对应的 `HsFundAccount / HsSerialNo / HsPosStr` 等类型。

### 2. 代码索引漏掉 `.uftatomservice`

检查代码索引构建完整性时发现：

- 当前代码库中存在 `.uftatomservice` 文件。
- `UftDslParser` 已经支持解析 `.uftatomservice`。
- `all` 模式会收集 `.uftatomservice`。
- 但 `code` 专用索引里 `.uftatomservice` 数量为 `0`。

最终确认 `code` 模式漏掉 `97` 个 `.uftatomservice` 文件。

## 问题分析

### 表结构索引分析

先只查索引库确认问题边界：

- `business_table_index.db` 中存在 `uses_entrust`。
- `uses_entrust` 有 `76` 个字段。
- `uses_entrust` 有 `10` 个索引。
- 但 `table_fields.chinese_name / data_type / dictionary_type` 为空。

这说明不是表结构文件没有入库，而是字段元数据补全没有生效。

继续检查构建入口：

- `build_indexes.py` 中 `stdfield_path` 指向 `upub_codes/uftstructure/stdfield.stdfield`。
- 实际标准字段文件在 `upub_codes/metadata/stdfield.stdfield`。

因此表结构索引只能从 `.uftstructure` 解析字段名，无法从标准字段文件补中文名、类型和字典。

### 代码索引分析

对代码收集规则做对账：

- `SUPPORTED_CODE_SUFFIXES` 包含 `.uftatomservice`。
- `UftDslParser.parse_path()` 支持 `.uftatomservice`。
- `_collect_files(index_type="code")` 内部硬编码了一份后缀列表。
- 这份硬编码列表漏掉了 `.uftatomservice`。

这说明 parser 和构建收集逻辑存在“双份后缀定义”，产生了同步缺口。

## 问题原因

两个问题本质都是“构建边界和解析能力没有统一成单一事实源”。

表结构索引的问题：

- 构建脚本中标准字段路径写错。
- 缺少对 `standard_field_count` 的 summary 记录。
- 缺少字段元数据覆盖率检查。
- 没有测试“未显式传 stdfield 时能自动发现 metadata/stdfield.stdfield”。

代码索引的问题：

- parser 支持的代码后缀和构建收集的代码后缀不是同一份定义。
- 新增 `.uftatomservice` 支持后，没有相应的构建覆盖测试。
- 当前 summary 只记录总文件数，之前没有检查每类后缀覆盖率。

## 解决方法

### 1. 表结构索引修复

修改内容：

- `build_indexes.py` 默认 `stdfield_path` 改为 `upub_codes/metadata/stdfield.stdfield`。
- `TableIndexer` 增加自动发现标准字段文件能力：
  - `source_root/stdfield.stdfield`
  - `source_root.parent/metadata/stdfield.stdfield`
  - 上级目录中的 `metadata/stdfield.stdfield`
- `TableField` 增加：
  - `description`
  - `public_type`
  - `comments`
- `table_fields` 表增加：
  - `description`
  - `public_type`
  - `comments`
- `table_fields_fts` 同步纳入这些字段。
- 新增 `tests/test_table_indexer.py`。

修复后验证：

- 表数量：`1204`
- 字段数量：`24672`
- 索引数量：`2542`
- 字段中文名覆盖：`24672 / 24672`
- 字段数据类型覆盖：`24672 / 24672`
- 字典类型覆盖：`5923 / 24672`

`uses_entrust` 可以只查索引得到：

- `fund_account`：资产账户 / `HsFundAccount` / `C18`
- `entrust_no`：委托编号 / `HsSerialNo` / `N10`
- `branch_no`：分支机构 / `HsBranchNo` / 字典 `100`
- `position_str`：定位串 / `HsPosStr` / `C100` / 拼接规则注释

### 2. 代码索引修复

修改内容：

- `_collect_files()` 的 `is_code_path()` 改为复用 `SUPPORTED_CODE_SUFFIXES`。
- 删除硬编码后缀列表。
- 新增 `test_code_index_includes_uft_atom_service_files`。
- 重建 `business_code_index.db`。

修复后验证：

- 代码索引文件数：`23895`
- `.uftatomservice` 文件数：`97`
- chunk 数：`201368`
- 向量数：`201368`
- procedure_features：`23895`

### 3. 元数据索引复核

元数据索引检查结论：

- 当前业务元数据文件数：`40`
- metadata statements：`55873`
- metadata chunks：`55873`
- metadata vectors：`55873`
- procedure_features：`40`

额外发现的 `30` 个 `.metadata/.plugins` XML 文件属于 Eclipse 工作区配置，不属于业务元数据，合理排除。

## 举一反三

### 1. 单一事实源

文件类型支持应只有一个来源：

- parser 支持什么，构建收集就应该复用什么。
- 不应在多个模块里重复硬编码后缀列表。

### 2. 构建 summary 要记录覆盖率

每类索引都应该在 summary 中记录可解释的覆盖指标：

- 代码索引：按后缀统计文件数。
- 元数据索引：按元数据文件类型统计。
- 表结构索引：字段中文名、类型、字典、注释覆盖率。

### 3. 索引查询优先，源码回退要克制

正常用户查询时应只查索引。

只有当问题是“索引为什么没查到”或“索引构建是否完整”时，才允许回退源码做诊断，并且要明确说明这是调试手段。

### 4. 新增文件类型必须有回归测试

以后新增一种文件后缀或元数据类型时，至少补三类测试：

- parser 能解析。
- build collect 能收集。
- db summary 能反映。

### 5. 重建后必须做数据库对账

每次修改构建边界后，不应只看构建成功，还要检查：

- 预期文件数。
- 实际入库文件数。
- 关键分类数量。
- chunks 与 vectors 是否一致。
- procedure_features 是否覆盖所有 procedure。

这些检查可以逐步沉淀成自动化健康检查命令。

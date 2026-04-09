# Architecture

## 目标

这个项目面向 `/Users/songzuoqiang/Documents/agent/code/uses_codes` 这样的 UFT/USES DSL 代码库。

第一阶段目标不是“直接问答”，而是先建立一个可靠的解析层，让后续索引和问答建立在结构化数据上。

## 当前阶段范围

第一版只做这些事情：

- 识别文件类型：`LF / LS / AF / RS`
- 解析 XML 元信息
- 解析 `CDATA` 中的 DSL 代码体
- 产出统一的 JSON 结构

第一版暂时不做这些事情：

- 完整编译器级 AST
- 精确块嵌套恢复
- SQLite 索引落库
- 向量检索
- RAG 问答

## 代码库观察结论

基于完整代码目录的抽样和统计，这个仓库有几个重要特点：

- 文件格式高度统一，属于稳定 DSL
- XML 壳固定，逻辑集中在 `CDATA`
- 业务层和 atom 层都使用同一套 DSL，只是厚薄不同
- DSL 与 C/C++ 风格原始语句混用
- 需要支持标签、跳转、SQL、异常块、事务块

## 文件模型

每个文件会先被解析成一个 `ParsedUnit`：

- `path`
- `unit_kind`
  - `Function`
  - `Service`
  - `FactorService`
- `prefix`
  - `LF`
  - `LS`
  - `AF`
  - `RS`
- `name`
- `chinese_name`
- `object_id`
- `attributes`
- `histories`
- `parameters`
- `statements`

## 语句模型

第一版不会强行恢复完整语法树，而是先产出“结构化扁平语句流”。

主要语句类型：

- `comment`
- `label`
- `brace`
- `action`
- `call`
- `control`
- `goto`
- `assignment`
- `raw`

其中：

- `action` 表示 `[获取记录]`、`[通用SQL执行]` 这类 DSL 动作
- `call` 表示 `[LF_xxx]`、`[AF_xxx]`、`[LS_xxx]`、`[RS_xxx]` 这类过程调用
- `control` 表示 `if / else if / else / while / switch / break / continue`

## 为什么先做扁平语句流

这样做有三个好处：

1. 实现快，能快速覆盖全仓库
2. 即使局部语法特殊，也能保留原文不丢信息
3. 后续可以在现有语句流基础上继续恢复块关系，而不需要推翻重做

## 下一阶段索引方向

当解析层稳定后，下一阶段会增加：

- `files`
- `procedures`
- `params`
- `histories`
- `actions`
- `db_access`
- `edges`
- `chunks`

重点关系：

- `LS -> LF`
- `LF -> AF`
- `procedure -> table`
- `procedure -> error code`
- `procedure -> config id`
- `procedure -> rpc/service`

## 文档策略

这个项目采用“边做边记”的方式：

- `README.md` 记录当前可用能力和使用方式
- `docs/ARCHITECTURE.md` 记录架构和设计取舍
- `docs/WORKLOG.md` 记录实施过程

说明文档不是最后补，而是和实现同步推进。

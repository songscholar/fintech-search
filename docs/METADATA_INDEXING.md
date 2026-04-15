# Metadata Indexing

## 目标

这份文档说明当前项目如何处理 `/metadata` 目录，以及这些元数据为什么必须和业务 DSL 代码一起索引。

在这套代码体系里，`metadata` 不是附属说明，而是很多业务语义的定义源：

- 标准字段
- 常量
- 错误号
- 系统宏 / 用户宏
- 主题域
- 缓存表
- 组件 / 组件字段
- 数据类型 / 默认值 / 数据字典
- 业务状态域 / 序列号 / 系统配置

如果只索引 UFT/USES 代码而不索引这些元数据，很多问题即使命中了代码，也无法解释清楚“这个名字到底是什么”。

## 当前覆盖

当前索引器会递归扫描完整根目录下所有 `metadata` 目录，并把其中的文件纳入索引。

当前已覆盖的典型文件包括：

- `stdfield.stdfield`
- `stdobj.xml`
- `datatype.datatype`
- `commondatatype.commondatatype`
- `defaultvalue.defaultvalue`
- `defaulttype.defaulttype`
- `dict.dict`
- `constant.constant`
- `errorno.errorno`
- `systemmacro.xml`
- `usermacro.xml`
- `topic.xml`
- `status.xml`
- `component.xml`
- `memoperation.xml`
- `sysconfig.sysconfig`
- `serialNumber.xml`
- `userContext.xml`
- `interfaceStruct.xml`
- `multicast.xml`
- `heterogeneouscomponent.xml`
- `wordChangeRule.xml`

## 条目级解析

当前不是把整个元数据文件当一段大文本塞进 FTS，而是把条目拆成 `metadata_item`。

典型条目包括：

- 一个宏定义
- 一个 topic 定义
- 一个常量定义
- 一个错误号定义
- 一个标准字段定义
- 一个缓存表定义
- 一个组件定义
- 一个组件字段
- 一个组件索引

这样做的直接收益是：

- 问“`手工打包头` 宏定义在哪里”时，能直接命中宏定义条目
- 问“`CNST_MC_UFT_OPTSYNC` 对应什么主题”时，能直接命中 topic 条目
- 问“`pbs_init_config` 缓存表怎么定义”时，能直接命中内存表条目

## 当前关系边

元数据条目除了进入 `statements / chunks / actions_fts` 以外，还会补充关系边，常见类型包括：

- `defines_macro`
- `defines_topic_alias`
- `defines_constant`
- `defines_error_code`
- `defines_standard_field`
- `defines_component`
- `defines_memory_table`
- `maps_topic_name`
- `maps_db_table`
- `maps_sync_table`
- `maps_error_number`
- `contains_field`
- `contains_index`
- `references_constant`
- `references_component`
- `references_datatype`
- `references_topic_name`

这些关系的作用不是做“漂亮图谱”，而是为了让检索后的证据更可解释。

## 典型增强场景

### 宏定义解释

例如代码里常见：

- `[手工打包头]`
- `[查询缓存表]`
- `[通用SQL执行]`

如果没有元数据索引，系统只能知道“代码里用了这个名字”。

接入 `systemmacro.xml / usermacro.xml` 之后，系统还可以回答：

- 宏定义在哪个文件
- 宏模板内容是什么
- 宏内部又引用了哪些动作或其他宏

### Topic 解释

例如代码里：

- `[消息发布][topic_name = CNST_MC_UFT_OPTSYNC]`

接入 `topic.xml` 之后，系统不仅知道“发布了 `CNST_MC_UFT_OPTSYNC`”，还可以继续解释：

- 它映射到哪个真实 topic
- topic 的过滤字段有哪些

### 缓存表解释

例如代码里：

- `[查询缓存表]`
- `[获取记录][upbs_arg(...)]`

接入 `memoperation.xml` 之后，系统可以进一步回答：

- 这个缓存表对应哪个物理表
- 同步表是谁
- 索引字段是什么

## 当前边界

当前已经做到“全 metadata 文件纳入索引”和“条目级检索 + 关系边补充”，但还没有做到：

- 把每一种 metadata 都做成完全定制化的图数据库模型
- 对所有宏内容做完整 DSL 级二次编译
- 自动识别消息中心消费端订阅关系

也就是说，当前阶段已经能很好支撑检索和问答，但后面仍然可以继续增强语义深度。

# upbs_umtconfig - 内存交易参数表

**表对象ID**: 53
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | partition_no | 否 |  |  |
| 2 | partition_name | 否 |  |  |
| 3 | umt_node_status | 否 |  |  |
| 4 | sysnode_id | 否 |  |  |
| 5 | sysnode_version | 否 |  |  |
| 6 | umt_partition_status | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | transaction_str | 否 |  |  |
| 9 | partition_no | 否 |  |  |
| 10 | partition_name | 否 |  |  |
| 11 | umt_node_status | 否 |  |  |
| 12 | sysnode_id | 否 |  |  |
| 13 | sysnode_version | 否 |  |  |
| 14 | umt_partition_status | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | transaction_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_umtconfig | ART | 是 | partition_no, partition_no |
| idx_upbs_umtconfig | ART | 是 | partition_no, partition_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_umtconfig | partition_no, partition_no |
| idx_upbs_umtconfig | partition_no, partition_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-06-13 14:58:13 | 3.0.6.1008 | 汪迎 | 物理表upbs_umtconfig，添加了表字段(transaction_str);
 |
| 2023-09-19 10:51:21 | V3.0.1.8 | 沈勋 | 物理表upbs_umtconfig，添加了表字段(umt_partition_status);
物理表upbs_umt... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-29 21:01 | 0.3.3.118 | 程猛 | umt_core_status调整为umt_node_status |
| 2023-09-18 16:17:31 | 0.3.3.110 | 程猛 | 物理表upbs_umtconfig，添加了表字段(umt_core_status);
 |
| 2023-09-18 16:17:18 | 0.3.3.110 | 程猛 | 物理表upbs_umtconfig，删除了表字段(umt_partition_status);
 |
| 2023-06-27 11:06 | 0.3.3.110 | 程猛 | upbs_umtconfig表字段umt_partition_status调整为umt_core_status（对应新增... |
| 2023-05-19 15:32 | 0.0.0.2 | 汪林 | 新增表upbs_umtconfig |
| 2025-06-13 14:58:13 | 3.0.6.1008 | 汪迎 | 物理表upbs_umtconfig，添加了表字段(transaction_str);
 |
| 2023-09-19 10:51:21 | V3.0.1.8 | 沈勋 | 物理表upbs_umtconfig，添加了表字段(umt_partition_status);
物理表upbs_umt... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-29 21:01 | 0.3.3.118 | 程猛 | umt_core_status调整为umt_node_status |
| 2023-09-18 16:17:31 | 0.3.3.110 | 程猛 | 物理表upbs_umtconfig，添加了表字段(umt_core_status);
 |
| 2023-09-18 16:17:18 | 0.3.3.110 | 程猛 | 物理表upbs_umtconfig，删除了表字段(umt_partition_status);
 |
| 2023-06-27 11:06 | 0.3.3.110 | 程猛 | upbs_umtconfig表字段umt_partition_status调整为umt_core_status（对应新增... |

> 共 16 条修改记录，仅显示最近15条

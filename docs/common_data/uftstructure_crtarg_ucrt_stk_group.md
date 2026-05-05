# ucrt_stk_group - 证券分组表

**表对象ID**: 7028
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stockgroup_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | remove_stockgroup_no_str | 否 |  |  |
| 6 | registration_flag | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | stockgroup_name | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | position_str | 否 |  | stock_code(8)+exchange_type(4)+stockgroup_no(10)+stock_type( |
| 13 | stockgroup_no | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | stock_type | 否 |  |  |
| 17 | remove_stockgroup_no_str | 否 |  |  |
| 18 | registration_flag | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | stockgroup_name | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | stock_code(8)+exchange_type(4)+stockgroup_no(10)+stock_type( |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stk_group_no | 默认 | 否 | stockgroup_no, stockgroup_no |
| idx_ucrt_stk_group_no | ART | 是 | stockgroup_no, stockgroup_no |
| idx_ucrt_stk_group_code | ART | 是 | stock_code, exchange_type, stock_type, stock_code, exchange_type, stock_type |
| idx_ucrt_stk_group | ART | 是 | stock_code, exchange_type, stockgroup_no, stock_type, stock_code, exchange_type, stockgroup_no, stock_type |
| idx_ucrt_stk_group_type | ART | 是 | stock_type, stock_type |
| idx_ucrt_stk_group_no | 默认 | 否 | stockgroup_no, stockgroup_no |
| idx_ucrt_stk_group_no | ART | 是 | stockgroup_no, stockgroup_no |
| idx_ucrt_stk_group_code | ART | 是 | stock_code, exchange_type, stock_type, stock_code, exchange_type, stock_type |
| idx_ucrt_stk_group | ART | 是 | stock_code, exchange_type, stockgroup_no, stock_type, stock_code, exchange_type, stockgroup_no, stock_type |
| idx_ucrt_stk_group_type | ART | 是 | stock_type, stock_type |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stk_group | stock_code, exchange_type, stockgroup_no, stock_type, stock_code, exchange_type, stockgroup_no, stock_type |
| idx_ucrt_stk_group_no | stockgroup_no, stockgroup_no |
| idx_ucrt_stk_group | stock_code, exchange_type, stockgroup_no, stock_type, stock_code, exchange_type, stockgroup_no, stock_type |
| idx_ucrt_stk_group_no | stockgroup_no, stockgroup_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-17 10:23:42 | 3.0.6.116 | 常行 | 物理表ucrt_stk_group，增加索引(idx_ucrt_stk_group_no:[stockgroup_no]... |
| 2025-02-18 10:49:11 | 3.0.6.74 | 李想 | 物理表ucrt_stk_group，添加了表字段(remark);
物理表ucrt_stk_group，添加了表字段(... |
| 2025-02-11 15:28:16 | 3.0.6.35 | 许琮擎 | 增加索引 |
| 2025-03-10 20:54:51 | V3.0.2.18 | 全春辉 | 增加索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-07-05 09:43 | 0.3.3.123 | 程猛 | ucrt_stk_group、ucrt_stk_group_concentrate取消N:N的关联关系 |
| 2023-06-30 09:06 | 0.3.3.119 | 吴威 | 删除删除索引 |
| 2023-06-29 20:44 | 0.3.3.117 | 程猛 | idx_ucrt_stk_group_code调整为全局非唯一索引 |
| 2023-06-29 20:35 | 0.3.3.116 | 吴威 | 新增删除索引 |
| 2023-06-23 15:19 | 0.3.3.109 | 董瑞辉 | 新增表字段stockgroup_name |
| 2023-06-13 15:21 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |
| 2025-07-17 10:23:42 | 3.0.6.116 | 常行 | 物理表ucrt_stk_group，增加索引(idx_ucrt_stk_group_no:[stockgroup_no]... |
| 2025-02-18 10:49:11 | 3.0.6.74 | 李想 | 物理表ucrt_stk_group，添加了表字段(remark);
物理表ucrt_stk_group，添加了表字段(... |
| 2025-02-11 15:28:16 | 3.0.6.35 | 许琮擎 | 增加索引 |
| 2025-03-10 20:54:51 | V3.0.2.18 | 全春辉 | 增加索引 |

> 共 22 条修改记录，仅显示最近15条

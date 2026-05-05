# ucrt_split_compact - 合约拆分表

**表对象ID**: 7517
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | compact_id | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_microtime | 否 |  |  |
| 4 | op_branch_no | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_entrust_way | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | repaid_date | 否 |  |  |
| 9 | prev_end_date | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | position_str | 否 |  | curr_date(8)+partition_no(2)+curr_microtime(9)+branch_no(5)+ |
| 13 | compact_id | 否 |  |  |
| 14 | curr_date | 否 |  |  |
| 15 | curr_microtime | 否 |  |  |
| 16 | op_branch_no | 否 |  |  |
| 17 | operator_no | 否 |  |  |
| 18 | op_entrust_way | 否 |  |  |
| 19 | op_station | 否 |  |  |
| 20 | repaid_date | 否 |  |  |
| 21 | prev_end_date | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | fund_account | 否 |  |  |
| 24 | position_str | 否 |  | curr_date(8)+partition_no(2)+curr_microtime(9)+branch_no(5)+ |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_split_compact | ART | 是 | compact_id, compact_id |
| idx_ucrt_split_compact | ART | 是 | compact_id, compact_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_split_compact | compact_id, compact_id |
| idx_ucrt_split_compact | compact_id, compact_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-16 17:04:15 | 3.0.6.1065 | 周兆军 | 所有表ucrt_share，添加了表字段(position_str);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

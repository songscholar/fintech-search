# stkrestrict - 证券限制控制表2

**表对象ID**: 5590
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | entrust_bs | 否 |  |  |
| 6 | client_group | 否 |  |  |
| 7 | room_code | 否 |  |  |
| 8 | res_entrust_way | 否 |  |  |
| 9 | res_entrust_type | 否 |  |  |
| 10 | res_entrust_prop | 否 |  |  |
| 11 | begin_date | 否 |  |  |
| 12 | end_date | 否 |  |  |
| 13 | organ_flag | 否 |  |  |
| 14 | res_sub_stock_type | 否 |  |  |
| 15 | ordinal | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_type(4)+stock_code(6)+en |
| 20 | remark | 否 |  |  |
| 21 | restrict_str | 否 |  |  |
| 22 | branch_no | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_type | 否 |  |  |
| 25 | stock_code | 否 |  |  |
| 26 | entrust_bs | 否 |  |  |
| 27 | client_group | 否 |  |  |
| 28 | room_code | 否 |  |  |
| 29 | res_entrust_way | 否 |  |  |
| 30 | res_entrust_type | 否 |  |  |
| 31 | res_entrust_prop | 否 |  |  |
| 32 | begin_date | 否 |  |  |
| 33 | end_date | 否 |  |  |
| 34 | organ_flag | 否 |  |  |
| 35 | res_sub_stock_type | 否 |  |  |
| 36 | ordinal | 否 |  |  |
| 37 | update_date | 否 |  |  |
| 38 | update_time | 否 |  |  |
| 39 | transaction_no | 否 |  |  |
| 40 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_type(4)+stock_code(6)+en |
| 41 | remark | 否 |  |  |
| 42 | restrict_str | 否 |  |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stkrestrict | 默认 | 否 |  |
| idx_stkrestrict | 默认 | 否 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal |
| idx_stkrestrict | 默认 | 否 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, fund_account, branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, fund_account |
| idx_stkrestrict_pos | ART | 是 | position_str, position_str |
| idx_stkrestrict | ART | 是 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal |
| uk_rpt_stkrestrict | ART | 是 | end_date, position_str, end_date, position_str |
| idx_stkrestrict | 默认 | 否 |  |
| idx_stkrestrict | 默认 | 否 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal |
| idx_stkrestrict | 默认 | 否 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, fund_account, branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, fund_account |
| idx_stkrestrict_pos | ART | 是 | position_str, position_str |
| idx_stkrestrict | ART | 是 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal |
| uk_rpt_stkrestrict | ART | 是 | end_date, position_str, end_date, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_stkrestrict_pos | position_str, position_str |
| idx_stkrestrict | branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal |
| idx_stkrestrict_pos | position_str, position_str |
| idx_stkrestrict | branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, room_code, client_group, ordinal |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:34:49 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.1021 | 周兆军 | 维护历史表 |
| 2025-08-12 10:55:49 | 3.0.2.75 | 高志强 | 修改position_str注释与代码逻辑一致 |
| 2025-07-26 11:55:17 | 3.0.6.1005 |  | 所有表stkrestrict，删除了表字段（fund_account）；
所有表stkrestrict，删除了表字段（... |
| 2025-07-26 11:54:41 | 3.0.6.1004 |  |  |
| 2025-07-26 11:54:10 | 3.0.6.1003 |  |  |
| 2025-07-17 15:35:03 | 3.0.6.1002 | 常行 | 物理表stkrestrict，增加索引(idx_stkrestrict:[branch_no,exchange_type... |
| 2025-02-14 14:19:42 | 3.0.6.7 | 常行 | 新增表stkrestrict |
| 2026-03-09 14:34:49 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.6.1021 | 周兆军 | 维护历史表 |
| 2025-08-12 10:55:49 | 3.0.2.75 | 高志强 | 修改position_str注释与代码逻辑一致 |
| 2025-07-26 11:55:17 | 3.0.6.1005 |  | 所有表stkrestrict，删除了表字段（fund_account）；
所有表stkrestrict，删除了表字段（... |
| 2025-07-26 11:54:41 | 3.0.6.1004 |  |  |
| 2025-07-26 11:54:10 | 3.0.6.1003 |  |  |
| 2025-07-17 15:35:03 | 3.0.6.1002 | 常行 | 物理表stkrestrict，增加索引(idx_stkrestrict:[branch_no,exchange_type... |

> 共 16 条修改记录，仅显示最近15条

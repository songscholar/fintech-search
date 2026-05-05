# uses_stkrestrict - 证券限制控制表

**表对象ID**: 5517
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 44 个）

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
| 16 | transaction_no | 否 |  |  |
| 17 | position_str | 否 |  |  |
| 18 | restrict_str | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | stock_name | 否 | H |  |
| 22 | sub_stock_type | 否 | H |  |
| 23 | branch_no | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | stock_type | 否 |  |  |
| 26 | stock_code | 否 |  |  |
| 27 | entrust_bs | 否 |  |  |
| 28 | client_group | 否 |  |  |
| 29 | room_code | 否 |  |  |
| 30 | res_entrust_way | 否 |  |  |
| 31 | res_entrust_type | 否 |  |  |
| 32 | res_entrust_prop | 否 |  |  |
| 33 | begin_date | 否 |  |  |
| 34 | end_date | 否 |  |  |
| 35 | organ_flag | 否 |  |  |
| 36 | res_sub_stock_type | 否 |  |  |
| 37 | ordinal | 否 |  |  |
| 38 | transaction_no | 否 |  |  |
| 39 | position_str | 否 |  |  |
| 40 | restrict_str | 否 |  |  |
| 41 | update_date | 否 |  |  |
| 42 | update_time | 否 |  |  |
| 43 | stock_name | 否 | H |  |
| 44 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_stkrestrictctrl_pos | 默认 | 否 |  |
| idx_uses_stkrestrict_type | ART | 是 | exchange_type, exchange_type |
| idx_uses_stkrestrict | ART | 是 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal |
| idx_uses_stkrestrictctrl_pos | ART | 是 | position_str, position_str |
| uk_rpt_usesstkrestrict | ART | 是 | end_date, position_str, end_date, position_str |
| idx_uses_stkrestrictctrl_pos | 默认 | 否 |  |
| idx_uses_stkrestrict_type | ART | 是 | exchange_type, exchange_type |
| idx_uses_stkrestrict | ART | 是 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal |
| idx_uses_stkrestrictctrl_pos | ART | 是 | position_str, position_str |
| uk_rpt_usesstkrestrict | ART | 是 | end_date, position_str, end_date, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_stkrestrict | branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal |
| idx_uses_stkrestrictctrl_pos | position_str, position_str |
| idx_uses_stkrestrict | branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal |
| idx_uses_stkrestrictctrl_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:43:02 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-21 09:59:09 | 3.0.2.72 | 杨涛 | 物理表uses_stkrestrict，添加了表字段(update_date);
物理表uses_stkrestric... |
| 2025-05-21 11:16:06 | 3.0.2.68 | 於达 | 物理表uses_stkrestrict，添加了表字段(restrict_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2024-10-17 09:56:13 | 3.0.5.1051 | 洪略 | 表字段position_str;新增idx_uses_stkrestrictctrl_pos索引;idx_uses_st... |
| 2024-05-20 15:08:10 | 3.0.2.10 | 范文浩 | 勾选不回库 |
| 2024-04-24 10:43:23 | 3.0.2.3 | 阮善宏 | 物理表uses_stkrestrict，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 13:43:02 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-21 09:59:09 | 3.0.2.72 | 杨涛 | 物理表uses_stkrestrict，添加了表字段(update_date);
物理表uses_stkrestric... |
| 2025-05-21 11:16:06 | 3.0.2.68 | 於达 | 物理表uses_stkrestrict，添加了表字段(restrict_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2024-10-17 09:56:13 | 3.0.5.1051 | 洪略 | 表字段position_str;新增idx_uses_stkrestrictctrl_pos索引;idx_uses_st... |

> 共 18 条修改记录，仅显示最近15条

# ucrt_stkrestrict - 融资融券证券限制控制表

**表对象ID**: 7006
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 34 个）

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
| 17 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_type(4)+stock_code(6)+en |
| 18 | branch_no | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_type | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | entrust_bs | 否 |  |  |
| 23 | client_group | 否 |  |  |
| 24 | room_code | 否 |  |  |
| 25 | res_entrust_way | 否 |  |  |
| 26 | res_entrust_type | 否 |  |  |
| 27 | res_entrust_prop | 否 |  |  |
| 28 | begin_date | 否 |  |  |
| 29 | end_date | 否 |  |  |
| 30 | organ_flag | 否 |  |  |
| 31 | res_sub_stock_type | 否 |  |  |
| 32 | ordinal | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_type(4)+stock_code(6)+en |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stkrestrictctrl_pos | 默认 | 否 | position_str, position_str |
| idx_ucrt_stkrestrict | 默认 | 否 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal |
| idx_ucrt_stkrestrict | ART | 是 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal |
| idx_ucrt_stkrestrictctrl_pos | ART | 是 | position_str, position_str |
| idx_ucrt_stkrestrictctrl_pos | 默认 | 否 | position_str, position_str |
| idx_ucrt_stkrestrict | 默认 | 否 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal |
| idx_ucrt_stkrestrict | ART | 是 | branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal |
| idx_ucrt_stkrestrictctrl_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stkrestrict | branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal |
| idx_ucrt_stkrestrictctrl_pos | position_str, position_str |
| idx_ucrt_stkrestrict | branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal, branch_no, exchange_type, stock_type, stock_code, entrust_bs, client_group, room_code, organ_flag, ordinal |
| idx_ucrt_stkrestrictctrl_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-10-21 18:56:52 | 3.0.6.11 | 卢杰 | 新增表字段position_str;新增idx_ucrt_stkrestrictctrl_pos索引;idx_ucrt_... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:22 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |
| 2024-10-21 18:56:52 | 3.0.6.11 | 卢杰 | 新增表字段position_str;新增idx_ucrt_stkrestrictctrl_pos索引;idx_ucrt_... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:22 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no |

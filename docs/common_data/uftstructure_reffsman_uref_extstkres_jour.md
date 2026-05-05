# uref_extstkres_jour - 转融通外部券源流水表

**表对象ID**: 6202
**所属模块**: reffsman
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | business_flag | 否 |  |  |
| 10 | refextstkres_id | 否 |  |  |
| 11 | refextstkres_type | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | seat_no | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_name | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | occur_amount | 否 |  |  |
| 18 | post_amount | 否 |  |  |
| 19 | end_date | 否 |  |  |
| 20 | refapply_id | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | stock_type | 否 | H |  |
| 24 | sub_stock_type | 否 | H |  |
| 25 | init_date | 否 |  |  |
| 26 | serial_no | 否 |  |  |
| 27 | curr_date | 否 |  |  |
| 28 | curr_time | 否 |  |  |
| 29 | operator_no | 否 |  |  |
| 30 | op_branch_no | 否 |  |  |
| 31 | op_entrust_way | 否 |  |  |
| 32 | op_station | 否 |  |  |
| 33 | business_flag | 否 |  |  |
| 34 | refextstkres_id | 否 |  |  |
| 35 | refextstkres_type | 否 |  |  |
| 36 | stock_account | 否 |  |  |
| 37 | seat_no | 否 |  |  |
| 38 | stock_code | 否 |  |  |
| 39 | stock_name | 否 |  |  |
| 40 | exchange_type | 否 |  |  |
| 41 | occur_amount | 否 |  |  |
| 42 | post_amount | 否 |  |  |
| 43 | end_date | 否 |  |  |
| 44 | refapply_id | 否 |  |  |
| 45 | remark | 否 |  |  |
| 46 | position_str | 否 |  |  |
| 47 | stock_type | 否 | H |  |
| 48 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refextstkresjour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refextstkresjour_acct | ART | 是 | stock_account, stock_code, stock_account, stock_code |
| idx_refextstkresjour_pos | ART | 是 | position_str, position_str |
| idx_refextstkresjour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_refextstkresjour_acct | ART | 是 | stock_account, stock_code, stock_account, stock_code |
| idx_refextstkresjour_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 10 个）

| 索引名 | 字段 |
|--------|------|
| idx_refextstkresjour | init_date, serial_no, init_date, serial_no |
| idx_refextstkresjour_acct | stock_account, stock_code, stock_account, stock_code |
| idx_refextstkresjour_pos | position_str, position_str |
| uk_rpt_urefextstkresjour | init_date, position_str, init_date, position_str |
| idx_rpt_urefextstkresjour_acct | stock_account, position_str, stock_account, position_str |
| idx_refextstkresjour | init_date, serial_no, init_date, serial_no |
| idx_refextstkresjour_acct | stock_account, stock_code, stock_account, stock_code |
| idx_refextstkresjour_pos | position_str, position_str |
| uk_rpt_urefextstkresjour | init_date, position_str, init_date, position_str |
| idx_rpt_urefextstkresjour_acct | stock_account, position_str, stock_account, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-16 10:33:49 | V3.0.2.1 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 10:33:49 | V3.0.2.1 | 廖宏玮 | 增加历史表索引与字段 |

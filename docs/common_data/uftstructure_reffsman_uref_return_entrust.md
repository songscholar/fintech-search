# uref_return_entrust - 转融通还券划转委托表

**表对象ID**: 6200
**所属模块**: reffsman
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 92 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_milltime | 否 |  |  |
| 4 | op_branch_no | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_entrust_way | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | ref_type | 否 |  |  |
| 9 | reftransfer_type | 否 |  |  |
| 10 | compact_id | 否 |  |  |
| 11 | csfc_compact_id | 否 |  |  |
| 12 | settlement_account | 否 |  |  |
| 13 | stock_account_src | 否 |  |  |
| 14 | seat_no_src | 否 |  |  |
| 15 | stock_account_dest | 否 |  |  |
| 16 | seat_no_dest | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | entrust_amount | 否 |  |  |
| 20 | entrust_price | 否 |  |  |
| 21 | payer_bank_no | 否 |  |  |
| 22 | shdc_payer_account | 否 |  |  |
| 23 | oppo_bank_no | 否 |  |  |
| 24 | shdc_oppo_account | 否 |  |  |
| 25 | shdc_password | 否 |  |  |
| 26 | shdc_business_no | 否 |  |  |
| 27 | accept_date | 否 |  |  |
| 28 | accept_time | 否 |  |  |
| 29 | entrust_balance | 否 |  |  |
| 30 | return_code | 否 |  |  |
| 31 | return_info | 否 |  |  |
| 32 | remark | 否 |  |  |
| 33 | position_str | 否 |  |  |
| 34 | report_no | 否 |  |  |
| 35 | entrust_no | 否 |  |  |
| 36 | entrust_status | 否 |  |  |
| 37 | entrust_type | 否 |  |  |
| 38 | record_no | 否 |  |  |
| 39 | trade_date | 否 |  |  |
| 40 | return_serial_no | 否 |  |  |
| 41 | company_no | 否 |  |  |
| 42 | csfc_borrow_accttype | 否 |  |  |
| 43 | json_data | 否 |  |  |
| 44 | stock_name | 否 | H |  |
| 45 | stock_type | 否 | H |  |
| 46 | sub_stock_type | 否 | H |  |
| 47 | init_date | 否 |  |  |
| 48 | curr_date | 否 |  |  |
| 49 | curr_milltime | 否 |  |  |
| 50 | op_branch_no | 否 |  |  |
| 51 | operator_no | 否 |  |  |
| 52 | op_entrust_way | 否 |  |  |
| 53 | op_station | 否 |  |  |
| 54 | ref_type | 否 |  |  |
| 55 | reftransfer_type | 否 |  |  |
| 56 | compact_id | 否 |  |  |
| 57 | csfc_compact_id | 否 |  |  |
| 58 | settlement_account | 否 |  |  |
| 59 | stock_account_src | 否 |  |  |
| 60 | seat_no_src | 否 |  |  |
| 61 | stock_account_dest | 否 |  |  |
| 62 | seat_no_dest | 否 |  |  |
| 63 | exchange_type | 否 |  |  |
| 64 | stock_code | 否 |  |  |
| 65 | entrust_amount | 否 |  |  |
| 66 | entrust_price | 否 |  |  |
| 67 | payer_bank_no | 否 |  |  |
| 68 | shdc_payer_account | 否 |  |  |
| 69 | oppo_bank_no | 否 |  |  |
| 70 | shdc_oppo_account | 否 |  |  |
| 71 | shdc_password | 否 |  |  |
| 72 | shdc_business_no | 否 |  |  |
| 73 | accept_date | 否 |  |  |
| 74 | accept_time | 否 |  |  |
| 75 | entrust_balance | 否 |  |  |
| 76 | return_code | 否 |  |  |
| 77 | return_info | 否 |  |  |
| 78 | remark | 否 |  |  |
| 79 | position_str | 否 |  |  |
| 80 | report_no | 否 |  |  |
| 81 | entrust_no | 否 |  |  |
| 82 | entrust_status | 否 |  |  |
| 83 | entrust_type | 否 |  |  |
| 84 | record_no | 否 |  |  |
| 85 | trade_date | 否 |  |  |
| 86 | return_serial_no | 否 |  |  |
| 87 | company_no | 否 |  |  |
| 88 | csfc_borrow_accttype | 否 |  |  |
| 89 | json_data | 否 |  |  |
| 90 | stock_name | 否 | H |  |
| 91 | stock_type | 否 | H |  |
| 92 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refrtentrust | ART | 是 | init_date, entrust_no, init_date, entrust_no |
| idx_refrtentrust_pos | ART | 是 | position_str, position_str |
| idx_entrust_status | ART | 是 | entrust_status, entrust_status |
| idx_refrtentrust_polling | ART | 是 | exchange_type, exchange_type |
| idx_refrtentrust | ART | 是 | init_date, entrust_no, init_date, entrust_no |
| idx_refrtentrust_pos | ART | 是 | position_str, position_str |
| idx_entrust_status | ART | 是 | entrust_status, entrust_status |
| idx_refrtentrust_polling | ART | 是 | exchange_type, exchange_type |

## 数据库索引（共 8 个）

| 索引名 | 字段 |
|--------|------|
| idx_refrtentrust | init_date, entrust_no, init_date, entrust_no |
| idx_refrtentrust_pos | position_str, position_str |
| idx_entrust_status | entrust_status, entrust_status |
| uk_rpt_urefreturnentrust_pos | init_date, position_str, init_date, position_str |
| idx_refrtentrust | init_date, entrust_no, init_date, entrust_no |
| idx_refrtentrust_pos | position_str, position_str |
| idx_entrust_status | entrust_status, entrust_status |
| uk_rpt_urefreturnentrust_pos | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-04 14:56:17 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 14:03:36 | V3.0.2.1 | 廖宏玮 | 所有表uref_return_entrust，添加了表字段(json_data);
 |
| 2025-11-04 14:56:17 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-10-16 14:03:36 | V3.0.2.1 | 廖宏玮 | 所有表uref_return_entrust，添加了表字段(json_data);
 |

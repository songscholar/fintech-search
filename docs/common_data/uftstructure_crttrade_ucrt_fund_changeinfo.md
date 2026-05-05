# ucrt_fund_changeinfo - 交易资金变更信息表

**表对象ID**: 7552
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 96 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | serial_no | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | frozen_balance | 否 |  |  |
| 6 | unfrozen_balance | 否 |  |  |
| 7 | current_balance | 否 |  |  |
| 8 | correct_balance | 否 |  |  |
| 9 | cancel_serial_no | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | business_flag | 否 |  |  |
| 12 | op_branch_no | 否 |  |  |
| 13 | operator_no | 否 |  |  |
| 14 | op_station | 否 |  |  |
| 15 | op_entrust_way | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | cash_balance | 是 |  |  |
| 18 | check_balance | 是 |  |  |
| 19 | foregift_balance | 是 |  |  |
| 20 | mortgage_balance | 是 |  |  |
| 21 | curr_date | 是 |  |  |
| 22 | curr_time | 是 |  |  |
| 23 | post_balance | 是 |  |  |
| 24 | bk_serial_no | 是 |  |  |
| 25 | frozen_kind | 是 |  |  |
| 26 | rate_kind | 是 |  |  |
| 27 | begin_balance | 是 |  |  |
| 28 | integral_balance | 是 |  |  |
| 29 | fine_integral | 是 |  |  |
| 30 | interest | 是 |  |  |
| 31 | interest_tax | 是 |  |  |
| 32 | integral_update | 是 |  |  |
| 33 | integral_flag | 是 |  |  |
| 34 | real_status | 是 |  |  |
| 35 | join_date | 否 |  |  |
| 36 | join_serial_no | 否 |  |  |
| 37 | client_id | 否 | H |  |
| 38 | client_name | 否 | H |  |
| 39 | branch_no | 否 | H |  |
| 40 | client_group | 否 | H |  |
| 41 | asset_prop | 否 | H |  |
| 42 | limit_flag | 否 | H |  |
| 43 | client_prop | 否 | H |  |
| 44 | asset_level | 否 | H |  |
| 45 | risk_level | 否 | H |  |
| 46 | corp_risk_level | 否 | H |  |
| 47 | room_code | 否 | H |  |
| 48 | corp_client_group | 否 | H |  |
| 49 | init_date | 否 |  |  |
| 50 | fund_account | 否 |  |  |
| 51 | serial_no | 否 |  |  |
| 52 | money_type | 否 |  |  |
| 53 | frozen_balance | 否 |  |  |
| 54 | unfrozen_balance | 否 |  |  |
| 55 | current_balance | 否 |  |  |
| 56 | correct_balance | 否 |  |  |
| 57 | cancel_serial_no | 否 |  |  |
| 58 | exchange_type | 否 |  |  |
| 59 | business_flag | 否 |  |  |
| 60 | op_branch_no | 否 |  |  |
| 61 | operator_no | 否 |  |  |
| 62 | op_station | 否 |  |  |
| 63 | op_entrust_way | 否 |  |  |
| 64 | remark | 否 |  |  |
| 65 | cash_balance | 是 |  |  |
| 66 | check_balance | 是 |  |  |
| 67 | foregift_balance | 是 |  |  |
| 68 | mortgage_balance | 是 |  |  |
| 69 | curr_date | 是 |  |  |
| 70 | curr_time | 是 |  |  |
| 71 | post_balance | 是 |  |  |
| 72 | bk_serial_no | 是 |  |  |
| 73 | frozen_kind | 是 |  |  |
| 74 | rate_kind | 是 |  |  |
| 75 | begin_balance | 是 |  |  |
| 76 | integral_balance | 是 |  |  |
| 77 | fine_integral | 是 |  |  |
| 78 | interest | 是 |  |  |
| 79 | interest_tax | 是 |  |  |
| 80 | integral_update | 是 |  |  |
| 81 | integral_flag | 是 |  |  |
| 82 | real_status | 是 |  |  |
| 83 | join_date | 否 |  |  |
| 84 | join_serial_no | 否 |  |  |
| 85 | client_id | 否 | H |  |
| 86 | client_name | 否 | H |  |
| 87 | branch_no | 否 | H |  |
| 88 | client_group | 否 | H |  |
| 89 | asset_prop | 否 | H |  |
| 90 | limit_flag | 否 | H |  |
| 91 | client_prop | 否 | H |  |
| 92 | asset_level | 否 | H |  |
| 93 | risk_level | 否 | H |  |
| 94 | corp_risk_level | 否 | H |  |
| 95 | room_code | 否 | H |  |
| 96 | corp_client_group | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_fund_changeinfo | 默认 | 否 | fund_account, serial_no, money_type, fund_account, serial_no, money_type |
| idx_ucrt_fund_changeinfo | ART | 是 | fund_account, serial_no, money_type, fund_account, serial_no, money_type |
| uk_rpt_ucrtfundchangeinfo | ART | 是 | init_date, fund_account, serial_no, money_type, init_date, fund_account, serial_no, money_type |
| idx_ucrt_fund_changeinfo | 默认 | 否 | fund_account, serial_no, money_type, fund_account, serial_no, money_type |
| idx_ucrt_fund_changeinfo | ART | 是 | fund_account, serial_no, money_type, fund_account, serial_no, money_type |
| uk_rpt_ucrtfundchangeinfo | ART | 是 | init_date, fund_account, serial_no, money_type, init_date, fund_account, serial_no, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_fund_changeinfo | fund_account, serial_no, money_type, fund_account, serial_no, money_type |
| idx_ucrt_fund_changeinfo | fund_account, serial_no, money_type, fund_account, serial_no, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-03 15:04:59 | 3.0.2.23 | 高志强 | 所有表ucrt_fund_changeinfo，添加了表字段(join_date);
所有表ucrt_fund_cha... |
| 2025-09-03 16:06:35 | 3.0.6.1066 | 沈勋 | 所有表ucrt_fund_changeinfo，添加了表字段(rate_kind);
所有表ucrt_fund_cha... |
| 2025-08-26 14:45:17 | 3.0.6.1064 | 沈勋 | 所有表ucrt_fund_changeinfo，添加了表字段(cash_balance);
所有表ucrt_fund_... |
| 2023-10-30 13:26:22 | V3.0.1.8 | 汪杰 | 物理表ucrt_fund_changeinfo，添加了表字段(exchange_type);
物理表ucrt_fund... |
| 2023-10-12 15:35:19 | V3.0.1.3 | 汪杰 | 物理表ucrt_fund_changeinfo，增加索引(idx_ucrt_fund_changeinfo:[fund_... |
| 2023-10-12 15:29:43 | V3.0.1.3 | 汪杰 | 物理表ucrt_fund_changeinfo，添加了表字段(init_date);
物理表ucrt_fund_cha... |
| 2025-12-03 15:04:59 | 3.0.2.23 | 高志强 | 所有表ucrt_fund_changeinfo，添加了表字段(join_date);
所有表ucrt_fund_cha... |
| 2025-09-03 16:06:35 | 3.0.6.1066 | 沈勋 | 所有表ucrt_fund_changeinfo，添加了表字段(rate_kind);
所有表ucrt_fund_cha... |
| 2025-08-26 14:45:17 | 3.0.6.1064 | 沈勋 | 所有表ucrt_fund_changeinfo，添加了表字段(cash_balance);
所有表ucrt_fund_... |
| 2023-10-30 13:26:22 | V3.0.1.8 | 汪杰 | 物理表ucrt_fund_changeinfo，添加了表字段(exchange_type);
物理表ucrt_fund... |
| 2023-10-12 15:35:19 | V3.0.1.3 | 汪杰 | 物理表ucrt_fund_changeinfo，增加索引(idx_ucrt_fund_changeinfo:[fund_... |
| 2023-10-12 15:29:43 | V3.0.1.3 | 汪杰 | 物理表ucrt_fund_changeinfo，添加了表字段(init_date);
物理表ucrt_fund_cha... |

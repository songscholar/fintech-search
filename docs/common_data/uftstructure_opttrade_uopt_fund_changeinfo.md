# uopt_fund_changeinfo - 期权交易资金变更信息表

**表对象ID**: 9631
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 76 个）

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
| 9 | cash_balance | 否 |  |  |
| 10 | check_balance | 否 |  |  |
| 11 | post_balance | 否 |  |  |
| 12 | foregift_balance | 否 |  |  |
| 13 | mortgage_balance | 否 |  |  |
| 14 | cancel_serial_no | 否 |  |  |
| 15 | business_flag | 否 |  |  |
| 16 | op_branch_no | 否 |  |  |
| 17 | operator_no | 否 |  |  |
| 18 | op_station | 否 |  |  |
| 19 | op_entrust_way | 否 |  |  |
| 20 | join_date | 否 |  |  |
| 21 | join_serial_no | 否 |  |  |
| 22 | bk_serial_no | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | real_status | 否 |  |  |
| 25 | frozen_kind | 否 |  |  |
| 26 | rate_kind | 否 |  |  |
| 27 | integral_balance | 否 |  |  |
| 28 | fine_integral | 否 |  |  |
| 29 | interest | 否 |  |  |
| 30 | interest_tax | 否 |  |  |
| 31 | curr_date | 否 |  |  |
| 32 | curr_time | 否 |  |  |
| 33 | real_action | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | begin_balance | 否 |  |  |
| 36 | integral_update | 否 |  |  |
| 37 | integral_flag | 否 |  |  |
| 38 | position_str | 否 |  |  |
| 39 | init_date | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | serial_no | 否 |  |  |
| 42 | money_type | 否 |  |  |
| 43 | frozen_balance | 否 |  |  |
| 44 | unfrozen_balance | 否 |  |  |
| 45 | current_balance | 否 |  |  |
| 46 | correct_balance | 否 |  |  |
| 47 | cash_balance | 否 |  |  |
| 48 | check_balance | 否 |  |  |
| 49 | post_balance | 否 |  |  |
| 50 | foregift_balance | 否 |  |  |
| 51 | mortgage_balance | 否 |  |  |
| 52 | cancel_serial_no | 否 |  |  |
| 53 | business_flag | 否 |  |  |
| 54 | op_branch_no | 否 |  |  |
| 55 | operator_no | 否 |  |  |
| 56 | op_station | 否 |  |  |
| 57 | op_entrust_way | 否 |  |  |
| 58 | join_date | 否 |  |  |
| 59 | join_serial_no | 否 |  |  |
| 60 | bk_serial_no | 否 |  |  |
| 61 | remark | 否 |  |  |
| 62 | real_status | 否 |  |  |
| 63 | frozen_kind | 否 |  |  |
| 64 | rate_kind | 否 |  |  |
| 65 | integral_balance | 否 |  |  |
| 66 | fine_integral | 否 |  |  |
| 67 | interest | 否 |  |  |
| 68 | interest_tax | 否 |  |  |
| 69 | curr_date | 否 |  |  |
| 70 | curr_time | 否 |  |  |
| 71 | real_action | 否 |  |  |
| 72 | exchange_type | 否 |  |  |
| 73 | begin_balance | 否 |  |  |
| 74 | integral_update | 否 |  |  |
| 75 | integral_flag | 否 |  |  |
| 76 | position_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_fund_changeinfo | ART | 是 | fund_account, serial_no, money_type, fund_account, serial_no, money_type |
| idx_uopt_fund_changeinfo | ART | 是 | fund_account, serial_no, money_type, fund_account, serial_no, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_fund_changeinfo | fund_account, serial_no, money_type, fund_account, serial_no, money_type |
| idx_uopt_fund_changeinfo | fund_account, serial_no, money_type, fund_account, serial_no, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-14 18:54:25 | V3.0.2.21 | 韦子晗 | 所有表uopt_fund_changeinfo，删除了表字段（occur_balance）；
 |
| 2025-10-29 18:54:51 | V3.0.2.16 | 韦子晗 | 所有表uopt_fund_changeinfo，添加了表字段(position_str);
 |
| 2025-09-05 17:56:12 | V3.0.2.8 | 韦子晗 | 所有表uopt_fund_changeinfo，添加了表字段(rate_kind);
所有表uopt_fund_cha... |
| 2025-09-05 11:04:11 | V3.0.2.7 | 韦子晗 | 所有表uopt_fund_changeinfo，添加了表字段(frozen_kind);
 |
| 2025-08-27 16:37:13 | V3.0.2.5 | 韦子晗 | 新增 |
| 2026-01-14 18:54:25 | V3.0.2.21 | 韦子晗 | 所有表uopt_fund_changeinfo，删除了表字段（occur_balance）；
 |
| 2025-10-29 18:54:51 | V3.0.2.16 | 韦子晗 | 所有表uopt_fund_changeinfo，添加了表字段(position_str);
 |
| 2025-09-05 17:56:12 | V3.0.2.8 | 韦子晗 | 所有表uopt_fund_changeinfo，添加了表字段(rate_kind);
所有表uopt_fund_cha... |
| 2025-09-05 11:04:11 | V3.0.2.7 | 韦子晗 | 所有表uopt_fund_changeinfo，添加了表字段(frozen_kind);
 |
| 2025-08-27 16:37:13 | V3.0.2.5 | 韦子晗 | 新增 |

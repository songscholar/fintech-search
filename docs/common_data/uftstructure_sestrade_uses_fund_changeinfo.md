# uses_fund_changeinfo - 证券交易资金变更信息表

**表对象ID**: 5520
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 74 个）

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
| 16 | join_date | 否 |  |  |
| 17 | join_serial_no | 否 |  |  |
| 18 | cash_balance | 是 |  |  |
| 19 | check_balance | 是 |  |  |
| 20 | foregift_balance | 是 |  |  |
| 21 | mortgage_balance | 是 |  |  |
| 22 | curr_date | 是 |  |  |
| 23 | curr_time | 是 |  |  |
| 24 | post_balance | 是 |  |  |
| 25 | bk_serial_no | 是 |  |  |
| 26 | frozen_kind | 是 |  |  |
| 27 | begin_balance | 是 |  |  |
| 28 | integral_balance | 是 |  |  |
| 29 | fine_integral | 是 |  |  |
| 30 | interest | 是 |  |  |
| 31 | interest_tax | 是 |  |  |
| 32 | integral_update | 是 |  |  |
| 33 | integral_flag | 是 |  |  |
| 34 | real_status | 是 |  |  |
| 35 | rate_kind | 是 |  |  |
| 36 | remark | 否 |  |  |
| 37 | position_str | 否 |  | fund_account(18)+money_type(3)+serial_no(10) |
| 38 | init_date | 否 |  |  |
| 39 | fund_account | 否 |  |  |
| 40 | serial_no | 否 |  |  |
| 41 | money_type | 否 |  |  |
| 42 | frozen_balance | 否 |  |  |
| 43 | unfrozen_balance | 否 |  |  |
| 44 | current_balance | 否 |  |  |
| 45 | correct_balance | 否 |  |  |
| 46 | cancel_serial_no | 否 |  |  |
| 47 | exchange_type | 否 |  |  |
| 48 | business_flag | 否 |  |  |
| 49 | op_branch_no | 否 |  |  |
| 50 | operator_no | 否 |  |  |
| 51 | op_station | 否 |  |  |
| 52 | op_entrust_way | 否 |  |  |
| 53 | join_date | 否 |  |  |
| 54 | join_serial_no | 否 |  |  |
| 55 | cash_balance | 是 |  |  |
| 56 | check_balance | 是 |  |  |
| 57 | foregift_balance | 是 |  |  |
| 58 | mortgage_balance | 是 |  |  |
| 59 | curr_date | 是 |  |  |
| 60 | curr_time | 是 |  |  |
| 61 | post_balance | 是 |  |  |
| 62 | bk_serial_no | 是 |  |  |
| 63 | frozen_kind | 是 |  |  |
| 64 | begin_balance | 是 |  |  |
| 65 | integral_balance | 是 |  |  |
| 66 | fine_integral | 是 |  |  |
| 67 | interest | 是 |  |  |
| 68 | interest_tax | 是 |  |  |
| 69 | integral_update | 是 |  |  |
| 70 | integral_flag | 是 |  |  |
| 71 | real_status | 是 |  |  |
| 72 | rate_kind | 是 |  |  |
| 73 | remark | 否 |  |  |
| 74 | position_str | 否 |  | fund_account(18)+money_type(3)+serial_no(10) |

## 索引（共 16 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_fund_change_info_pos | 默认 | 否 |  |
| idx_uses_fund_changeinfo | 默认 | 否 |  |
| idx_uses_fund_change_info_pos | 默认 | 否 |  |
| idx_uses_fund_change_info_pos | 默认 | 否 | position_str, position_str |
| idx_uses_fund_changeinfo | ART | 是 | fund_account, serial_no, money_type, fund_account, serial_no, money_type |
| idx_uses_fund_change_info_pos | ART | 是 | position_str, position_str |
| idx_rpt_uses_fund_changeinfo | ART | 是 | init_date, fund_account, serial_no, money_type, init_date, fund_account, serial_no, money_type |
| idx_rpt_uses_fund_change_info_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_uses_fund_change_info_pos | 默认 | 否 |  |
| idx_uses_fund_changeinfo | 默认 | 否 |  |
| idx_uses_fund_change_info_pos | 默认 | 否 |  |
| idx_uses_fund_change_info_pos | 默认 | 否 | position_str, position_str |
| idx_uses_fund_changeinfo | ART | 是 | fund_account, serial_no, money_type, fund_account, serial_no, money_type |
| idx_uses_fund_change_info_pos | ART | 是 | position_str, position_str |
| idx_rpt_uses_fund_changeinfo | ART | 是 | init_date, fund_account, serial_no, money_type, init_date, fund_account, serial_no, money_type |
| idx_rpt_uses_fund_change_info_pos | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_fund_changeinfo | fund_account, serial_no, money_type, fund_account, serial_no, money_type |
| idx_uses_fund_changeinfo | fund_account, serial_no, money_type, fund_account, serial_no, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:44:20 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:27:10 | V3.0.8.13 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:42:33 | 3.0.2.104 | taocong45644 | 当前表uses_fund_changeinfo，修改了索引idx_uses_fund_change_info_pos,索... |
| 2025-11-07 10:02:30 | V3.0.2.103 | 洪略 | 新增历史表 |
| 2025-09-25 16:14:56 | 3.0.6.1019 | yangxz | 当前表uses_fund_changeinfo，增加索引（ idx_uses_fund_change_info_pos:... |
| 2025-09-25 16:13:59 | 3.0.6.1019 | yangxz | 所有表uses_fund_changeinfo，添加了表字段(position_str);
 |
| 2025-09-05 19:07:03 | 3.0.6.1019 | yusz | 所有表uses_fund_changeinfo，添加了表字段(begin_balance);
所有表uses_fund... |
| 2025-09-04 10:31:24 | 3.0.6.1019 | yusz | 所有表uses_fund_changeinfo，添加了表字段(cash_balance);
所有表uses_fund_... |
| 2025-02-21 11:10:17 | 3.0.2.60 | 董乾坤 | 物理表uses_fund_changeinfo，添加了表字段(join_date);
物理表uses_fund_cha... |
| 2024-08-14 14:09:28 | 3.0.2.38 | 张剑 | remark设置为变长字段 |
| 2026-03-09 13:44:20 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:27:10 | V3.0.8.13 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:42:33 | 3.0.2.104 | taocong45644 | 当前表uses_fund_changeinfo，修改了索引idx_uses_fund_change_info_pos,索... |
| 2025-11-07 10:02:30 | V3.0.2.103 | 洪略 | 新增历史表 |
| 2025-09-25 16:14:56 | 3.0.6.1019 | yangxz | 当前表uses_fund_changeinfo，增加索引（ idx_uses_fund_change_info_pos:... |

> 共 20 条修改记录，仅显示最近15条

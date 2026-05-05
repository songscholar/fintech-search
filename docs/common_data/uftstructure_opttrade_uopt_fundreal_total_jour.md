# uopt_fundreal_total_jour - 期权交易资金汇总流水表

**表对象ID**: 9629
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | sett_batch_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | serial_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | current_balance | 否 |  |  |
| 10 | enable_balance | 否 |  |  |
| 11 | frozen_balance | 否 |  |  |
| 12 | unfrozen_balance | 否 |  |  |
| 13 | cash_balance | 否 |  |  |
| 14 | check_balance | 否 |  |  |
| 15 | correct_balance | 否 |  |  |
| 16 | interest | 否 |  |  |
| 17 | fine_interest | 否 |  |  |
| 18 | integral_balance | 否 |  |  |
| 19 | interest_tax | 否 |  |  |
| 20 | fine_integral | 否 |  |  |
| 21 | init_date | 否 |  |  |
| 22 | sett_batch_no | 否 |  |  |
| 23 | curr_date | 否 |  |  |
| 24 | curr_time | 否 |  |  |
| 25 | serial_no | 否 |  |  |
| 26 | fund_account | 否 |  |  |
| 27 | money_type | 否 |  |  |
| 28 | client_id | 否 |  |  |
| 29 | current_balance | 否 |  |  |
| 30 | enable_balance | 否 |  |  |
| 31 | frozen_balance | 否 |  |  |
| 32 | unfrozen_balance | 否 |  |  |
| 33 | cash_balance | 否 |  |  |
| 34 | check_balance | 否 |  |  |
| 35 | correct_balance | 否 |  |  |
| 36 | interest | 否 |  |  |
| 37 | fine_interest | 否 |  |  |
| 38 | integral_balance | 否 |  |  |
| 39 | interest_tax | 否 |  |  |
| 40 | fine_integral | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_fundreal_total_jour | 默认 | 是 | init_date, sett_batch_no, fund_account, money_type, serial_no, init_date, sett_batch_no, fund_account, money_type, serial_no |
| idx_uopt_fundreal_total_jour | 默认 | 是 | init_date, sett_batch_no, fund_account, money_type, serial_no, init_date, sett_batch_no, fund_account, money_type, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_fundreal_total_jour | init_date, sett_batch_no, fund_account, money_type, serial_no, init_date, sett_batch_no, fund_account, money_type, serial_no |
| idx_uopt_fundreal_total_jour | init_date, sett_batch_no, fund_account, money_type, serial_no, init_date, sett_batch_no, fund_account, money_type, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-06 16:52:24 | V3.0.2.8 | 韦子晗 | 所有表uopt_fundreal_total_jour，添加了表字段(interest);
所有表uopt_fundr... |
| 2025-08-02 21:30:33 | V3.0.3.17 | 韦子晗 | 新增索引字段serial_no |
| 2025-07-30 22:52:37 | V3.0.2.2 | 吴笑东 | 新增 |
| 2025-09-06 16:52:24 | V3.0.2.8 | 韦子晗 | 所有表uopt_fundreal_total_jour，添加了表字段(interest);
所有表uopt_fundr... |
| 2025-08-02 21:30:33 | V3.0.3.17 | 韦子晗 | 新增索引字段serial_no |
| 2025-07-30 22:52:37 | V3.0.2.2 | 吴笑东 | 新增 |

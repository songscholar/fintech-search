# uopt_fundreal_total - 期权交易资金汇总表

**表对象ID**: 9626
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | sett_batch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | current_balance | 否 |  |  |
| 7 | enable_balance | 否 |  |  |
| 8 | frozen_balance | 否 |  |  |
| 9 | unfrozen_balance | 否 |  |  |
| 10 | cash_balance | 否 |  |  |
| 11 | check_balance | 否 |  |  |
| 12 | correct_balance | 否 |  |  |
| 13 | interest | 否 |  |  |
| 14 | fine_interest | 否 |  |  |
| 15 | integral_balance | 否 |  |  |
| 16 | interest_tax | 否 |  |  |
| 17 | fine_integral | 否 |  |  |
| 18 | init_date | 否 |  |  |
| 19 | sett_batch_no | 否 |  |  |
| 20 | fund_account | 否 |  |  |
| 21 | money_type | 否 |  |  |
| 22 | client_id | 否 |  |  |
| 23 | current_balance | 否 |  |  |
| 24 | enable_balance | 否 |  |  |
| 25 | frozen_balance | 否 |  |  |
| 26 | unfrozen_balance | 否 |  |  |
| 27 | cash_balance | 否 |  |  |
| 28 | check_balance | 否 |  |  |
| 29 | correct_balance | 否 |  |  |
| 30 | interest | 否 |  |  |
| 31 | fine_interest | 否 |  |  |
| 32 | integral_balance | 否 |  |  |
| 33 | interest_tax | 否 |  |  |
| 34 | fine_integral | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_fundreal_total | 默认 | 是 | init_date, sett_batch_no, fund_account, money_type, init_date, sett_batch_no, fund_account, money_type |
| idx_uopt_fundreal_total | 默认 | 是 | init_date, sett_batch_no, fund_account, money_type, init_date, sett_batch_no, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_fundreal_total | init_date, sett_batch_no, fund_account, money_type, init_date, sett_batch_no, fund_account, money_type |
| idx_uopt_fundreal_total | init_date, sett_batch_no, fund_account, money_type, init_date, sett_batch_no, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-06 14:08:41 | V3.0.2.8 | 韦子晗 | 所有表uopt_fundreal_total，添加了表字段(fine_interest);
所有表uopt_fundr... |
| 2025-07-30 22:44:58 | V3.0.2.2 | 吴笑东 | 新增 |
| 2025-09-06 14:08:41 | V3.0.2.8 | 韦子晗 | 所有表uopt_fundreal_total，添加了表字段(fine_interest);
所有表uopt_fundr... |
| 2025-07-30 22:44:58 | V3.0.2.2 | 吴笑东 | 新增 |

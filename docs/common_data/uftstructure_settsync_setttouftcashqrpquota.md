# setttouftcashqrpquota - 清算头寸报价回购额度控制表

**表对象ID**: 3049
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | stock_code | 是 |  |  |
| 4 | qrp_approv_quota | 是 |  |  |
| 5 | qrp_actual_quota | 是 |  |  |
| 6 | qrp_impawn_balance | 是 |  |  |
| 7 | qrp_buy_quota | 是 |  |  |
| 8 | qrp_term_quota | 是 |  |  |
| 9 | qrp_huge_ratio | 是 |  |  |
| 10 | qrp_buy_balance | 是 |  |  |
| 11 | qrp_term_balance | 是 |  |  |
| 12 | qrp_undue_balance | 是 |  |  |
| 13 | qrp_due_balance | 是 |  |  |
| 14 | company_no | 是 |  |  |
| 15 | modify_date | 是 |  |  |
| 16 | cash_balance | 是 |  |  |
| 17 | qrp_day_orderup_quota | 是 |  |  |
| 18 | qrp_sum_uncomebalance_limit | 是 |  |  |
| 19 | init_date | 是 |  |  |
| 20 | exchange_type | 是 |  |  |
| 21 | stock_code | 是 |  |  |
| 22 | qrp_approv_quota | 是 |  |  |
| 23 | qrp_actual_quota | 是 |  |  |
| 24 | qrp_impawn_balance | 是 |  |  |
| 25 | qrp_buy_quota | 是 |  |  |
| 26 | qrp_term_quota | 是 |  |  |
| 27 | qrp_huge_ratio | 是 |  |  |
| 28 | qrp_buy_balance | 是 |  |  |
| 29 | qrp_term_balance | 是 |  |  |
| 30 | qrp_undue_balance | 是 |  |  |
| 31 | qrp_due_balance | 是 |  |  |
| 32 | company_no | 是 |  |  |
| 33 | modify_date | 是 |  |  |
| 34 | cash_balance | 是 |  |  |
| 35 | qrp_day_orderup_quota | 是 |  |  |
| 36 | qrp_sum_uncomebalance_limit | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settcashqrpquota | 默认 | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_settcashqrpquota_company | 默认 | 是 | company_no, company_no |
| idx_settcashqrpquota | 默认 | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_settcashqrpquota_company | 默认 | 是 | company_no, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settcashqrpquota | stock_code, stock_code |
| idx_settcashqrpquota | stock_code, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-09-03 11:12 | 8.26.1.93 | 罗佳楠 | 新增 |
| 2020-09-03 11:12 | 8.26.1.93 | 罗佳楠 | 新增 |

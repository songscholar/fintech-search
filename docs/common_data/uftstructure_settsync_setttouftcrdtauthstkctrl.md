# setttouftcrdtauthstkctrl - 清算权益份额表

**表对象ID**: 3030
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_id | 是 |  |  |
| 3 | authority_str | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | stock_code | 是 |  |  |
| 8 | fund_account | 是 |  |  |
| 9 | stock_type | 是 |  |  |
| 10 | current_amount | 是 |  |  |
| 11 | uncome_buy_amount | 是 |  |  |
| 12 | uncome_sell_amount | 是 |  |  |
| 13 | business_type | 是 |  |  |
| 14 | init_date | 是 |  |  |
| 15 | sett_id | 是 |  |  |
| 16 | authority_str | 是 |  |  |
| 17 | branch_no | 是 |  |  |
| 18 | exchange_type | 是 |  |  |
| 19 | stock_account | 是 |  |  |
| 20 | stock_code | 是 |  |  |
| 21 | fund_account | 是 |  |  |
| 22 | stock_type | 是 |  |  |
| 23 | current_amount | 是 |  |  |
| 24 | uncome_buy_amount | 是 |  |  |
| 25 | uncome_sell_amount | 是 |  |  |
| 26 | business_type | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_authoritystock | 默认 | 是 | authority_str, stock_account, exchange_type, stock_code, fund_account, authority_str, stock_account, exchange_type, stock_code, fund_account |
| idx_authoritystock | 默认 | 是 | authority_str, stock_account, exchange_type, stock_code, fund_account, authority_str, stock_account, exchange_type, stock_code, fund_account |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_authoritystock | authority_str, stock_account, exchange_type, stock_code, fund_account, authority_str, stock_account, exchange_type, stock_code, fund_account |
| idx_crdtauthstkctrl | fund_account, stock_account, authority_str, stock_code, exchange_type, fund_account, stock_account, authority_str, stock_code, exchange_type |
| idx_authoritystock | authority_str, stock_account, exchange_type, stock_code, fund_account, authority_str, stock_account, exchange_type, stock_code, fund_account |
| idx_crdtauthstkctrl | fund_account, stock_account, authority_str, stock_code, exchange_type, fund_account, stock_account, authority_str, stock_code, exchange_type |

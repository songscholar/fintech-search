# setttouftsecuauthoritystock - 清算证券权益表

**表对象ID**: 3092
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | authority_str | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | exchange_type | 是 |  |  |
| 5 | stock_account | 是 |  |  |
| 6 | stock_code | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | stock_type | 是 |  |  |
| 9 | current_amount | 是 |  |  |
| 10 | uncome_buy_amount | 是 |  |  |
| 11 | uncome_sell_amount | 是 |  |  |
| 12 | business_type | 是 |  |  |
| 13 | init_date | 是 |  |  |
| 14 | authority_str | 是 |  |  |
| 15 | branch_no | 是 |  |  |
| 16 | exchange_type | 是 |  |  |
| 17 | stock_account | 是 |  |  |
| 18 | stock_code | 是 |  |  |
| 19 | fund_account | 是 |  |  |
| 20 | stock_type | 是 |  |  |
| 21 | current_amount | 是 |  |  |
| 22 | uncome_buy_amount | 是 |  |  |
| 23 | uncome_sell_amount | 是 |  |  |
| 24 | business_type | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secuauthoritystock | 默认 | 否 | authority_str, exchange_type, stock_account, stock_code, fund_account, authority_str, exchange_type, stock_account, stock_code, fund_account |
| idx_secuauthoritystock | 默认 | 否 | authority_str, exchange_type, stock_account, stock_code, fund_account, authority_str, exchange_type, stock_account, stock_code, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_secuauthoritystock | authority_str, exchange_type, stock_account, stock_code, fund_account, authority_str, exchange_type, stock_account, stock_code, fund_account |
| idx_secuauthoritystock | authority_str, exchange_type, stock_account, stock_code, fund_account, authority_str, exchange_type, stock_account, stock_code, fund_account |

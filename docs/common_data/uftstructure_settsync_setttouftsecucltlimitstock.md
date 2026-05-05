# setttouftsecucltlimitstock - 清算客户限售股信息表

**表对象ID**: 3005
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | fund_account | 是 |  |  |
| 4 | stock_account | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_code | 是 |  |  |
| 7 | total_tax | 是 |  |  |
| 8 | tax_ratio | 是 |  |  |
| 9 | tax_balance | 是 |  |  |
| 10 | tax | 是 |  |  |
| 11 | baseprice_kind | 是 |  |  |
| 12 | cost_price | 是 |  |  |
| 13 | drawback_flag | 是 |  |  |
| 14 | modify_date | 是 |  |  |
| 15 | remark | 是 |  |  |
| 16 | uft_data_change_status | 是 |  |  |
| 17 | client_id | 是 |  |  |
| 18 | branch_no | 是 |  |  |
| 19 | fund_account | 是 |  |  |
| 20 | stock_account | 是 |  |  |
| 21 | exchange_type | 是 |  |  |
| 22 | stock_code | 是 |  |  |
| 23 | total_tax | 是 |  |  |
| 24 | tax_ratio | 是 |  |  |
| 25 | tax_balance | 是 |  |  |
| 26 | tax | 是 |  |  |
| 27 | baseprice_kind | 是 |  |  |
| 28 | cost_price | 是 |  |  |
| 29 | drawback_flag | 是 |  |  |
| 30 | modify_date | 是 |  |  |
| 31 | remark | 是 |  |  |
| 32 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settsecucltlimitstocktotal | 默认 | 是 | stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code, fund_account |
| idx_settsecucltlimitstocktotal_acct | 默认 | 是 | fund_account, fund_account |
| idx_settsecucltlimitstocktotal | 默认 | 是 | stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code, fund_account |
| idx_settsecucltlimitstocktotal_acct | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settsecucltlimitstocktotal | stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code, fund_account |
| idx_settsecucltlimitstocktotal | stock_account, exchange_type, stock_code, fund_account, stock_account, exchange_type, stock_code, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-11-21 17:46 | 8.26.1.58 | 曾哲 | 唯一索引分级顺序调整 |
| 2018-09-20 14:59 | 8.26.1.21 | 蒋迪 | 新增 |
| 2020-11-21 17:46 | 8.26.1.58 | 曾哲 | 唯一索引分级顺序调整 |
| 2018-09-20 14:59 | 8.26.1.21 | 蒋迪 | 新增 |

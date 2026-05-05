# product_basic_info - 产品基础信息表

**表对象ID**: 2511
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_name | 否 |  |  |
| 4 | stock_name_long | 否 |  |  |
| 5 | stock_type_source | 否 |  |  |
| 6 | sub_stock_type_source | 否 |  |  |
| 7 | stock_type_tag | 否 |  |  |
| 8 | en_trade_type | 否 |  |  |
| 9 | stkcode_status | 否 |  |  |
| 10 | bond_end_date | 否 |  |  |
| 11 | market_date | 否 |  |  |
| 12 | issue_date | 否 |  |  |
| 13 | final_trade_date | 否 |  |  |
| 14 | par_value | 否 |  |  |
| 15 | close_price | 否 |  |  |
| 16 | close_weightavg_price | 否 |  |  |
| 17 | product_info_ctrlstr | 否 |  |  |
| 18 | hq_date | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | stock_name | 否 |  |  |
| 23 | stock_name_long | 否 |  |  |
| 24 | stock_type_source | 否 |  |  |
| 25 | sub_stock_type_source | 否 |  |  |
| 26 | stock_type_tag | 否 |  |  |
| 27 | en_trade_type | 否 |  |  |
| 28 | stkcode_status | 否 |  |  |
| 29 | bond_end_date | 否 |  |  |
| 30 | market_date | 否 |  |  |
| 31 | issue_date | 否 |  |  |
| 32 | final_trade_date | 否 |  |  |
| 33 | par_value | 否 |  |  |
| 34 | close_price | 否 |  |  |
| 35 | close_weightavg_price | 否 |  |  |
| 36 | product_info_ctrlstr | 否 |  |  |
| 37 | hq_date | 否 |  |  |
| 38 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_productbasicinfo | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_productbasicinfo | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_productbasicinfo | stock_code, exchange_type, stock_code, exchange_type |
| idx_productbasicinfo | stock_code, exchange_type, stock_code, exchange_type |

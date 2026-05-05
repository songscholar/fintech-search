# uref_stock_detail - 转融通战略配售股明细表

**表对象ID**: 6170
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_account | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | current_amount | 否 |  |  |
| 5 | lend_report_amount | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | enable_status | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | current_amount | 否 |  |  |
| 12 | lend_report_amount | 否 |  |  |
| 13 | init_date | 否 |  |  |
| 14 | enable_status | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refspsstockdetail | ART | 是 | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |
| idx_refspsstockdetail | ART | 是 | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refspsstockdetail | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |
| idx_refspsstockdetail | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |

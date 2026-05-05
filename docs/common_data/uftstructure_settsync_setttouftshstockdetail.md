# setttouftshstockdetail - 清算上海证券余额信息表

**表对象ID**: 3026
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_id | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | pbu_clear_no | 是 |  |  |
| 4 | stock_account | 是 |  |  |
| 5 | seat_no | 是 |  |  |
| 6 | stock_code | 是 |  |  |
| 7 | shdc_stock_type | 是 |  |  |
| 8 | shdc_circulate_type | 是 |  |  |
| 9 | shdc_authority_type | 是 |  |  |
| 10 | shdc_market_year | 是 |  |  |
| 11 | total_amount | 是 |  |  |
| 12 | end_frozen_amount | 是 |  |  |
| 13 | shdc_by | 是 |  |  |
| 14 | shdc_end_date | 是 |  |  |
| 15 | ocpused_amount | 是 |  |  |
| 16 | busiflow_id | 是 |  |  |
| 17 | sett_id | 是 |  |  |
| 18 | exchange_type | 是 |  |  |
| 19 | pbu_clear_no | 是 |  |  |
| 20 | stock_account | 是 |  |  |
| 21 | seat_no | 是 |  |  |
| 22 | stock_code | 是 |  |  |
| 23 | shdc_stock_type | 是 |  |  |
| 24 | shdc_circulate_type | 是 |  |  |
| 25 | shdc_authority_type | 是 |  |  |
| 26 | shdc_market_year | 是 |  |  |
| 27 | total_amount | 是 |  |  |
| 28 | end_frozen_amount | 是 |  |  |
| 29 | shdc_by | 是 |  |  |
| 30 | shdc_end_date | 是 |  |  |
| 31 | ocpused_amount | 是 |  |  |
| 32 | busiflow_id | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_shstockdetail | 默认 | 是 | stock_account, exchange_type, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year, stock_account, exchange_type, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year |
| idx_shstockdetail_stkcode | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_shstockdetail | 默认 | 是 | stock_account, exchange_type, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year, stock_account, exchange_type, stock_code, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year |
| idx_shstockdetail_stkcode | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_shstockdetail | stock_account, stock_code, exchange_type, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year, stock_account, stock_code, exchange_type, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year |
| idx_shstockdetail | stock_account, stock_code, exchange_type, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year, stock_account, stock_code, exchange_type, shdc_stock_type, shdc_circulate_type, shdc_authority_type, shdc_market_year |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-10-29 18:46 | 8.26.2.85 | 贾子凡 | 增加stkcode索引，删除businflow_id索引 |
| 2022-10-27 15:11 | 8.26.2.38 | 张军 | 增加busiflow_id索引 |
| 2024-10-29 18:46 | 8.26.2.85 | 贾子凡 | 增加stkcode索引，删除businflow_id索引 |
| 2022-10-27 15:11 | 8.26.2.38 | 张军 | 增加busiflow_id索引 |

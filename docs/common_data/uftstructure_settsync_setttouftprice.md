# setttouftprice - 清算证券行情表

**表对象ID**: 3000
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_code | 是 |  |  |
| 3 | init_date | 是 |  |  |
| 4 | asset_price | 是 |  |  |
| 5 | last_price | 是 |  |  |
| 6 | money_type | 是 |  |  |
| 7 | rate_price | 是 |  |  |
| 8 | business_balance | 是 |  |  |
| 9 | close_flag | 是 |  |  |
| 10 | low_price | 是 |  |  |
| 11 | high_price | 是 |  |  |
| 12 | closing_price | 是 |  |  |
| 13 | weightavg_price | 是 |  |  |
| 14 | stkcode_status | 是 |  |  |
| 15 | dr_price | 是 |  |  |
| 16 | pre_dr_price | 是 |  |  |
| 17 | exchange_type | 是 |  |  |
| 18 | stock_code | 是 |  |  |
| 19 | init_date | 是 |  |  |
| 20 | asset_price | 是 |  |  |
| 21 | last_price | 是 |  |  |
| 22 | money_type | 是 |  |  |
| 23 | rate_price | 是 |  |  |
| 24 | business_balance | 是 |  |  |
| 25 | close_flag | 是 |  |  |
| 26 | low_price | 是 |  |  |
| 27 | high_price | 是 |  |  |
| 28 | closing_price | 是 |  |  |
| 29 | weightavg_price | 是 |  |  |
| 30 | stkcode_status | 是 |  |  |
| 31 | dr_price | 是 |  |  |
| 32 | pre_dr_price | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sett_price | 默认 | 是 | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_sett_price | 默认 | 是 | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sett_price | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_sett_price | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-23 20:02 | 8.26.2.35 | 董子文 | 新增pre_dr_price字段 |
| 2018-05-21 21:18 | 8.26.1.11 | 曾哲 | 新增dr_price字段 |
| 2024-09-23 20:02 | 8.26.2.35 | 董子文 | 新增pre_dr_price字段 |
| 2018-05-21 21:18 | 8.26.1.11 | 曾哲 | 新增dr_price字段 |

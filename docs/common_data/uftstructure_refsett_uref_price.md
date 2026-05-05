# uref_price - 转融通行情表

**表对象ID**: 6169
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | asset_price | 否 |  |  |
| 5 | init_date | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | asset_price | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refprice | ART | 是 | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_refprice | ART | 是 | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refprice | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |
| idx_refprice | stock_code, exchange_type, init_date, stock_code, exchange_type, init_date |

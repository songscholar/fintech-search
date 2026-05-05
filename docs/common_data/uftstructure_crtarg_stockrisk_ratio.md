# stockrisk_ratio - 流动性风险控制参数表

**表对象ID**: 7096
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | market_value | 否 |  |  |
| 6 | stock_assets_ratio | 否 |  |  |
| 7 | assurescale_value | 否 |  |  |
| 8 | risk_restriction | 否 |  |  |
| 9 | assure_close_balance | 否 |  |  |
| 10 | assurescale_in | 否 |  |  |
| 11 | assurescale_out | 否 |  |  |
| 12 | stockrisk_type | 否 |  |  |
| 13 | date_count | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 18 | company_no | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | stock_type | 否 |  |  |
| 22 | market_value | 否 |  |  |
| 23 | stock_assets_ratio | 否 |  |  |
| 24 | assurescale_value | 否 |  |  |
| 25 | risk_restriction | 否 |  |  |
| 26 | assure_close_balance | 否 |  |  |
| 27 | assurescale_in | 否 |  |  |
| 28 | assurescale_out | 否 |  |  |
| 29 | stockrisk_type | 否 |  |  |
| 30 | date_count | 否 |  |  |
| 31 | update_date | 否 |  |  |
| 32 | update_time | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | position_str | 否 |  | init_date(8)+serial_no(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stockrisk_ratio | ART | 是 | stock_code, stock_type, exchange_type, company_no, stockrisk_type, assurescale_in, assurescale_out, stock_code, stock_type, exchange_type, company_no, stockrisk_type, assurescale_in, assurescale_out |
| idx_stockrisk_ratio | ART | 是 | stock_code, stock_type, exchange_type, company_no, stockrisk_type, assurescale_in, assurescale_out, stock_code, stock_type, exchange_type, company_no, stockrisk_type, assurescale_in, assurescale_out |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stockrisk_ratio | stock_code, stock_type, exchange_type, company_no, stockrisk_type, assurescale_in, assurescale_out, stock_code, stock_type, exchange_type, company_no, stockrisk_type, assurescale_in, assurescale_out |
| idx_stockrisk_ratio | stock_code, stock_type, exchange_type, company_no, stockrisk_type, assurescale_in, assurescale_out, stock_code, stock_type, exchange_type, company_no, stockrisk_type, assurescale_in, assurescale_out |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 13:46:18 | 3.0.6.81 | 李想 | 新增表 |
| 2025-02-18 13:46:18 | 3.0.6.81 | 李想 | 新增表 |

# settredo_stb_dlsinfo - 清算重做股转摘牌转让信息表

**表对象ID**: 5804
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | entrust_bs | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | entrust_date | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | sett_dml_type | 否 |  |  |
| 9 | sett_batch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | entrust_bs | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | entrust_date | 否 |  |  |
| 16 | date_clear | 否 |  |  |
| 17 | sett_dml_type | 否 |  |  |
| 18 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_stb_dlsinfo | ART | 是 | sett_batch_no, fund_account, stock_account, exchange_type, stock_code, entrust_bs, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, entrust_bs |
| idx_settredo_stb_dlsinfo | ART | 是 | sett_batch_no, fund_account, stock_account, exchange_type, stock_code, entrust_bs, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, entrust_bs |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_stb_dlsinfo | sett_batch_no, fund_account, stock_account, exchange_type, stock_code, entrust_bs, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, entrust_bs |
| idx_settredo_stb_dlsinfo | sett_batch_no, fund_account, stock_account, exchange_type, stock_code, entrust_bs, sett_batch_no, fund_account, stock_account, exchange_type, stock_code, entrust_bs |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:45:05 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:49:50 | 3.0.6.1014 | yangxz |  |
| 2026-03-09 14:45:05 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:49:50 | 3.0.6.1014 | yangxz |  |

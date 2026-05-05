# settredo_stock_code_match - 清算重做北交所股转代码对照表

**表对象ID**: 507
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | trans_code_tz | 否 |  |  |
| 3 | effect_date | 否 |  |  |
| 4 | sett_dml_type | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | trans_code_tz | 否 |  |  |
| 8 | effect_date | 否 |  |  |
| 9 | sett_dml_type | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sett_stock_code_match | ART | 是 | sett_batch_no, stock_code, sett_batch_no, stock_code |
| idx_sett_stock_code_match | ART | 是 | sett_batch_no, stock_code, sett_batch_no, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sett_stock_code_match | sett_batch_no, stock_code, sett_batch_no, stock_code |
| idx_sett_stock_code_match | sett_batch_no, stock_code, sett_batch_no, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-24 09:56:35 | 3.0.6.1012 | yangxz |  |
| 2025-07-24 09:56:35 | 3.0.6.1012 | yangxz |  |

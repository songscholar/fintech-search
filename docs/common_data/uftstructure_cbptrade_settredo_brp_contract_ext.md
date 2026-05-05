# settredo_brp_contract_ext - 清算重做债券质押协议回购合约扩展表

**表对象ID**: 12357
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | impawn_amount | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | join_position_str | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | stock_property | 否 |  |  |
| 7 | sett_dml_type | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | impawn_amount | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | join_position_str | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | stock_property | 否 |  |  |
| 15 | sett_dml_type | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_brpcontractext | ART | 是 | sett_batch_no, join_position_str, exchange_type, stock_code, stock_property, sett_batch_no, join_position_str, exchange_type, stock_code, stock_property |
| idx_settredo_brpcontractext | ART | 是 | sett_batch_no, join_position_str, exchange_type, stock_code, stock_property, sett_batch_no, join_position_str, exchange_type, stock_code, stock_property |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_brpcontractext | sett_batch_no, join_position_str, exchange_type, stock_code, stock_property, sett_batch_no, join_position_str, exchange_type, stock_code, stock_property |
| idx_settredo_brpcontractext | sett_batch_no, join_position_str, exchange_type, stock_code, stock_property, sett_batch_no, join_position_str, exchange_type, stock_code, stock_property |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:33:48 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2026-03-04 16:33:48 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |

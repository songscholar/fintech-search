# ucrt_out_asset - 信用场外资产信息表

**表对象ID**: 7513
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | out_asset_type | 否 |  |  |
| 5 | out_assure_value | 否 |  |  |
| 6 | begin_out_assure_value | 否 |  |  |
| 7 | valid_date | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | current_amount | 否 |  |  |
| 12 | assure_ratio | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | position_str | 否 |  | branch_no(5) + fund_account(18) + out_asset_type(1) + exchan |
| 15 | stock_name | 否 | H |  |
| 16 | sub_stock_type | 否 | H |  |
| 17 | stock_type | 否 | H |  |
| 18 | client_group | 否 | H |  |
| 19 | room_code | 否 | H |  |
| 20 | asset_prop | 否 | H |  |
| 21 | limit_flag | 否 | H |  |
| 22 | risk_level | 否 | H |  |
| 23 | corp_client_group | 否 | H |  |
| 24 | corp_risk_level | 否 | H |  |
| 25 | asset_level | 否 | H |  |
| 26 | client_name | 否 | H |  |
| 27 | client_prop | 否 | H |  |
| 28 | init_date | 否 |  |  |
| 29 | client_id | 否 |  |  |
| 30 | fund_account | 否 |  |  |
| 31 | out_asset_type | 否 |  |  |
| 32 | out_assure_value | 否 |  |  |
| 33 | begin_out_assure_value | 否 |  |  |
| 34 | valid_date | 否 |  |  |
| 35 | date_clear | 否 |  |  |
| 36 | exchange_type | 否 |  |  |
| 37 | stock_code | 否 |  |  |
| 38 | current_amount | 否 |  |  |
| 39 | assure_ratio | 否 |  |  |
| 40 | branch_no | 否 |  |  |
| 41 | position_str | 否 |  | branch_no(5) + fund_account(18) + out_asset_type(1) + exchan |
| 42 | stock_name | 否 | H |  |
| 43 | sub_stock_type | 否 | H |  |
| 44 | stock_type | 否 | H |  |
| 45 | client_group | 否 | H |  |
| 46 | room_code | 否 | H |  |
| 47 | asset_prop | 否 | H |  |
| 48 | limit_flag | 否 | H |  |
| 49 | risk_level | 否 | H |  |
| 50 | corp_client_group | 否 | H |  |
| 51 | corp_risk_level | 否 | H |  |
| 52 | asset_level | 否 | H |  |
| 53 | client_name | 否 | H |  |
| 54 | client_prop | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_out_asset_unique | ART | 是 | fund_account, out_asset_type, exchange_type, stock_code, fund_account, out_asset_type, exchange_type, stock_code |
| idx_ucrt_out_asset_type | ART | 是 | fund_account, stock_code, out_asset_type, fund_account, stock_code, out_asset_type |
| uk_rpt_ucrtoutasset | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_ucrtoutasset_tolast | ART | 是 | date_clear, date_clear |
| idx_ucrt_out_asset_unique | ART | 是 | fund_account, out_asset_type, exchange_type, stock_code, fund_account, out_asset_type, exchange_type, stock_code |
| idx_ucrt_out_asset_type | ART | 是 | fund_account, stock_code, out_asset_type, fund_account, stock_code, out_asset_type |
| uk_rpt_ucrtoutasset | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_ucrtoutasset_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_out_asset_unique | fund_account, out_asset_type, exchange_type, stock_code, fund_account, out_asset_type, exchange_type, stock_code |
| idx_ucrt_out_asset_unique | fund_account, out_asset_type, exchange_type, stock_code, fund_account, out_asset_type, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-21 18:37:24 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_out_asset，添加了表字段(branch_no);
物理表ucrt_out_asset，添加了表... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-21 18:37:24 | 3.0.6.1065 | 徐世晗 | 物理表ucrt_out_asset，添加了表字段(branch_no);
物理表ucrt_out_asset，添加了表... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

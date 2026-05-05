# usps_srp_code - 股票质押代码表

**表对象ID**: 350
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | srp_kind | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | stock_conc_ratio | 否 |  |  |
| 7 | srp_capital_ratio | 否 |  |  |
| 8 | srp_one_capital_ratio | 否 |  |  |
| 9 | capital_amount | 否 |  |  |
| 10 | circulate_amount | 否 |  |  |
| 11 | srp_assure_ratio | 否 |  |  |
| 12 | assure_price | 否 |  |  |
| 13 | fair_price | 否 |  |  |
| 14 | fair_price_flag | 否 |  |  |
| 15 | assure_status | 否 |  |  |
| 16 | uncirculate_ratio | 否 |  |  |
| 17 | margin_focus_ratio | 否 |  |  |
| 18 | margin_alert_ratio | 否 |  |  |
| 19 | margin_treat_ratio | 否 |  |  |
| 20 | uncir_margin_focus_ratio | 否 |  |  |
| 21 | uncir_margin_alert_ratio | 否 |  |  |
| 22 | uncir_margin_treat_ratio | 否 |  |  |
| 23 | margin_immtreat_ratio | 否 |  |  |
| 24 | uncir_margin_immtreat_ratio | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | update_date | 否 |  |  |
| 27 | update_time | 否 |  |  |
| 28 | position_str | 否 |  | stock_code(8)+exchange_type(4)+srp_kind(1)+company_no(4) |
| 29 | company_no | 否 |  |  |
| 30 | exchange_type | 否 |  |  |
| 31 | stock_code | 否 |  |  |
| 32 | srp_kind | 否 |  |  |
| 33 | stock_type | 否 |  |  |
| 34 | stock_conc_ratio | 否 |  |  |
| 35 | srp_capital_ratio | 否 |  |  |
| 36 | srp_one_capital_ratio | 否 |  |  |
| 37 | capital_amount | 否 |  |  |
| 38 | circulate_amount | 否 |  |  |
| 39 | srp_assure_ratio | 否 |  |  |
| 40 | assure_price | 否 |  |  |
| 41 | fair_price | 否 |  |  |
| 42 | fair_price_flag | 否 |  |  |
| 43 | assure_status | 否 |  |  |
| 44 | uncirculate_ratio | 否 |  |  |
| 45 | margin_focus_ratio | 否 |  |  |
| 46 | margin_alert_ratio | 否 |  |  |
| 47 | margin_treat_ratio | 否 |  |  |
| 48 | uncir_margin_focus_ratio | 否 |  |  |
| 49 | uncir_margin_alert_ratio | 否 |  |  |
| 50 | uncir_margin_treat_ratio | 否 |  |  |
| 51 | margin_immtreat_ratio | 否 |  |  |
| 52 | uncir_margin_immtreat_ratio | 否 |  |  |
| 53 | transaction_no | 否 |  |  |
| 54 | update_date | 否 |  |  |
| 55 | update_time | 否 |  |  |
| 56 | position_str | 否 |  | stock_code(8)+exchange_type(4)+srp_kind(1)+company_no(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpcode | ART | 是 | stock_code, exchange_type, srp_kind, company_no, stock_code, exchange_type, srp_kind, company_no |
| idx_srpcode | ART | 是 | stock_code, exchange_type, srp_kind, company_no, stock_code, exchange_type, srp_kind, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpcode | stock_code, exchange_type, srp_kind, company_no, stock_code, exchange_type, srp_kind, company_no |
| idx_srpcode | stock_code, exchange_type, srp_kind, company_no, stock_code, exchange_type, srp_kind, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 17:09:14 | 3.0.6.108 | 李想 | 物理表usps_srp_code，添加了表字段(update_date);
物理表usps_srp_code，添加了表... |
| 2024-12-05 16:39:54 | 3.0.2.33 | 范文浩 | 勾选不回库 |
| 2024-10-23 14:43:58 | 3.0.4.3 | wuxd | 新增 |
| 2025-02-19 17:09:14 | 3.0.6.108 | 李想 | 物理表usps_srp_code，添加了表字段(update_date);
物理表usps_srp_code，添加了表... |
| 2024-12-05 16:39:54 | 3.0.2.33 | 范文浩 | 勾选不回库 |
| 2024-10-23 14:43:58 | 3.0.4.3 | wuxd | 新增 |

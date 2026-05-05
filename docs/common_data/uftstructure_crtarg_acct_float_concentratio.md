# acct_float_concentratio - 客户浮动集中度参数表

**表对象ID**: 7088
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | conc_ratio_kind | 否 |  |  |
| 4 | conc_ratio_type | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | market_forward5_date_flag | 否 |  |  |
| 9 | stockgroup_no | 否 |  |  |
| 10 | followdate_flag | 否 |  |  |
| 11 | ratio_package_kind_t | 否 |  |  |
| 12 | stock_conc_floatratio | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | stockgroup_name | 否 |  |  |
| 15 | assurescale_value_max | 否 |  |  |
| 16 | assurescale_value_min | 否 |  |  |
| 17 | organ_flag | 否 |  |  |
| 18 | registration_flag | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |
| 23 | branch_no | 否 |  |  |
| 24 | fund_account | 否 |  |  |
| 25 | conc_ratio_kind | 否 |  |  |
| 26 | conc_ratio_type | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | stock_code | 否 |  |  |
| 29 | stock_type | 否 |  |  |
| 30 | market_forward5_date_flag | 否 |  |  |
| 31 | stockgroup_no | 否 |  |  |
| 32 | followdate_flag | 否 |  |  |
| 33 | ratio_package_kind_t | 否 |  |  |
| 34 | stock_conc_floatratio | 否 |  |  |
| 35 | remark | 否 |  |  |
| 36 | stockgroup_name | 否 |  |  |
| 37 | assurescale_value_max | 否 |  |  |
| 38 | assurescale_value_min | 否 |  |  |
| 39 | organ_flag | 否 |  |  |
| 40 | registration_flag | 否 |  |  |
| 41 | update_date | 否 |  |  |
| 42 | update_time | 否 |  |  |
| 43 | transaction_no | 否 |  |  |
| 44 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_acct_float_concentratio | ART | 是 | fund_account, stock_code, stock_type, stockgroup_no, exchange_type, conc_ratio_type, conc_ratio_kind, market_forward5_date_flag, followdate_flag, ratio_package_kind_t, assurescale_value_min, organ_flag, registration_flag, fund_account, stock_code, stock_type, stockgroup_no, exchange_type, conc_ratio_type, conc_ratio_kind, market_forward5_date_flag, followdate_flag, ratio_package_kind_t, assurescale_value_min, organ_flag, registration_flag |
| idx_acct_float_concentratio | ART | 是 | fund_account, stock_code, stock_type, stockgroup_no, exchange_type, conc_ratio_type, conc_ratio_kind, market_forward5_date_flag, followdate_flag, ratio_package_kind_t, assurescale_value_min, organ_flag, registration_flag, fund_account, stock_code, stock_type, stockgroup_no, exchange_type, conc_ratio_type, conc_ratio_kind, market_forward5_date_flag, followdate_flag, ratio_package_kind_t, assurescale_value_min, organ_flag, registration_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_acct_float_concentratio | fund_account, stock_code, stock_type, stockgroup_no, exchange_type, conc_ratio_type, conc_ratio_kind, market_forward5_date_flag, followdate_flag, ratio_package_kind_t, assurescale_value_min, organ_flag, registration_flag, fund_account, stock_code, stock_type, stockgroup_no, exchange_type, conc_ratio_type, conc_ratio_kind, market_forward5_date_flag, followdate_flag, ratio_package_kind_t, assurescale_value_min, organ_flag, registration_flag |
| idx_acct_float_concentratio | fund_account, stock_code, stock_type, stockgroup_no, exchange_type, conc_ratio_type, conc_ratio_kind, market_forward5_date_flag, followdate_flag, ratio_package_kind_t, assurescale_value_min, organ_flag, registration_flag, fund_account, stock_code, stock_type, stockgroup_no, exchange_type, conc_ratio_type, conc_ratio_kind, market_forward5_date_flag, followdate_flag, ratio_package_kind_t, assurescale_value_min, organ_flag, registration_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 11:35:45 | 3.0.6.76 | 李想 | 新增表 |
| 2025-02-18 11:35:45 | 3.0.6.76 | 李想 | 新增表 |

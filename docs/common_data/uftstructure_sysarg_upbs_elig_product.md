# upbs_elig_product - 产品适当性属性表

**表对象ID**: 83
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | invest_type | 否 |  |  |
| 4 | income_type | 否 |  |  |
| 5 | prodrisk_level | 否 |  |  |
| 6 | invest_term | 否 |  |  |
| 7 | elig_ctrlstr | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | prodta_no | 否 |  |  |
| 10 | prod_code | 否 |  |  |
| 11 | prod_name | 否 |  |  |
| 12 | prod_type | 否 |  |  |
| 13 | prod_type_ass | 否 |  |  |
| 14 | en_corp_risk_level | 否 |  |  |
| 15 | prodpre_ratio | 否 |  |  |
| 16 | max_deficit_rate | 否 |  |  |
| 17 | prod_term | 否 |  |  |
| 18 | prod_begin_date | 否 |  |  |
| 19 | prod_end_date | 否 |  |  |
| 20 | min_asset_need | 否 |  |  |
| 21 | cooling_period | 否 |  |  |
| 22 | low_corp_risk_level | 否 |  |  |
| 23 | sub_stock_type | 否 |  |  |
| 24 | stock_type | 否 |  |  |
| 25 | finance_type | 否 |  |  |
| 26 | valid_days | 否 |  |  |
| 27 | state_kind | 否 |  |  |
| 28 | en_entrust_way | 否 |  |  |
| 29 | bank_risk_level | 否 |  |  |
| 30 | exchange_type | 否 |  |  |
| 31 | stock_code | 否 |  |  |
| 32 | invest_type | 否 |  |  |
| 33 | income_type | 否 |  |  |
| 34 | prodrisk_level | 否 |  |  |
| 35 | invest_term | 否 |  |  |
| 36 | elig_ctrlstr | 否 |  |  |
| 37 | transaction_no | 否 |  |  |
| 38 | prodta_no | 否 |  |  |
| 39 | prod_code | 否 |  |  |
| 40 | prod_name | 否 |  |  |
| 41 | prod_type | 否 |  |  |
| 42 | prod_type_ass | 否 |  |  |
| 43 | en_corp_risk_level | 否 |  |  |
| 44 | prodpre_ratio | 否 |  |  |
| 45 | max_deficit_rate | 否 |  |  |
| 46 | prod_term | 否 |  |  |
| 47 | prod_begin_date | 否 |  |  |
| 48 | prod_end_date | 否 |  |  |
| 49 | min_asset_need | 否 |  |  |
| 50 | cooling_period | 否 |  |  |
| 51 | low_corp_risk_level | 否 |  |  |
| 52 | sub_stock_type | 否 |  |  |
| 53 | stock_type | 否 |  |  |
| 54 | finance_type | 否 |  |  |
| 55 | valid_days | 否 |  |  |
| 56 | state_kind | 否 |  |  |
| 57 | en_entrust_way | 否 |  |  |
| 58 | bank_risk_level | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_elig_product | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_upbs_elig_product | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_elig_product | exchange_type, stock_code, exchange_type, stock_code |
| idx_upbs_elig_product | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-23 11:09:07 | 3.0.3.12 | 张明月 | 物理表upbs_elig_product，添加了表字段(bank_risk_level);
物理表upbs_elig_... |
| 2023-11-10 10:11:15 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |
| 2024-09-23 11:09:07 | 3.0.3.12 | 张明月 | 物理表upbs_elig_product，添加了表字段(bank_risk_level);
物理表upbs_elig_... |
| 2023-11-10 10:11:15 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |

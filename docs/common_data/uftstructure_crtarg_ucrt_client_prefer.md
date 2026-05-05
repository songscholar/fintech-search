# ucrt_client_prefer - 适当性偏好表

**表对象ID**: 7040
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | asset_balance | 否 |  |  |
| 3 | en_invest_term | 否 |  |  |
| 4 | en_invest_kind | 否 |  |  |
| 5 | prof_begin_date | 否 |  |  |
| 6 | prof_end_date | 否 |  |  |
| 7 | prof_type | 否 |  |  |
| 8 | pf_risk_level | 否 |  |  |
| 9 | pf_risk_begin_date | 否 |  |  |
| 10 | pf_risk_end_date | 否 |  |  |
| 11 | en_pf_invest_kind | 否 |  |  |
| 12 | en_pf_invest_term | 否 |  |  |
| 13 | corp_risk_level | 否 |  |  |
| 14 | corp_begin_date | 否 |  |  |
| 15 | corp_end_date | 否 |  |  |
| 16 | en_maxdeficit_rate | 否 |  |  |
| 17 | organ_flag | 否 |  |  |
| 18 | min_rank_flag | 否 |  |  |
| 19 | client_income_type | 否 |  |  |
| 20 | birthday | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | client_id | 否 |  |  |
| 23 | asset_balance | 否 |  |  |
| 24 | en_invest_term | 否 |  |  |
| 25 | en_invest_kind | 否 |  |  |
| 26 | prof_begin_date | 否 |  |  |
| 27 | prof_end_date | 否 |  |  |
| 28 | prof_type | 否 |  |  |
| 29 | pf_risk_level | 否 |  |  |
| 30 | pf_risk_begin_date | 否 |  |  |
| 31 | pf_risk_end_date | 否 |  |  |
| 32 | en_pf_invest_kind | 否 |  |  |
| 33 | en_pf_invest_term | 否 |  |  |
| 34 | corp_risk_level | 否 |  |  |
| 35 | corp_begin_date | 否 |  |  |
| 36 | corp_end_date | 否 |  |  |
| 37 | en_maxdeficit_rate | 否 |  |  |
| 38 | organ_flag | 否 |  |  |
| 39 | min_rank_flag | 否 |  |  |
| 40 | client_income_type | 否 |  |  |
| 41 | birthday | 否 |  |  |
| 42 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_client_prefer | ART | 是 | client_id, client_id |
| idx_ucrt_client_prefer | ART | 是 | client_id, client_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_client_prefer | client_id, client_id |
| idx_ucrt_client_prefer | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

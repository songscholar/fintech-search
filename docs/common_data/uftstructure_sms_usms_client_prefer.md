# usms_client_prefer - 客户适当性偏好表

**表对象ID**: 2800
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | asset_balance | 是 |  |  |
| 3 | en_invest_term | 是 |  |  |
| 4 | en_invest_kind | 是 |  |  |
| 5 | prof_begin_date | 是 |  |  |
| 6 | prof_end_date | 是 |  |  |
| 7 | prof_type | 是 |  |  |
| 8 | pf_risk_level | 是 |  |  |
| 9 | pf_risk_begin_date | 是 |  |  |
| 10 | pf_risk_end_date | 是 |  |  |
| 11 | en_pf_invest_kind | 是 |  |  |
| 12 | en_pf_invest_term | 是 |  |  |
| 13 | corp_risk_level | 是 |  |  |
| 14 | corp_begin_date | 是 |  |  |
| 15 | corp_end_date | 是 |  |  |
| 16 | en_maxdeficit_rate | 是 |  |  |
| 17 | organ_flag | 是 |  |  |
| 18 | min_rank_flag | 是 |  |  |
| 19 | client_income_type | 是 |  |  |
| 20 | birthday | 是 |  |  |
| 21 | transaction_no | 是 |  |  |
| 22 | client_id | 是 |  |  |
| 23 | asset_balance | 是 |  |  |
| 24 | en_invest_term | 是 |  |  |
| 25 | en_invest_kind | 是 |  |  |
| 26 | prof_begin_date | 是 |  |  |
| 27 | prof_end_date | 是 |  |  |
| 28 | prof_type | 是 |  |  |
| 29 | pf_risk_level | 是 |  |  |
| 30 | pf_risk_begin_date | 是 |  |  |
| 31 | pf_risk_end_date | 是 |  |  |
| 32 | en_pf_invest_kind | 是 |  |  |
| 33 | en_pf_invest_term | 是 |  |  |
| 34 | corp_risk_level | 是 |  |  |
| 35 | corp_begin_date | 是 |  |  |
| 36 | corp_end_date | 是 |  |  |
| 37 | en_maxdeficit_rate | 是 |  |  |
| 38 | organ_flag | 是 |  |  |
| 39 | min_rank_flag | 是 |  |  |
| 40 | client_income_type | 是 |  |  |
| 41 | birthday | 是 |  |  |
| 42 | transaction_no | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sms_client_preferctrl | 默认 | 是 | client_id, client_id |
| idx_sms_client_preferctrl | 默认 | 是 | client_id, client_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sms_client_preferctrl | client_id, client_id |
| idx_sms_client_preferctrl | client_id, client_id |

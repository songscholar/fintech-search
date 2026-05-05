# setttouftfinexeapply - 证券融资行权申请表

**表对象ID**: 3012
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 74 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | contract_id | 是 |  |  |
| 4 | join_contract_id | 是 |  |  |
| 5 | finexe_contract_type | 是 |  |  |
| 6 | branch_no | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | client_id | 是 |  |  |
| 9 | stock_account | 是 |  |  |
| 10 | exchange_type | 是 |  |  |
| 11 | sopt_code | 是 |  |  |
| 12 | stock_code | 是 |  |  |
| 13 | stock_type | 是 |  |  |
| 14 | entrust_balance | 是 |  |  |
| 15 | entrust_amount | 是 |  |  |
| 16 | repaid_balance | 是 |  |  |
| 17 | date_back | 是 |  |  |
| 18 | back_balance | 是 |  |  |
| 19 | finexe_apply_type | 是 |  |  |
| 20 | finexe_apply_status | 是 |  |  |
| 21 | expire_year_rate | 是 |  |  |
| 22 | orig_real_date_back | 是 |  |  |
| 23 | orig_real_year_rate | 是 |  |  |
| 24 | orig_back_balance | 是 |  |  |
| 25 | audit_remark | 是 |  |  |
| 26 | remark | 是 |  |  |
| 27 | date_clear | 是 |  |  |
| 28 | position_str | 是 |  |  |
| 29 | client_group | 是 |  |  |
| 30 | room_code | 是 |  |  |
| 31 | asset_prop | 是 |  |  |
| 32 | limit_flag | 是 |  |  |
| 33 | corp_client_group | 是 |  |  |
| 34 | corp_risk_level | 是 |  |  |
| 35 | asset_level | 是 |  |  |
| 36 | stock_name | 是 |  |  |
| 37 | uft_data_change_status | 是 |  |  |
| 38 | init_date | 是 |  |  |
| 39 | serial_no | 是 |  |  |
| 40 | contract_id | 是 |  |  |
| 41 | join_contract_id | 是 |  |  |
| 42 | finexe_contract_type | 是 |  |  |
| 43 | branch_no | 是 |  |  |
| 44 | fund_account | 是 |  |  |
| 45 | client_id | 是 |  |  |
| 46 | stock_account | 是 |  |  |
| 47 | exchange_type | 是 |  |  |
| 48 | sopt_code | 是 |  |  |
| 49 | stock_code | 是 |  |  |
| 50 | stock_type | 是 |  |  |
| 51 | entrust_balance | 是 |  |  |
| 52 | entrust_amount | 是 |  |  |
| 53 | repaid_balance | 是 |  |  |
| 54 | date_back | 是 |  |  |
| 55 | back_balance | 是 |  |  |
| 56 | finexe_apply_type | 是 |  |  |
| 57 | finexe_apply_status | 是 |  |  |
| 58 | expire_year_rate | 是 |  |  |
| 59 | orig_real_date_back | 是 |  |  |
| 60 | orig_real_year_rate | 是 |  |  |
| 61 | orig_back_balance | 是 |  |  |
| 62 | audit_remark | 是 |  |  |
| 63 | remark | 是 |  |  |
| 64 | date_clear | 是 |  |  |
| 65 | position_str | 是 |  |  |
| 66 | client_group | 是 |  |  |
| 67 | room_code | 是 |  |  |
| 68 | asset_prop | 是 |  |  |
| 69 | limit_flag | 是 |  |  |
| 70 | corp_client_group | 是 |  |  |
| 71 | corp_risk_level | 是 |  |  |
| 72 | asset_level | 是 |  |  |
| 73 | stock_name | 是 |  |  |
| 74 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settfinexeapply | 默认 | 是 | init_date, serial_no, init_date, serial_no |
| idx_settfinexeapply_pos | 默认 | 是 | position_str, position_str |
| idx_settfinexeapply | 默认 | 是 | init_date, serial_no, init_date, serial_no |
| idx_settfinexeapply_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settfinexeapply_pos | position_str, position_str |
| idx_settfinexeapply_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2022-01-26 16:37 | 8.26.2.1 | 郑天翔 | 新增 |
| 2022-01-26 16:37 | 8.26.2.1 | 郑天翔 | 新增 |

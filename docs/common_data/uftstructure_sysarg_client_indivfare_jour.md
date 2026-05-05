# client_indivfare_jour - 账户独立佣金签约流水表

**表对象ID**: 146
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | indiv_fare_kind | 否 |  |  |
| 9 | asset_prop | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | sign_date | 否 |  |  |
| 12 | sign_time | 否 |  |  |
| 13 | unsign_date | 否 |  |  |
| 14 | unsign_time | 否 |  |  |
| 15 | begin_date | 否 |  |  |
| 16 | end_date | 否 |  |  |
| 17 | position_str | 否 |  |  |
| 18 | op_branch_no | 否 |  |  |
| 19 | operator_no | 否 |  |  |
| 20 | op_entrust_way | 否 |  |  |
| 21 | op_station | 否 |  |  |
| 22 | client_name | 否 | H |  |
| 23 | corp_client_group | 否 | H |  |
| 24 | client_group | 否 | H |  |
| 25 | room_code | 否 | H |  |
| 26 | limit_flag | 否 | H |  |
| 27 | client_prop | 否 | H |  |
| 28 | asset_level | 否 | H |  |
| 29 | risk_level | 否 | H |  |
| 30 | corp_risk_level | 否 | H |  |
| 31 | init_date | 否 |  |  |
| 32 | serial_no | 否 |  |  |
| 33 | curr_date | 否 |  |  |
| 34 | curr_time | 否 |  |  |
| 35 | fund_account | 否 |  |  |
| 36 | client_id | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | indiv_fare_kind | 否 |  |  |
| 39 | asset_prop | 否 |  |  |
| 40 | remark | 否 |  |  |
| 41 | sign_date | 否 |  |  |
| 42 | sign_time | 否 |  |  |
| 43 | unsign_date | 否 |  |  |
| 44 | unsign_time | 否 |  |  |
| 45 | begin_date | 否 |  |  |
| 46 | end_date | 否 |  |  |
| 47 | position_str | 否 |  |  |
| 48 | op_branch_no | 否 |  |  |
| 49 | operator_no | 否 |  |  |
| 50 | op_entrust_way | 否 |  |  |
| 51 | op_station | 否 |  |  |
| 52 | client_name | 否 | H |  |
| 53 | corp_client_group | 否 | H |  |
| 54 | client_group | 否 | H |  |
| 55 | room_code | 否 | H |  |
| 56 | limit_flag | 否 | H |  |
| 57 | client_prop | 否 | H |  |
| 58 | asset_level | 否 | H |  |
| 59 | risk_level | 否 | H |  |
| 60 | corp_risk_level | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_cindivfarejour_pos | 默认 | 是 | position_str, position_str |
| idx_cindivfarejour_acct | 默认 | 是 | fund_account, fund_account |
| idx_cindivfarejour_client | 默认 | 是 | client_id, client_id |
| uk_rpt_clientindivfarejour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_clientindivfarejour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_cindivfarejour_pos | 默认 | 是 | position_str, position_str |
| idx_cindivfarejour_acct | 默认 | 是 | fund_account, fund_account |
| idx_cindivfarejour_client | 默认 | 是 | client_id, client_id |
| uk_rpt_clientindivfarejour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_clientindivfarejour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_cindivfarejour_pos | position_str, position_str |
| idx_cindivfarejour_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1019 | 周兆军 | 维护历史表 |
| 2025-05-08 13:39:24 | 3.0.6.135 | 常行 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1019 | 周兆军 | 维护历史表 |
| 2025-05-08 13:39:24 | 3.0.6.135 | 常行 | 新增表 |

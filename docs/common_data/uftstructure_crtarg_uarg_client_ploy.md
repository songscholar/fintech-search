# uarg_client_ploy - 客户平仓策略设置表2

**表对象ID**: 7120
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | payoffploy_no | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | date_clear | 否 |  |  |
| 7 | clientploy_id | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | poptarget_value | 否 |  |  |
| 10 | popdeal_flag | 否 |  |  |
| 11 | create_date | 否 |  |  |
| 12 | create_time | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  |  |
| 17 | client_group | 否 | H |  |
| 18 | room_code | 否 | H |  |
| 19 | asset_prop | 否 | H |  |
| 20 | client_prop | 否 | H |  |
| 21 | limit_flag | 否 | H |  |
| 22 | risk_level | 否 | H |  |
| 23 | corp_client_group | 否 | H |  |
| 24 | corp_risk_level | 否 | H |  |
| 25 | asset_level | 否 | H |  |
| 26 | client_name | 否 | H |  |
| 27 | init_date | 否 |  |  |
| 28 | client_id | 否 |  |  |
| 29 | fund_account | 否 |  |  |
| 30 | payoffploy_no | 否 |  |  |
| 31 | transaction_no | 否 |  |  |
| 32 | date_clear | 否 |  |  |
| 33 | clientploy_id | 否 |  |  |
| 34 | branch_no | 否 |  |  |
| 35 | poptarget_value | 否 |  |  |
| 36 | popdeal_flag | 否 |  |  |
| 37 | create_date | 否 |  |  |
| 38 | create_time | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | position_str | 否 |  |  |
| 43 | client_group | 否 | H |  |
| 44 | room_code | 否 | H |  |
| 45 | asset_prop | 否 | H |  |
| 46 | client_prop | 否 | H |  |
| 47 | limit_flag | 否 | H |  |
| 48 | risk_level | 否 | H |  |
| 49 | corp_client_group | 否 | H |  |
| 50 | corp_risk_level | 否 | H |  |
| 51 | asset_level | 否 | H |  |
| 52 | client_name | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_client_ploy | 默认 | 否 | clientploy_id, clientploy_id |
| idx_uarg_client_ploy | 默认 | 否 |  |
| idx_uarg_client_ploy | ART | 是 | clientploy_id, clientploy_id |
| uk_rpt_uargclientploy | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_uargclientploy_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_uargclientploy_tolast | ART | 是 | date_clear, date_clear |
| idx_uarg_client_ploy | 默认 | 否 | clientploy_id, clientploy_id |
| idx_uarg_client_ploy | 默认 | 否 |  |
| idx_uarg_client_ploy | ART | 是 | clientploy_id, clientploy_id |
| uk_rpt_uargclientploy | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_uargclientploy_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_uargclientploy_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_client_ploy | clientploy_id, clientploy_id |
| idx_uarg_client_ploy | clientploy_id, clientploy_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-07-08 14:35:03 | 3.0.6.114 | 李奕轩 | 物理表uarg_client_ploy，增加索引(idx_uarg_client_ploy:[clientploy_id... |
| 2025-07-08 14:26:52 | 3.0.6.114 | 李奕轩 | 物理表uarg_client_ploy，删除了表索引(idx_uarg_client_ploy);
 |
| 2025-04-29 17:48:42 | 3.0.6.108 | 李奕轩 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-07-08 14:35:03 | 3.0.6.114 | 李奕轩 | 物理表uarg_client_ploy，增加索引(idx_uarg_client_ploy:[clientploy_id... |
| 2025-07-08 14:26:52 | 3.0.6.114 | 李奕轩 | 物理表uarg_client_ploy，删除了表索引(idx_uarg_client_ploy);
 |
| 2025-04-29 17:48:42 | 3.0.6.108 | 李奕轩 | 新增表 |

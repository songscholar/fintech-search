# client_strategyfare_jour - 账户策略服务佣金流水表

**表对象ID**: 111
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | strategyfare_id | 否 |  |  |
| 7 | sign_date | 否 |  |  |
| 8 | sign_time | 否 |  |  |
| 9 | unsign_date | 否 |  |  |
| 10 | unsign_time | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 13 | curr_date | 否 |  |  |
| 14 | curr_time | 否 |  |  |
| 15 | op_branch_no | 否 |  |  |
| 16 | operator_no | 否 |  |  |
| 17 | op_entrust_way | 否 |  |  |
| 18 | op_station | 否 |  |  |
| 19 | asset_prop | 否 |  |  |
| 20 | client_name | 否 | H |  |
| 21 | corp_client_group | 否 | H |  |
| 22 | client_group | 否 | H |  |
| 23 | room_code | 否 | H |  |
| 24 | limit_flag | 否 | H |  |
| 25 | client_prop | 否 | H |  |
| 26 | asset_level | 否 | H |  |
| 27 | risk_level | 否 | H |  |
| 28 | corp_risk_level | 否 | H |  |
| 29 | init_date | 否 |  |  |
| 30 | serial_no | 否 |  |  |
| 31 | fund_account | 否 |  |  |
| 32 | client_id | 否 |  |  |
| 33 | branch_no | 否 |  |  |
| 34 | strategyfare_id | 否 |  |  |
| 35 | sign_date | 否 |  |  |
| 36 | sign_time | 否 |  |  |
| 37 | unsign_date | 否 |  |  |
| 38 | unsign_time | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 41 | curr_date | 否 |  |  |
| 42 | curr_time | 否 |  |  |
| 43 | op_branch_no | 否 |  |  |
| 44 | operator_no | 否 |  |  |
| 45 | op_entrust_way | 否 |  |  |
| 46 | op_station | 否 |  |  |
| 47 | asset_prop | 否 |  |  |
| 48 | client_name | 否 | H |  |
| 49 | corp_client_group | 否 | H |  |
| 50 | client_group | 否 | H |  |
| 51 | room_code | 否 | H |  |
| 52 | limit_flag | 否 | H |  |
| 53 | client_prop | 否 | H |  |
| 54 | asset_level | 否 | H |  |
| 55 | risk_level | 否 | H |  |
| 56 | corp_risk_level | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_client_strategyfare_jour_pos | 默认 | 是 | position_str, position_str |
| idx_client_strategyfare_jour_sbi | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_client_strategyfare_jour_fs | 默认 | 是 | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_client_strategyfare_jour_f | 默认 | 是 | fund_account, fund_account |
| idx_client_strategyfare_jour_c | 默认 | 是 | client_id, client_id |
| uk_rpt_clientstrategyfarejour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_clientstrategyfarejour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_uarg_client_strategyfare_jour_pos | 默认 | 是 | position_str, position_str |
| idx_client_strategyfare_jour_sbi | 默认 | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_client_strategyfare_jour_fs | 默认 | 是 | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_client_strategyfare_jour_f | 默认 | 是 | fund_account, fund_account |
| idx_client_strategyfare_jour_c | 默认 | 是 | client_id, client_id |
| uk_rpt_clientstrategyfarejour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_clientstrategyfarejour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_client_strategyfare_jour_pos | position_str, position_str |
| idx_client_strategyfare_jour_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1019 | 周兆军 | 维护历史表 |
| 2025-02-14 13:35:29 | 3.0.6.22 | 李想 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1019 | 周兆军 | 维护历史表 |
| 2025-02-14 13:35:29 | 3.0.6.22 | 李想 | 新增表 |

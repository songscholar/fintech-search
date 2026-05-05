# strategyfare_contract_jour - 策略服务佣金签约信息流水表

**表对象ID**: 114
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | strategyfare_id | 否 |  |  |
| 9 | sign_date | 否 |  |  |
| 10 | sign_time | 否 |  |  |
| 11 | unsign_date | 否 |  |  |
| 12 | unsign_time | 否 |  |  |
| 13 | op_branch_no | 否 |  |  |
| 14 | operator_no | 否 |  |  |
| 15 | op_entrust_way | 否 |  |  |
| 16 | op_station | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |
| 19 | client_name | 否 | H |  |
| 20 | corp_client_group | 否 | H |  |
| 21 | client_group | 否 | H |  |
| 22 | room_code | 否 | H |  |
| 23 | asset_prop | 否 | H |  |
| 24 | limit_flag | 否 | H |  |
| 25 | client_prop | 否 | H |  |
| 26 | asset_level | 否 | H |  |
| 27 | risk_level | 否 | H |  |
| 28 | corp_risk_level | 否 | H |  |
| 29 | init_date | 否 |  |  |
| 30 | serial_no | 否 |  |  |
| 31 | curr_date | 否 |  |  |
| 32 | curr_time | 否 |  |  |
| 33 | fund_account | 否 |  |  |
| 34 | client_id | 否 |  |  |
| 35 | branch_no | 否 |  |  |
| 36 | strategyfare_id | 否 |  |  |
| 37 | sign_date | 否 |  |  |
| 38 | sign_time | 否 |  |  |
| 39 | unsign_date | 否 |  |  |
| 40 | unsign_time | 否 |  |  |
| 41 | op_branch_no | 否 |  |  |
| 42 | operator_no | 否 |  |  |
| 43 | op_entrust_way | 否 |  |  |
| 44 | op_station | 否 |  |  |
| 45 | remark | 否 |  |  |
| 46 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |
| 47 | client_name | 否 | H |  |
| 48 | corp_client_group | 否 | H |  |
| 49 | client_group | 否 | H |  |
| 50 | room_code | 否 | H |  |
| 51 | asset_prop | 否 | H |  |
| 52 | limit_flag | 否 | H |  |
| 53 | client_prop | 否 | H |  |
| 54 | asset_level | 否 | H |  |
| 55 | risk_level | 否 | H |  |
| 56 | corp_risk_level | 否 | H |  |

## 索引（共 24 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strategyfare_contract_jour_pos | 默认 | 否 |  |
| idx_strategyfare_contract_jour_sbi | 默认 | 否 |  |
| idx_strategyfare_contract_jour_fs | 默认 | 否 |  |
| idx_strategyfare_contract_jour_f | 默认 | 否 |  |
| idx_strategyfare_contract_jour_c | 默认 | 否 |  |
| idx_strategyfare_contract_jour_pos | ART | 是 | position_str, position_str |
| idx_strategyfare_contract_jour_sbi | ART | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_strategyfare_contract_jour_fs | ART | 是 | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_strategyfare_contract_jour_f | ART | 是 | fund_account, fund_account |
| idx_strategyfare_contract_jour_c | ART | 是 | client_id, client_id |
| uk_rpt_strategyfarecontractjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_strategyfarecontractjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_strategyfare_contract_jour_pos | 默认 | 否 |  |
| idx_strategyfare_contract_jour_sbi | 默认 | 否 |  |
| idx_strategyfare_contract_jour_fs | 默认 | 否 |  |
| idx_strategyfare_contract_jour_f | 默认 | 否 |  |
| idx_strategyfare_contract_jour_c | 默认 | 否 |  |
| idx_strategyfare_contract_jour_pos | ART | 是 | position_str, position_str |
| idx_strategyfare_contract_jour_sbi | ART | 是 | serial_no, branch_no, init_date, serial_no, branch_no, init_date |
| idx_strategyfare_contract_jour_fs | ART | 是 | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_strategyfare_contract_jour_f | ART | 是 | fund_account, fund_account |
| idx_strategyfare_contract_jour_c | ART | 是 | client_id, client_id |
| uk_rpt_strategyfarecontractjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_strategyfarecontractjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strategyfare_contract_jour_pos | position_str, position_str |
| idx_strategyfare_contract_jour_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 14:56:07 | 3.0.2.103 | taocong45644 | 当前表strategyfare_contract_jour，修改了索引idx_strategyfare_contract... |
| 2025-02-14 14:14:27 | 3.0.6.25 | 李想 | 新增表 |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 14:56:07 | 3.0.2.103 | taocong45644 | 当前表strategyfare_contract_jour，修改了索引idx_strategyfare_contract... |
| 2025-02-14 14:14:27 | 3.0.6.25 | 李想 | 新增表 |

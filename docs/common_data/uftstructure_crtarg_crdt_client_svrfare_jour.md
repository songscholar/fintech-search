# crdt_client_svrfare_jour - 信用账户特殊服务佣金流水表

**表对象ID**: 7072
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | svr_fare_kind | 否 |  |  |
| 9 | begin_date | 否 |  |  |
| 10 | end_date | 否 |  |  |
| 11 | op_branch_no | 否 |  |  |
| 12 | operator_no | 否 |  |  |
| 13 | op_entrust_way | 否 |  |  |
| 14 | op_station | 否 |  |  |
| 15 | sign_date | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |
| 18 | client_group | 否 | H |  |
| 19 | room_code | 否 | H |  |
| 20 | asset_prop | 否 | H |  |
| 21 | limit_flag | 否 | H |  |
| 22 | risk_level | 否 | H |  |
| 23 | corp_client_group | 否 | H |  |
| 24 | corp_risk_level | 否 | H |  |
| 25 | asset_level | 否 | H |  |
| 26 | client_name | 否 | H |  |
| 27 | client_prop | 否 | H |  |
| 28 | init_date | 否 |  |  |
| 29 | serial_no | 否 |  |  |
| 30 | curr_date | 否 |  |  |
| 31 | curr_time | 否 |  |  |
| 32 | client_id | 否 |  |  |
| 33 | fund_account | 否 |  |  |
| 34 | branch_no | 否 |  |  |
| 35 | svr_fare_kind | 否 |  |  |
| 36 | begin_date | 否 |  |  |
| 37 | end_date | 否 |  |  |
| 38 | op_branch_no | 否 |  |  |
| 39 | operator_no | 否 |  |  |
| 40 | op_entrust_way | 否 |  |  |
| 41 | op_station | 否 |  |  |
| 42 | sign_date | 否 |  |  |
| 43 | remark | 否 |  |  |
| 44 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |
| 45 | client_group | 否 | H |  |
| 46 | room_code | 否 | H |  |
| 47 | asset_prop | 否 | H |  |
| 48 | limit_flag | 否 | H |  |
| 49 | risk_level | 否 | H |  |
| 50 | corp_client_group | 否 | H |  |
| 51 | corp_risk_level | 否 | H |  |
| 52 | asset_level | 否 | H |  |
| 53 | client_name | 否 | H |  |
| 54 | client_prop | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_client_svrfare_jour_pos | ART | 是 | position_str, position_str |
| uk_rpt_crdtclientsvrfarejour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_crdtclientsvrfarejour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_crdt_client_svrfare_jour_pos | ART | 是 | position_str, position_str |
| uk_rpt_crdtclientsvrfarejour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_crdtclientsvrfarejour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_client_svrfare_jour_pos | position_str, position_str |
| idx_crdt_client_svrfare_jour_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-14 16:37:17 | 3.0.6.35 | 常行 | 新增表crdt_client_svrfare_jour |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-14 16:37:17 | 3.0.6.35 | 常行 | 新增表crdt_client_svrfare_jour |

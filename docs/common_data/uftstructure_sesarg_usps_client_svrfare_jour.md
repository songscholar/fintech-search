# usps_client_svrfare_jour - 账户特殊服务佣金流水表

**表对象ID**: 5005
**所属模块**: sesarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

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
| 17 | position_str | 否 |  | init_date(8)+serial_no(10)+branch_no(10) |
| 18 | init_date | 否 |  |  |
| 19 | serial_no | 否 |  |  |
| 20 | curr_date | 否 |  |  |
| 21 | curr_time | 否 |  |  |
| 22 | client_id | 否 |  |  |
| 23 | fund_account | 否 |  |  |
| 24 | branch_no | 否 |  |  |
| 25 | svr_fare_kind | 否 |  |  |
| 26 | begin_date | 否 |  |  |
| 27 | end_date | 否 |  |  |
| 28 | op_branch_no | 否 |  |  |
| 29 | operator_no | 否 |  |  |
| 30 | op_entrust_way | 否 |  |  |
| 31 | op_station | 否 |  |  |
| 32 | sign_date | 否 |  |  |
| 33 | remark | 否 |  |  |
| 34 | position_str | 否 |  | init_date(8)+serial_no(10)+branch_no(10) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_client_svrfare_jour_pos | 默认 | 否 |  |
| idx_usps_client_svrfare_jour_pos | ART | 是 | position_str, position_str |
| idx_usps_client_svrfare_jour_pos | 默认 | 否 |  |
| idx_usps_client_svrfare_jour_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_client_svrfare_jour_pos | position_str, position_str |
| idx_usps_client_svrfare_jour_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:21:10 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:17:28 | 3.0.2.84 | taocong45644 | 当前表usps_client_svrfare_jour，修改了索引idx_usps_client_svrfare_jou... |
| 2025-02-14 16:37:48 | 3.0.6.35 | 常行 | 新增表usps_client_svrfare_jour |
| 2026-03-05 17:21:10 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:17:28 | 3.0.2.84 | taocong45644 | 当前表usps_client_svrfare_jour，修改了索引idx_usps_client_svrfare_jou... |
| 2025-02-14 16:37:48 | 3.0.6.35 | 常行 | 新增表usps_client_svrfare_jour |

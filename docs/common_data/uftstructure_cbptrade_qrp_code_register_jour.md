# qrp_code_register_jour - 报价回购签约信息流水表

**表对象ID**: 2401
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | sign_src | 否 |  |  |
| 10 | resign_date | 否 |  |  |
| 11 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 12 | client_name | 否 | H |  |
| 13 | corp_client_group | 否 | H |  |
| 14 | client_group | 否 | H |  |
| 15 | room_code | 否 | H |  |
| 16 | asset_prop | 否 | H |  |
| 17 | limit_flag | 否 | H |  |
| 18 | client_prop | 否 | H |  |
| 19 | asset_level | 否 | H |  |
| 20 | risk_level | 否 | H |  |
| 21 | corp_risk_level | 否 | H |  |
| 22 | stock_type | 否 | H |  |
| 23 | stock_name | 否 | H |  |
| 24 | sub_stock_type | 否 | H |  |
| 25 | init_date | 否 |  |  |
| 26 | serial_no | 否 |  |  |
| 27 | branch_no | 否 |  |  |
| 28 | exchange_type | 否 |  |  |
| 29 | stock_code | 否 |  |  |
| 30 | fund_account | 否 |  |  |
| 31 | client_id | 否 |  |  |
| 32 | remark | 否 |  |  |
| 33 | sign_src | 否 |  |  |
| 34 | resign_date | 否 |  |  |
| 35 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 36 | client_name | 否 | H |  |
| 37 | corp_client_group | 否 | H |  |
| 38 | client_group | 否 | H |  |
| 39 | room_code | 否 | H |  |
| 40 | asset_prop | 否 | H |  |
| 41 | limit_flag | 否 | H |  |
| 42 | client_prop | 否 | H |  |
| 43 | asset_level | 否 | H |  |
| 44 | risk_level | 否 | H |  |
| 45 | corp_risk_level | 否 | H |  |
| 46 | stock_type | 否 | H |  |
| 47 | stock_name | 否 | H |  |
| 48 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrp_code_register_jour | ART | 是 | position_str, position_str |
| uk_rpt_qrpcoderegisterjour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_qrpcoderegisterjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_qrp_code_register_jour | ART | 是 | position_str, position_str |
| uk_rpt_qrpcoderegisterjour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_qrpcoderegisterjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrp_code_register_jour | position_str, position_str |
| idx_qrp_code_register_jour | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:45:20 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-30 14:29:40 | V3.0.2.6 | 洪略 | 历史表字段需要加上H标记 |
| 2025-11-17 11:54:25 | V3.0.2.5 | 洪略 | 补齐历史表资源 |
| 2025-02-20 11:33:50 | V3.0.5.1022 | 李想 | 新增表 |
| 2026-03-04 15:45:20 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-30 14:29:40 | V3.0.2.6 | 洪略 | 历史表字段需要加上H标记 |
| 2025-11-17 11:54:25 | V3.0.2.5 | 洪略 | 补齐历史表资源 |
| 2025-02-20 11:33:50 | V3.0.5.1022 | 李想 | 新增表 |

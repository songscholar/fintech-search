# srp_risk_list - 股票质押风险名单表

**表对象ID**: 2615
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | id_kind | 否 |  |  |
| 2 | id_no | 否 |  |  |
| 3 | srp_risk_type | 否 |  |  |
| 4 | full_name | 否 |  |  |
| 5 | risk_enddate | 否 |  |  |
| 6 | remark | 否 |  |  |
| 7 | status | 否 |  |  |
| 8 | risk_record_source | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | break_occur_date | 否 |  |  |
| 11 | risk_begindate | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | id_kind | 否 |  |  |
| 14 | id_no | 否 |  |  |
| 15 | srp_risk_type | 否 |  |  |
| 16 | full_name | 否 |  |  |
| 17 | risk_enddate | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | status | 否 |  |  |
| 20 | risk_record_source | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | break_occur_date | 否 |  |  |
| 23 | risk_begindate | 否 |  |  |
| 24 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srprisklist | ART | 是 | id_no, id_kind, full_name, srp_risk_type, stock_code, risk_record_source, id_no, id_kind, full_name, srp_risk_type, stock_code, risk_record_source |
| idx_srprisklist | ART | 是 | id_no, id_kind, full_name, srp_risk_type, stock_code, risk_record_source, id_no, id_kind, full_name, srp_risk_type, stock_code, risk_record_source |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srprisklist | id_no, id_kind, full_name, srp_risk_type, stock_code, risk_record_source, id_no, id_kind, full_name, srp_risk_type, stock_code, risk_record_source |
| idx_srprisklist | id_no, id_kind, full_name, srp_risk_type, stock_code, risk_record_source, id_no, id_kind, full_name, srp_risk_type, stock_code, risk_record_source |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:49:59 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-09-17 14:39:47 | 3.0.2.3 | 洪略 | 表空间hs_uft更改为hs_uarg，数据库存储介质DB改成DB+MDB |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:20 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:49:59 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-09-17 14:39:47 | 3.0.2.3 | 洪略 | 表空间hs_uft更改为hs_uarg，数据库存储介质DB改成DB+MDB |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:20 | 3.0.3.1 | wuxd | 新增 |

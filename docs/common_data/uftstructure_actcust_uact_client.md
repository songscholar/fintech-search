# uact_client - 客户基本信息

**表对象ID**: 500
**所属模块**: actcust
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | client_status | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | id_kind | 否 |  |  |
| 5 | id_no | 否 |  |  |
| 6 | id_begindate | 否 |  |  |
| 7 | id_enddate | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | full_name | 否 |  |  |
| 10 | corp_client_group | 否 |  |  |
| 11 | corp_risk_level | 否 |  |  |
| 12 | organ_flag | 否 |  |  |
| 13 | open_date | 否 |  |  |
| 14 | client_name | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | client_status | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | id_kind | 否 |  |  |
| 19 | id_no | 否 |  |  |
| 20 | id_begindate | 否 |  |  |
| 21 | id_enddate | 否 |  |  |
| 22 | branch_no | 否 |  |  |
| 23 | full_name | 否 |  |  |
| 24 | corp_client_group | 否 |  |  |
| 25 | corp_risk_level | 否 |  |  |
| 26 | organ_flag | 否 |  |  |
| 27 | open_date | 否 |  |  |
| 28 | client_name | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uact_client | ART | 是 | client_id, client_id |
| idx_uact_client_idno | ART | 是 | id_no, full_name, id_kind, id_no, full_name, id_kind |
| idx_uact_client | ART | 是 | client_id, client_id |
| idx_uact_client_idno | ART | 是 | id_no, full_name, id_kind, id_no, full_name, id_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uact_client | client_id, client_id |
| idx_uact_client | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:33:14 | V3.0.2.5 | taocong45644 | 勾选回库使用索引 |
| 2024-12-02 19:54:52 | V3.0.6.4 | 沈勋 | 新增idx_uact_client_idno索引 |
| 2024-09-23 10:53:11 | V3.0.1.2 | 张明月 | 物理表uact_client，添加了表字段(open_date);
物理表uact_client，添加了表字段(org... |
| 2024-09-12 20:01:24 | V3.0.1.1 | 曾剑辉 | 物理表uact_client，添加了表字段(id_begindate);
物理表uact_client，添加了表字段(... |
| 2024-07-18 09:52:57 | V3.0.1.1 | 王锦汇 | 物理表uact_client，添加了表字段(id_kind);
物理表uact_client，添加了表字段(id_no... |
| 2023-11-27 09:50:25 | V3.0.1.1 | 沈勋 | 新增表结构 |
| 2026-03-06 16:33:14 | V3.0.2.5 | taocong45644 | 勾选回库使用索引 |
| 2024-12-02 19:54:52 | V3.0.6.4 | 沈勋 | 新增idx_uact_client_idno索引 |
| 2024-09-23 10:53:11 | V3.0.1.2 | 张明月 | 物理表uact_client，添加了表字段(open_date);
物理表uact_client，添加了表字段(org... |
| 2024-09-12 20:01:24 | V3.0.1.1 | 曾剑辉 | 物理表uact_client，添加了表字段(id_begindate);
物理表uact_client，添加了表字段(... |
| 2024-07-18 09:52:57 | V3.0.1.1 | 王锦汇 | 物理表uact_client，添加了表字段(id_kind);
物理表uact_client，添加了表字段(id_no... |
| 2023-11-27 09:50:25 | V3.0.1.1 | 沈勋 | 新增表结构 |

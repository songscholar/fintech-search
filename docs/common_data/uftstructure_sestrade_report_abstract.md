# report_abstract - 虚拟股东申报账号

**表对象ID**: 5700
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | abstract_account | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | report_account | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | holder_level | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | abstract_account | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | report_account | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | holder_level | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_report_abstractctrl | ART | 是 | abstract_account, branch_no, exchange_type, abstract_account, branch_no, exchange_type |
| idx_report_abstractctrl_account | ART | 是 | report_account, report_account |
| idx_report_abstractctrl | ART | 是 | abstract_account, branch_no, exchange_type, abstract_account, branch_no, exchange_type |
| idx_report_abstractctrl_account | ART | 是 | report_account, report_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_report_abstractctrl | abstract_account, branch_no, exchange_type, abstract_account, branch_no, exchange_type |
| idx_report_abstractctrl | abstract_account, branch_no, exchange_type, abstract_account, branch_no, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:35:20 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:18:19 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2026-03-09 14:35:20 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:18:19 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |

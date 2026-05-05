# csdc_acode_acct - 中登一码通账户表

**表对象ID**: 5547
**所属模块**: sestrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | csdc_acode_account | 否 |  |  |
| 2 | csdc_client_name | 否 |  |  |
| 3 | csdc_id_kind | 否 |  |  |
| 4 | csdc_id_no | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | csdc_acode_account | 否 |  |  |
| 7 | csdc_client_name | 否 |  |  |
| 8 | csdc_id_kind | 否 |  |  |
| 9 | csdc_id_no | 否 |  |  |
| 10 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_csdcacodeacct_id | ART | 是 | csdc_acode_account, csdc_acode_account |
| idx_csdcacodeacct_id | ART | 是 | csdc_acode_account, csdc_acode_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_csdcacodeacct_id | csdc_acode_account, csdc_acode_account |
| idx_csdcacodeacct_id | csdc_acode_account, csdc_acode_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:01:41 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:15:25 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-06-27 11:28:16 | 3.0.2.22 | 董乾坤 | 新增 |
| 2026-03-09 14:01:41 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:15:25 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-06-27 11:28:16 | 3.0.2.22 | 董乾坤 | 新增 |

# uqms_ststock_quota_used - 风险警示股使用信息

**表对象ID**: 1601
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | used_quota | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | acode_account | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | used_quota | 否 |  |  |
| 10 | client_id | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uqms_ststock_quota_used | ART | 是 | acode_account, exchange_type, stock_code, acode_account, exchange_type, stock_code |
| uk_uqms_ststock_quota_used | ART | 是 | acode_account, exchange_type, stock_code, acode_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_ststock_quota_used | acode_account, exchange_type, stock_code, acode_account, exchange_type, stock_code |
| idx_uqms_ststock_quota_used | acode_account, exchange_type, stock_code, acode_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:37:22 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-04-11 15:18:27 | 3.0.2.8 | 李江霖 | 修改物理表索引名 |
| 2024-12-14 16:54:06 | 3.0.2.7 | 祝丁恺 | 物理表uqms_ststock_quota_used，添加了表字段(client_id);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:37:22 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-04-11 15:18:27 | 3.0.2.8 | 李江霖 | 修改物理表索引名 |
| 2024-12-14 16:54:06 | 3.0.2.7 | 祝丁恺 | 物理表uqms_ststock_quota_used，添加了表字段(client_id);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

# uqms_ststock_quota_allocation - 风险警示股限额配置

**表对象ID**: 1600
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | total_quota | 否 |  |  |
| 5 | begin_date | 否 |  |  |
| 6 | end_date | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | acode_account | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | total_quota | 否 |  |  |
| 14 | begin_date | 否 |  |  |
| 15 | end_date | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | client_id | 否 |  |  |
| 18 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uqms_ststock_quota_al | ART | 是 | acode_account, exchange_type, stock_code, acode_account, exchange_type, stock_code |
| uk_uqms_ststock_quota_al | ART | 是 | acode_account, exchange_type, stock_code, acode_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_ststock_quota_al | acode_account, exchange_type, stock_code, acode_account, exchange_type, stock_code |
| idx_uqms_ststock_quota_al | acode_account, exchange_type, stock_code, acode_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:36:55 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-09-02 13:56:41 | 3.0.2.7 | tongck54118 | 支持表回物理库 |
| 2025-07-01 10:12:33 | 3.0.6.13 | tongck54118 | 物理表uqms_ststock_quota_allocation，添加了表字段(client_id);
物理表uqms... |
| 2025-04-11 15:18:27 | 3.0.2.6 | 李江霖 | 修改物理表索引名 |
| 2024-05-16 15:16:08 | 3.0.2.5 | 吴威 | 物理表uqms_ststock_quota_allocation，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:36:55 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-09-02 13:56:41 | 3.0.2.7 | tongck54118 | 支持表回物理库 |
| 2025-07-01 10:12:33 | 3.0.6.13 | tongck54118 | 物理表uqms_ststock_quota_allocation，添加了表字段(client_id);
物理表uqms... |
| 2025-04-11 15:18:27 | 3.0.2.6 | 李江霖 | 修改物理表索引名 |
| 2024-05-16 15:16:08 | 3.0.2.5 | 吴威 | 物理表uqms_ststock_quota_allocation，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

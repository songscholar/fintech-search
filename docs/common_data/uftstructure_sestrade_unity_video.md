# unity_video - 视频音频记录控制表

**表对象ID**: 5530
**所属模块**: sestrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | valid_date | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | valid_date | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_unity_videoctrl | ART | 是 | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |
| idx_unity_videoctrl | ART | 是 | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_unity_videoctrl | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |
| idx_unity_videoctrl | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:49:14 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-08-03 09:25:24 | 3.0.2.49 | honglue | 物理表unity_video，添加了表字段(valid_date);
 |
| 2024-09-23 11:05:26 | 3.0.2.48 | 张明月 | 物理表unity_video，添加了表字段(client_id);
 |
| 2024-05-29 21:29:58 | 3.0.2.18 | 祝丁恺 | 勾选不回库选项 |
| 2026-03-09 13:49:14 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-08-03 09:25:24 | 3.0.2.49 | honglue | 物理表unity_video，添加了表字段(valid_date);
 |
| 2024-09-23 11:05:26 | 3.0.2.48 | 张明月 | 物理表unity_video，添加了表字段(client_id);
 |
| 2024-05-29 21:29:58 | 3.0.2.18 | 祝丁恺 | 勾选不回库选项 |

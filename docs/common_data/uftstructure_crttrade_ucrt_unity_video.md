# ucrt_unity_video - 视频音频控制表

**表对象ID**: 7553
**所属模块**: crttrade
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
| idx_ucrt_unity_video | ART | 是 | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |
| idx_ucrt_unity_video | ART | 是 | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_unity_video | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |
| idx_ucrt_unity_video | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-07 10:23:18 | 3.0.6.1072 | tongck54118 | 所有表ucrt_unity_video，添加了表字段(client_id);
所有表ucrt_unity_video，... |
| 2024-05-16 15:09:44 | 3.0.2.9 | 叶慧军 | 开发工具告警的关联索引相关问题修改 |
| 2023-11-10 11:00:15 | V3.0.1.18 | 沈勋 | 新增表，支持适当性交易匹配 |
| 2025-10-07 10:23:18 | 3.0.6.1072 | tongck54118 | 所有表ucrt_unity_video，添加了表字段(client_id);
所有表ucrt_unity_video，... |
| 2024-05-16 15:09:44 | 3.0.2.9 | 叶慧军 | 开发工具告警的关联索引相关问题修改 |
| 2023-11-10 11:00:15 | V3.0.1.18 | 沈勋 | 新增表，支持适当性交易匹配 |

# usms_stbstd_holder - 三板合规证券账户表(交易管理)

**表对象ID**: 2831
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | seat_no | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | id_no | 否 |  |  |
| 6 | sub_risk_status | 否 |  |  |
| 7 | deal_type | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | seat_no | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | id_no | 否 |  |  |
| 14 | sub_risk_status | 否 |  |  |
| 15 | deal_type | 否 |  |  |
| 16 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usmsstbstdholder | 默认 | 是 | exchange_type, stock_code, stock_account, exchange_type, stock_code, stock_account |
| idx_usmsstbstdholder | 默认 | 是 | exchange_type, stock_code, stock_account, exchange_type, stock_code, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usmsstbstdholder | exchange_type, stock_code, stock_account, exchange_type, stock_code, stock_account |
| idx_usmsstbstdholder | exchange_type, stock_code, stock_account, exchange_type, stock_code, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-18 09:37:15 | 3.0.2.3 | 高志强 | 所有表usms_stbstd_holder，添加了表字段(transaction_no);
 |
| 2025-05-12 15:36:49 | 3.0.2.2004 | 高志强 | 新增 |
| 2025-08-18 09:37:15 | 3.0.2.3 | 高志强 | 所有表usms_stbstd_holder，添加了表字段(transaction_no);
 |
| 2025-05-12 15:36:49 | 3.0.2.2004 | 高志强 | 新增 |

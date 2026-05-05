# stb_dlsinfo - 股转摘牌转让信息表

**表对象ID**: 5569
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | entrust_bs | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | entrust_date | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | entrust_bs | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | entrust_date | 否 |  |  |
| 14 | date_clear | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stb_dlsinfo | ART | 是 | fund_account, stock_account, exchange_type, stock_code, entrust_bs, fund_account, stock_account, exchange_type, stock_code, entrust_bs |
| idx_stb_dlsinfo | ART | 是 | fund_account, stock_account, exchange_type, stock_code, entrust_bs, fund_account, stock_account, exchange_type, stock_code, entrust_bs |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stb_dlsinfo | fund_account, stock_account, exchange_type, stock_code, entrust_bs, fund_account, stock_account, exchange_type, stock_code, entrust_bs |
| idx_stb_dlsinfo | fund_account, stock_account, exchange_type, stock_code, entrust_bs, fund_account, stock_account, exchange_type, stock_code, entrust_bs |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:19:11 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:17:15 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-08-01 11:21:48 | 3.0.2.31 | 赵良梓 | 新增表结构 |
| 2026-03-09 14:19:11 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:17:15 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-08-01 11:21:48 | 3.0.2.31 | 赵良梓 | 新增表结构 |

# ucbp_account_limit_stkcode - 综合业务限售表

**表对象ID**: 2000
**所属模块**: cbparg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_account | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | cbplimit_type | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | modify_date | 否 |  |  |
| 6 | holder_name | 否 |  |  |
| 7 | stock_name | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | stock_account(20)+stock_code(8)+cbplimit_type(1) |
| 11 | stock_account | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | cbplimit_type | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | modify_date | 否 |  |  |
| 16 | holder_name | 否 |  |  |
| 17 | stock_name | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | stock_account(20)+stock_code(8)+cbplimit_type(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucbp_accountlimitstkcode | ART | 是 | stock_account, stock_code, cbplimit_type, stock_account, stock_code, cbplimit_type |
| idx_ucbp_accountlimitstkcode | ART | 是 | stock_account, stock_code, cbplimit_type, stock_account, stock_code, cbplimit_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucbp_accountlimitstkcode | stock_account, stock_code, cbplimit_type, stock_account, stock_code, cbplimit_type |
| idx_ucbp_accountlimitstkcode | stock_account, stock_code, cbplimit_type, stock_account, stock_code, cbplimit_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:38:28 | 3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-26 16:53:35 | 3.0.2.1 | 高志强 | 数据存储介质改为DB+MDB,数据库表空间改为HS_UARG_DATA |
| 2025-02-19 16:10:11 | V3.0.1.5 | 李想 | 物理表ucbp_account_limit_stkcode，添加了表字段(holder_name);
物理表ucbp_... |
| 2023-09-25 15:56:54 | V3.0.1.4 | 许琮擎 | 物理表ucbp_account_limit_stkcode，添加了表字段(modify_date);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-07-18 18:16 | 0.3.3.126 | 李海洋 | 修改表名称 |
| 2026-03-06 16:38:28 | 3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-26 16:53:35 | 3.0.2.1 | 高志强 | 数据存储介质改为DB+MDB,数据库表空间改为HS_UARG_DATA |
| 2025-02-19 16:10:11 | V3.0.1.5 | 李想 | 物理表ucbp_account_limit_stkcode，添加了表字段(holder_name);
物理表ucbp_... |
| 2023-09-25 15:56:54 | V3.0.1.4 | 许琮擎 | 物理表ucbp_account_limit_stkcode，添加了表字段(modify_date);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-07-18 18:16 | 0.3.3.126 | 李海洋 | 修改表名称 |

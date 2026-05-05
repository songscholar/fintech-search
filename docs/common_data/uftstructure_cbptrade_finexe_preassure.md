# finexe_preassure - 融资行权个人担保标的设置

**表对象ID**: 2333
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | assure_ratio | 否 |  |  |
| 8 | execv_assure_ratio | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_code(8) |
| 13 | fund_account | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | stock_type | 否 |  |  |
| 19 | assure_ratio | 否 |  |  |
| 20 | execv_assure_ratio | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_code(8) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexepreassure | 默认 | 否 |  |
| idx_finexepreassure | ART | 是 | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |
| idx_finexepreassure | 默认 | 否 |  |
| idx_finexepreassure | ART | 是 | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexepreassure | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |
| idx_finexepreassure | fund_account, exchange_type, stock_code, fund_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:28:30 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-03-12 10:58:58 | V3.0.5.1024 | 李想 | 物理表finexe_preassure，添加了表字段(update_date);
物理表finexe_preassur... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |
| 2026-03-04 15:28:30 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-03-12 10:58:58 | V3.0.5.1024 | 李想 | 物理表finexe_preassure，添加了表字段(update_date);
物理表finexe_preassur... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |

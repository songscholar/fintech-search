# qrp_code_register - 报价回购签约信息表

**表对象ID**: 2324
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | sign_src | 否 |  |  |
| 7 | resign_date | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | fund_account(18)+stock_code(8)+exchange_type(4) |
| 12 | branch_no | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | sign_src | 否 |  |  |
| 18 | resign_date | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | fund_account(18)+stock_code(8)+exchange_type(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrpcoderegister | 默认 | 否 |  |
| idx_qrpcoderegister | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_qrpcoderegister | 默认 | 否 |  |
| idx_qrpcoderegister | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrpcoderegister | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_qrpcoderegister | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:23:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 11:24:47 | V3.0.5.1020 | 李想 | 物理表qrp_code_register，添加了表字段(update_date);
物理表qrp_code_regis... |
| 2024-08-06 10:25:47 | V3.0.2.1003 | 骆鹏程 | 新增 |
| 2026-03-04 15:23:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 11:24:47 | V3.0.5.1020 | 李想 | 物理表qrp_code_register，添加了表字段(update_date);
物理表qrp_code_regis... |
| 2024-08-06 10:25:47 | V3.0.2.1003 | 骆鹏程 | 新增 |

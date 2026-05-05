# btoa_speacct - B转A特殊账户表

**表对象ID**: 5571
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | fund_account(18)+stock_account(20)+branch_no(6)+exchange_typ |
| 10 | branch_no | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+stock_account(20)+branch_no(6)+exchange_typ |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_spstkaccountctrl | ART | 是 | fund_account, stock_account, branch_no, exchange_type, stock_code, fund_account, stock_account, branch_no, exchange_type, stock_code |
| idx_spstkaccountctrl | ART | 是 | fund_account, stock_account, branch_no, exchange_type, stock_code, fund_account, stock_account, branch_no, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_spstkaccountctrl | fund_account, stock_account, branch_no, exchange_type, stock_code, fund_account, stock_account, branch_no, exchange_type, stock_code |
| idx_spstkaccountctrl | fund_account, stock_account, branch_no, exchange_type, stock_code, fund_account, stock_account, branch_no, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:21:01 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 16:06:43 | 3.0.6.14 | 李想 | 物理表btoa_speacct，添加了表字段(update_date);
物理表btoa_speacct，添加了表字段... |
| 2024-08-09 14:30:32 | 3.0.2.33 | 骆鹏程 | 新增 事务号， 修改对象号5880->5571 |
| 2026-03-09 14:21:01 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 16:06:43 | 3.0.6.14 | 李想 | 物理表btoa_speacct，添加了表字段(update_date);
物理表btoa_speacct，添加了表字段... |
| 2024-08-09 14:30:32 | 3.0.2.33 | 骆鹏程 | 新增 事务号， 修改对象号5880->5571 |

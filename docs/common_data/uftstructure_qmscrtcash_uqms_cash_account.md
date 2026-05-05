# uqms_cash_account - 头寸账户表

**表对象ID**: 1000
**所属模块**: qmscrtcash
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | cashgroup_prop | 否 |  |  |
| 4 | cashgroup_name | 否 |  |  |
| 5 | stock_account_sh | 否 |  |  |
| 6 | seat_no_sh | 否 |  |  |
| 7 | stock_account_sz | 否 |  |  |
| 8 | seat_no_sz | 否 |  |  |
| 9 | stock_account_stb | 否 |  |  |
| 10 | seat_no_stb | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | cash_fund_account | 否 |  |  |
| 13 | cash_client_id | 否 |  |  |
| 14 | cash_branch_no | 否 |  |  |
| 15 | cashgroup_no | 否 |  |  |
| 16 | company_no | 否 |  |  |
| 17 | cashgroup_prop | 否 |  |  |
| 18 | cashgroup_name | 否 |  |  |
| 19 | stock_account_sh | 否 |  |  |
| 20 | seat_no_sh | 否 |  |  |
| 21 | stock_account_sz | 否 |  |  |
| 22 | seat_no_sz | 否 |  |  |
| 23 | stock_account_stb | 否 |  |  |
| 24 | seat_no_stb | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | cash_fund_account | 否 |  |  |
| 27 | cash_client_id | 否 |  |  |
| 28 | cash_branch_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_ucrt_cash_account | ART | 是 | cashgroup_no, cashgroup_no |
| idx_uqms_cash_account_fund | ART | 是 | cash_fund_account, cash_fund_account |
| uk_ucrt_cash_account | ART | 是 | cashgroup_no, cashgroup_no |
| idx_uqms_cash_account_fund | ART | 是 | cash_fund_account, cash_fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_cash_account | cashgroup_no, cashgroup_no |
| idx_ucrt_cash_account | cashgroup_no, cashgroup_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:51:16 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-07 14:25:28 | 3.0.2.1 | 沈勋 | 增加idx_uqms_cash_account_fund索引 |
| 2025-07-08 09:41:47 | 3.0.6.7 | tongck54118 | 物理表uqms_cash_account，添加了表字段(cash_fund_account);
物理表uqms_cas... |
| 2025-06-13 11:22:37 | 3.0.6.7 | 常行 | 表空间改为HS_UARG_DATA |
| 2025-04-11 15:18:27 | 3.0.2.7 | 李江霖 | 修改物理表索引名 |
| 2024-05-31 15:48:11 | 3.0.2.6 | 牟家乐 | uqms_cash_account增加关联关系 |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:51:16 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-07 14:25:28 | 3.0.2.1 | 沈勋 | 增加idx_uqms_cash_account_fund索引 |
| 2025-07-08 09:41:47 | 3.0.6.7 | tongck54118 | 物理表uqms_cash_account，添加了表字段(cash_fund_account);
物理表uqms_cas... |
| 2025-06-13 11:22:37 | 3.0.6.7 | 常行 | 表空间改为HS_UARG_DATA |
| 2025-04-11 15:18:27 | 3.0.2.7 | 李江霖 | 修改物理表索引名 |
| 2024-05-31 15:48:11 | 3.0.2.6 | 牟家乐 | uqms_cash_account增加关联关系 |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |

> 共 16 条修改记录，仅显示最近15条

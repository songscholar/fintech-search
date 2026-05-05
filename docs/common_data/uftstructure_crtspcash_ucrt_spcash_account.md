# ucrt_spcash_account - 专项头寸账户表

**表对象ID**: 8000
**所属模块**: crtspcash
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | cashgroup_no | 否 |  |  |
| 3 | cashgroup_prop | 否 |  |  |
| 4 | cashgroup_name | 否 |  |  |
| 5 | stock_account_sh | 否 |  |  |
| 6 | seat_no_sh | 否 |  |  |
| 7 | stock_account_sz | 否 |  |  |
| 8 | seat_no_sz | 否 |  |  |
| 9 | stock_account_stb | 否 |  |  |
| 10 | seat_no_stb | 否 |  |  |
| 11 | bonusalloc_flag | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | cash_fund_account | 否 |  |  |
| 14 | cash_client_id | 否 |  |  |
| 15 | cash_branch_no | 否 |  |  |
| 16 | partition_no | 是 |  |  |
| 17 | company_no | 否 |  |  |
| 18 | cashgroup_no | 否 |  |  |
| 19 | cashgroup_prop | 否 |  |  |
| 20 | cashgroup_name | 否 |  |  |
| 21 | stock_account_sh | 否 |  |  |
| 22 | seat_no_sh | 否 |  |  |
| 23 | stock_account_sz | 否 |  |  |
| 24 | seat_no_sz | 否 |  |  |
| 25 | stock_account_stb | 否 |  |  |
| 26 | seat_no_stb | 否 |  |  |
| 27 | bonusalloc_flag | 否 |  |  |
| 28 | transaction_no | 否 |  |  |
| 29 | cash_fund_account | 否 |  |  |
| 30 | cash_client_id | 否 |  |  |
| 31 | cash_branch_no | 否 |  |  |
| 32 | partition_no | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_spcash_account | ART | 是 | cashgroup_no, cashgroup_no |
| idx_ucrt_spcash_account_fund | ART | 是 | cash_fund_account, cash_fund_account |
| idx_ucrt_spcash_account | ART | 是 | cashgroup_no, cashgroup_no |
| idx_ucrt_spcash_account_fund | ART | 是 | cash_fund_account, cash_fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_spcash_account | cashgroup_no, cashgroup_no |
| idx_ucrt_spcash_account | cashgroup_no, cashgroup_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-15 16:33:05 | 3.0.2.2016 | huangzh | 所有表ucrt_spcash_account，添加了表字段(partition_no);
 |
| 2025-08-07 14:25:28 | 3.0.2.1 | 沈勋 | 增加idx_ucrt_spcash_account_fund索引 |
| 2025-07-08 09:43:58 | 3.0.6.6 | tongck54118 | 物理表ucrt_spcash_account，添加了表字段(cash_fund_account);
物理表ucrt_s... |
| 2025-06-13 14:05:27 | 3.0.6.6 | 常行 | 表空间改为HS_UARG_DATA |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-09-15 16:33:05 | 3.0.2.2016 | huangzh | 所有表ucrt_spcash_account，添加了表字段(partition_no);
 |
| 2025-08-07 14:25:28 | 3.0.2.1 | 沈勋 | 增加idx_ucrt_spcash_account_fund索引 |
| 2025-07-08 09:43:58 | 3.0.6.6 | tongck54118 | 物理表ucrt_spcash_account，添加了表字段(cash_fund_account);
物理表ucrt_s... |
| 2025-06-13 14:05:27 | 3.0.6.6 | 常行 | 表空间改为HS_UARG_DATA |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

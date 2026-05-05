# ucrt_stock_holder - 融资融券证券账户控制表

**表对象ID**: 7530
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | holder_kind | 否 |  |  |
| 6 | holder_level | 否 |  |  |
| 7 | holder_restriction | 否 |  |  |
| 8 | holder_rights | 否 |  |  |
| 9 | holder_status | 否 |  |  |
| 10 | main_flag | 否 |  |  |
| 11 | regflag | 否 |  |  |
| 12 | seat_no | 否 |  |  |
| 13 | stkholder_ctrlstr | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | szdc_use_flag | 否 |  |  |
| 16 | acode_account | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | holder_kind | 否 |  |  |
| 21 | holder_level | 否 |  |  |
| 22 | holder_restriction | 否 |  |  |
| 23 | holder_rights | 否 |  |  |
| 24 | holder_status | 否 |  |  |
| 25 | main_flag | 否 |  |  |
| 26 | regflag | 否 |  |  |
| 27 | seat_no | 否 |  |  |
| 28 | stkholder_ctrlstr | 否 |  |  |
| 29 | stock_account | 否 |  |  |
| 30 | szdc_use_flag | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stock_holder | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| idx_ucrt_stock_holder_unique | ART | 是 | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |
| idx_ucrt_stock_holder_code | ART | 是 | acode_account, acode_account |
| idx_ucrt_stock_holder | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| idx_ucrt_stock_holder_unique | ART | 是 | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |
| idx_ucrt_stock_holder_code | ART | 是 | acode_account, acode_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stock_holder_unique | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |
| idx_ucrt_stock_holder_unique | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-08 20:27:20 | 3.0.2.2001 | 高志强 | 去除idx_ucrt_stock_real的空校验 |
| 2025-03-12 20:05:54 | 3.0.6.42 | 徐世晗 | 调整idx_ucrt_stock_holder索引顺序 |
| 2024-10-18 09:39:26 | 3.0.6.6 | 沈勋 | 调整ucrt_bond_exemptricon表的关联关系，迁移到ucrt_fund_account表上 |
| 2024-07-29 10:58:44 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2024-07-16 14:57:00 | 3.0.3.4 | 沈勋 | idx_ucrt_stock_holder_unique改为分级索引 |
| 2024-05-22 20:22:08 | 3.0.2.10 | 叶慧军 | ucrt_subequity关联关系改为1:1类型 |
| 2023-11-08 14:41:51 | V3.0.1.14 | 吴威 | 新增索引 |
| 2023-08-25 16:33:12 | 0.3.3.143 | 徐志坚 | 调整事务控制方式，删除transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-04-08 20:27:20 | 3.0.2.2001 | 高志强 | 去除idx_ucrt_stock_real的空校验 |
| 2025-03-12 20:05:54 | 3.0.6.42 | 徐世晗 | 调整idx_ucrt_stock_holder索引顺序 |
| 2024-10-18 09:39:26 | 3.0.6.6 | 沈勋 | 调整ucrt_bond_exemptricon表的关联关系，迁移到ucrt_fund_account表上 |
| 2024-07-29 10:58:44 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2024-07-16 14:57:00 | 3.0.3.4 | 沈勋 | idx_ucrt_stock_holder_unique改为分级索引 |
| 2024-05-22 20:22:08 | 3.0.2.10 | 叶慧军 | ucrt_subequity关联关系改为1:1类型 |

> 共 18 条修改记录，仅显示最近15条

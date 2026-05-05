# uses_stock_holder - 证券账户控制表

**表对象ID**: 5502
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | holder_kind | 否 |  |  |
| 5 | holder_level | 否 |  |  |
| 6 | holder_status | 否 |  |  |
| 7 | main_flag | 否 |  |  |
| 8 | regflag | 否 |  |  |
| 9 | report_level | 否 |  |  |
| 10 | seat_no | 否 |  |  |
| 11 | stkholder_ctrlstr | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | szdc_use_flag | 否 |  |  |
| 14 | partition_no | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | internal_account | 否 |  |  |
| 18 | client_id | 否 |  |  |
| 19 | ordinal | 否 |  |  |
| 20 | bondreg | 否 |  |  |
| 21 | open_date | 否 |  |  |
| 22 | en_ext_holder_rights | 否 |  |  |
| 23 | holder_rights | 否 |  |  |
| 24 | holder_restriction | 否 |  |  |
| 25 | acode_account | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | holder_kind | 否 |  |  |
| 29 | holder_level | 否 |  |  |
| 30 | holder_status | 否 |  |  |
| 31 | main_flag | 否 |  |  |
| 32 | regflag | 否 |  |  |
| 33 | report_level | 否 |  |  |
| 34 | seat_no | 否 |  |  |
| 35 | stkholder_ctrlstr | 否 |  |  |
| 36 | stock_account | 否 |  |  |
| 37 | szdc_use_flag | 否 |  |  |
| 38 | partition_no | 否 |  |  |
| 39 | branch_no | 否 |  |  |
| 40 | transaction_no | 否 |  |  |
| 41 | internal_account | 否 |  |  |
| 42 | client_id | 否 |  |  |
| 43 | ordinal | 否 |  |  |
| 44 | bondreg | 否 |  |  |
| 45 | open_date | 否 |  |  |
| 46 | en_ext_holder_rights | 否 |  |  |
| 47 | holder_rights | 否 |  |  |
| 48 | holder_restriction | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_stock_holder_uk | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| idx_uses_stock_holder_acode | ART | 是 | acode_account, acode_account |
| idx_uses_stock_holder_acct | ART | 是 | stock_account, exchange_type, stock_account, exchange_type |
| idx_uses_stock_holder_fund_acct | ART | 是 | fund_account, exchange_type, fund_account, exchange_type |
| idx_uses_stock_holder_uk | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| idx_uses_stock_holder_acode | ART | 是 | acode_account, acode_account |
| idx_uses_stock_holder_acct | ART | 是 | stock_account, exchange_type, stock_account, exchange_type |
| idx_uses_stock_holder_fund_acct | ART | 是 | fund_account, exchange_type, fund_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_stock_holder_uk | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |
| idx_uses_stock_holder_uk | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 11:18:02 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-10 10:43:01 | 3.0.2.72 | 钟兆星 | 调整索引字段顺序，保证持仓查询先查上海市场后查深圳市场 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-08 20:27:20 | 3.0.2.2001 | 高志强 | 去除idx_ucrt_stock_real的空校验 |
| 2024-09-23 10:09:53 | 3.0.2.48 | 张明月 | 物理表uses_stock_holder，添加了表字段(internal_account);
物理表uses_stoc... |
| 2024-08-14 14:10:40 | 3.0.2.40 | 张剑 | holder_rights、holder_restriction设置为变长字段 |
| 2024-05-29 21:31:08 | 3.0.2.19 | 祝丁恺 | 勾选不回库选项 |
| 2024-05-21 15:16:09 | 3.0.2.9 | 吴威 | 支持uses_fund_account、uses_stock_holder账户同步 |
| 2024-04-28 20:21:09 | 3.0.2.3 | 阮善宏 | 内存表uses_stock_holder，增加索引(idx_uses_stock_holder_acode:[acode... |
| 2024-04-28 10:44:43 | 3.0.2.3 | 阮善宏 | 物理表uses_stock_holder，添加了表字段(partition_no);
物理表uses_stock_ho... |
| 2023-08-25 16:36:17 | 0.3.3.143 | 徐志坚 | 调整事务控制方式，删除transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-16 18:49 | 0.3.3.134 | 吴威 | idx_uses_stock_holder改为唯一索引 |
| 2026-03-09 11:18:02 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-10 10:43:01 | 3.0.2.72 | 钟兆星 | 调整索引字段顺序，保证持仓查询先查上海市场后查深圳市场 |

> 共 26 条修改记录，仅显示最近15条

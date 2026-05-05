# uses_fund_detail - 证券交易资金详细信息表

**表对象ID**: 5509
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | business_frozen_balance | 否 |  |  |
| 6 | business_unfrozen_balance | 否 |  |  |
| 7 | fund_enable_level | 否 |  |  |
| 8 | partition_no | 否 |  |  |
| 9 | position_str | 否 |  | fund_account(18)+money_type(3)+fund_enable_level(10)+init_da |
| 10 | init_date | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | money_type | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | business_frozen_balance | 否 |  |  |
| 15 | business_unfrozen_balance | 否 |  |  |
| 16 | fund_enable_level | 否 |  |  |
| 17 | partition_no | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+money_type(3)+fund_enable_level(10)+init_da |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fund_detail | ART | 是 | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |
| idx_fund_detail_pos | ART | 是 | position_str, position_str |
| idx_fund_detail | ART | 是 | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |
| idx_fund_detail_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fund_detail | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |
| idx_fund_detail | fund_account, money_type, fund_enable_level, init_date, fund_account, money_type, fund_enable_level, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:35:17 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-27 20:22:40 | 3.0.2.74 | 全春辉 | 物理表uses_fund_detail，添加了表字段(position_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-11 15:18:27 | 3.0.2.4 | 李江霖 | 修改物理表索引名 |
| 2024-04-28 17:00:28 | 3.0.2.3 | 阮善宏 | 物理表uses_fund_detail，添加了表字段(partition_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 13:35:17 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-27 20:22:40 | 3.0.2.74 | 全春辉 | 物理表uses_fund_detail，添加了表字段(position_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-11 15:18:27 | 3.0.2.4 | 李江霖 | 修改物理表索引名 |
| 2024-04-28 17:00:28 | 3.0.2.3 | 阮善宏 | 物理表uses_fund_detail，添加了表字段(partition_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

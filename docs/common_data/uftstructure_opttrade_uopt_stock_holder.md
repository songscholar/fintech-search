# uopt_stock_holder - 期权账户控制表

**表对象ID**: 9601
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | holder_kind | 否 |  |  |
| 6 | holder_level | 否 |  |  |
| 7 | holder_status | 否 |  |  |
| 8 | regflag | 否 |  |  |
| 9 | seat_no | 否 |  |  |
| 10 | open_date | 否 |  |  |
| 11 | partition_no | 否 |  |  |
| 12 | position_str | 否 |  |  |
| 13 | stkholder_ctrlstr | 否 |  |  |
| 14 | holder_restriction | 否 |  |  |
| 15 | holder_rights | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | stock_account | 否 |  |  |
| 20 | holder_kind | 否 |  |  |
| 21 | holder_level | 否 |  |  |
| 22 | holder_status | 否 |  |  |
| 23 | regflag | 否 |  |  |
| 24 | seat_no | 否 |  |  |
| 25 | open_date | 否 |  |  |
| 26 | partition_no | 否 |  |  |
| 27 | position_str | 否 |  |  |
| 28 | stkholder_ctrlstr | 否 |  |  |
| 29 | holder_restriction | 否 |  |  |
| 30 | holder_rights | 否 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_stock_holder_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_stock_holder | 默认 | 否 | exchange_type, exchange_type |
| idx_uopt_stock_holder_global | 默认 | 是 | exchange_type, fund_account, exchange_type, fund_account |
| idx_uopt_stock_holder_stockaccount | 默认 | 是 | exchange_type, stock_account, exchange_type, stock_account |
| idx_uopt_stock_holder_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_stock_holder_pos | 默认 | 否 | position_str, position_str |
| idx_uopt_stock_holder | 默认 | 否 | exchange_type, exchange_type |
| idx_uopt_stock_holder_global | 默认 | 是 | exchange_type, fund_account, exchange_type, fund_account |
| idx_uopt_stock_holder_stockaccount | 默认 | 是 | exchange_type, stock_account, exchange_type, stock_account |
| idx_uopt_stock_holder_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_stock_holder | exchange_type, fund_account, exchange_type, fund_account |
| idx_uopt_stock_holder | exchange_type, fund_account, exchange_type, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-16 15:35:20 | V3.0.2.11 | 韦子晗 | uopt_entrustaid表的关联关系取消关联记录为空校验 |
| 2025-07-25 16:45:45 | V3.0.2.1 | 汪迎 | 物理表uopt_stock_holder，添加了表字段(position_str);
,物理表uopt_stock_h... |
| 2024-09-20 15:23:42 | V3.0.3.13 | 周君杰 | 新增关联索引关联uopt_entrust表 |
| 2024-06-25 10:24:32 | V3.0.3.11 | 张明月 | uopt_entrust表的关联关系取消关联记录为空校验 |
| 2024-05-09 09:33:30 | V3.0.3.7 | 韦子晗 | 新增partition_no字段 |
| 2025-09-16 15:35:20 | V3.0.2.11 | 韦子晗 | uopt_entrustaid表的关联关系取消关联记录为空校验 |
| 2025-07-25 16:45:45 | V3.0.2.1 | 汪迎 | 物理表uopt_stock_holder，添加了表字段(position_str);
,物理表uopt_stock_h... |
| 2024-09-20 15:23:42 | V3.0.3.13 | 周君杰 | 新增关联索引关联uopt_entrust表 |
| 2024-06-25 10:24:32 | V3.0.3.11 | 张明月 | uopt_entrust表的关联关系取消关联记录为空校验 |
| 2024-05-09 09:33:30 | V3.0.3.7 | 韦子晗 | 新增partition_no字段 |

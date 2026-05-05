# uses_stock_changeinfo - 证券存管股份变更信息表

**表对象ID**: 5969
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | operator_no | 否 |  |  |
| 3 | op_station | 否 |  |  |
| 4 | op_entrust_way | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | stock_type | 否 |  |  |
| 11 | current_amount | 否 |  |  |
| 12 | frozen_amount | 否 |  |  |
| 13 | unfrozen_amount | 否 |  |  |
| 14 | correct_amount | 否 |  |  |
| 15 | serial_no | 否 |  |  |
| 16 | sum_sell_amount | 否 |  |  |
| 17 | sum_sell_balance | 否 |  |  |
| 18 | cancel_serial_no | 否 |  |  |
| 19 | business_flag | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | occur_amount | 否 |  |  |
| 22 | cost_price | 否 |  |  |
| 23 | uncome_buy_amount | 否 |  |  |
| 24 | uncome_sell_amount | 否 |  |  |
| 25 | sum_buy_amount | 否 |  |  |
| 26 | sum_buy_balance | 否 |  |  |
| 27 | real_status | 否 |  |  |
| 28 | init_date | 否 |  |  |
| 29 | operator_no | 否 |  |  |
| 30 | op_station | 否 |  |  |
| 31 | op_entrust_way | 否 |  |  |
| 32 | fund_account | 否 |  |  |
| 33 | client_id | 否 |  |  |
| 34 | exchange_type | 否 |  |  |
| 35 | stock_account | 否 |  |  |
| 36 | stock_code | 否 |  |  |
| 37 | stock_type | 否 |  |  |
| 38 | current_amount | 否 |  |  |
| 39 | frozen_amount | 否 |  |  |
| 40 | unfrozen_amount | 否 |  |  |
| 41 | correct_amount | 否 |  |  |
| 42 | serial_no | 否 |  |  |
| 43 | sum_sell_amount | 否 |  |  |
| 44 | sum_sell_balance | 否 |  |  |
| 45 | cancel_serial_no | 否 |  |  |
| 46 | business_flag | 否 |  |  |
| 47 | remark | 否 |  |  |
| 48 | occur_amount | 否 |  |  |
| 49 | cost_price | 否 |  |  |
| 50 | uncome_buy_amount | 否 |  |  |
| 51 | uncome_sell_amount | 否 |  |  |
| 52 | sum_buy_amount | 否 |  |  |
| 53 | sum_buy_balance | 否 |  |  |
| 54 | real_status | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_stock_changeinfo | ART | 是 | fund_account, serial_no, fund_account, serial_no |
| idx_rpt_uses_stock_changeinfo | ART | 是 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| idx_uses_stock_changeinfo | ART | 是 | fund_account, serial_no, fund_account, serial_no |
| idx_rpt_uses_stock_changeinfo | ART | 是 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_stock_changeinfo | fund_account, serial_no, fund_account, serial_no |
| idx_uses_stock_changeinfo | fund_account, serial_no, fund_account, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-17 11:08:21 | V3.0.8.33 | 杨新照 | 所有表uses_stock_changeinfo，添加了表字段(real_status);
 |
| 2026-03-09 14:48:05 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:28:29 | V3.0.8.22 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-07 10:06:13 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2025-02-25 09:57:00 | 3.0.2.2001 | 蒋浩 | 物理表uses_stock_changeinfo，添加了表字段(cost_price);
物理表uses_stock_... |
| 2025-01-13 19:25:09 | 3.0.2.56 | 杨森峰 | 物理表uses_stock_changeinfo，添加了表字段(occur_amount);
 |
| 2025-01-13 19:25:09 | 3.0.2.56 | 杨森峰 | 物理表uses_stock_changeinfo，添加了表字段(occur_amount);
 |
| 2025-01-13 19:25:09 | 3.0.2.56 | 杨森峰 | 物理表uses_stock_changeinfo，添加了表字段(occur_amount);
 |
| 2024-09-19 15:18:15 | 3.0.2.47 | 张训华 | 物理表uses_stock_changeinfo，添加了表字段(init_date);
物理表uses_stock_c... |
| 2024-09-12 18:40:27 | 3.0.2.46 | 曾剑辉 | 新增表结构 |
| 2026-03-17 11:08:21 | V3.0.8.33 | 杨新照 | 所有表uses_stock_changeinfo，添加了表字段(real_status);
 |
| 2026-03-09 14:48:05 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:28:29 | V3.0.8.22 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-07 10:06:13 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2025-02-25 09:57:00 | 3.0.2.2001 | 蒋浩 | 物理表uses_stock_changeinfo，添加了表字段(cost_price);
物理表uses_stock_... |

> 共 20 条修改记录，仅显示最近15条

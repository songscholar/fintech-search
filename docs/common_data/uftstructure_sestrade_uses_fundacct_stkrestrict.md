# uses_fundacct_stkrestrict - 证券资产账户证券限制控制表

**表对象ID**: 5503
**所属模块**: sestrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | anti_flag | 否 |  |  |
| 2 | begin_date | 否 |  |  |
| 3 | end_date | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | ordinal | 否 |  |  |
| 6 | res_entrust_bs | 否 |  |  |
| 7 | res_entrust_prop | 否 |  |  |
| 8 | res_entrust_type | 否 |  |  |
| 9 | res_entrust_way | 否 |  |  |
| 10 | res_exchange_type | 否 |  |  |
| 11 | res_stock_code | 否 |  |  |
| 12 | res_stock_type | 否 |  |  |
| 13 | res_sub_stock_type | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | position_str | 否 |  | fund_account(18)+stock_account(20)+ordinal(10) |
| 18 | restrict_str | 否 |  |  |
| 19 | branch_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | anti_flag | 否 |  |  |
| 24 | begin_date | 否 |  |  |
| 25 | end_date | 否 |  |  |
| 26 | fund_account | 否 |  |  |
| 27 | ordinal | 否 |  |  |
| 28 | res_entrust_bs | 否 |  |  |
| 29 | res_entrust_prop | 否 |  |  |
| 30 | res_entrust_type | 否 |  |  |
| 31 | res_entrust_way | 否 |  |  |
| 32 | res_exchange_type | 否 |  |  |
| 33 | res_stock_code | 否 |  |  |
| 34 | res_stock_type | 否 |  |  |
| 35 | res_sub_stock_type | 否 |  |  |
| 36 | stock_account | 否 |  |  |
| 37 | client_id | 否 |  |  |
| 38 | transaction_no | 否 |  |  |
| 39 | position_str | 否 |  | fund_account(18)+stock_account(20)+ordinal(10) |
| 40 | restrict_str | 否 |  |  |
| 41 | branch_no | 否 |  |  |
| 42 | update_date | 否 |  |  |
| 43 | update_time | 否 |  |  |
| 44 | remark | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_fundacct_stkrestrict | 默认 | 否 | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |
| idx_uses_fundacct_stkrestrict | 默认 | 否 | position_str, position_str |
| idx_uses_fundacct_stkrestrict | ART | 是 | position_str, position_str |
| idx_uses_fundacct_stkrestrict_stock | ART | 是 | fund_account, stock_account, anti_flag, fund_account, stock_account, anti_flag |
| idx_uses_fundacct_stkrestrict | 默认 | 否 | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |
| idx_uses_fundacct_stkrestrict | 默认 | 否 | position_str, position_str |
| idx_uses_fundacct_stkrestrict | ART | 是 | position_str, position_str |
| idx_uses_fundacct_stkrestrict_stock | ART | 是 | fund_account, stock_account, anti_flag, fund_account, stock_account, anti_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_fundacct_stkrestrict | position_str, position_str |
| idx_uses_fundacct_stkrestrict | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 11:18:29 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-09-15 16:56:57 | 3.0.6.1019 | tongck54118 | 物理表uses_fundacct_stkrestrict，添加了表字段(remark);
 |
| 2025-07-21 09:59:09 | 3.0.2.72 | 杨涛 | 物理表uses_fundacct_stkrestrict，添加了表字段(update_date);
物理表uses_f... |
| 2025-05-20 13:48:08 | 3.0.2.68 | 於达 | 物理表uses_fundacct_stkrestrict，添加了表字段(restrict_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2024-11-06 10:09:58 | 3.0.5.1058 | 张训华 | idx_uses_fundacct_stkrestrict_stock增加字段 |
| 2024-09-30 15:05:16 | 3.0.2.48 | 乐闽庭 | 物理表uses_fundacct_stkrestrict，删除索引字段(索引idx_uses_fundacct_stkr... |
| 2024-09-30 15:04:55 | 3.0.2.48 | 乐闽庭 | 物理表uses_fundacct_stkrestrict，增加索引字段(索引idx_uses_fundacct_stkr... |
| 2024-09-30 15:02:45 | 3.0.2.48 | 乐闽庭 | 物理表uses_fundacct_stkrestrict，添加了表字段(position_str);
 |
| 2024-05-20 15:26:38 | 3.0.2.10 | 范文浩 | 物理表uses_fundacct_stkrestrict，添加了表字段(client_id);
物理表uses_fun... |
| 2024-05-13 20:53:23 | 3.0.2.7 | 泮新国 | 修改资产账户表的关联索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-09 11:18:29 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-09-15 16:56:57 | 3.0.6.1019 | tongck54118 | 物理表uses_fundacct_stkrestrict，添加了表字段(remark);
 |
| 2025-07-21 09:59:09 | 3.0.2.72 | 杨涛 | 物理表uses_fundacct_stkrestrict，添加了表字段(update_date);
物理表uses_f... |

> 共 24 条修改记录，仅显示最近15条

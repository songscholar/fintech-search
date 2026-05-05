# arp_acct_arg - 约定购回客户综合设置表

**表对象ID**: 2476
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | money_type | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | en_entrust_way | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | fund_account(18)+money_type(3) |
| 10 | branch_no | 否 |  |  |
| 11 | money_type | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | en_entrust_way | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+money_type(3) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpacctarg | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_arpacctarg | ART | 是 | fund_account, money_type, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpacctarg | fund_account, money_type, fund_account, money_type |
| idx_arpacctarg | fund_account, money_type, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:45:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-04-21 16:26:08 | V3.0.5.1028 | 常行 | 物理表arp_acct_arg，添加了表字段(update_date);
物理表arp_acct_arg，添加了表字段... |
| 2024-12-06 16:00:05 | V3.0.2.1009 | 黄积冲 | 新增表 |
| 2026-03-04 15:45:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-04-21 16:26:08 | V3.0.5.1028 | 常行 | 物理表arp_acct_arg，添加了表字段(update_date);
物理表arp_acct_arg，添加了表字段... |
| 2024-12-06 16:00:05 | V3.0.2.1009 | 黄积冲 | 新增表 |

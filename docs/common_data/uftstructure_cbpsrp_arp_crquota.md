# arp_crquota - 约定购回授信表

**表对象ID**: 2604
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | arp_credit_quota | 否 |  |  |
| 6 | arp_credit_rate | 否 |  |  |
| 7 | break_times | 否 |  |  |
| 8 | risk_rate | 否 |  |  |
| 9 | cbpacct_type | 否 |  |  |
| 10 | en_cbpbusi_type | 否 |  |  |
| 11 | allow_break_times | 否 |  |  |
| 12 | curr_break_times | 否 |  |  |
| 13 | blacklist_flag | 否 |  |  |
| 14 | black_times | 否 |  |  |
| 15 | self_credit_quota | 否 |  |  |
| 16 | papercont_id | 否 |  |  |
| 17 | valid_date | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |
| 22 | fund_account | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | branch_no | 否 |  |  |
| 25 | money_type | 否 |  |  |
| 26 | arp_credit_quota | 否 |  |  |
| 27 | arp_credit_rate | 否 |  |  |
| 28 | break_times | 否 |  |  |
| 29 | risk_rate | 否 |  |  |
| 30 | cbpacct_type | 否 |  |  |
| 31 | en_cbpbusi_type | 否 |  |  |
| 32 | allow_break_times | 否 |  |  |
| 33 | curr_break_times | 否 |  |  |
| 34 | blacklist_flag | 否 |  |  |
| 35 | black_times | 否 |  |  |
| 36 | self_credit_quota | 否 |  |  |
| 37 | papercont_id | 否 |  |  |
| 38 | valid_date | 否 |  |  |
| 39 | transaction_no | 否 |  |  |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpcrquota | ART | 是 | fund_account, en_cbpbusi_type, money_type, cbpacct_type, fund_account, en_cbpbusi_type, money_type, cbpacct_type |
| idx_arpcrquota | ART | 是 | fund_account, en_cbpbusi_type, money_type, cbpacct_type, fund_account, en_cbpbusi_type, money_type, cbpacct_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpcrquota | fund_account, en_cbpbusi_type, money_type, cbpacct_type, fund_account, en_cbpbusi_type, money_type, cbpacct_type |
| idx_arpcrquota | fund_account, en_cbpbusi_type, money_type, cbpacct_type, fund_account, en_cbpbusi_type, money_type, cbpacct_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:44:58 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-26 16:59:05 | 3.0.2.5 | 高志强 | 数据存储介质改为MDB |
| 2025-02-21 20:02:20 | 3.0.3.10 | 李想 | 物理表arp_crquota，添加了表字段(update_date);
物理表arp_crquota，添加了表字段(u... |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:20:53 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:44:58 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-26 16:59:05 | 3.0.2.5 | 高志强 | 数据存储介质改为MDB |
| 2025-02-21 20:02:20 | 3.0.3.10 | 李想 | 物理表arp_crquota，添加了表字段(update_date);
物理表arp_crquota，添加了表字段(u... |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:20:53 | 3.0.3.1 | wuxd | 新增 |

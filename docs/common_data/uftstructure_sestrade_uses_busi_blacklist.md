# uses_busi_blacklist - 证券业务黑名单表

**表对象ID**: 5504
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | busiblack_kind | 否 |  |  |
| 6 | en_stock_type | 否 |  |  |
| 7 | en_stock_code | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | busiblack_kind | 否 |  |  |
| 17 | en_stock_type | 否 |  |  |
| 18 | en_stock_code | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_busi_blacklist | ART | 是 | busiblack_kind, busiblack_kind |
| idx_uses_busi_blacklist_uk | ART | 是 | busiblack_kind, fund_account, exchange_type, stock_account, branch_no, busiblack_kind, fund_account, exchange_type, stock_account, branch_no |
| idx_uses_busi_blacklist | ART | 是 | busiblack_kind, busiblack_kind |
| idx_uses_busi_blacklist_uk | ART | 是 | busiblack_kind, fund_account, exchange_type, stock_account, branch_no, busiblack_kind, fund_account, exchange_type, stock_account, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_busi_blacklist_uk | busiblack_kind, fund_account, exchange_type, stock_account, branch_no, busiblack_kind, fund_account, exchange_type, stock_account, branch_no |
| idx_uses_busi_blacklist_uk | busiblack_kind, fund_account, exchange_type, stock_account, branch_no, busiblack_kind, fund_account, exchange_type, stock_account, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 11:19:23 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-21 09:59:09 | 3.0.2.72 | 杨涛 | 物理表uses_busi_blacklist，添加了表字段(update_date);
物理表uses_busi_bl... |
| 2024-05-29 21:24:19 | 3.0.2.14 | 祝丁恺 | 勾选不回库选项 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段，并增加唯一索引idx_uses_busi_blacklist_uk |
| 2026-03-09 11:19:23 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-21 09:59:09 | 3.0.2.72 | 杨涛 | 物理表uses_busi_blacklist，添加了表字段(update_date);
物理表uses_busi_bl... |
| 2024-05-29 21:24:19 | 3.0.2.14 | 祝丁恺 | 勾选不回库选项 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段，并增加唯一索引idx_uses_busi_blacklist_uk |

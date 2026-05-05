# ucrt_busi_blacklist - 融资融券业务黑名单表

**表对象ID**: 7545
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

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
| 9 | exchange_type | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | busiblack_kind | 否 |  |  |
| 14 | en_stock_type | 否 |  |  |
| 15 | en_stock_code | 否 |  |  |
| 16 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_busi_blacklist_uk | ART | 是 | fund_account, busiblack_kind, exchange_type, stock_account, branch_no, fund_account, busiblack_kind, exchange_type, stock_account, branch_no |
| idx_ucrt_busi_blacklist_uk | ART | 是 | fund_account, busiblack_kind, exchange_type, stock_account, branch_no, fund_account, busiblack_kind, exchange_type, stock_account, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_busi_blacklist_uk | busiblack_kind, fund_account, exchange_type, stock_account, branch_no, busiblack_kind, fund_account, exchange_type, stock_account, branch_no |
| idx_ucrt_busi_blacklist_uk | busiblack_kind, fund_account, exchange_type, stock_account, branch_no, busiblack_kind, fund_account, exchange_type, stock_account, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段，并增加唯一索引idx_ucrt_busi_blacklist_uk |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段，并增加唯一索引idx_ucrt_busi_blacklist_uk |

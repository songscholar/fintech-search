# uarg_busi_blacklist - 业务黑名单表

**表对象ID**: 143
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
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
| 11 | position_str | 否 |  | busiblack_kind(1)+fund_account(18)+exchange_type(4)+stock_ac |
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
| 22 | position_str | 否 |  | busiblack_kind(1)+fund_account(18)+exchange_type(4)+stock_ac |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_busi_blacklist | 默认 | 否 |  |
| idx_uarg_busi_blacklist_uk | 默认 | 否 |  |
| idx_uarg_busi_blacklist | ART | 是 | busiblack_kind, busiblack_kind |
| idx_uarg_busi_blacklist_uk | ART | 是 | busiblack_kind, fund_account, exchange_type, stock_account, branch_no, busiblack_kind, fund_account, exchange_type, stock_account, branch_no |
| idx_uarg_busi_blacklist | 默认 | 否 |  |
| idx_uarg_busi_blacklist_uk | 默认 | 否 |  |
| idx_uarg_busi_blacklist | ART | 是 | busiblack_kind, busiblack_kind |
| idx_uarg_busi_blacklist_uk | ART | 是 | busiblack_kind, fund_account, exchange_type, stock_account, branch_no, busiblack_kind, fund_account, exchange_type, stock_account, branch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_busi_blacklist_uk | busiblack_kind, fund_account, exchange_type, stock_account, branch_no, busiblack_kind, fund_account, exchange_type, stock_account, branch_no |
| idx_uarg_busi_blacklist_uk | busiblack_kind, fund_account, exchange_type, stock_account, branch_no, busiblack_kind, fund_account, exchange_type, stock_account, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:19:04 | 3.0.2.103 | taocong45644 | 当前表uarg_busi_blacklist，修改了索引idx_uarg_busi_blacklist,索引字段修改为：... |
| 2025-03-13 17:16:35 | 3.0.6.125 | 李想 | 新增表 |
| 2025-12-01 15:19:04 | 3.0.2.103 | taocong45644 | 当前表uarg_busi_blacklist，修改了索引idx_uarg_busi_blacklist,索引字段修改为：... |
| 2025-03-13 17:16:35 | 3.0.6.125 | 李想 | 新增表 |

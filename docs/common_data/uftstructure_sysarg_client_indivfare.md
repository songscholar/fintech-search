# client_indivfare - 账户独立佣金签约表

**表对象ID**: 145
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | asset_prop | 否 |  |  |
| 5 | indiv_fare_kind | 否 |  |  |
| 6 | remark | 否 |  |  |
| 7 | sign_date | 否 |  |  |
| 8 | sign_time | 否 |  |  |
| 9 | unsign_date | 否 |  |  |
| 10 | unsign_time | 否 |  |  |
| 11 | begin_date | 否 |  |  |
| 12 | end_date | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | position_str | 否 |  | fund_account(18)+indiv_fare_kind(10) |
| 17 | fund_account | 否 |  |  |
| 18 | client_id | 否 |  |  |
| 19 | branch_no | 否 |  |  |
| 20 | asset_prop | 否 |  |  |
| 21 | indiv_fare_kind | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | sign_date | 否 |  |  |
| 24 | sign_time | 否 |  |  |
| 25 | unsign_date | 否 |  |  |
| 26 | unsign_time | 否 |  |  |
| 27 | begin_date | 否 |  |  |
| 28 | end_date | 否 |  |  |
| 29 | update_date | 否 |  |  |
| 30 | update_time | 否 |  |  |
| 31 | transaction_no | 否 |  |  |
| 32 | position_str | 否 |  | fund_account(18)+indiv_fare_kind(10) |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_clientindivfare | 默认 | 否 |  |
| idx_clientindivfare_acct | 默认 | 否 |  |
| idx_clientindivfare | ART | 是 | fund_account, indiv_fare_kind, fund_account, indiv_fare_kind |
| idx_clientindivfare_acct | ART | 是 | fund_account, fund_account |
| idx_clientindivfare | 默认 | 否 |  |
| idx_clientindivfare_acct | 默认 | 否 |  |
| idx_clientindivfare | ART | 是 | fund_account, indiv_fare_kind, fund_account, indiv_fare_kind |
| idx_clientindivfare_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_clientindivfare | fund_account, indiv_fare_kind, fund_account, indiv_fare_kind |
| idx_clientindivfare | fund_account, indiv_fare_kind, fund_account, indiv_fare_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:37:11 | 3.0.2.103 | taocong45644 | 当前表client_indivfare，修改了索引idx_clientindivfare,索引字段修改为：(fund_a... |
| 2025-05-08 13:38:17 | 3.0.6.135 | 常行 | 新增表 |
| 2025-12-01 14:37:11 | 3.0.2.103 | taocong45644 | 当前表client_indivfare，修改了索引idx_clientindivfare,索引字段修改为：(fund_a... |
| 2025-05-08 13:38:17 | 3.0.6.135 | 常行 | 新增表 |

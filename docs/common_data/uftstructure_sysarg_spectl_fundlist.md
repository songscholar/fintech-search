# spectl_fundlist - 特殊控制资金账户表

**表对象ID**: 137
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | spectlbusi_kind | 否 |  |  |
| 4 | remark | 否 |  |  |
| 5 | update_date | 否 |  |  |
| 6 | update_time | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | position_str | 否 |  | fund_account(18)+spectlbusi_kind(3) |
| 9 | branch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | spectlbusi_kind | 否 |  |  |
| 12 | remark | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | position_str | 否 |  | fund_account(18)+spectlbusi_kind(3) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_spectl_fundlist | 默认 | 否 |  |
| idx_spectl_fundlist | ART | 是 | fund_account, spectlbusi_kind, fund_account, spectlbusi_kind |
| idx_spectl_fundlist | 默认 | 否 |  |
| idx_spectl_fundlist | ART | 是 | fund_account, spectlbusi_kind, fund_account, spectlbusi_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_spectl_fundlist | fund_account, spectlbusi_kind, fund_account, spectlbusi_kind |
| idx_spectl_fundlist | fund_account, spectlbusi_kind, fund_account, spectlbusi_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:49:47 | 3.0.2.103 | taocong45644 | 当前表spectl_fundlist，修改了索引idx_spectl_fundlist,索引字段修改为：(fund_ac... |
| 2025-02-19 15:52:05 | 3.0.6.96 | 李想 | 新增表 |
| 2025-12-01 14:49:47 | 3.0.2.103 | taocong45644 | 当前表spectl_fundlist，修改了索引idx_spectl_fundlist,索引字段修改为：(fund_ac... |
| 2025-02-19 15:52:05 | 3.0.6.96 | 李想 | 新增表 |

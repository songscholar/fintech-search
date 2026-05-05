# ucrt_deducte_frozen_total - 融资融券缴款冻结汇总表

**表对象ID**: 7599
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | money_type | 否 |  |  |
| 4 | clear_balance | 否 |  |  |
| 5 | overdraft_balance | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | position_str | 否 |  | init_date(10) + fund_account(18) + money_type(3) + sett_batc |
| 8 | init_date | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | money_type | 否 |  |  |
| 11 | clear_balance | 否 |  |  |
| 12 | overdraft_balance | 否 |  |  |
| 13 | sett_batch_no | 否 |  |  |
| 14 | position_str | 否 |  | init_date(10) + fund_account(18) + money_type(3) + sett_batc |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrtdeductefrozentotal | ART | 是 | init_date, money_type, sett_batch_no, fund_account, init_date, money_type, sett_batch_no, fund_account |
| idx_ucrtdeductefrozentotal_pos | ART | 是 | position_str, position_str |
| idx_ucrtdeductefrozentotal | ART | 是 | init_date, money_type, sett_batch_no, fund_account, init_date, money_type, sett_batch_no, fund_account |
| idx_ucrtdeductefrozentotal_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrtdeductefrozentotal | init_date, money_type, sett_batch_no, fund_account, init_date, money_type, sett_batch_no, fund_account |
| idx_ucrtdeductefrozentotal | init_date, money_type, sett_batch_no, fund_account, init_date, money_type, sett_batch_no, fund_account |

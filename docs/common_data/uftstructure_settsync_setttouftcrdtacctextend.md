# setttouftcrdtacctextend - 清算融资融券扩展信息表

**表对象ID**: 3069
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 是 |  |  |
| 2 | client_id | 是 |  |  |
| 3 | fund_account | 是 |  |  |
| 4 | crdt_score | 是 |  |  |
| 5 | riskcrdt_flag | 是 |  |  |
| 6 | payoff_flag | 是 |  |  |
| 7 | remark | 是 |  |  |
| 8 | cashchange_status | 是 |  |  |
| 9 | cashchange_date | 是 |  |  |
| 10 | break_times | 是 |  |  |
| 11 | payoff_count | 是 |  |  |
| 12 | black_times | 是 |  |  |
| 13 | risk_restriction | 是 |  |  |
| 14 | join_acct_flag | 是 |  |  |
| 15 | uft_data_change_status | 是 |  |  |
| 16 | branch_no | 是 |  |  |
| 17 | client_id | 是 |  |  |
| 18 | fund_account | 是 |  |  |
| 19 | crdt_score | 是 |  |  |
| 20 | riskcrdt_flag | 是 |  |  |
| 21 | payoff_flag | 是 |  |  |
| 22 | remark | 是 |  |  |
| 23 | cashchange_status | 是 |  |  |
| 24 | cashchange_date | 是 |  |  |
| 25 | break_times | 是 |  |  |
| 26 | payoff_count | 是 |  |  |
| 27 | black_times | 是 |  |  |
| 28 | risk_restriction | 是 |  |  |
| 29 | join_acct_flag | 是 |  |  |
| 30 | uft_data_change_status | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settcrdtacctextend | 默认 | 是 | fund_account, fund_account |
| idx_settcrdtacctextend | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtacctextend | fund_account, fund_account |
| idx_crdtacctextend | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-07-13 17:26 | 8.26.1.29 | 彭立 | 新增 |
| 2018-07-13 17:26 | 8.26.1.29 | 彭立 | 新增 |

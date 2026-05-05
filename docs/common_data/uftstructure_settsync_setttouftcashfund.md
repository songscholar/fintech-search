# setttouftcashfund - 清算头寸资金额度表

**表对象ID**: 3301
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 是 |  |  |
| 2 | cashgroup_type | 是 |  |  |
| 3 | money_type | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | client_id | 是 |  |  |
| 6 | fin_total_balance | 是 |  |  |
| 7 | fin_used_balance | 是 |  |  |
| 8 | ref_due_balance | 是 |  |  |
| 9 | cashgroup_prop | 是 |  | 内存减少关联cashgroup取该字段 |
| 10 | company_no | 是 |  |  |
| 11 | position_str | 是 |  |  |
| 12 | uft_data_change_status | 是 |  |  |
| 13 | cashgroup_no | 是 |  |  |
| 14 | cashgroup_type | 是 |  |  |
| 15 | money_type | 是 |  |  |
| 16 | fund_account | 是 |  |  |
| 17 | client_id | 是 |  |  |
| 18 | fin_total_balance | 是 |  |  |
| 19 | fin_used_balance | 是 |  |  |
| 20 | ref_due_balance | 是 |  |  |
| 21 | cashgroup_prop | 是 |  | 内存减少关联cashgroup取该字段 |
| 22 | company_no | 是 |  |  |
| 23 | position_str | 是 |  |  |
| 24 | uft_data_change_status | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settcashfund | 默认 | 是 | cashgroup_no, cashgroup_type, money_type, cashgroup_no, cashgroup_type, money_type |
| idx_settcashfund_acct | 默认 | 是 | fund_account, fund_account |
| idx_settcashfund_prop | 默认 | 是 | cashgroup_prop, cashgroup_no, cashgroup_prop, cashgroup_no |
| idx_settcashfund_cash | 默认 | 是 | position_str, position_str |
| idx_settcashfund | 默认 | 是 | cashgroup_no, cashgroup_type, money_type, cashgroup_no, cashgroup_type, money_type |
| idx_settcashfund_acct | 默认 | 是 | fund_account, fund_account |
| idx_settcashfund_prop | 默认 | 是 | cashgroup_prop, cashgroup_no, cashgroup_prop, cashgroup_no |
| idx_settcashfund_cash | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtfund | cashgroup_no, cashgroup_type, money_type, cashgroup_no, cashgroup_type, money_type |
| idx_crdtfund | cashgroup_no, cashgroup_type, money_type, cashgroup_no, cashgroup_type, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2019-11-27 11:36 | 8.26.1.58 | 蒋迪 | 新增uft_data_change_status |
| 2019-05-14 21:11 | 8.26.1.52 | 林忠芝 | 内存新增cashgroup_prop和company_no字段，为减少关联cashgroup取该字段 |
| 2019-11-27 11:36 | 8.26.1.58 | 蒋迪 | 新增uft_data_change_status |
| 2019-05-14 21:11 | 8.26.1.52 | 林忠芝 | 内存新增cashgroup_prop和company_no字段，为减少关联cashgroup取该字段 |

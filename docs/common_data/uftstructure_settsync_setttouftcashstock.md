# setttouftcashstock - 清算头寸股份额度表

**表对象ID**: 3302
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 是 |  |  |
| 2 | cashgroup_type | 是 |  |  |
| 3 | fund_account | 是 |  |  |
| 4 | client_id | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | stock_code | 是 |  |  |
| 8 | stock_type | 是 |  |  |
| 9 | money_type | 是 |  |  |
| 10 | slo_total_amount | 是 |  |  |
| 11 | slo_used_amount | 是 |  |  |
| 12 | ref_due_amount | 是 |  |  |
| 13 | surstock_amount | 是 |  |  |
| 14 | cashgroup_prop | 是 |  |  |
| 15 | company_no | 是 |  |  |
| 16 | position_str | 是 |  |  |
| 17 | uft_data_change_status | 是 |  |  |
| 18 | cashgroup_no | 是 |  |  |
| 19 | cashgroup_type | 是 |  |  |
| 20 | fund_account | 是 |  |  |
| 21 | client_id | 是 |  |  |
| 22 | exchange_type | 是 |  |  |
| 23 | stock_account | 是 |  |  |
| 24 | stock_code | 是 |  |  |
| 25 | stock_type | 是 |  |  |
| 26 | money_type | 是 |  |  |
| 27 | slo_total_amount | 是 |  |  |
| 28 | slo_used_amount | 是 |  |  |
| 29 | ref_due_amount | 是 |  |  |
| 30 | surstock_amount | 是 |  |  |
| 31 | cashgroup_prop | 是 |  |  |
| 32 | company_no | 是 |  |  |
| 33 | position_str | 是 |  |  |
| 34 | uft_data_change_status | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settcashstock | 默认 | 是 | cashgroup_no, cashgroup_type, stock_code, exchange_type, cashgroup_no, cashgroup_type, stock_code, exchange_type |
| idx_settcashstock_porp | 默认 | 是 | cashgroup_prop, cashgroup_no, cashgroup_prop, cashgroup_no |
| idx_settcashstock_pos | 默认 | 是 | position_str, position_str |
| idx_settcashstock | 默认 | 是 | cashgroup_no, cashgroup_type, stock_code, exchange_type, cashgroup_no, cashgroup_type, stock_code, exchange_type |
| idx_settcashstock_porp | 默认 | 是 | cashgroup_prop, cashgroup_no, cashgroup_prop, cashgroup_no |
| idx_settcashstock_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_cashstock | cashgroup_no, cashgroup_type, stock_code, exchange_type, cashgroup_no, cashgroup_type, stock_code, exchange_type |
| idx_cashstock | cashgroup_no, cashgroup_type, stock_code, exchange_type, cashgroup_no, cashgroup_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-04-23 16:55 | 8.26.1.61 | 曾哲 | 新增字段stock_type,surstock_amount |
| 2019-11-27 13:43 | 8.26.1.58 | 蒋迪 | 新增uft_data_change_status |
| 2019-05-14 21:12 | 8.26.1.52 | 林忠芝 | 内存新增cashgroup_prop和company_no字段，为减少关联cashgroup取该字段 |
| 2020-04-23 16:55 | 8.26.1.61 | 曾哲 | 新增字段stock_type,surstock_amount |
| 2019-11-27 13:43 | 8.26.1.58 | 蒋迪 | 新增uft_data_change_status |
| 2019-05-14 21:12 | 8.26.1.52 | 林忠芝 | 内存新增cashgroup_prop和company_no字段，为减少关联cashgroup取该字段 |

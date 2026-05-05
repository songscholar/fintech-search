# setttouftszhkequity - 清算深港通权益信息表

**表对象ID**: 3043
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_id | 是 |  |  |
| 2 | init_date | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | stock_code | 是 |  |  |
| 8 | entrust_amount | 是 |  |  |
| 9 | market_prop | 是 |  |  |
| 10 | szhk_authority_prop | 是 |  |  |
| 11 | szhk_authority_id | 是 |  |  |
| 12 | position_str | 是 |  |  |
| 13 | seat_no | 是 |  |  |
| 14 | frozen_amount | 是 |  |  |
| 15 | uft_data_change_status | 是 |  |  |
| 16 | sett_id | 是 |  |  |
| 17 | init_date | 是 |  |  |
| 18 | branch_no | 是 |  |  |
| 19 | fund_account | 是 |  |  |
| 20 | exchange_type | 是 |  |  |
| 21 | stock_account | 是 |  |  |
| 22 | stock_code | 是 |  |  |
| 23 | entrust_amount | 是 |  |  |
| 24 | market_prop | 是 |  |  |
| 25 | szhk_authority_prop | 是 |  |  |
| 26 | szhk_authority_id | 是 |  |  |
| 27 | position_str | 是 |  |  |
| 28 | seat_no | 是 |  |  |
| 29 | frozen_amount | 是 |  |  |
| 30 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_settszhkequity | 默认 | 是 | position_str, position_str |
| idx_settszhkequity_fund | 默认 | 是 | fund_account, stock_code, fund_account, stock_code |
| uk_settszhkequity | 默认 | 是 | position_str, position_str |
| idx_settszhkequity_fund | 默认 | 是 | fund_account, stock_code, fund_account, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settszhkequity_fund | fund_account, stock_code, fund_account, stock_code |
| idx_settszhkequity_fund | fund_account, stock_code, fund_account, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-03-30 11:04 | 8.26.1.77 | 曾哲 | 增加idx_settszhkequity_fund索引 |
| 2018-12-19 10:18 | 8.26.1.53 | 曾哲 | 新增 |
| 2020-03-30 11:04 | 8.26.1.77 | 曾哲 | 增加idx_settszhkequity_fund索引 |
| 2018-12-19 10:18 | 8.26.1.53 | 曾哲 | 新增 |

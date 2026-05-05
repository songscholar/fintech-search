# setttouftassurestock - 清算担保持仓表

**表对象ID**: 3034
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 是 |  |  |
| 2 | client_id | 是 |  |  |
| 3 | stock_account | 是 |  |  |
| 4 | stock_open_date | 是 |  |  |
| 5 | branch_no | 是 |  |  |
| 6 | stock_code | 是 |  |  |
| 7 | exchange_type | 是 |  |  |
| 8 | stock_type | 是 |  |  |
| 9 | assure_type | 是 |  |  |
| 10 | impawn_amount | 是 |  |  |
| 11 | pre_impawn_amount | 是 |  |  |
| 12 | position_str | 是 |  |  |
| 13 | remark | 是 |  |  |
| 14 | uft_data_change_status | 是 |  |  |
| 15 | out_impawn_amount | 是 |  |  |
| 16 | fund_account | 是 |  |  |
| 17 | client_id | 是 |  |  |
| 18 | stock_account | 是 |  |  |
| 19 | stock_open_date | 是 |  |  |
| 20 | branch_no | 是 |  |  |
| 21 | stock_code | 是 |  |  |
| 22 | exchange_type | 是 |  |  |
| 23 | stock_type | 是 |  |  |
| 24 | assure_type | 是 |  |  |
| 25 | impawn_amount | 是 |  |  |
| 26 | pre_impawn_amount | 是 |  |  |
| 27 | position_str | 是 |  |  |
| 28 | remark | 是 |  |  |
| 29 | uft_data_change_status | 是 |  |  |
| 30 | out_impawn_amount | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settassurestock_acct | 默认 | 是 | fund_account, fund_account |
| idx_settassurestock_pos | 默认 | 是 | position_str, position_str |
| idx_settassurestock_acct | 默认 | 是 | fund_account, fund_account |
| idx_settassurestock_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_settassurestock_acct | fund_account, fund_account |
| idx_settassurestock_pos | position_str, position_str |
| idx_settassurestock_acct | fund_account, fund_account |
| idx_settassurestock_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-09-04 09:52 | 8.26.2.56 | 丁界成 | 增加out_impawn_amount |
| 2018-05-18 15:55 | 8.26.1.15 | 王天成 | 新增 |
| 2023-09-04 09:52 | 8.26.2.56 | 丁界成 | 增加out_impawn_amount |
| 2018-05-18 15:55 | 8.26.1.15 | 王天成 | 新增 |

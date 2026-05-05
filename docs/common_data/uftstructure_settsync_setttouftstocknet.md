# setttouftstocknet - 清算股份轧差表

**表对象ID**: 3033
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_account | 是 |  |  |
| 2 | stock_code | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | exchange_type | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | stock_type | 是 |  |  |
| 8 | stocknet_kind | 是 |  |  |
| 9 | begin_gap_amount | 是 |  |  |
| 10 | buy_real_amount1 | 是 |  |  |
| 11 | buy_real_amount2 | 是 |  |  |
| 12 | prev_amount | 是 |  |  |
| 13 | uft_data_change_status | 是 |  |  |
| 14 | stock_account | 是 |  |  |
| 15 | stock_code | 是 |  |  |
| 16 | branch_no | 是 |  |  |
| 17 | exchange_type | 是 |  |  |
| 18 | fund_account | 是 |  |  |
| 19 | client_id | 是 |  |  |
| 20 | stock_type | 是 |  |  |
| 21 | stocknet_kind | 是 |  |  |
| 22 | begin_gap_amount | 是 |  |  |
| 23 | buy_real_amount1 | 是 |  |  |
| 24 | buy_real_amount2 | 是 |  |  |
| 25 | prev_amount | 是 |  |  |
| 26 | uft_data_change_status | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settstocknet | 默认 | 是 | stock_account, stock_code, branch_no, exchange_type, fund_account, stocknet_kind, stock_account, stock_code, branch_no, exchange_type, fund_account, stocknet_kind |
| idx_settstocknet_acct | 默认 | 是 | fund_account, fund_account |
| idx_settstocknet_exch | 默认 | 是 | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |
| idx_settstocknet | 默认 | 是 | stock_account, stock_code, branch_no, exchange_type, fund_account, stocknet_kind, stock_account, stock_code, branch_no, exchange_type, fund_account, stocknet_kind |
| idx_settstocknet_acct | 默认 | 是 | fund_account, fund_account |
| idx_settstocknet_exch | 默认 | 是 | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settstocknet | stock_account, stock_code, branch_no, exchange_type, fund_account, stocknet_kind, stock_account, stock_code, branch_no, exchange_type, fund_account, stocknet_kind |
| idx_settstocknet | stock_account, stock_code, branch_no, exchange_type, fund_account, stocknet_kind, stock_account, stock_code, branch_no, exchange_type, fund_account, stocknet_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-05-03 19:02 | 8.26.1.11 | 王泽贵 | 新增表 |
| 2018-05-03 19:02 | 8.26.1.11 | 王泽贵 | 新增表 |

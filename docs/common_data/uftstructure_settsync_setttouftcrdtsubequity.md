# setttouftcrdtsubequity - 融资融券申购权益表

**表对象ID**: 3058
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | stock_account | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | exchange_type | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | enable_amount | 是 |  |  |
| 8 | register_date | 是 |  |  |
| 9 | seat_no | 是 |  |  |
| 10 | set_seat_no | 是 |  |  |
| 11 | stib_enable_quota | 是 |  |  |
| 12 | init_date | 是 |  |  |
| 13 | stock_account | 是 |  |  |
| 14 | branch_no | 是 |  |  |
| 15 | exchange_type | 是 |  |  |
| 16 | fund_account | 是 |  |  |
| 17 | client_id | 是 |  |  |
| 18 | enable_amount | 是 |  |  |
| 19 | register_date | 是 |  |  |
| 20 | seat_no | 是 |  |  |
| 21 | set_seat_no | 是 |  |  |
| 22 | stib_enable_quota | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtsubequity | 默认 | 是 | stock_account, branch_no, exchange_type, fund_account, stock_account, branch_no, exchange_type, fund_account |
| idx_crdtsubequity | 默认 | 是 | stock_account, branch_no, exchange_type, fund_account, stock_account, branch_no, exchange_type, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtsubequity | stock_account, branch_no, stock_account, branch_no |
| idx_crdtsubequity | stock_account, branch_no, stock_account, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2019-04-29 09:42 | 8.26.1.50 | 王天成 | 增加字段stib_enable_quota |
| 2019-04-29 09:42 | 8.26.1.50 | 王天成 | 增加字段stib_enable_quota |

# setttouftarpequity - 清算约定购回权益表

**表对象ID**: 3022
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_id | 是 |  |  |
| 3 | contract_id | 是 |  |  |
| 4 | arp_equity_type | 是 |  |  |
| 5 | branch_no | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | stock_account | 是 |  |  |
| 9 | exchange_type | 是 |  |  |
| 10 | stock_code | 是 |  |  |
| 11 | stock_type | 是 |  |  |
| 12 | money_type | 是 |  |  |
| 13 | register_amount | 是 |  |  |
| 14 | bonus_amount | 是 |  |  |
| 15 | bonus_balance | 是 |  |  |
| 16 | orig_entrust_date | 是 |  |  |
| 17 | orig_entrust_no | 是 |  |  |
| 18 | entrust_date | 是 |  |  |
| 19 | entrust_no | 是 |  |  |
| 20 | deal_status | 是 |  |  |
| 21 | date_clear | 是 |  |  |
| 22 | date_back | 是 |  |  |
| 23 | report_id | 是 |  |  |
| 24 | premark | 是 |  |  |
| 25 | position_str | 是 |  |  |
| 26 | uft_data_change_status | 是 |  |  |
| 27 | init_date | 是 |  |  |
| 28 | sett_id | 是 |  |  |
| 29 | contract_id | 是 |  |  |
| 30 | arp_equity_type | 是 |  |  |
| 31 | branch_no | 是 |  |  |
| 32 | fund_account | 是 |  |  |
| 33 | client_id | 是 |  |  |
| 34 | stock_account | 是 |  |  |
| 35 | exchange_type | 是 |  |  |
| 36 | stock_code | 是 |  |  |
| 37 | stock_type | 是 |  |  |
| 38 | money_type | 是 |  |  |
| 39 | register_amount | 是 |  |  |
| 40 | bonus_amount | 是 |  |  |
| 41 | bonus_balance | 是 |  |  |
| 42 | orig_entrust_date | 是 |  |  |
| 43 | orig_entrust_no | 是 |  |  |
| 44 | entrust_date | 是 |  |  |
| 45 | entrust_no | 是 |  |  |
| 46 | deal_status | 是 |  |  |
| 47 | date_clear | 是 |  |  |
| 48 | date_back | 是 |  |  |
| 49 | report_id | 是 |  |  |
| 50 | premark | 是 |  |  |
| 51 | position_str | 是 |  |  |
| 52 | uft_data_change_status | 是 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settarpequity | 默认 | 是 | contract_id, arp_equity_type, contract_id, arp_equity_type |
| idx_settarpequity_entrust | 默认 | 是 | entrust_no, entrust_date, entrust_no, entrust_date |
| idx_settarpequity_code | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_settarpequity_acct | 默认 | 是 | fund_account, fund_account |
| idx_settarpequity_exch | 默认 | 是 | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |
| idx_settarpequity | 默认 | 是 | contract_id, arp_equity_type, contract_id, arp_equity_type |
| idx_settarpequity_entrust | 默认 | 是 | entrust_no, entrust_date, entrust_no, entrust_date |
| idx_settarpequity_code | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_settarpequity_acct | 默认 | 是 | fund_account, fund_account |
| idx_settarpequity_exch | 默认 | 是 | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settarpequity | contract_id, contract_id |
| idx_settarpequity | contract_id, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-03-24 10:26 | 8.26.1.3 | 黄飞 | 添加idx_settarpequity_code、idx_settarpequity_acct、idx_settarpe... |
| 2018-03-24 10:26 | 8.26.1.3 | 黄飞 | 添加idx_settarpequity_code、idx_settarpequity_acct、idx_settarpe... |

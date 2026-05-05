# transferentrust_tosett - 清算非交易过户委托表

**表对象ID**: 3093
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | company_no | 是 |  |  |
| 4 | entrust_no | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | client_id | 是 |  |  |
| 7 | fund_account_src | 是 |  |  |
| 8 | client_id_src | 是 |  |  |
| 9 | stock_account_src | 是 |  |  |
| 10 | seat_no_src | 是 |  |  |
| 11 | branch_no_src | 是 |  |  |
| 12 | fund_account_dest | 是 |  |  |
| 13 | client_id_dest | 是 |  |  |
| 14 | stock_account_dest | 是 |  |  |
| 15 | seat_no_dest | 是 |  |  |
| 16 | branch_no_dest | 是 |  |  |
| 17 | withdraw_flag | 是 |  |  |
| 18 | frozen_serial_no | 是 |  |  |
| 19 | unfrozen_status | 是 |  |  |
| 20 | cost_price | 是 |  |  |
| 21 | position_str | 是 |  |  |
| 22 | return_serial_no | 是 |  |  |
| 23 | return_time | 是 |  |  |
| 24 | return_code | 是 |  |  |
| 25 | return_info | 是 |  |  |
| 26 | cancel_serial_no | 是 |  |  |
| 27 | init_date | 是 |  |  |
| 28 | branch_no | 是 |  |  |
| 29 | company_no | 是 |  |  |
| 30 | entrust_no | 是 |  |  |
| 31 | fund_account | 是 |  |  |
| 32 | client_id | 是 |  |  |
| 33 | fund_account_src | 是 |  |  |
| 34 | client_id_src | 是 |  |  |
| 35 | stock_account_src | 是 |  |  |
| 36 | seat_no_src | 是 |  |  |
| 37 | branch_no_src | 是 |  |  |
| 38 | fund_account_dest | 是 |  |  |
| 39 | client_id_dest | 是 |  |  |
| 40 | stock_account_dest | 是 |  |  |
| 41 | seat_no_dest | 是 |  |  |
| 42 | branch_no_dest | 是 |  |  |
| 43 | withdraw_flag | 是 |  |  |
| 44 | frozen_serial_no | 是 |  |  |
| 45 | unfrozen_status | 是 |  |  |
| 46 | cost_price | 是 |  |  |
| 47 | position_str | 是 |  |  |
| 48 | return_serial_no | 是 |  |  |
| 49 | return_time | 是 |  |  |
| 50 | return_code | 是 |  |  |
| 51 | return_info | 是 |  |  |
| 52 | cancel_serial_no | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_transferentrust_tosett | 默认 | 是 | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_transferentrust_tosett_status | 默认 | 是 | unfrozen_status, unfrozen_status |
| idx_transferentrust_tosett | 默认 | 是 | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_transferentrust_tosett_status | 默认 | 是 | unfrozen_status, unfrozen_status |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_transfer_entrust_tosett | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_transfer_entrust_tosett | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |

# setttouftarpapply - 清算约定购回申请表

**表对象ID**: 3035
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 86 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | contract_id | 是 |  |  |
| 4 | join_contract_id | 是 |  |  |
| 5 | papercont_id | 是 |  |  |
| 6 | arp_apply_type | 是 |  |  |
| 7 | op_entrust_way | 是 |  |  |
| 8 | branch_no | 是 |  |  |
| 9 | fund_account | 是 |  |  |
| 10 | client_id | 是 |  |  |
| 11 | stock_account | 是 |  |  |
| 12 | exchange_type | 是 |  |  |
| 13 | funder_no | 是 |  |  |
| 14 | stock_code | 是 |  |  |
| 15 | stock_type | 是 |  |  |
| 16 | expire_year_rate | 是 |  |  |
| 17 | entrust_amount | 是 |  |  |
| 18 | entrust_balance | 是 |  |  |
| 19 | back_principal | 是 |  |  |
| 20 | back_balance | 是 |  |  |
| 21 | date_back | 是 |  |  |
| 22 | entrust_date | 是 |  |  |
| 23 | entrust_no | 是 |  |  |
| 24 | ask_back_balance | 是 |  |  |
| 25 | ask_date_back | 是 |  |  |
| 26 | ask_year_rate | 是 |  |  |
| 27 | arp_apply_status | 是 |  |  |
| 28 | sign_date | 是 |  |  |
| 29 | sign_operator_no | 是 |  |  |
| 30 | fund_useage | 是 |  |  |
| 31 | audit_remark | 是 |  |  |
| 32 | rate_mode | 是 |  |  |
| 33 | assure_ratio | 是 |  |  |
| 34 | assure_price | 是 |  |  |
| 35 | stkused_flag | 是 |  |  |
| 36 | stkused_year_rate | 是 |  |  |
| 37 | margin_focus_ratio | 是 |  |  |
| 38 | margin_alert_ratio | 是 |  |  |
| 39 | margin_treat_ratio | 是 |  |  |
| 40 | date_clear | 是 |  |  |
| 41 | remark | 是 |  |  |
| 42 | position_str | 是 |  |  |
| 43 | uft_data_change_status | 是 |  |  |
| 44 | init_date | 是 |  |  |
| 45 | serial_no | 是 |  |  |
| 46 | contract_id | 是 |  |  |
| 47 | join_contract_id | 是 |  |  |
| 48 | papercont_id | 是 |  |  |
| 49 | arp_apply_type | 是 |  |  |
| 50 | op_entrust_way | 是 |  |  |
| 51 | branch_no | 是 |  |  |
| 52 | fund_account | 是 |  |  |
| 53 | client_id | 是 |  |  |
| 54 | stock_account | 是 |  |  |
| 55 | exchange_type | 是 |  |  |
| 56 | funder_no | 是 |  |  |
| 57 | stock_code | 是 |  |  |
| 58 | stock_type | 是 |  |  |
| 59 | expire_year_rate | 是 |  |  |
| 60 | entrust_amount | 是 |  |  |
| 61 | entrust_balance | 是 |  |  |
| 62 | back_principal | 是 |  |  |
| 63 | back_balance | 是 |  |  |
| 64 | date_back | 是 |  |  |
| 65 | entrust_date | 是 |  |  |
| 66 | entrust_no | 是 |  |  |
| 67 | ask_back_balance | 是 |  |  |
| 68 | ask_date_back | 是 |  |  |
| 69 | ask_year_rate | 是 |  |  |
| 70 | arp_apply_status | 是 |  |  |
| 71 | sign_date | 是 |  |  |
| 72 | sign_operator_no | 是 |  |  |
| 73 | fund_useage | 是 |  |  |
| 74 | audit_remark | 是 |  |  |
| 75 | rate_mode | 是 |  |  |
| 76 | assure_ratio | 是 |  |  |
| 77 | assure_price | 是 |  |  |
| 78 | stkused_flag | 是 |  |  |
| 79 | stkused_year_rate | 是 |  |  |
| 80 | margin_focus_ratio | 是 |  |  |
| 81 | margin_alert_ratio | 是 |  |  |
| 82 | margin_treat_ratio | 是 |  |  |
| 83 | date_clear | 是 |  |  |
| 84 | remark | 是 |  |  |
| 85 | position_str | 是 |  |  |
| 86 | uft_data_change_status | 是 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settarpapply | 默认 | 是 | serial_no, init_date, serial_no, init_date |
| idx_settarpapply_id | 默认 | 是 | contract_id, contract_id |
| idx_settarpapply_acct | 默认 | 是 | fund_account, fund_account |
| idx_settarpapply_code | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_settarpapply_exch | 默认 | 是 | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |
| idx_settarpapply | 默认 | 是 | serial_no, init_date, serial_no, init_date |
| idx_settarpapply_id | 默认 | 是 | contract_id, contract_id |
| idx_settarpapply_acct | 默认 | 是 | fund_account, fund_account |
| idx_settarpapply_code | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_settarpapply_exch | 默认 | 是 | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settarpapply | serial_no, init_date, serial_no, init_date |
| idx_settarpapply | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-05-29 19:19 | 8.26.1.24 | 黄飞 | 修改索引属性 |
| 2018-05-21 17:38 | 8.26.1.16 | 曾哲 | 新增 |
| 2018-05-29 19:19 | 8.26.1.24 | 黄飞 | 修改索引属性 |
| 2018-05-21 17:38 | 8.26.1.16 | 曾哲 | 新增 |

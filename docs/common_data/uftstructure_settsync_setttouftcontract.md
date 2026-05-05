# setttouftcontract - 清算存管信用合同表

**表对象ID**: 3068
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 84 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | contract_id | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | client_id | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | crdtint_mode | 是 |  |  |
| 7 | settpay_mode | 是 |  |  |
| 8 | crdt_fare_str | 是 |  |  |
| 9 | contract_rights | 是 |  |  |
| 10 | fin_max_quota | 是 |  |  |
| 11 | slo_max_quota | 是 |  |  |
| 12 | total_max_quota | 是 |  |  |
| 13 | papercont_id | 是 |  |  |
| 14 | compact_term | 是 |  |  |
| 15 | crdt_level | 是 |  |  |
| 16 | build_date | 是 |  |  |
| 17 | begin_date | 是 |  |  |
| 18 | end_date | 是 |  |  |
| 19 | sign_operator_no | 是 |  |  |
| 20 | sign_date | 是 |  |  |
| 21 | sign_address | 是 |  |  |
| 22 | cashgroup_no | 是 |  |  |
| 23 | fin_cashgroup_no | 是 |  |  |
| 24 | slo_cashgroup_no | 是 |  |  |
| 25 | clientcr_id | 是 |  |  |
| 26 | contract_status | 是 |  |  |
| 27 | auto_interest_cycle | 是 |  |  |
| 28 | auto_interest_mode | 是 |  |  |
| 29 | date_clear | 是 |  |  |
| 30 | position_str | 是 |  |  |
| 31 | remark | 是 |  |  |
| 32 | primerate_begin_date | 是 |  |  |
| 33 | primerate_end_date | 是 |  |  |
| 34 | uft_data_change_status | 是 |  |  |
| 35 | onsale_mode | 是 |  |  |
| 36 | package_kind_str | 是 |  |  |
| 37 | package_begin_date | 是 |  |  |
| 38 | package_end_date | 是 |  |  |
| 39 | pendfare_deferred_days | 是 |  |  |
| 40 | corp_end_date | 是 |  |  |
| 41 | contract_selfcancel_flag | 是 |  |  |
| 42 | violate_days | 是 |  |  |
| 43 | init_date | 是 |  |  |
| 44 | contract_id | 是 |  |  |
| 45 | branch_no | 是 |  |  |
| 46 | client_id | 是 |  |  |
| 47 | fund_account | 是 |  |  |
| 48 | crdtint_mode | 是 |  |  |
| 49 | settpay_mode | 是 |  |  |
| 50 | crdt_fare_str | 是 |  |  |
| 51 | contract_rights | 是 |  |  |
| 52 | fin_max_quota | 是 |  |  |
| 53 | slo_max_quota | 是 |  |  |
| 54 | total_max_quota | 是 |  |  |
| 55 | papercont_id | 是 |  |  |
| 56 | compact_term | 是 |  |  |
| 57 | crdt_level | 是 |  |  |
| 58 | build_date | 是 |  |  |
| 59 | begin_date | 是 |  |  |
| 60 | end_date | 是 |  |  |
| 61 | sign_operator_no | 是 |  |  |
| 62 | sign_date | 是 |  |  |
| 63 | sign_address | 是 |  |  |
| 64 | cashgroup_no | 是 |  |  |
| 65 | fin_cashgroup_no | 是 |  |  |
| 66 | slo_cashgroup_no | 是 |  |  |
| 67 | clientcr_id | 是 |  |  |
| 68 | contract_status | 是 |  |  |
| 69 | auto_interest_cycle | 是 |  |  |
| 70 | auto_interest_mode | 是 |  |  |
| 71 | date_clear | 是 |  |  |
| 72 | position_str | 是 |  |  |
| 73 | remark | 是 |  |  |
| 74 | primerate_begin_date | 是 |  |  |
| 75 | primerate_end_date | 是 |  |  |
| 76 | uft_data_change_status | 是 |  |  |
| 77 | onsale_mode | 是 |  |  |
| 78 | package_kind_str | 是 |  |  |
| 79 | package_begin_date | 是 |  |  |
| 80 | package_end_date | 是 |  |  |
| 81 | pendfare_deferred_days | 是 |  |  |
| 82 | corp_end_date | 是 |  |  |
| 83 | contract_selfcancel_flag | 是 |  |  |
| 84 | violate_days | 是 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settcontract | 默认 | 是 | contract_id, contract_id |
| idx_settcontract_id | 默认 | 是 | client_id, client_id |
| idx_settcontract_acct | 默认 | 是 | fund_account, fund_account |
| idx_settcontract_pos | 默认 | 是 | position_str, position_str |
| idx_settcontract | 默认 | 是 | contract_id, contract_id |
| idx_settcontract_id | 默认 | 是 | client_id, client_id |
| idx_settcontract_acct | 默认 | 是 | fund_account, fund_account |
| idx_settcontract_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 8 个）

| 索引名 | 字段 |
|--------|------|
| idx_contract | init_date, position_str, init_date, position_str |
| idx_contract_id | client_id, client_id |
| idx_contract_acct | fund_account, fund_account |
| idx_contract_pos | position_str, position_str |
| idx_contract | init_date, position_str, init_date, position_str |
| idx_contract_id | client_id, client_id |
| idx_contract_acct | fund_account, fund_account |
| idx_contract_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-03-17 16:58 | 8.26.2.35 | 徐开 | 增加corp_end_date、contract_selfcancel_flag字段 |
| 2021-05-11 10:44 | 8.26.1.94 | 罗佳楠 | 新增pendfare_deferred_days |
| 2021-04-15 18:03 | 8.26.1.90 | 罗佳楠 | 补充字段 |
| 2020-05-03 09:36 | 8.26.1.66 | 曾哲 | 补充字段，与UF20保持一致 |
| 2018-06-12 21:00 | 8.26.1.25 | 徐斐 | 新增onsale_mode |
| 2018-05-21 11:39 | 8.26.1.22 | 徐斐 | 新增 |
| 2023-03-17 16:58 | 8.26.2.35 | 徐开 | 增加corp_end_date、contract_selfcancel_flag字段 |
| 2021-05-11 10:44 | 8.26.1.94 | 罗佳楠 | 新增pendfare_deferred_days |
| 2021-04-15 18:03 | 8.26.1.90 | 罗佳楠 | 补充字段 |
| 2020-05-03 09:36 | 8.26.1.66 | 曾哲 | 补充字段，与UF20保持一致 |
| 2018-06-12 21:00 | 8.26.1.25 | 徐斐 | 新增onsale_mode |
| 2018-05-21 11:39 | 8.26.1.22 | 徐斐 | 新增 |

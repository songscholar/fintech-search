# settredo_arp_equity - 清算重做约定购回权益表

**表对象ID**: 12506
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | contract_id | 否 |  |  |
| 3 | arp_equity_type | 否 |  |  |
| 4 | register_amount | 否 |  |  |
| 5 | bonus_amount | 否 |  |  |
| 6 | bonus_balance | 否 |  |  |
| 7 | deal_status | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | sett_dml_type | 否 |  |  |
| 11 | sett_batch_no | 否 |  |  |
| 12 | branch_no | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | stock_type | 否 |  |  |
| 19 | money_type | 否 |  |  |
| 20 | orig_entrust_date | 否 |  |  |
| 21 | orig_entrust_no | 否 |  |  |
| 22 | entrust_date | 否 |  |  |
| 23 | entrust_no | 否 |  |  |
| 24 | date_back | 否 |  |  |
| 25 | report_id | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | init_date | 否 |  |  |
| 28 | contract_id | 否 |  |  |
| 29 | arp_equity_type | 否 |  |  |
| 30 | register_amount | 否 |  |  |
| 31 | bonus_amount | 否 |  |  |
| 32 | bonus_balance | 否 |  |  |
| 33 | deal_status | 否 |  |  |
| 34 | date_clear | 否 |  |  |
| 35 | remark | 否 |  |  |
| 36 | sett_dml_type | 否 |  |  |
| 37 | sett_batch_no | 否 |  |  |
| 38 | branch_no | 否 |  |  |
| 39 | fund_account | 否 |  |  |
| 40 | client_id | 否 |  |  |
| 41 | stock_account | 否 |  |  |
| 42 | exchange_type | 否 |  |  |
| 43 | stock_code | 否 |  |  |
| 44 | stock_type | 否 |  |  |
| 45 | money_type | 否 |  |  |
| 46 | orig_entrust_date | 否 |  |  |
| 47 | orig_entrust_no | 否 |  |  |
| 48 | entrust_date | 否 |  |  |
| 49 | entrust_no | 否 |  |  |
| 50 | date_back | 否 |  |  |
| 51 | report_id | 否 |  |  |
| 52 | position_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_arpequity | ART | 是 | sett_batch_no, contract_id, arp_equity_type, sett_batch_no, contract_id, arp_equity_type |
| idx_settredo_arpequity | ART | 是 | sett_batch_no, contract_id, arp_equity_type, sett_batch_no, contract_id, arp_equity_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_arpequity | sett_batch_no, contract_id, arp_equity_type, sett_batch_no, contract_id, arp_equity_type |
| idx_settredo_arpequity | sett_batch_no, contract_id, arp_equity_type, sett_batch_no, contract_id, arp_equity_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:34:15 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-11-10 16:37:32 | 8.26.2.92 |  | 所有表settredo_arp_equity，添加了表字段(branch_no);
所有表settredo_arp_e... |
| 2025-08-04 16:14:06 | V3.0.6.13 | taocong45644 | 新增表 |
| 2026-03-04 16:34:15 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-11-10 16:37:32 | 8.26.2.92 |  | 所有表settredo_arp_equity，添加了表字段(branch_no);
所有表settredo_arp_e... |
| 2025-08-04 16:14:06 | V3.0.6.13 | taocong45644 | 新增表 |

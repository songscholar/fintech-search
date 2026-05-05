# settredo_srp_equity - 清算重做股票质押权益表

**表对象ID**: 2653
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | register_amount | 否 |  |  |
| 2 | bonus_amount | 否 |  |  |
| 3 | bonus_balance | 否 |  |  |
| 4 | deal_status | 否 |  |  |
| 5 | date_clear | 否 |  |  |
| 6 | remark | 否 |  |  |
| 7 | position_str | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | sett_dml_type | 否 |  |  |
| 10 | init_date | 否 |  |  |
| 11 | contract_id | 否 |  |  |
| 12 | srp_equity_type | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | money_type | 否 |  |  |
| 21 | orig_entrust_date | 否 |  |  |
| 22 | orig_entrust_no | 否 |  |  |
| 23 | entrust_date | 否 |  |  |
| 24 | entrust_no | 否 |  |  |
| 25 | date_back | 否 |  |  |
| 26 | register_amount | 否 |  |  |
| 27 | bonus_amount | 否 |  |  |
| 28 | bonus_balance | 否 |  |  |
| 29 | deal_status | 否 |  |  |
| 30 | date_clear | 否 |  |  |
| 31 | remark | 否 |  |  |
| 32 | position_str | 否 |  |  |
| 33 | sett_batch_no | 否 |  |  |
| 34 | sett_dml_type | 否 |  |  |
| 35 | init_date | 否 |  |  |
| 36 | contract_id | 否 |  |  |
| 37 | srp_equity_type | 否 |  |  |
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

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_srpequity_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_srpequity_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_srpequity_pos | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_srpequity_pos | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:01:39 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-11-12 14:16:36 | 8.26.2.92 | 马天宇 | 所有表settredo_srp_equity，添加了表字段(init_date);
所有表settredo_srp_e... |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2026-03-06 17:01:39 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-11-12 14:16:36 | 8.26.2.92 | 马天宇 | 所有表settredo_srp_equity，添加了表字段(init_date);
所有表settredo_srp_e... |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |

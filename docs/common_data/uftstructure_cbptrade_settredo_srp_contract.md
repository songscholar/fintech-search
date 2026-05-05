# settredo_srp_contract - 清算重做股票质押合同表

**表对象ID**: 2646
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sum_back_amount | 否 |  |  |
| 2 | sum_back_balance | 否 |  |  |
| 3 | bonus_amount | 否 |  |  |
| 4 | bonus_balance | 否 |  |  |
| 5 | back_principal | 否 |  |  |
| 6 | repaid_balance | 否 |  |  |
| 7 | settle_interest | 否 |  |  |
| 8 | unsettle_interest | 否 |  |  |
| 9 | real_date_back | 否 |  |  |
| 10 | real_back_balance | 否 |  |  |
| 11 | back_type | 否 |  |  |
| 12 | impawn_id | 否 |  |  |
| 13 | report_id | 否 |  |  |
| 14 | stock_property | 否 |  |  |
| 15 | srp_contract_status | 否 |  |  |
| 16 | date_clear | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | prev_back_type | 否 |  |  |
| 19 | fine_balance | 否 |  |  |
| 20 | unrepaid_fine_balance | 否 |  |  |
| 21 | contract_id | 否 |  |  |
| 22 | sett_dml_type | 否 |  |  |
| 23 | sett_batch_no | 否 |  |  |
| 24 | sum_spb_amount | 否 |  |  |
| 25 | sum_back_amount | 否 |  |  |
| 26 | sum_back_balance | 否 |  |  |
| 27 | bonus_amount | 否 |  |  |
| 28 | bonus_balance | 否 |  |  |
| 29 | back_principal | 否 |  |  |
| 30 | repaid_balance | 否 |  |  |
| 31 | settle_interest | 否 |  |  |
| 32 | unsettle_interest | 否 |  |  |
| 33 | real_date_back | 否 |  |  |
| 34 | real_back_balance | 否 |  |  |
| 35 | back_type | 否 |  |  |
| 36 | impawn_id | 否 |  |  |
| 37 | report_id | 否 |  |  |
| 38 | stock_property | 否 |  |  |
| 39 | srp_contract_status | 否 |  |  |
| 40 | date_clear | 否 |  |  |
| 41 | remark | 否 |  |  |
| 42 | prev_back_type | 否 |  |  |
| 43 | fine_balance | 否 |  |  |
| 44 | unrepaid_fine_balance | 否 |  |  |
| 45 | contract_id | 否 |  |  |
| 46 | sett_dml_type | 否 |  |  |
| 47 | sett_batch_no | 否 |  |  |
| 48 | sum_spb_amount | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_srp_contract | ART | 是 | sett_batch_no, contract_id, sett_batch_no, contract_id |
| idx_settredo_srp_contract | ART | 是 | sett_batch_no, contract_id, sett_batch_no, contract_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_srp_contract | sett_batch_no, contract_id, sett_batch_no, contract_id |
| idx_settredo_srp_contract | sett_batch_no, contract_id, sett_batch_no, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:30:35 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-11-24 10:52:48 | 8.26.2.92 | yangxz | 所有表settredo_srp_contract，添加了表字段(sum_spb_amount);
 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2026-03-04 16:30:35 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-11-24 10:52:48 | 8.26.2.92 | yangxz | 所有表settredo_srp_contract，添加了表字段(sum_spb_amount);
 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |

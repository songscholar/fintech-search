# settredo_sopt_entrust - 清算重做非交易报送委托表

**表对象ID**: 2549
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | entrust_status | 否 |  |  |
| 2 | return_info | 否 |  |  |
| 3 | error_no | 否 |  |  |
| 4 | sett_batch_no | 否 |  |  |
| 5 | sett_dml_type | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | entrust_no | 否 |  |  |
| 9 | entrust_status | 否 |  |  |
| 10 | return_info | 否 |  |  |
| 11 | error_no | 否 |  |  |
| 12 | sett_batch_no | 否 |  |  |
| 13 | sett_dml_type | 否 |  |  |
| 14 | init_date | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | entrust_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_sopt_entrust | ART | 是 | sett_batch_no, init_date, fund_account, entrust_no, sett_batch_no, init_date, fund_account, entrust_no |
| idx_settredo_sopt_entrust | ART | 是 | sett_batch_no, init_date, fund_account, entrust_no, sett_batch_no, init_date, fund_account, entrust_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_sopt_entrust | sett_batch_no, init_date, fund_account, entrust_no, sett_batch_no, init_date, fund_account, entrust_no |
| idx_settredo_sopt_entrust | sett_batch_no, init_date, fund_account, entrust_no, sett_batch_no, init_date, fund_account, entrust_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:29:20 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-08-20 13:37:42 | 3.0.2.40 | 张训华 | 新增 |
| 2026-03-04 16:29:20 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-08-20 13:37:42 | 3.0.2.40 | 张训华 | 新增 |

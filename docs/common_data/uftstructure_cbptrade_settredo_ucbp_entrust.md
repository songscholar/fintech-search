# settredo_ucbp_entrust - 清算重做综合业务委托表

**表对象ID**: 12507
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | return_code | 否 |  |  |
| 4 | date_back | 否 |  |  |
| 5 | date_clear | 否 |  |  |
| 6 | enable_polling | 否 |  |  |
| 7 | cbp_business_id | 否 |  |  |
| 8 | cbpcontract_id | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | back_balance | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | stock_type | 否 |  |  |
| 13 | entrust_prop | 否 |  |  |
| 14 | entrust_status | 否 |  |  |
| 15 | sett_batch_no | 否 |  |  |
| 16 | init_date | 否 |  |  |
| 17 | entrust_no | 否 |  |  |
| 18 | return_code | 否 |  |  |
| 19 | date_back | 否 |  |  |
| 20 | date_clear | 否 |  |  |
| 21 | enable_polling | 否 |  |  |
| 22 | cbp_business_id | 否 |  |  |
| 23 | cbpcontract_id | 否 |  |  |
| 24 | remark | 否 |  |  |
| 25 | back_balance | 否 |  |  |
| 26 | stock_code | 否 |  |  |
| 27 | stock_type | 否 |  |  |
| 28 | entrust_prop | 否 |  |  |
| 29 | entrust_status | 否 |  |  |
| 30 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_ucbp_entrust | ART | 是 | sett_batch_no, init_date, entrust_no, sett_batch_no, init_date, entrust_no |
| idx_settredo_ucbp_entrust | ART | 是 | sett_batch_no, init_date, entrust_no, sett_batch_no, init_date, entrust_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_ucbp_entrust | sett_batch_no, init_date, entrust_no, sett_batch_no, init_date, entrust_no |
| idx_settredo_ucbp_entrust | sett_batch_no, init_date, entrust_no, sett_batch_no, init_date, entrust_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:34:44 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-08-04 16:11:44 | V3.0.2.61 | taocong45644 | 新增表 |
| 2026-03-04 16:34:44 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-08-04 16:11:44 | V3.0.2.61 | taocong45644 | 新增表 |

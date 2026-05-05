# settredo_uref_borrow_entrust - 清算重做转融通借入委托表

**表对象ID**: 6113
**所属模块**: reftrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | refentrust_status | 否 |  |  |
| 4 | sett_dml_type | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | entrust_no | 否 |  |  |
| 8 | refentrust_status | 否 |  |  |
| 9 | sett_dml_type | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |
| 11 | init_date | 否 |  |  |
| 12 | entrust_no | 否 |  |  |
| 13 | refentrust_status | 否 |  |  |
| 14 | sett_dml_type | 否 |  |  |
| 15 | sett_batch_no | 否 |  |  |
| 16 | init_date | 否 |  |  |
| 17 | entrust_no | 否 |  |  |
| 18 | refentrust_status | 否 |  |  |
| 19 | sett_dml_type | 否 |  |  |
| 20 | sett_batch_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_refbentrust | 默认 | 是 | sett_batch_no, init_date, entrust_no, sett_batch_no, init_date, entrust_no |
| idx_settredo_refbentrust | ART | 是 | sett_batch_no, init_date, entrust_no, sett_batch_no, init_date, entrust_no |
| idx_settredo_refbentrust | 默认 | 是 | sett_batch_no, init_date, entrust_no, sett_batch_no, init_date, entrust_no |
| idx_settredo_refbentrust | ART | 是 | sett_batch_no, init_date, entrust_no, sett_batch_no, init_date, entrust_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_refbentrust | sett_batch_no, init_date, entrust_no, sett_batch_no, init_date, entrust_no |
| idx_settredo_refbentrust | sett_batch_no, init_date, entrust_no, sett_batch_no, init_date, entrust_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-20 09:36:15 | V3.0.2.1 | 廖宏玮 | 添加表 |
| 2025-08-20 09:36:15 | V3.0.2.1 |  |  |
| 2025-08-20 09:36:15 | V3.0.2.1 | 廖宏玮 | 添加表 |
| 2025-08-20 09:36:15 | V3.0.2.1 |  |  |

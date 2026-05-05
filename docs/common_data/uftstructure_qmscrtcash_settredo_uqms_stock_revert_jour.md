# settredo_uqms_stock_revert_jour - 日终清算股份反向操作流水

**表对象ID**: 1014
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | treat_status | 否 |  |  |
| 4 | valid_date | 否 |  |  |
| 5 | sett_dml_type | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | serial_no | 否 |  |  |
| 9 | treat_status | 否 |  |  |
| 10 | valid_date | 否 |  |  |
| 11 | sett_dml_type | 否 |  |  |
| 12 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_uqms_stockrevertjour | ART | 是 | init_date, serial_no, sett_batch_no, init_date, serial_no, sett_batch_no |
| idx_strd_uqms_stockrevertjour | ART | 是 | init_date, serial_no, sett_batch_no, init_date, serial_no, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_uqms_stockrevertjour | init_date, serial_no, sett_batch_no, init_date, serial_no, sett_batch_no |
| idx_strd_uqms_stockrevertjour | init_date, serial_no, sett_batch_no, init_date, serial_no, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:56:46 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2026-03-05 16:56:46 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

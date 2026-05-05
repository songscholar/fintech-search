# settredo_qrp_busin - 清算重做报价回购业务计划表

**表对象ID**: 12339
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | qrpbusin_status | 否 |  |  |
| 4 | date_clear | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | serial_no | 否 |  |  |
| 8 | qrpbusin_status | 否 |  |  |
| 9 | date_clear | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_qrp_busin | ART | 是 | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |
| idx_settredo_qrp_busin | ART | 是 | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_qrp_busin | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |
| idx_settredo_qrp_busin | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:33:19 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-08-04 16:14:28 | V3.0.2.61 | taocong45644 | 新增表 |
| 2026-03-04 16:33:19 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-08-04 16:14:28 | V3.0.2.61 | taocong45644 | 新增表 |

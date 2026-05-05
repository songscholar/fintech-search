# settredo_uqms_ass_equity - 日终清算头寸担保证券权益信息表

**表对象ID**: 1015
**所属模块**: qmscrtcash
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | deal_status | 否 |  |  |
| 2 | date_clear | 否 |  |  |
| 3 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 4 | sett_dml_type | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | deal_status | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 9 | sett_dml_type | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_uqms_ass_equity | ART | 是 | position_str, sett_batch_no, position_str, sett_batch_no |
| idx_strd_uqms_ass_equity | ART | 是 | position_str, sett_batch_no, position_str, sett_batch_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_uqms_ass_equity | position_str, sett_batch_no, position_str, sett_batch_no |
| idx_strd_uqms_ass_equity | position_str, sett_batch_no, position_str, sett_batch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:57:07 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |
| 2026-03-05 16:57:07 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-08-18 19:10:59 | 3.0.2.1 | 沈勋 | 新增表，支持清算入账重做 |
| 2025-10-07 12:37:18 | 3.0.2.1 | 沈勋 | 去除不回库勾选 |

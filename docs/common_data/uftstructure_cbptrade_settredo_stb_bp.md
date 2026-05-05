# settredo_stb_bp - 清算重做特别股份表

**表对象ID**: 2550
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 2 | sett_batch_no | 否 |  |  |
| 3 | send_status | 否 |  |  |
| 4 | remark | 否 |  |  |
| 5 | return_code | 否 |  |  |
| 6 | sett_dml_type | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 9 | sett_batch_no | 否 |  |  |
| 10 | send_status | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | return_code | 否 |  |  |
| 13 | sett_dml_type | 否 |  |  |
| 14 | fund_account | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_stb_bp | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_stb_bp | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_stb_bp | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_stb_bp | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:29:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-08-20 13:37:42 | 3.0.2.40 | 张训华 | 新增 |
| 2026-03-04 16:29:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-08-20 13:37:42 | 3.0.2.40 | 张训华 | 新增 |

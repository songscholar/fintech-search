# settredo_fundpend_jour - 清算重做资金待扣收流水表

**表对象ID**: 2856
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | deal_date | 否 |  |  |
| 2 | deal_flag | 否 |  |  |
| 3 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 4 | pend_fare | 否 |  |  |
| 5 | sett_dml_type | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | total_pend_fare | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | deal_date | 否 |  |  |
| 10 | deal_flag | 否 |  |  |
| 11 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 12 | pend_fare | 否 |  |  |
| 13 | sett_dml_type | 否 |  |  |
| 14 | init_date | 否 |  |  |
| 15 | total_pend_fare | 否 |  |  |
| 16 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_fundpend_jour | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_fundpend_jour | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_fundpend_jour | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_fundpend_jour | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-20 13:37:42 | 3.0.2.2 | 张训华 | 新增 |
| 2025-08-20 13:37:42 | 3.0.2.2 | 张训华 | 新增 |

# settredo_srp_apply - 清算重做股票质押申请表

**表对象ID**: 2657
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | srp_apply_status | 否 |  |  |
| 2 | date_clear | 否 |  |  |
| 3 | remark | 否 |  |  |
| 4 | init_date | 否 |  |  |
| 5 | serial_no | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | srp_apply_status | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | init_date | 否 |  |  |
| 11 | serial_no | 否 |  |  |
| 12 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_srpapply | ART | 是 | sett_batch_no, serial_no, init_date, sett_batch_no, serial_no, init_date |
| idx_settredo_srpapply | ART | 是 | sett_batch_no, serial_no, init_date, sett_batch_no, serial_no, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_srpapply | sett_batch_no, serial_no, init_date, sett_batch_no, serial_no, init_date |
| idx_settredo_srpapply | sett_batch_no, serial_no, init_date, sett_batch_no, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:03:17 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2026-03-06 17:03:17 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |

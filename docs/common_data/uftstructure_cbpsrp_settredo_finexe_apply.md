# settredo_finexe_apply - 清算重做融资行权申请表

**表对象ID**: 2655
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | finexe_apply_status | 否 |  |  |
| 2 | date_clear | 否 |  |  |
| 3 | init_date | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | finexe_apply_status | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | serial_no | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_finexeapply | ART | 是 | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |
| idx_settredo_finexeapply | ART | 是 | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_finexeapply | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |
| idx_settredo_finexeapply | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:02:27 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2026-03-06 17:02:27 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |

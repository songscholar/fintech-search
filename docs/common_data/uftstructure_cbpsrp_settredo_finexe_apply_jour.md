# settredo_finexe_apply_jour - 清算重做融资行权申请流水表

**表对象ID**: 2654
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | sett_dml_type | 否 |  |  |
| 4 | sett_batch_no | 否 |  |  |
| 5 | init_date | 否 |  |  |
| 6 | serial_no | 否 |  |  |
| 7 | sett_dml_type | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_finexeapplyjour | ART | 是 | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |
| idx_settredo_finexeapplyjour | ART | 是 | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_finexeapplyjour | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |
| idx_settredo_finexeapplyjour | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:02:02 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2026-03-06 17:02:02 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |

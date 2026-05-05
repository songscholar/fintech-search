# ics_farekind - 机构柜台费用类别信息表

**表对象ID**: 115
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | charge_no | 否 |  |  |
| 2 | fare_kind | 否 |  |  |
| 3 | charge_name | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | sync_flag | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | position_str | 否 |  | charge_no(10)+fare_kind(10) |
| 10 | charge_no | 否 |  |  |
| 11 | fare_kind | 否 |  |  |
| 12 | charge_name | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | sync_flag | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | position_str | 否 |  | charge_no(10)+fare_kind(10) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ics_farekind | 默认 | 否 |  |
| idx_ics_farekind | ART | 是 | charge_no, fare_kind, charge_no, fare_kind |
| idx_ics_farekind | 默认 | 否 |  |
| idx_ics_farekind | ART | 是 | charge_no, fare_kind, charge_no, fare_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ics_farekind | charge_no, fare_kind, charge_no, fare_kind |
| idx_ics_farekind | charge_no, fare_kind, charge_no, fare_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:41:09 | 3.0.2.103 | taocong45644 | 当前表ics_farekind，修改了索引idx_ics_farekind,索引字段修改为：(charge_no,far... |
| 2025-02-14 14:39:14 | 3.0.6.26 | 李想 | 新增表 |
| 2025-12-01 14:41:09 | 3.0.2.103 | taocong45644 | 当前表ics_farekind，修改了索引idx_ics_farekind,索引字段修改为：(charge_no,far... |
| 2025-02-14 14:39:14 | 3.0.6.26 | 李想 | 新增表 |

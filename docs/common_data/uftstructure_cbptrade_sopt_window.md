# sopt_window - 自主行权窗口表

**表对象ID**: 2327
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | sopt_code | 否 |  |  |
| 3 | begin_date | 否 |  |  |
| 4 | end_date | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | sopt_code(8)+exchange_type(4)+begin_date(8) |
| 10 | exchange_type | 否 |  |  |
| 11 | sopt_code | 否 |  |  |
| 12 | begin_date | 否 |  |  |
| 13 | end_date | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | sopt_code(8)+exchange_type(4)+begin_date(8) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_soptwindow | 默认 | 否 |  |
| idx_soptwindow | ART | 是 | sopt_code, exchange_type, begin_date, sopt_code, exchange_type, begin_date |
| idx_soptwindow | 默认 | 否 |  |
| idx_soptwindow | ART | 是 | sopt_code, exchange_type, begin_date, sopt_code, exchange_type, begin_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_soptwindow | sopt_code, exchange_type, begin_date, sopt_code, exchange_type, begin_date |
| idx_soptwindow | sopt_code, exchange_type, begin_date, sopt_code, exchange_type, begin_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:25:41 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 20:11:56 | V3.0.5.1017 | 李想 | 物理表sopt_window，添加了表字段(update_date);
物理表sopt_window，添加了表字段(u... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |
| 2026-03-04 15:25:41 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 20:11:56 | V3.0.5.1017 | 李想 | 物理表sopt_window，添加了表字段(update_date);
物理表sopt_window，添加了表字段(u... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |

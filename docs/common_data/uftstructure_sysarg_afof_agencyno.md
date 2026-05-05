# afof_agencyno - 基金盘后代销商表

**表对象ID**: 339
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | agency_no | 否 |  |  |
| 2 | agency_name | 否 |  |  |
| 3 | register_address | 否 |  |  |
| 4 | company_prin | 否 |  |  |
| 5 | contact_person | 否 |  |  |
| 6 | agency_flag | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | agency_no |
| 11 | agency_no | 否 |  |  |
| 12 | agency_name | 否 |  |  |
| 13 | register_address | 否 |  |  |
| 14 | company_prin | 否 |  |  |
| 15 | contact_person | 否 |  |  |
| 16 | agency_flag | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | agency_no |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_afof_agencyno | 默认 | 否 | agency_no, agency_no |
| idx_afof_agencyno | ART | 是 | agency_no, agency_no |
| idx_afof_agencyno | 默认 | 否 | agency_no, agency_no |
| idx_afof_agencyno | ART | 是 | agency_no, agency_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_afof_agencyno | agency_no, agency_no |
| idx_afof_agencyno | agency_no, agency_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-03 10:34:30 | 3.0.2.94 | 高志强 | 所有表afof_agencyno，添加了表字段(position_str);
 |
| 2025-02-19 16:53:46 | 3.0.6.105 | 李想 | 物理表afof_agencyno，添加了表字段(update_date);
物理表afof_agencyno，添加了表... |
| 2024-12-27 16:20:37 | 3.0.2.37 | 谢宗艺 | 表afof_agencyno，添加了表字段(transaction_no);
 |
| 2024-12-16 14:05:58 | 3.0.2.36 | 谢宗艺 | 物理表afof_agencyno，增加索引(idx_afof_agencyno:[agency_no]);
 |
| 2025-09-03 10:34:30 | 3.0.2.94 | 高志强 | 所有表afof_agencyno，添加了表字段(position_str);
 |
| 2025-02-19 16:53:46 | 3.0.6.105 | 李想 | 物理表afof_agencyno，添加了表字段(update_date);
物理表afof_agencyno，添加了表... |
| 2024-12-27 16:20:37 | 3.0.2.37 | 谢宗艺 | 表afof_agencyno，添加了表字段(transaction_no);
 |
| 2024-12-16 14:05:58 | 3.0.2.36 | 谢宗艺 | 物理表afof_agencyno，增加索引(idx_afof_agencyno:[agency_no]);
 |

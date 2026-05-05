# ucbp_blob_file - 存管外部数据信息

**表对象ID**: 2308
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | file_guid | 否 |  |  |
| 3 | ordinal | 否 |  |  |
| 4 | blob_no | 否 |  |  |
| 5 | deal_flag | 否 |  |  |
| 6 | file_obj | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | file_obj_v2 | 否 |  |  |
| 10 | client_id | 否 | H |  |
| 11 | branch_no | 否 | H |  |
| 12 | asset_prop | 否 | H |  |
| 13 | limit_flag | 否 | H |  |
| 14 | risk_level | 否 | H |  |
| 15 | corp_client_group | 否 | H |  |
| 16 | corp_risk_level | 否 | H |  |
| 17 | asset_level | 否 | H |  |
| 18 | client_name | 否 | H |  |
| 19 | client_prop | 否 | H |  |
| 20 | room_code | 否 | H |  |
| 21 | init_date | 否 |  |  |
| 22 | file_guid | 否 |  |  |
| 23 | ordinal | 否 |  |  |
| 24 | blob_no | 否 |  |  |
| 25 | deal_flag | 否 |  |  |
| 26 | file_obj | 否 |  |  |
| 27 | date_clear | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | file_obj_v2 | 否 |  |  |
| 30 | client_id | 否 | H |  |
| 31 | branch_no | 否 | H |  |
| 32 | asset_prop | 否 | H |  |
| 33 | limit_flag | 否 | H |  |
| 34 | risk_level | 否 | H |  |
| 35 | corp_client_group | 否 | H |  |
| 36 | corp_risk_level | 否 | H |  |
| 37 | asset_level | 否 | H |  |
| 38 | client_name | 否 | H |  |
| 39 | client_prop | 否 | H |  |
| 40 | room_code | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucbp_blobfile | 默认 | 否 |  |
| idx_ucbp_blobfile | 默认 | 否 | file_guid, ordinal, file_guid, ordinal |
| idx_ucbp_blobfile | ART | 是 | file_guid, ordinal, file_guid, ordinal |
| uk_rpt_ucbpblobfile | ART | 是 | init_date, file_guid, ordinal, init_date, file_guid, ordinal |
| idx_rpt_ucbpblobfile_tolast | ART | 是 | date_clear, date_clear |
| idx_ucbp_blobfile | 默认 | 否 |  |
| idx_ucbp_blobfile | 默认 | 否 | file_guid, ordinal, file_guid, ordinal |
| idx_ucbp_blobfile | ART | 是 | file_guid, ordinal, file_guid, ordinal |
| uk_rpt_ucbpblobfile | ART | 是 | init_date, file_guid, ordinal, init_date, file_guid, ordinal |
| idx_rpt_ucbpblobfile_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucbp_blobfile | file_guid, ordinal, file_guid, ordinal |
| idx_ucbp_blobfile | file_guid, ordinal, file_guid, ordinal |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:11:58 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-19 15:20:01 | 8.26.2.93 | yusz | 所有表ucbp_blob_file，添加了表字段(file_obj_v2);
 |
| 2025-12-04 14:24:41 | V3.0.1.5 | 洪略 | 历史表删除stock_name字段 |
| 2025-11-21 19:56:55 | V3.0.8.9 | 周兆军 | 维护历史表 |
| 2024-08-20 14:20:55 | V3.0.2.1006 | 张云焘 | 内存表ucbp_blob_file，修改索引idx_ucbp_blobfile为分级索引 |
| 2023-09-30 16:48:36 | V3.0.1.5 | huangzh | 物理表ucbp_blob_file，添加了表字段(fund_account);
 |
| 2023-09-30 10:50:02 | V3.0.1.5 | huangzh | 物理表ucbp_blob_file，增加索引(idx_ucbp_blobfile:[file_guid,ordinal]... |
| 2026-03-04 15:11:58 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-19 15:20:01 | 8.26.2.93 | yusz | 所有表ucbp_blob_file，添加了表字段(file_obj_v2);
 |
| 2025-12-04 14:24:41 | V3.0.1.5 | 洪略 | 历史表删除stock_name字段 |
| 2025-11-21 19:56:55 | V3.0.8.9 | 周兆军 | 维护历史表 |
| 2024-08-20 14:20:55 | V3.0.2.1006 | 张云焘 | 内存表ucbp_blob_file，修改索引idx_ucbp_blobfile为分级索引 |
| 2023-09-30 16:48:36 | V3.0.1.5 | huangzh | 物理表ucbp_blob_file，添加了表字段(fund_account);
 |
| 2023-09-30 10:50:02 | V3.0.1.5 | huangzh | 物理表ucbp_blob_file，增加索引(idx_ucbp_blobfile:[file_guid,ordinal]... |

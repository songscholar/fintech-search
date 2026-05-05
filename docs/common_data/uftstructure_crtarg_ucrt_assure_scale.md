# ucrt_assure_scale - 维持担保比例参数表

**表对象ID**: 7001
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | assurescale_type | 否 |  |  |
| 2 | assurescale_value | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | assurescale_package_kind | 否 |  |  |
| 5 | update_date | 否 |  |  |
| 6 | update_time | 否 |  |  |
| 7 | position_str | 否 |  | assurescale_type(1)+assurescale_package_kind(10) |
| 8 | remark | 否 |  |  |
| 9 | tohis_date | 否 | H |  |
| 10 | assurescale_type | 否 |  |  |
| 11 | assurescale_value | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | assurescale_package_kind | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | assurescale_type(1)+assurescale_package_kind(10) |
| 17 | remark | 否 |  |  |
| 18 | tohis_date | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_assure_scale | 默认 | 否 | assurescale_package_kind, assurescale_package_kind |
| idx_ucrt_assure_scale | ART | 是 | assurescale_type, assurescale_package_kind, assurescale_type, assurescale_package_kind |
| uk_rpt_ucrtassurescale | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_ucrt_assure_scale | 默认 | 否 | assurescale_package_kind, assurescale_package_kind |
| idx_ucrt_assure_scale | ART | 是 | assurescale_type, assurescale_package_kind, assurescale_type, assurescale_package_kind |
| uk_rpt_ucrtassurescale | ART | 是 | tohis_date, position_str, tohis_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_assure_scale | assurescale_type, assurescale_package_kind, assurescale_type, assurescale_package_kind |
| idx_ucrt_assure_scale | assurescale_type, assurescale_package_kind, assurescale_type, assurescale_package_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-03-10 10:50:13 | 3.0.6.94 |  | 物理表ucrt_assure_scale，添加了表字段(remark);
 |
| 2025-02-17 15:29:25 | 3.0.6.44 | 李想 | 物理表ucrt_assure_scale，添加了表字段(update_date);
物理表ucrt_assure_sc... |
| 2024-12-24 10:36:42 | 3.0.6.23 | 沈勋 | 物理表ucrt_assure_scale，增加索引字段(索引idx_ucrt_assure_scale:增加了索引字段：... |
| 2024-12-24 10:34:35 | 3.0.6.23 | 沈勋 | 物理表ucrt_assure_scale，添加了表字段(assurescale_package_kind);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-03-10 10:50:13 | 3.0.6.94 |  | 物理表ucrt_assure_scale，添加了表字段(remark);
 |
| 2025-02-17 15:29:25 | 3.0.6.44 | 李想 | 物理表ucrt_assure_scale，添加了表字段(update_date);
物理表ucrt_assure_sc... |
| 2024-12-24 10:36:42 | 3.0.6.23 | 沈勋 | 物理表ucrt_assure_scale，增加索引字段(索引idx_ucrt_assure_scale:增加了索引字段：... |
| 2024-12-24 10:34:35 | 3.0.6.23 | 沈勋 | 物理表ucrt_assure_scale，添加了表字段(assurescale_package_kind);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

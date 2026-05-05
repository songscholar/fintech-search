# upbs_license_info - 许可证信息表

**表对象ID**: 96
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | license_id | 否 |  |  |
| 2 | license_type | 否 |  |  |
| 3 | module_id | 否 |  |  |
| 4 | valid_date | 否 |  |  |
| 5 | busin_caption | 否 |  |  |
| 6 | license_id_1 | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | license_id | 否 |  |  |
| 9 | license_type | 否 |  |  |
| 10 | module_id | 否 |  |  |
| 11 | valid_date | 否 |  |  |
| 12 | busin_caption | 否 |  |  |
| 13 | license_id_1 | 否 |  |  |
| 14 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_licenseinfo | ART | 是 | license_id, license_id |
| idx_upbs_licenseinfo | ART | 是 | license_id, license_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_licenseinfo | license_id, license_id |
| idx_upbs_licenseinfo | license_id, license_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-23 10:48:18 | 3.0.2.92 | 高志强 | 改为DB+MDB模式,表空间改为HS_USMS_DATA |
| 2025-01-06 10:48:05 | 3.0.5.1006 | 黄积冲 | 新增表upbs_license_info |
| 2025-08-23 10:48:18 | 3.0.2.92 | 高志强 | 改为DB+MDB模式,表空间改为HS_USMS_DATA |
| 2025-01-06 10:48:05 | 3.0.5.1006 | 黄积冲 | 新增表upbs_license_info |

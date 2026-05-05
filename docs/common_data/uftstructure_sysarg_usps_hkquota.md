# usps_hkquota - 港股额度表

**表对象ID**: 316
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | total_quota | 否 |  |  |
| 3 | surplus_quota | 否 |  |  |
| 4 | hkquota_status | 否 |  |  |
| 5 | hkmarket_status | 否 |  |  |
| 6 | secumarket_ctrlstr | 否 |  |  |
| 7 | valid_date | 否 |  |  |
| 8 | modify_date | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | total_quota | 否 |  |  |
| 14 | surplus_quota | 否 |  |  |
| 15 | hkquota_status | 否 |  |  |
| 16 | hkmarket_status | 否 |  |  |
| 17 | secumarket_ctrlstr | 否 |  |  |
| 18 | valid_date | 否 |  |  |
| 19 | modify_date | 否 |  |  |
| 20 | transaction_no | 否 |  |  |
| 21 | update_date | 否 |  |  |
| 22 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_hkquota | ART | 是 | exchange_type, exchange_type |
| idx_usps_hkquota | ART | 是 | exchange_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_hkquota | exchange_type, exchange_type |
| idx_usps_hkquota | exchange_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 13:27:33 | 3.0.6.82 | 李想 | 物理表usps_hkquota，添加了表字段(update_date);
物理表usps_hkquota，添加了表字段... |
| 2024-07-24 15:22:24 | 3.0.2.24 | 乐闽庭 | 新增表 |
| 2025-02-19 13:27:33 | 3.0.6.82 | 李想 | 物理表usps_hkquota，添加了表字段(update_date);
物理表usps_hkquota，添加了表字段... |
| 2024-07-24 15:22:24 | 3.0.2.24 | 乐闽庭 | 新增表 |

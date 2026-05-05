# ref_quota - 转融通限额参数表

**表对象ID**: 6009
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | refquota_type | 否 |  |  |
| 2 | report_unit | 否 |  |  |
| 3 | one_lower_rpt_quota | 否 |  |  |
| 4 | one_upper_rpt_quota | 否 |  |  |
| 5 | day_upper_rpt_quota | 否 |  |  |
| 6 | client_one_stkcode_total | 否 |  |  |
| 7 | client_all_stkcode_total | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | refquota_type | 否 |  |  |
| 12 | report_unit | 否 |  |  |
| 13 | one_lower_rpt_quota | 否 |  |  |
| 14 | one_upper_rpt_quota | 否 |  |  |
| 15 | day_upper_rpt_quota | 否 |  |  |
| 16 | client_one_stkcode_total | 否 |  |  |
| 17 | client_all_stkcode_total | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_quota | ART | 是 | refquota_type, refquota_type |
| idx_ref_quota | ART | 是 | refquota_type, refquota_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_quota | refquota_type, refquota_type |
| idx_ref_quota | refquota_type, refquota_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 11:04:53 | 1.0.0.8 | 李想 | 新增表 |
| 2025-02-21 11:04:53 | 1.0.0.8 | 李想 | 新增表 |

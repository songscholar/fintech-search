# uopt_client_prefer - 股票期权客户适当性偏好表

**表对象ID**: 9025
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | asset_balance | 否 |  |  |
| 3 | prof_flag | 否 |  |  |
| 4 | prof_begin_date | 否 |  |  |
| 5 | prof_end_date | 否 |  |  |
| 6 | prof_type | 否 |  |  |
| 7 | corp_risk_level | 否 |  |  |
| 8 | corp_begin_date | 否 |  |  |
| 9 | corp_end_date | 否 |  |  |
| 10 | optacct_type | 否 |  |  |
| 11 | birthday | 否 |  |  |
| 12 | min_rank_flag | 否 |  |  |
| 13 | partition_no | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | asset_balance | 否 |  |  |
| 16 | prof_flag | 否 |  |  |
| 17 | prof_begin_date | 否 |  |  |
| 18 | prof_end_date | 否 |  |  |
| 19 | prof_type | 否 |  |  |
| 20 | corp_risk_level | 否 |  |  |
| 21 | corp_begin_date | 否 |  |  |
| 22 | corp_end_date | 否 |  |  |
| 23 | optacct_type | 否 |  |  |
| 24 | birthday | 否 |  |  |
| 25 | min_rank_flag | 否 |  |  |
| 26 | partition_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_client_prefer | 默认 | 否 | client_id, partition_no, client_id, partition_no |
| idx_client_prefer | 默认 | 是 | client_id, partition_no, client_id, partition_no |
| idx_client_prefer | 默认 | 否 | client_id, partition_no, client_id, partition_no |
| idx_client_prefer | 默认 | 是 | client_id, partition_no, client_id, partition_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_client_prefer | partition_no, client_id, partition_no, client_id |
| idx_client_prefer | partition_no, client_id, partition_no, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-05-14 19:59:30 | V3.0.3.4 | wuxd | 物理表uopt_client_prefer，增加索引(idx_client_prefer:[client_id,part... |
| 2024-05-09 09:26:20 | V3.0.3.3 | 韦子晗 | 新增partition_no字段 |
| 2024-05-14 19:59:30 | V3.0.3.4 | wuxd | 物理表uopt_client_prefer，增加索引(idx_client_prefer:[client_id,part... |
| 2024-05-09 09:26:20 | V3.0.3.3 | 韦子晗 | 新增partition_no字段 |

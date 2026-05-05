# pbs_sysdeploy - 子系统部署表

**表对象ID**: 2806
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | subsys_id | 是 |  |  |
| 2 | subsys_name | 是 |  |  |
| 3 | subsys_status | 是 |  |  |
| 4 | micro_service | 是 |  |  |
| 5 | uf2_enable_flag | 是 |  |  |
| 6 | uf3_enable_flag | 是 |  |  |
| 7 | update_date | 是 |  |  |
| 8 | update_time | 是 |  |  |
| 9 | transaction_no | 是 |  |  |
| 10 | subsys_id | 是 |  |  |
| 11 | subsys_name | 是 |  |  |
| 12 | subsys_status | 是 |  |  |
| 13 | micro_service | 是 |  |  |
| 14 | uf2_enable_flag | 是 |  |  |
| 15 | uf3_enable_flag | 是 |  |  |
| 16 | update_date | 是 |  |  |
| 17 | update_time | 是 |  |  |
| 18 | transaction_no | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_pbs_sysdeploy | 默认 | 是 | subsys_id, subsys_id |
| uk_pbs_sysdeploy | 默认 | 是 | subsys_id, subsys_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_pbs_sysdeploy | subsys_id, subsys_id |
| uk_pbs_sysdeploy | subsys_id, subsys_id |

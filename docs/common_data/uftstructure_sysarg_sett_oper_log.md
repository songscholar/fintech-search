# sett_oper_log - 清算操作日志表

**表对象ID**: 104
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | operator_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_milltime | 否 |  |  |
| 5 | op_station | 否 |  |  |
| 6 | subsys_id | 否 |  |  |
| 7 | node_id | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |
| 9 | busiflow_id | 否 |  |  |
| 10 | oper_flag | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | operator_no | 否 |  |  |
| 14 | curr_date | 否 |  |  |
| 15 | curr_milltime | 否 |  |  |
| 16 | op_station | 否 |  |  |
| 17 | subsys_id | 否 |  |  |
| 18 | node_id | 否 |  |  |
| 19 | sett_batch_no | 否 |  |  |
| 20 | busiflow_id | 否 |  |  |
| 21 | oper_flag | 否 |  |  |
| 22 | remark | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sett_oper_log | 默认 | 否 |  |
| idx_sett_oper_log | ART | 是 | init_date, curr_milltime, subsys_id, node_id, init_date, curr_milltime, subsys_id, node_id |
| idx_sett_oper_log | 默认 | 否 |  |
| idx_sett_oper_log | ART | 是 | init_date, curr_milltime, subsys_id, node_id, init_date, curr_milltime, subsys_id, node_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sett_oper_log | init_date, curr_milltime, subsys_id, node_id, init_date, curr_milltime, subsys_id, node_id |
| idx_sett_oper_log | init_date, curr_milltime, subsys_id, node_id, init_date, curr_milltime, subsys_id, node_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:52:25 | 3.0.2.103 | taocong45644 | 当前表sett_oper_log，修改了索引idx_sett_oper_log,索引字段修改为：(init_date,c... |
| 2025-03-21 10:45:04 | 3.0.6.128 | 常行 | 新增表 |
| 2025-12-01 14:52:25 | 3.0.2.103 | taocong45644 | 当前表sett_oper_log，修改了索引idx_sett_oper_log,索引字段修改为：(init_date,c... |
| 2025-03-21 10:45:04 | 3.0.6.128 | 常行 | 新增表 |

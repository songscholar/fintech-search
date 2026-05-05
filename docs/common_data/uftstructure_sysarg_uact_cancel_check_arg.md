# uact_cancel_check_arg - 销户检查参数表

**表对象ID**: 502
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | check_id | 否 |  |  |
| 2 | check_name | 否 |  |  |
| 3 | active_flag | 否 |  |  |
| 4 | update_date | 否 |  |  |
| 5 | update_time | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | transaction_str | 否 |  |  |
| 8 | check_id | 否 |  |  |
| 9 | check_name | 否 |  |  |
| 10 | active_flag | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | transaction_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uact_cancel_check_arg | 默认 | 否 |  |
| idx_uact_cancel_check_arg | ART | 是 | check_id, check_id |
| idx_uact_cancel_check_arg | 默认 | 否 |  |
| idx_uact_cancel_check_arg | ART | 是 | check_id, check_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uact_cancel_check_arg | check_id, check_id |
| idx_uact_cancel_check_arg | check_id, check_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:17:54 | 3.0.2.103 | taocong45644 | 当前表uact_cancel_check_arg，修改了索引idx_uact_cancel_check_arg,索引字段... |
| 2025-09-20 16:40:04 | 3.0.2.96 | 韦子晗 | 表空间调整为usms |
| 2025-07-08 17:12:52 | 3.0.6.1010 | 韦子晗 | 新增表uact_cancel_check_arg |
| 2025-12-01 15:17:54 | 3.0.2.103 | taocong45644 | 当前表uact_cancel_check_arg，修改了索引idx_uact_cancel_check_arg,索引字段... |
| 2025-09-20 16:40:04 | 3.0.2.96 | 韦子晗 | 表空间调整为usms |
| 2025-07-08 17:12:52 | 3.0.6.1010 | 韦子晗 | 新增表uact_cancel_check_arg |

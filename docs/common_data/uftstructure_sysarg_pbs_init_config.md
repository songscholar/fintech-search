# pbs_init_config - 初始化配置表

**表对象ID**: 381
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | service_name | 否 |  |  |
| 2 | table_name | 否 |  |  |
| 3 | initconfig_flag | 否 |  |  |
| 4 | initconfig_cond | 否 |  |  |
| 5 | tolast_flag | 否 |  |  |
| 6 | tolast_cond | 否 |  |  |
| 7 | clear_by_acct | 否 |  |  |
| 8 | service_name | 否 |  |  |
| 9 | table_name | 否 |  |  |
| 10 | initconfig_flag | 否 |  |  |
| 11 | initconfig_cond | 否 |  |  |
| 12 | tolast_flag | 否 |  |  |
| 13 | tolast_cond | 否 |  |  |
| 14 | clear_by_acct | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_init_config | 默认 | 否 |  |
| uk_init_config | ART | 是 | service_name, table_name, service_name, table_name |
| uk_init_config | 默认 | 否 |  |
| uk_init_config | ART | 是 | service_name, table_name, service_name, table_name |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_init_config | service_name, table_name, service_name, table_name |
| uk_init_config | service_name, table_name, service_name, table_name |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-28 09:25:32 | 3.0.2.106 | 陆良铠 | 支持redo文件 |
| 2025-12-01 14:51:49 | 3.0.2.103 | taocong45644 | 当前表pbs_init_config，修改了索引uk_init_config,索引字段修改为：(service_name... |
| 2025-02-19 19:03:48 | 3.0.6.81 | 马明智 | 新增 |
| 2025-02-19 19:03:48 | 3.0.6.80 | 马明智 | 新增 |
| 2026-02-28 09:25:32 | 3.0.2.106 | 陆良铠 | 支持redo文件 |
| 2025-12-01 14:51:49 | 3.0.2.103 | taocong45644 | 当前表pbs_init_config，修改了索引uk_init_config,索引字段修改为：(service_name... |
| 2025-02-19 19:03:48 | 3.0.6.81 | 马明智 | 新增 |
| 2025-02-19 19:03:48 | 3.0.6.80 | 马明智 | 新增 |

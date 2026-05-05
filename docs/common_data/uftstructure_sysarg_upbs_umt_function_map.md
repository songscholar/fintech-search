# upbs_umt_function_map - 内存交易功能映射表

**表对象ID**: 151
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 4 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | function_str | 否 |  |  |
| 2 | function_id | 否 |  |  |
| 3 | function_str | 否 |  |  |
| 4 | function_id | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_umt_function_map | 默认 | 否 |  |
| idx_upbs_umt_function_map | ART | 是 | function_str, function_str |
| idx_upbs_umt_function_map | 默认 | 否 |  |
| idx_upbs_umt_function_map | ART | 是 | function_str, function_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_umt_function_map | function_str, function_str |
| idx_upbs_umt_function_map | function_str, function_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:38:19 | 3.0.2.103 | taocong45644 | 当前表upbs_umt_function_map，修改了索引idx_upbs_umt_function_map,索引字段... |
| 2024-11-20 15:40:15 | V3.0.3.12 | 韦子晗 | 新增表upbs_umt_function_map |
| 2025-12-01 15:38:19 | 3.0.2.103 | taocong45644 | 当前表upbs_umt_function_map，修改了索引idx_upbs_umt_function_map,索引字段... |
| 2024-11-20 15:40:15 | V3.0.3.12 | 韦子晗 | 新增表upbs_umt_function_map |

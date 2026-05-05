# uarg_syncinfo - 参数同步流水表

**表对象ID**: 601
**所属模块**: arg
**数据空间**: HS_UARG_DATA
**运行模式**: DB

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | table_name | 否 |  |  |
| 2 | position_str | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | param_oper_type | 否 |  |  |
| 5 | tohis_date | 否 | H |  |
| 6 | table_name | 否 |  |  |
| 7 | position_str | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | param_oper_type | 否 |  |  |
| 10 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_syncinfo | 默认 | 是 | table_name, position_str, table_name, position_str |
| idx_rpt_uarg_syncinfo | ART | 是 | tohis_date, table_name, position_str, tohis_date, table_name, position_str |
| idx_uarg_syncinfo | 默认 | 是 | table_name, position_str, table_name, position_str |
| idx_rpt_uarg_syncinfo | ART | 是 | tohis_date, table_name, position_str, tohis_date, table_name, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-24 19:24:16 | 3.0.2.2 | 洪略 | 增加历史表 |
| 2025-07-29 20:25:48 | 3.0.2.1 | 高志强 | 添加表 |
| 2025-12-24 19:24:16 | 3.0.2.2 | 洪略 | 增加历史表 |
| 2025-07-29 20:25:48 | 3.0.2.1 | 高志强 | 添加表 |

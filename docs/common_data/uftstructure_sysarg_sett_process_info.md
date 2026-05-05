# sett_process_info - 清算流程信息表

**表对象ID**: 109
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | sett_prop | 否 |  |  |
| 4 | treat_flag | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | position_str | 否 |  | init_date(8)+exchange_type(4)+sett_prop |
| 7 | init_date | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | sett_prop | 否 |  |  |
| 10 | treat_flag | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | position_str | 否 |  | init_date(8)+exchange_type(4)+sett_prop |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sett_process_info | ART | 是 | init_date, exchange_type, sett_prop, init_date, exchange_type, sett_prop |
| idx_sett_process_info | ART | 是 | init_date, exchange_type, sett_prop, init_date, exchange_type, sett_prop |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sett_process_info | init_date, exchange_type, sett_prop, init_date, exchange_type, sett_prop |
| idx_sett_process_info | init_date, exchange_type, sett_prop, init_date, exchange_type, sett_prop |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-03 11:33:42 | 3.0.2.94 | 高志强 | 所有表sett_process_info，添加了表字段(position_str);
 |
| 2025-03-21 10:45:57 | 3.0.6.127 | 常行 | 新增表 |
| 2025-09-03 11:33:42 | 3.0.2.94 | 高志强 | 所有表sett_process_info，添加了表字段(position_str);
 |
| 2025-03-21 10:45:57 | 3.0.6.127 | 常行 | 新增表 |

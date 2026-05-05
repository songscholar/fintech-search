# assure_code_extinfo - 担保证券外部信息表

**表对象ID**: 7094
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | circulate_amount | 否 |  |  |
| 5 | capital_amount | 否 |  |  |
| 6 | static_pe_ratio | 否 |  |  |
| 7 | remark | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | position_str | 否 |  | exchange_type(4)+stock_code(8) |
| 12 | init_date | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | circulate_amount | 否 |  |  |
| 16 | capital_amount | 否 |  |  |
| 17 | static_pe_ratio | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | position_str | 否 |  | exchange_type(4)+stock_code(8) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assure_code_extinfo | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| uk_rpt_assurecodeextinfo | ART | 是 | init_date, exchange_type, stock_code, init_date, exchange_type, stock_code |
| idx_assure_code_extinfo | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| uk_rpt_assurecodeextinfo | ART | 是 | init_date, exchange_type, stock_code, init_date, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_assure_code_extinfo | exchange_type, stock_code, exchange_type, stock_code |
| idx_assure_code_extinfo | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 21:36:29 | 3.0.6.64 | 李想 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 21:36:29 | 3.0.6.64 | 李想 | 新增表 |

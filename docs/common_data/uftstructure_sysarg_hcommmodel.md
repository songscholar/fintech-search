# hcommmodel - 二级回购佣金模板表

**表对象ID**: 331
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | comm_model | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | entrust_bs | 否 |  |  |
| 6 | commcalcu_mode | 否 |  |  |
| 7 | commission_rate | 否 |  |  |
| 8 | min_fare | 否 |  |  |
| 9 | max_fare | 否 |  |  |
| 10 | segment_flag | 否 |  |  |
| 11 | segment_kind | 否 |  |  |
| 12 | netfare0_flag | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | comm_model(8)+stock_code(8)+exchange_type(4)+entrust_bs(1) |
| 17 | comm_model | 否 |  |  |
| 18 | branch_no | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | entrust_bs | 否 |  |  |
| 22 | commcalcu_mode | 否 |  |  |
| 23 | commission_rate | 否 |  |  |
| 24 | min_fare | 否 |  |  |
| 25 | max_fare | 否 |  |  |
| 26 | segment_flag | 否 |  |  |
| 27 | segment_kind | 否 |  |  |
| 28 | netfare0_flag | 否 |  |  |
| 29 | transaction_no | 否 |  |  |
| 30 | update_date | 否 |  |  |
| 31 | update_time | 否 |  |  |
| 32 | position_str | 否 |  | comm_model(8)+stock_code(8)+exchange_type(4)+entrust_bs(1) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hcommmodel | ART | 是 | comm_model, stock_code, exchange_type, entrust_bs, comm_model, stock_code, exchange_type, entrust_bs |
| idx_hcommmodel | ART | 是 | comm_model, stock_code, exchange_type, entrust_bs, comm_model, stock_code, exchange_type, entrust_bs |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_hcommmodel | comm_model, stock_code, exchange_type, entrust_bs, comm_model, stock_code, exchange_type, entrust_bs |
| idx_hcommmodel | comm_model, stock_code, exchange_type, entrust_bs, comm_model, stock_code, exchange_type, entrust_bs |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-14 15:40:36 | 3.0.6.31 | 李想 | 物理表hcommmodel，添加了表字段(update_date);
物理表hcommmodel，添加了表字段(upd... |
| 2024-09-26 19:42:57 | 3.0.3.14 |  | 物理表hcommmodel，添加了表字段(transaction_no);
 |
| 2024-09-23 16:58:46 | 3.0.2.15 | 张明月 | 新增 |
| 2025-02-14 15:40:36 | 3.0.6.31 | 李想 | 物理表hcommmodel，添加了表字段(update_date);
物理表hcommmodel，添加了表字段(upd... |
| 2024-09-26 19:42:57 | 3.0.3.14 |  | 物理表hcommmodel，添加了表字段(transaction_no);
 |
| 2024-09-23 16:58:46 | 3.0.2.15 | 张明月 | 新增 |

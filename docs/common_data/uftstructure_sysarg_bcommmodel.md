# bcommmodel - 二级后台佣金模板表

**表对象ID**: 326
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | comm_model | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | entrust_bs | 否 |  |  |
| 7 | commcalcu_mode | 否 |  |  |
| 8 | commission_rate | 否 |  |  |
| 9 | min_fare | 否 |  |  |
| 10 | max_fare | 否 |  |  |
| 11 | segment_flag | 否 |  |  |
| 12 | segment_kind | 否 |  |  |
| 13 | netfare0_flag | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | position_str | 否 |  | comm_model(8)+stock_type(4)+exchange_type(4)+money_type(3)+e |
| 18 | comm_model | 否 |  |  |
| 19 | branch_no | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | stock_type | 否 |  |  |
| 22 | money_type | 否 |  |  |
| 23 | entrust_bs | 否 |  |  |
| 24 | commcalcu_mode | 否 |  |  |
| 25 | commission_rate | 否 |  |  |
| 26 | min_fare | 否 |  |  |
| 27 | max_fare | 否 |  |  |
| 28 | segment_flag | 否 |  |  |
| 29 | segment_kind | 否 |  |  |
| 30 | netfare0_flag | 否 |  |  |
| 31 | transaction_no | 否 |  |  |
| 32 | update_date | 否 |  |  |
| 33 | update_time | 否 |  |  |
| 34 | position_str | 否 |  | comm_model(8)+stock_type(4)+exchange_type(4)+money_type(3)+e |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bcommmodel | ART | 是 | comm_model, stock_type, exchange_type, money_type, entrust_bs, comm_model, stock_type, exchange_type, money_type, entrust_bs |
| idx_bcommmodel | ART | 是 | comm_model, stock_type, exchange_type, money_type, entrust_bs, comm_model, stock_type, exchange_type, money_type, entrust_bs |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bcommmodel | comm_model, stock_type, exchange_type, money_type, entrust_bs, comm_model, stock_type, exchange_type, money_type, entrust_bs |
| idx_bcommmodel | comm_model, stock_type, exchange_type, money_type, entrust_bs, comm_model, stock_type, exchange_type, money_type, entrust_bs |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-14 15:43:17 | 3.0.6.32 | 李想 | 物理表bcommmodel，添加了表字段(update_date);
物理表bcommmodel，添加了表字段(upd... |
| 2024-09-26 19:12:39 | 3.0.3.13 | 张明月 | 物理表bcommmodel，添加了表字段(transaction_no);
 |
| 2024-09-23 16:51:42 | 3.0.2.15 | 张明月 | 新增 |
| 2025-02-14 15:43:17 | 3.0.6.32 | 李想 | 物理表bcommmodel，添加了表字段(update_date);
物理表bcommmodel，添加了表字段(upd... |
| 2024-09-26 19:12:39 | 3.0.3.13 | 张明月 | 物理表bcommmodel，添加了表字段(transaction_no);
 |
| 2024-09-23 16:51:42 | 3.0.2.15 | 张明月 | 新增 |

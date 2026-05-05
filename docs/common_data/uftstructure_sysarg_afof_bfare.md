# afof_bfare - 基金盘后业务后台费用表

**表对象ID**: 125
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | entrust_way | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | business_flag | 否 |  |  |
| 6 | money_type | 否 |  |  |
| 7 | balance_step | 否 |  |  |
| 8 | rebate_flag | 否 |  |  |
| 9 | rebate_ratio | 否 |  |  |
| 10 | fare_ratio | 否 |  |  |
| 11 | fixed_fare | 否 |  |  |
| 12 | min_fare | 否 |  |  |
| 13 | max_fare | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | position_str | 否 |  | exchange_type(4)+stock_code(8)+entrust_way(1)+branch_no(6)+b |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | entrust_way | 否 |  |  |
| 21 | branch_no | 否 |  |  |
| 22 | business_flag | 否 |  |  |
| 23 | money_type | 否 |  |  |
| 24 | balance_step | 否 |  |  |
| 25 | rebate_flag | 否 |  |  |
| 26 | rebate_ratio | 否 |  |  |
| 27 | fare_ratio | 否 |  |  |
| 28 | fixed_fare | 否 |  |  |
| 29 | min_fare | 否 |  |  |
| 30 | max_fare | 否 |  |  |
| 31 | update_date | 否 |  |  |
| 32 | update_time | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | position_str | 否 |  | exchange_type(4)+stock_code(8)+entrust_way(1)+branch_no(6)+b |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_afof_bfare | 默认 | 否 |  |
| idx_afof_bfare | ART | 是 | exchange_type, stock_code, entrust_way, branch_no, business_flag, money_type, balance_step, exchange_type, stock_code, entrust_way, branch_no, business_flag, money_type, balance_step |
| idx_afof_bfare | 默认 | 否 |  |
| idx_afof_bfare | ART | 是 | exchange_type, stock_code, entrust_way, branch_no, business_flag, money_type, balance_step, exchange_type, stock_code, entrust_way, branch_no, business_flag, money_type, balance_step |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_afof_bfare | exchange_type, stock_code, entrust_way, branch_no, business_flag, money_type, balance_step, exchange_type, stock_code, entrust_way, branch_no, business_flag, money_type, balance_step |
| idx_afof_bfare | exchange_type, stock_code, entrust_way, branch_no, business_flag, money_type, balance_step, exchange_type, stock_code, entrust_way, branch_no, business_flag, money_type, balance_step |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:34:48 | 3.0.2.103 | taocong45644 | 当前表afof_bfare，修改了索引idx_afof_bfare,索引字段修改为：(exchange_type,sto... |
| 2025-02-14 16:46:50 | 3.0.6.40 | 李想 | 新增表 |
| 2025-12-01 14:34:48 | 3.0.2.103 | taocong45644 | 当前表afof_bfare，修改了索引idx_afof_bfare,索引字段修改为：(exchange_type,sto... |
| 2025-02-14 16:46:50 | 3.0.6.40 | 李想 | 新增表 |

# strategyfare - 策略服务佣金表

**表对象ID**: 112
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | strategyfare_id | 否 |  |  |
| 3 | strategy_client_group_no | 否 |  |  |
| 4 | fare_get_type | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | money_type | 否 |  |  |
| 7 | entrust_bs | 否 |  |  |
| 8 | entrust_type | 否 |  |  |
| 9 | entrust_way | 否 |  |  |
| 10 | entrust_prop | 否 |  |  |
| 11 | stock_type | 否 |  |  |
| 12 | sub_stock_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | balance_ratio | 否 |  |  |
| 15 | par_ratio | 否 |  |  |
| 16 | min_ratio | 否 |  |  |
| 17 | min_fare | 否 |  |  |
| 18 | max_fare | 否 |  |  |
| 19 | dispart_count | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | transaction_no | 否 |  |  |
| 23 | position_str | 否 |  | strategyfare_id(32)+stock_type(4)+entrust_way(1)+exchange_ty |
| 24 | branch_no | 否 |  |  |
| 25 | strategyfare_id | 否 |  |  |
| 26 | strategy_client_group_no | 否 |  |  |
| 27 | fare_get_type | 否 |  |  |
| 28 | exchange_type | 否 |  |  |
| 29 | money_type | 否 |  |  |
| 30 | entrust_bs | 否 |  |  |
| 31 | entrust_type | 否 |  |  |
| 32 | entrust_way | 否 |  |  |
| 33 | entrust_prop | 否 |  |  |
| 34 | stock_type | 否 |  |  |
| 35 | sub_stock_type | 否 |  |  |
| 36 | stock_code | 否 |  |  |
| 37 | balance_ratio | 否 |  |  |
| 38 | par_ratio | 否 |  |  |
| 39 | min_ratio | 否 |  |  |
| 40 | min_fare | 否 |  |  |
| 41 | max_fare | 否 |  |  |
| 42 | dispart_count | 否 |  |  |
| 43 | update_date | 否 |  |  |
| 44 | update_time | 否 |  |  |
| 45 | transaction_no | 否 |  |  |
| 46 | position_str | 否 |  | strategyfare_id(32)+stock_type(4)+entrust_way(1)+exchange_ty |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strategyfare | 默认 | 否 |  |
| idx_strategyfare_sese | 默认 | 否 |  |
| idx_strategyfare_bs | 默认 | 否 |  |
| idx_strategyfare | ART | 是 | strategyfare_id, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, stock_code, strategy_client_group_no, strategyfare_id, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, stock_code, strategy_client_group_no |
| idx_strategyfare_sese | ART | 是 | strategyfare_id, exchange_type, stock_type, entrust_bs, strategyfare_id, exchange_type, stock_type, entrust_bs |
| idx_strategyfare_bs | ART | 是 | branch_no, strategy_client_group_no, branch_no, strategy_client_group_no |
| idx_strategyfare | 默认 | 否 |  |
| idx_strategyfare_sese | 默认 | 否 |  |
| idx_strategyfare_bs | 默认 | 否 |  |
| idx_strategyfare | ART | 是 | strategyfare_id, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, stock_code, strategy_client_group_no, strategyfare_id, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, stock_code, strategy_client_group_no |
| idx_strategyfare_sese | ART | 是 | strategyfare_id, exchange_type, stock_type, entrust_bs, strategyfare_id, exchange_type, stock_type, entrust_bs |
| idx_strategyfare_bs | ART | 是 | branch_no, strategy_client_group_no, branch_no, strategy_client_group_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strategyfare | strategyfare_id, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, stock_code, strategy_client_group_no, strategyfare_id, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, stock_code, strategy_client_group_no |
| idx_strategyfare | strategyfare_id, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, stock_code, strategy_client_group_no, strategyfare_id, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, stock_code, strategy_client_group_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:54:48 | 3.0.2.103 | taocong45644 | 当前表strategyfare，修改了索引idx_strategyfare,索引字段修改为：(strategyfare_... |
| 2025-02-14 14:01:14 | 3.0.6.23 | 李想 | 新增表 |
| 2025-12-01 14:54:48 | 3.0.2.103 | taocong45644 | 当前表strategyfare，修改了索引idx_strategyfare,索引字段修改为：(strategyfare_... |
| 2025-02-14 14:01:14 | 3.0.6.23 | 李想 | 新增表 |

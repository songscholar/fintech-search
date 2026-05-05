# ics_prodfare_ratio - 产品佣金费率表

**表对象ID**: 117
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | entrust_bs | 否 |  |  |
| 8 | entrust_way | 否 |  |  |
| 9 | entrust_type | 否 |  |  |
| 10 | entrust_prop | 否 |  |  |
| 11 | sub_stock_type | 否 |  |  |
| 12 | balance_ratio | 否 |  |  |
| 13 | par_ratio | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | min_fare | 否 |  |  |
| 16 | max_fare | 否 |  |  |
| 17 | fare_kind_code | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | transaction_no | 否 |  |  |
| 21 | position_str | 否 |  | fund_account(18)+exchange_type(4)+money_type(3)+stock_type(4 |
| 22 | branch_no | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | fund_account | 否 |  |  |
| 25 | exchange_type | 否 |  |  |
| 26 | money_type | 否 |  |  |
| 27 | stock_type | 否 |  |  |
| 28 | entrust_bs | 否 |  |  |
| 29 | entrust_way | 否 |  |  |
| 30 | entrust_type | 否 |  |  |
| 31 | entrust_prop | 否 |  |  |
| 32 | sub_stock_type | 否 |  |  |
| 33 | balance_ratio | 否 |  |  |
| 34 | par_ratio | 否 |  |  |
| 35 | stock_code | 否 |  |  |
| 36 | min_fare | 否 |  |  |
| 37 | max_fare | 否 |  |  |
| 38 | fare_kind_code | 否 |  |  |
| 39 | update_date | 否 |  |  |
| 40 | update_time | 否 |  |  |
| 41 | transaction_no | 否 |  |  |
| 42 | position_str | 否 |  | fund_account(18)+exchange_type(4)+money_type(3)+stock_type(4 |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ics_prodfare_ratio | 默认 | 否 |  |
| idx_ics_prodfare_ratio_cli | 默认 | 否 |  |
| idx_ics_prodfare_ratio | ART | 是 | fund_account, exchange_type, money_type, stock_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, entrust_way, stock_code, fare_kind_code, fund_account, exchange_type, money_type, stock_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, entrust_way, stock_code, fare_kind_code |
| idx_ics_prodfare_ratio_cli | ART | 是 | client_id, client_id |
| idx_ics_prodfare_ratio | 默认 | 否 |  |
| idx_ics_prodfare_ratio_cli | 默认 | 否 |  |
| idx_ics_prodfare_ratio | ART | 是 | fund_account, exchange_type, money_type, stock_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, entrust_way, stock_code, fare_kind_code, fund_account, exchange_type, money_type, stock_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, entrust_way, stock_code, fare_kind_code |
| idx_ics_prodfare_ratio_cli | ART | 是 | client_id, client_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ics_prodfare_ratio | fund_account, exchange_type, money_type, stock_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, entrust_way, stock_code, fare_kind_code, fund_account, exchange_type, money_type, stock_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, entrust_way, stock_code, fare_kind_code |
| idx_ics_prodfare_ratio | fund_account, exchange_type, money_type, stock_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, entrust_way, stock_code, fare_kind_code, fund_account, exchange_type, money_type, stock_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, entrust_way, stock_code, fare_kind_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:42:08 | 3.0.2.103 | taocong45644 | 当前表ics_prodfare_ratio，修改了索引idx_ics_prodfare_ratio,索引字段修改为：(f... |
| 2025-02-14 15:33:08 | 3.0.6.28 | 李想 | 新增表 |
| 2025-12-01 14:42:08 | 3.0.2.103 | taocong45644 | 当前表ics_prodfare_ratio，修改了索引idx_ics_prodfare_ratio,索引字段修改为：(f... |
| 2025-02-14 15:33:08 | 3.0.6.28 | 李想 | 新增表 |

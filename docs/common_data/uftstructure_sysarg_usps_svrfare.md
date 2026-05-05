# usps_svrfare - 特殊服务佣金表

**表对象ID**: 32
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | svr_fare_kind | 否 |  |  |
| 3 | fare_type | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | entrust_bs | 否 |  |  |
| 7 | entrust_way | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | entrust_type | 否 |  |  |
| 10 | balance_ratio | 否 |  |  |
| 11 | par_ratio | 否 |  |  |
| 12 | min_fare | 否 |  |  |
| 13 | max_fare | 否 |  |  |
| 14 | dispart_count | 否 |  |  |
| 15 | min_ratio | 否 |  |  |
| 16 | entrust_prop | 否 |  |  |
| 17 | sub_stock_type | 否 |  |  |
| 18 | res_entrust_type | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | svr_fare_kind(10)+fare_type(1)+stock_type(4)+entrust_way(1)+ |
| 23 | branch_no | 否 |  |  |
| 24 | svr_fare_kind | 否 |  |  |
| 25 | fare_type | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | stock_type | 否 |  |  |
| 28 | entrust_bs | 否 |  |  |
| 29 | entrust_way | 否 |  |  |
| 30 | money_type | 否 |  |  |
| 31 | entrust_type | 否 |  |  |
| 32 | balance_ratio | 否 |  |  |
| 33 | par_ratio | 否 |  |  |
| 34 | min_fare | 否 |  |  |
| 35 | max_fare | 否 |  |  |
| 36 | dispart_count | 否 |  |  |
| 37 | min_ratio | 否 |  |  |
| 38 | entrust_prop | 否 |  |  |
| 39 | sub_stock_type | 否 |  |  |
| 40 | res_entrust_type | 否 |  |  |
| 41 | transaction_no | 否 |  |  |
| 42 | update_date | 否 |  |  |
| 43 | update_time | 否 |  |  |
| 44 | position_str | 否 |  | svr_fare_kind(10)+fare_type(1)+stock_type(4)+entrust_way(1)+ |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_svrfare_cur | ART | 是 | svr_fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way, svr_fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way |
| idx_svrfare | ART | 是 | svr_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, svr_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type |
| idx_svrfare_cur | ART | 是 | svr_fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way, svr_fare_kind, exchange_type, stock_type, entrust_bs, fare_type, entrust_type, entrust_prop, sub_stock_type, entrust_way |
| idx_svrfare | ART | 是 | svr_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, svr_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_svrfare | svr_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, svr_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type |
| idx_svrfare | svr_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type, svr_fare_kind, fare_type, stock_type, entrust_way, exchange_type, money_type, entrust_bs, entrust_type, entrust_prop, sub_stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 15:47:48 | 3.0.6.33 |  | 物理表usps_svrfare，添加了表字段(dispart_count);
物理表usps_svrfare，添加了表... |
| 2025-03-03 15:08:30 | 3.0.2.76 | 周富安 | 物理表usps_svrfare，添加了表字段(dispart_count);
物理表usps_svrfare，添加了表... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 15:47:48 | 3.0.6.33 |  | 物理表usps_svrfare，添加了表字段(dispart_count);
物理表usps_svrfare，添加了表... |
| 2025-03-03 15:08:30 | 3.0.2.76 | 周富安 | 物理表usps_svrfare，添加了表字段(dispart_count);
物理表usps_svrfare，添加了表... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

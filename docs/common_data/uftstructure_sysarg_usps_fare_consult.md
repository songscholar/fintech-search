# usps_fare_consult - 标准佣金表

**表对象ID**: 54
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fare_sort | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | index_field | 是 |  |  |
| 4 | en_exchange_type | 是 |  |  |
| 5 | en_stock_type | 是 |  |  |
| 6 | en_stock_code | 是 |  |  |
| 7 | en_entrust_bs | 是 |  |  |
| 8 | en_money_type | 是 |  |  |
| 9 | en_entrust_way | 是 |  |  |
| 10 | en_entrust_type | 是 |  |  |
| 11 | balance_type | 是 |  |  |
| 12 | calcu_mode | 是 |  |  |
| 13 | balance_ratio | 是 |  |  |
| 14 | balance_fare | 是 |  |  |
| 15 | min_fare | 是 |  |  |
| 16 | max_fare | 是 |  |  |
| 17 | netfare0_flag | 是 |  |  |
| 18 | en_sub_stock_type | 是 |  |  |
| 19 | transaction_no | 是 |  |  |
| 20 | fare_sort | 是 |  |  |
| 21 | branch_no | 是 |  |  |
| 22 | index_field | 是 |  |  |
| 23 | en_exchange_type | 是 |  |  |
| 24 | en_stock_type | 是 |  |  |
| 25 | en_stock_code | 是 |  |  |
| 26 | en_entrust_bs | 是 |  |  |
| 27 | en_money_type | 是 |  |  |
| 28 | en_entrust_way | 是 |  |  |
| 29 | en_entrust_type | 是 |  |  |
| 30 | balance_type | 是 |  |  |
| 31 | calcu_mode | 是 |  |  |
| 32 | balance_ratio | 是 |  |  |
| 33 | balance_fare | 是 |  |  |
| 34 | min_fare | 是 |  |  |
| 35 | max_fare | 是 |  |  |
| 36 | netfare0_flag | 是 |  |  |
| 37 | en_sub_stock_type | 是 |  |  |
| 38 | transaction_no | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_fare_consult | ART | 是 | fare_sort, index_field, fare_sort, index_field |
| idx_usps_fare_consult_cal | ART | 是 | en_stock_code, en_sub_stock_type, en_stock_type, en_entrust_way, en_entrust_bs, en_exchange_type, en_money_type, balance_ratio, en_stock_code, en_sub_stock_type, en_stock_type, en_entrust_way, en_entrust_bs, en_exchange_type, en_money_type, balance_ratio |
| idx_usps_fare_consult | ART | 是 | fare_sort, index_field, fare_sort, index_field |
| idx_usps_fare_consult_cal | ART | 是 | en_stock_code, en_sub_stock_type, en_stock_type, en_entrust_way, en_entrust_bs, en_exchange_type, en_money_type, balance_ratio, en_stock_code, en_sub_stock_type, en_stock_type, en_entrust_way, en_entrust_bs, en_exchange_type, en_money_type, balance_ratio |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_fare_consult | fare_sort, index_field, fare_sort, index_field |
| idx_usps_fare_consult | fare_sort, index_field, fare_sort, index_field |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-09-29 17:14:36 | V3.0.1.10 | 沈勋 | 物理表usps_fare_consult，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-09-29 17:14:36 | V3.0.1.10 | 沈勋 | 物理表usps_fare_consult，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

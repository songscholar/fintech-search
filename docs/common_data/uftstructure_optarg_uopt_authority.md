# uopt_authority - 期权标的证券权益信息表

**表对象ID**: 9014
**所属模块**: optarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_code | 是 |  |  |
| 3 | authority_kind | 是 |  |  |
| 4 | authority_code | 是 |  |  |
| 5 | register_date | 是 |  |  |
| 6 | update_date | 是 |  |  |
| 7 | update_time | 是 |  |  |
| 8 | dr_date | 是 |  |  |
| 9 | pay_date | 是 |  |  |
| 10 | market_date | 是 |  |  |
| 11 | alloted_price | 是 |  |  |
| 12 | close_price | 是 |  |  |
| 13 | distribute_rate | 是 |  |  |
| 14 | circulate_change_per | 是 |  |  |
| 15 | transaction_no | 是 |  |  |
| 16 | remark | 是 |  |  |
| 17 | exchange_type | 是 |  |  |
| 18 | stock_code | 是 |  |  |
| 19 | authority_kind | 是 |  |  |
| 20 | authority_code | 是 |  |  |
| 21 | register_date | 是 |  |  |
| 22 | update_date | 是 |  |  |
| 23 | update_time | 是 |  |  |
| 24 | dr_date | 是 |  |  |
| 25 | pay_date | 是 |  |  |
| 26 | market_date | 是 |  |  |
| 27 | alloted_price | 是 |  |  |
| 28 | close_price | 是 |  |  |
| 29 | distribute_rate | 是 |  |  |
| 30 | circulate_change_per | 是 |  |  |
| 31 | transaction_no | 是 |  |  |
| 32 | remark | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_authority | 默认 | 否 |  |
| idx_uopt_authority | 默认 | 是 | exchange_type, stock_code, authority_kind, register_date, exchange_type, stock_code, authority_kind, register_date |
| idx_uopt_authority | 默认 | 否 |  |
| idx_uopt_authority | 默认 | 是 | exchange_type, stock_code, authority_kind, register_date, exchange_type, stock_code, authority_kind, register_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_authority | exchange_type, stock_code, authority_kind, register_date, exchange_type, stock_code, authority_kind, register_date |
| idx_uopt_authority | exchange_type, stock_code, authority_kind, register_date, exchange_type, stock_code, authority_kind, register_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-18 17:02:54 | V3.0.3.8 | 汪迎 | 物理表uopt_authority，添加了表字段(transaction_no);
 |
| 2024-10-19 10:14:31 | V3.0.3.7 | 韦子晗 | 物理表uopt_authority，删除了表字段(stock_name);
物理表uopt_authority，删除了... |
| 2024-10-19 10:14:11 | V3.0.3.7 | 韦子晗 | 物理表uopt_authority，删除索引字段(索引idx_uopt_authority:删除了索引字段：dr_dat... |
| 2025-04-18 17:02:54 | V3.0.3.8 | 汪迎 | 物理表uopt_authority，添加了表字段(transaction_no);
 |
| 2024-10-19 10:14:31 | V3.0.3.7 | 韦子晗 | 物理表uopt_authority，删除了表字段(stock_name);
物理表uopt_authority，删除了... |
| 2024-10-19 10:14:11 | V3.0.3.7 | 韦子晗 | 物理表uopt_authority，删除索引字段(索引idx_uopt_authority:删除了索引字段：dr_dat... |

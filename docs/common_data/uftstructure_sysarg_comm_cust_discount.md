# comm_cust_discount - 客户佣金折扣表

**表对象ID**: 386
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | ordinal | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | en_stock_type | 否 |  |  |
| 7 | en_entrust_way | 否 |  |  |
| 8 | discount_type | 否 |  |  |
| 9 | discount_rate | 否 |  |  |
| 10 | modify_date | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | ordinal | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | en_stock_type | 否 |  |  |
| 18 | en_entrust_way | 否 |  |  |
| 19 | discount_type | 否 |  |  |
| 20 | discount_rate | 否 |  |  |
| 21 | modify_date | 否 |  |  |
| 22 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_comm_cust_discount | ART | 是 | client_id, ordinal, client_id, ordinal |
| idx_comm_cust_discount | ART | 是 | client_id, ordinal, client_id, ordinal |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_comm_cust_discount | client_id, ordinal, client_id, ordinal |
| idx_comm_cust_discount | client_id, ordinal, client_id, ordinal |

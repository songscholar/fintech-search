# crdt_client_min_fare - 融资融券客户多档最低佣金表

**表对象ID**: 7046
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | min_fare | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | entrust_way | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | min_fare | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_type | 否 |  |  |
| 11 | entrust_way | 否 |  |  |
| 12 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_client_min_fare | ART | 是 | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |
| idx_crdt_client_min_fare | ART | 是 | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_client_min_fare | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |
| idx_crdt_client_min_fare | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-04 10:31:41 | 3.0.4.2 | 沈勋 | 新增表 |
| 2024-09-04 10:31:41 | 3.0.4.2 | 沈勋 | 新增表 |

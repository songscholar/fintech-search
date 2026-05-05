# uarg_crt_client_minfare - 信用客户多档最低佣金表

**表对象ID**: 7110
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | min_fare | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | entrust_way | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_type(4)+entrust_way( |
| 11 | fund_account | 否 |  |  |
| 12 | min_fare | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_type | 否 |  |  |
| 15 | entrust_way | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_type(4)+entrust_way( |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_crt_client_minfare | ART | 是 | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |
| idx_uarg_crt_client_minfare | ART | 是 | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_crt_client_minfare | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |
| idx_uarg_crt_client_minfare | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-13 14:31:44 | 3.0.6.98 | 李想 | 新增表 |
| 2025-03-13 14:31:44 | 3.0.6.98 | 李想 | 新增表 |

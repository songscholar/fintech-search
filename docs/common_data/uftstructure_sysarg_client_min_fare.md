# client_min_fare - 客户多档最低佣金表

**表对象ID**: 304
**所属模块**: sysarg
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
| idx_client_min_fare | ART | 是 | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |
| idx_client_min_fare | ART | 是 | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_client_min_fare | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |
| idx_client_min_fare | fund_account, exchange_type, stock_type, entrust_way, fund_account, exchange_type, stock_type, entrust_way |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 15:12:34 | 3.0.6.12 | 常行 | 物理表client_min_fare，添加了表字段(branch_no);
物理表client_min_fare，添加... |
| 2024-05-29 21:26:13 | 3.0.2.10 | 祝丁恺 | 勾选不回库选项 |
| 2024-05-11 15:00:03 | 3.0.2.6 | 阮善宏 | 物理表client_min_fare，添加了表字段(transaction_no);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 15:12:34 | 3.0.6.12 | 常行 | 物理表client_min_fare，添加了表字段(branch_no);
物理表client_min_fare，添加... |
| 2024-05-29 21:26:13 | 3.0.2.10 | 祝丁恺 | 勾选不回库选项 |
| 2024-05-11 15:00:03 | 3.0.2.6 | 阮善宏 | 物理表client_min_fare，添加了表字段(transaction_no);
 |

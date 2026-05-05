# persecurate - 客户交易汇率浮动比率表

**表对象ID**: 317
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | perbuy_float_ratio | 否 |  |  |
| 4 | persell_float_ratio | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | fund_account(18)+exchange_type(4) |
| 11 | exchange_type | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | perbuy_float_ratio | 否 |  |  |
| 14 | persell_float_ratio | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | fund_account(18)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_pesecurate | ART | 是 | fund_account, exchange_type, fund_account, exchange_type |
| idx_pesecurate | ART | 是 | fund_account, exchange_type, fund_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_pesecurate | fund_account, exchange_type, fund_account, exchange_type |
| idx_pesecurate | fund_account, exchange_type, fund_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 16:02:22 | 3.0.6.97 | 李想 | 物理表persecurate，添加了表字段(client_id);
物理表persecurate，添加了表字段(bra... |
| 2024-07-24 15:26:32 | 3.0.2.24 | 乐闽庭 | 新增表 |
| 2025-02-19 16:02:22 | 3.0.6.97 | 李想 | 物理表persecurate，添加了表字段(client_id);
物理表persecurate，添加了表字段(bra... |
| 2024-07-24 15:26:32 | 3.0.2.24 | 乐闽庭 | 新增表 |

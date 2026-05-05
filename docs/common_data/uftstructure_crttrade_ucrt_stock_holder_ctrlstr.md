# ucrt_stock_holder_ctrlstr - 融资融券证券账户控制串表

**表对象ID**: 7996
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stkholder_ctrlstr | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | stkholder_ctrlstr | 否 |  |  |
| 8 | stock_account | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_stock_holder_ctrlstr | ART | 是 | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |
| idx_ucrt_stock_holder_ctrlstr | ART | 是 | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_stock_holder_ctrlstr_unique | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |
| idx_ucrt_stock_holder_ctrlstr_unique | stock_account, exchange_type, fund_account, stock_account, exchange_type, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-06-24 09:29:24 | 3.0.2.17 | 徐志坚 | 新增表结构，为了占用对象号，以防后续重复申请而导致冲突 |
| 2024-06-24 09:29:24 | 3.0.2.17 | 徐志坚 | 新增表结构，为了占用对象号，以防后续重复申请而导致冲突 |

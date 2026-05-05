# ucrt_bond_exemptricon - 可转债交易权限豁免名单信息表

**表对象ID**: 7035
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_bond_exemptricon | ART | 是 | fund_account, client_id, exchange_type, stock_code, fund_account, client_id, exchange_type, stock_code |
| idx_ucrt_bond_exemptricon | ART | 是 | fund_account, client_id, exchange_type, stock_code, fund_account, client_id, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_bond_exemptricon | client_id, fund_account, exchange_type, stock_code, client_id, fund_account, exchange_type, stock_code |
| idx_ucrt_bond_exemptricon | client_id, fund_account, exchange_type, stock_code, client_id, fund_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-07-23 15:46:14 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2024-07-23 15:46:14 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

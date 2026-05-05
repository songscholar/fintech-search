# vipbranch_prefix - 特殊申报营业部前缀表

**表对象ID**: 134
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | contract_prefix | 否 |  |  |
| 5 | rpt_branch_id | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | position_str | 否 |  | stock_account(20)+contract_prefix(6)+exchange_type(4) |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | branch_no | 否 |  |  |
| 13 | contract_prefix | 否 |  |  |
| 14 | rpt_branch_id | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | position_str | 否 |  | stock_account(20)+contract_prefix(6)+exchange_type(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_vipbranch_prefix | 默认 | 否 |  |
| idx_vipbranch_prefix | ART | 是 | stock_account, contract_prefix, exchange_type, stock_account, contract_prefix, exchange_type |
| idx_vipbranch_prefix | 默认 | 否 |  |
| idx_vipbranch_prefix | ART | 是 | stock_account, contract_prefix, exchange_type, stock_account, contract_prefix, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_vipbranch_prefix | stock_account, contract_prefix, exchange_type, stock_account, contract_prefix, exchange_type |
| idx_vipbranch_prefix | stock_account, contract_prefix, exchange_type, stock_account, contract_prefix, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:46:26 | 3.0.2.103 | taocong45644 | 当前表vipbranch_prefix，修改了索引idx_vipbranch_prefix,索引字段修改为：(stock... |
| 2025-02-19 14:21:36 | 3.0.6.89 | 李想 | 新增表 |
| 2025-12-01 15:46:26 | 3.0.2.103 | taocong45644 | 当前表vipbranch_prefix，修改了索引idx_vipbranch_prefix,索引字段修改为：(stock... |
| 2025-02-19 14:21:36 | 3.0.6.89 | 李想 | 新增表 |

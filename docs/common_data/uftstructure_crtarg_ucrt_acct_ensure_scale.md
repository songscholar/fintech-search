# ucrt_acct_ensure_scale - 个人保障比例参数表

**表对象ID**: 7031
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | ensurescale_value | 否 |  |  |
| 6 | init_ensurescale_value | 否 |  |  |
| 7 | short_ensurescale_value | 否 |  |  |
| 8 | short_init_ensurescale_value | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | stock_type | 否 |  |  |
| 14 | ensurescale_value | 否 |  |  |
| 15 | init_ensurescale_value | 否 |  |  |
| 16 | short_ensurescale_value | 否 |  |  |
| 17 | short_init_ensurescale_value | 否 |  |  |
| 18 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_acct_ensure_scale | ART | 是 | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |
| idx_ucrt_acct_ensure_scale | ART | 是 | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_acct_ensure_scale | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |
| idx_ucrt_acct_ensure_scale | fund_account, stock_code, stock_type, exchange_type, fund_account, stock_code, stock_type, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:25 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no；新增索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:25 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no；新增索引 |

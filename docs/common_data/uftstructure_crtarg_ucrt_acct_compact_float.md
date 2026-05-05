# ucrt_acct_compact_float - 客户合约浮动利率表

**表对象ID**: 7008
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | float_ratio | 否 |  |  |
| 4 | float_ratio_type | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | float_ratio | 否 |  |  |
| 9 | float_ratio_type | 否 |  |  |
| 10 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_acct_compact_float | ART | 是 | fund_account, float_ratio_type, fund_account, float_ratio_type |
| idx_ucrt_acct_compact_float | ART | 是 | fund_account, float_ratio_type, fund_account, float_ratio_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_acct_compact_float | fund_account, float_ratio_type, fund_account, float_ratio_type |
| idx_ucrt_acct_compact_float | fund_account, float_ratio_type, fund_account, float_ratio_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:23 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no；新增索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:23 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no；新增索引 |

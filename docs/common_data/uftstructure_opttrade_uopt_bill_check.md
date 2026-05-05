# uopt_bill_check - 期权账单确认表

**表对象ID**: 9030
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | bill_flag | 否 |  |  |
| 7 | remark | 否 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | curr_date | 否 |  |  |
| 12 | curr_time | 否 |  |  |
| 13 | bill_flag | 否 |  |  |
| 14 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_bill_check | 默认 | 是 | init_date, fund_account, init_date, fund_account |
| idx_uopt_bill_check | 默认 | 是 | init_date, fund_account, init_date, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_bill_check | init_date, fund_account, init_date, fund_account |
| idx_uopt_bill_check | init_date, fund_account, init_date, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-12-26 14:56:53 | V3.0.3.7 | 张明月 | 新增表uopt_bill_check |
| 2024-12-26 14:56:53 | V3.0.3.7 | 张明月 | 新增表uopt_bill_check |

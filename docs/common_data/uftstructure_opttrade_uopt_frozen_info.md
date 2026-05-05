# uopt_frozen_info - 期权冻结信息表

**表对象ID**: 9018
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | opt_frozen_type | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | stock_type | 否 |  |  |
| 11 | frozen_amount | 否 |  |  |
| 12 | frozen_balance | 否 |  |  |
| 13 | date_clear | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | init_date | 否 |  |  |
| 16 | company_no | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | client_id | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | opt_frozen_type | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | stock_account | 否 |  |  |
| 23 | stock_code | 否 |  |  |
| 24 | stock_type | 否 |  |  |
| 25 | frozen_amount | 否 |  |  |
| 26 | frozen_balance | 否 |  |  |
| 27 | date_clear | 否 |  |  |
| 28 | remark | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_frozen_info | 默认 | 是 | init_date, client_id, opt_frozen_type, exchange_type, stock_type, stock_code, init_date, client_id, opt_frozen_type, exchange_type, stock_type, stock_code |
| idx_uopt_frozen_qry | 默认 | 是 | fund_account, exchange_type, stock_type, stock_code, opt_frozen_type, fund_account, exchange_type, stock_type, stock_code, opt_frozen_type |
| idx_uopt_frozen_info | 默认 | 是 | init_date, client_id, opt_frozen_type, exchange_type, stock_type, stock_code, init_date, client_id, opt_frozen_type, exchange_type, stock_type, stock_code |
| idx_uopt_frozen_qry | 默认 | 是 | fund_account, exchange_type, stock_type, stock_code, opt_frozen_type, fund_account, exchange_type, stock_type, stock_code, opt_frozen_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_frozen_info | init_date, client_id, opt_frozen_type, exchange_type, stock_type, stock_code, init_date, client_id, opt_frozen_type, exchange_type, stock_type, stock_code |
| idx_uopt_frozen_info | init_date, client_id, opt_frozen_type, exchange_type, stock_type, stock_code, init_date, client_id, opt_frozen_type, exchange_type, stock_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-10-16 19:52:11 | V3.0.3.7 | 韦子晗 | 新增索引idx_uopt_frozen_qry |
| 2024-10-16 19:52:11 | V3.0.3.7 | 韦子晗 | 新增索引idx_uopt_frozen_qry |

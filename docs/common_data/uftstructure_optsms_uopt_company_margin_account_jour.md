# uopt_company_margin_account_jour - 期权公司保证金账户流水表

**表对象ID**: 9070
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | op_branch_no | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | company_no | 否 |  |  |
| 9 | optmargin_account | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | occur_balance | 否 |  |  |
| 12 | remark | 否 |  |  |
| 13 | position_str | 否 |  | 定位串 = 交易日期(8)＋流水号(10) |
| 14 | action_in | 否 |  | 0-转入,1-转出,2-外部系统登记 |
| 15 | init_date | 否 |  |  |
| 16 | serial_no | 否 |  |  |
| 17 | curr_date | 否 |  |  |
| 18 | curr_time | 否 |  |  |
| 19 | op_branch_no | 否 |  |  |
| 20 | operator_no | 否 |  |  |
| 21 | op_station | 否 |  |  |
| 22 | company_no | 否 |  |  |
| 23 | optmargin_account | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | occur_balance | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | position_str | 否 |  | 定位串 = 交易日期(8)＋流水号(10) |
| 28 | action_in | 否 |  | 0-转入,1-转出,2-外部系统登记 |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_company_margin_account_jour_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_company_margin_account_jour_com | 默认 | 是 | company_no, init_date, company_no, init_date |
| idx_uopt_company_margin_account_jour_pos | 默认 | 是 | position_str, position_str |
| idx_uopt_company_margin_account_jour_com | 默认 | 是 | company_no, init_date, company_no, init_date |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_company_margin_account_jour_pos | position_str, position_str |
| idx_uopt_company_margin_account_jour_com | company_no, init_date, company_no, init_date |
| idx_uopt_company_margin_account_jour_pos | position_str, position_str |
| idx_uopt_company_margin_account_jour_com | company_no, init_date, company_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-22 16:24:21 | V3.0.2.1 | 祁献毅 | 新增 |
| 2025-09-22 16:24:21 | V3.0.2.1 | 祁献毅 | 新增 |

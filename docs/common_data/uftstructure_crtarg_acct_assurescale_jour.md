# acct_assurescale_jour - 个人维持担保比例参数流水表

**表对象ID**: 7082
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | assurescale_type | 否 |  |  |
| 7 | remark | 否 |  |  |
| 8 | end_date | 否 |  |  |
| 9 | dynamic_flag | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | source_arg | 否 |  |  |
| 12 | assurescale_value | 否 |  |  |
| 13 | action_in | 否 |  |  |
| 14 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |
| 15 | init_date | 否 |  |  |
| 16 | serial_no | 否 |  |  |
| 17 | curr_date | 否 |  |  |
| 18 | curr_time | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | assurescale_type | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | end_date | 否 |  |  |
| 23 | dynamic_flag | 否 |  |  |
| 24 | branch_no | 否 |  |  |
| 25 | source_arg | 否 |  |  |
| 26 | assurescale_value | 否 |  |  |
| 27 | action_in | 否 |  |  |
| 28 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_acct_assurescale_jour | ART | 是 | position_str, position_str |
| idx_acct_assurescale_jour_acct | ART | 是 | fund_account, assurescale_type, fund_account, assurescale_type |
| uk_rpt_acctassurescalejour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_acctassurescalejour_acct | ART | 是 | init_date, fund_account, position_str, init_date, fund_account, position_str |
| idx_acct_assurescale_jour | ART | 是 | position_str, position_str |
| idx_acct_assurescale_jour_acct | ART | 是 | fund_account, assurescale_type, fund_account, assurescale_type |
| uk_rpt_acctassurescalejour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_acctassurescalejour_acct | ART | 是 | init_date, fund_account, position_str, init_date, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_acct_assurescale_jour | position_str, position_str |
| idx_acct_assurescale_jour | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 16:50:44 | 3.0.6.47 | 李想 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 16:50:44 | 3.0.6.47 | 李想 | 新增表 |

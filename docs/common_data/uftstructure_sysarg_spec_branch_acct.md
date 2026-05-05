# spec_branch_acct - 专门户登记表

**表对象ID**: 142
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | special_type | 否 |  |  |
| 5 | register_date | 否 |  |  |
| 6 | fund_company | 否 |  |  |
| 7 | company_name | 否 |  |  |
| 8 | pfund_product_id | 否 |  |  |
| 9 | pfund_product_name | 否 |  |  |
| 10 | ics_acct_busi_mode | 否 |  |  |
| 11 | open_branch_no | 否 |  |  |
| 12 | etfprod_flag | 否 |  |  |
| 13 | position_str | 否 |  |  |
| 14 | branch_no | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | special_type | 否 |  |  |
| 18 | register_date | 否 |  |  |
| 19 | fund_company | 否 |  |  |
| 20 | company_name | 否 |  |  |
| 21 | pfund_product_id | 否 |  |  |
| 22 | pfund_product_name | 否 |  |  |
| 23 | ics_acct_busi_mode | 否 |  |  |
| 24 | open_branch_no | 否 |  |  |
| 25 | etfprod_flag | 否 |  |  |
| 26 | position_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_spec_branch_acct | 默认 | 否 |  |
| idx_spec_branch_acct | ART | 是 | fund_account, branch_no, fund_account, branch_no |
| idx_spec_branch_acct | 默认 | 否 |  |
| idx_spec_branch_acct | ART | 是 | fund_account, branch_no, fund_account, branch_no |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_spec_branch_acct | fund_account, branch_no, fund_account, branch_no |
| idx_spec_branch_acct_cli | client_id, client_id |
| idx_spec_branch_acct_pos | position_str, position_str |
| idx_spec_branch_acct | fund_account, branch_no, fund_account, branch_no |
| idx_spec_branch_acct_cli | client_id, client_id |
| idx_spec_branch_acct_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:53:35 | 3.0.2.103 | taocong45644 | 当前表spec_branch_acct，修改了索引idx_spec_branch_acct,索引字段修改为：(fund_... |
| 2025-02-27 20:00:34 | 3.0.6.124 | 李想 | 新增表 |
| 2025-12-01 14:53:35 | 3.0.2.103 | taocong45644 | 当前表spec_branch_acct，修改了索引idx_spec_branch_acct,索引字段修改为：(fund_... |
| 2025-02-27 20:00:34 | 3.0.6.124 | 李想 | 新增表 |

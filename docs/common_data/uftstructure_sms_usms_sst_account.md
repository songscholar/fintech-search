# usms_sst_account - 股份转让投资者账户表(交易管理)

**表对象ID**: 2832
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | organ_flag | 否 |  |  |
| 7 | asset_balance | 否 |  |  |
| 8 | register_fund | 否 |  |  |
| 9 | first_exchdate | 否 |  |  |
| 10 | sub_risk_date | 否 |  |  |
| 11 | register_date | 否 |  |  |
| 12 | sstacct_status | 否 |  |  |
| 13 | right_open_date | 否 |  |  |
| 14 | report_date | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | position_str | 否 |  |  |
| 17 | op_branch_no | 否 |  |  |
| 18 | operator_no | 否 |  |  |
| 19 | sst_report_type | 否 |  |  |
| 20 | cancel_date | 否 |  |  |
| 21 | paid_capital | 否 |  |  |
| 22 | invest_exp_flag | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | client_id | 否 |  |  |
| 25 | fund_account | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | stock_account | 否 |  |  |
| 28 | branch_no | 否 |  |  |
| 29 | organ_flag | 否 |  |  |
| 30 | asset_balance | 否 |  |  |
| 31 | register_fund | 否 |  |  |
| 32 | first_exchdate | 否 |  |  |
| 33 | sub_risk_date | 否 |  |  |
| 34 | register_date | 否 |  |  |
| 35 | sstacct_status | 否 |  |  |
| 36 | right_open_date | 否 |  |  |
| 37 | report_date | 否 |  |  |
| 38 | remark | 否 |  |  |
| 39 | position_str | 否 |  |  |
| 40 | op_branch_no | 否 |  |  |
| 41 | operator_no | 否 |  |  |
| 42 | sst_report_type | 否 |  |  |
| 43 | cancel_date | 否 |  |  |
| 44 | paid_capital | 否 |  |  |
| 45 | invest_exp_flag | 否 |  |  |
| 46 | transaction_no | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sstaccount_syn | ART | 是 | stock_account, branch_no, exchange_type, fund_account, stock_account, branch_no, exchange_type, fund_account |
| idx_sstaccount | 默认 | 是 | stock_account, branch_no, exchange_type, sst_report_type, fund_account, stock_account, branch_no, exchange_type, sst_report_type, fund_account |
| idx_sstaccount_syn | ART | 是 | stock_account, branch_no, exchange_type, fund_account, stock_account, branch_no, exchange_type, fund_account |
| idx_sstaccount_pos | ART | 是 | position_str, position_str |
| idx_sstaccount_syn | ART | 是 | stock_account, branch_no, exchange_type, fund_account, stock_account, branch_no, exchange_type, fund_account |
| idx_sstaccount | 默认 | 是 | stock_account, branch_no, exchange_type, sst_report_type, fund_account, stock_account, branch_no, exchange_type, sst_report_type, fund_account |
| idx_sstaccount_syn | ART | 是 | stock_account, branch_no, exchange_type, fund_account, stock_account, branch_no, exchange_type, fund_account |
| idx_sstaccount_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sstaccount | stock_account, branch_no, exchange_type, sst_report_type, fund_account, stock_account, branch_no, exchange_type, sst_report_type, fund_account |
| idx_sstaccount | stock_account, branch_no, exchange_type, sst_report_type, fund_account, stock_account, branch_no, exchange_type, sst_report_type, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-04 10:05:52 | 8.26.2.95 | 刘大为 | 当前表usms_sst_account，增加索引（ idx_sstaccount_syn:[stock_account,... |
| 2025-08-18 09:37:54 | 3.0.2.3 | 高志强 | 所有表usms_sst_account，添加了表字段(transaction_no);
 |
| 2025-05-12 15:36:49 | 3.0.2.2004 | 高志强 | 新增 |
| 2025-12-04 10:05:52 | 8.26.2.95 | 刘大为 | 当前表usms_sst_account，增加索引（ idx_sstaccount_syn:[stock_account,... |
| 2025-08-18 09:37:54 | 3.0.2.3 | 高志强 | 所有表usms_sst_account，添加了表字段(transaction_no);
 |
| 2025-05-12 15:36:49 | 3.0.2.2004 | 高志强 | 新增 |

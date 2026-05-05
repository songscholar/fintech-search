# usms_qrp_agent_acct - 报价回购代理委托登记表(交易管理)

**表对象ID**: 2829
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 是 |  |  |
| 2 | client_id | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | stock_account | 是 |  |  |
| 5 | stock_code | 是 |  |  |
| 6 | open_date | 是 |  |  |
| 7 | qrp_agentacct_status | 是 |  |  |
| 8 | reserve_balance | 是 |  |  |
| 9 | postpone_flag | 是 |  |  |
| 10 | position_str | 是 |  |  |
| 11 | exchange_type | 是 |  |  |
| 12 | company_no | 是 |  |  |
| 13 | valid_date | 是 |  |  |
| 14 | transaction_no | 是 |  |  |
| 15 | qrp_agent_result | 是 |  |  |
| 16 | trade_restriction_flag | 是 |  |  |
| 17 | fund_account | 是 |  |  |
| 18 | client_id | 是 |  |  |
| 19 | branch_no | 是 |  |  |
| 20 | stock_account | 是 |  |  |
| 21 | stock_code | 是 |  |  |
| 22 | open_date | 是 |  |  |
| 23 | qrp_agentacct_status | 是 |  |  |
| 24 | reserve_balance | 是 |  |  |
| 25 | postpone_flag | 是 |  |  |
| 26 | position_str | 是 |  |  |
| 27 | exchange_type | 是 |  |  |
| 28 | company_no | 是 |  |  |
| 29 | valid_date | 是 |  |  |
| 30 | transaction_no | 是 |  |  |
| 31 | qrp_agent_result | 是 |  |  |
| 32 | trade_restriction_flag | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usmsqrpagentacct | 默认 | 是 | fund_account, fund_account |
| idx_usmsqrpagentacct | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usmsqrpagentacct | fund_account, fund_account |
| idx_usmsqrpagentacct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-29 10:39:11 | 3.0.2.2003 | 高志强 | 新增 |
| 2025-04-29 10:39:11 | 3.0.2.2003 | 高志强 | 新增 |

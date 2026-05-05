# qrp_agent_acct - 报价回购代理委托登记表

**表对象ID**: 2336
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | open_date | 否 |  |  |
| 7 | qrp_agentacct_status | 否 |  |  |
| 8 | reserve_balance | 否 |  |  |
| 9 | postpone_flag | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | company_no | 否 |  |  |
| 13 | valid_date | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | qrp_agent_result | 否 |  |  |
| 16 | trade_restriction_flag | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | client_id | 否 |  |  |
| 19 | branch_no | 否 |  |  |
| 20 | stock_account | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | open_date | 否 |  |  |
| 23 | qrp_agentacct_status | 否 |  |  |
| 24 | reserve_balance | 否 |  |  |
| 25 | postpone_flag | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | company_no | 否 |  |  |
| 29 | valid_date | 否 |  |  |
| 30 | transaction_no | 否 |  |  |
| 31 | qrp_agent_result | 否 |  |  |
| 32 | trade_restriction_flag | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrpagentacct | 默认 | 否 |  |
| idx_qrpagentacct | ART | 是 | fund_account, fund_account |
| idx_qrpagentacct | 默认 | 否 |  |
| idx_qrpagentacct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrpagentacct | fund_account, fund_account |
| idx_qrpagentacct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:30:09 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-04-30 14:53:10 | 3.0.2.2003 | 高志强 | 物理表qrp_agent_acct，添加了表字段(qrp_agent_result);
物理表qrp_agent_ac... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |
| 2026-03-04 15:30:09 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-04-30 14:53:10 | 3.0.2.2003 | 高志强 | 物理表qrp_agent_acct，添加了表字段(qrp_agent_result);
物理表qrp_agent_ac... |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |

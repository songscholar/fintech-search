# ucrt_riskacct_list - 风险客户名单表

**表对象ID**: 7536
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | seat_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | stock_account_sh | 否 |  |  |
| 5 | stock_account_sz | 否 |  |  |
| 6 | riskaccount_type | 否 |  |  |
| 7 | crdtsrc_type | 否 |  |  |
| 8 | create_date | 否 |  |  |
| 9 | crdtfine_type | 否 |  |  |
| 10 | date_clear | 否 |  |  |
| 11 | risk_enddate | 否 |  |  |
| 12 | stock_account_stb | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | seat_no | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | stock_account_sh | 否 |  |  |
| 18 | stock_account_sz | 否 |  |  |
| 19 | riskaccount_type | 否 |  |  |
| 20 | crdtsrc_type | 否 |  |  |
| 21 | create_date | 否 |  |  |
| 22 | crdtfine_type | 否 |  |  |
| 23 | date_clear | 否 |  |  |
| 24 | risk_enddate | 否 |  |  |
| 25 | stock_account_stb | 否 |  |  |
| 26 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_riskacct_list_type | ART | 是 | fund_account, riskaccount_type, fund_account, riskaccount_type |
| idx_ucrt_riskacct_list | ART | 是 | fund_account, crdtfine_type, create_date, fund_account, crdtfine_type, create_date |
| idx_ucrt_riskacct_list_type | ART | 是 | fund_account, riskaccount_type, fund_account, riskaccount_type |
| idx_ucrt_riskacct_list | ART | 是 | fund_account, crdtfine_type, create_date, fund_account, crdtfine_type, create_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_riskacct_list | fund_account, crdtfine_type, create_date, fund_account, crdtfine_type, create_date |
| idx_ucrt_riskacct_list | fund_account, crdtfine_type, create_date, fund_account, crdtfine_type, create_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-22 13:33:32 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-22 13:33:32 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

# srp_fund_detail - 股票质押融资申购资金明细表

**表对象ID**: 5838
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | ipo_balance | 否 |  |  |
| 7 | self_balance | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | date_clear | 否 |  |  |
| 10 | cancel_serialno | 否 |  |  |
| 11 | position_str | 否 |  |  |
| 12 | report_no | 否 |  |  |
| 13 | client_id | 否 | H |  |
| 14 | client_name | 否 | H |  |
| 15 | corp_client_group | 否 | H |  |
| 16 | client_group | 否 | H |  |
| 17 | room_code | 否 | H |  |
| 18 | asset_prop | 否 | H |  |
| 19 | limit_flag | 否 | H |  |
| 20 | client_prop | 否 | H |  |
| 21 | asset_level | 否 | H |  |
| 22 | risk_level | 否 | H |  |
| 23 | corp_risk_level | 否 | H |  |
| 24 | init_date | 否 |  |  |
| 25 | entrust_no | 否 |  |  |
| 26 | branch_no | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | money_type | 否 |  |  |
| 29 | ipo_balance | 否 |  |  |
| 30 | self_balance | 否 |  |  |
| 31 | remark | 否 |  |  |
| 32 | date_clear | 否 |  |  |
| 33 | cancel_serialno | 否 |  |  |
| 34 | position_str | 否 |  |  |
| 35 | report_no | 否 |  |  |
| 36 | client_id | 否 | H |  |
| 37 | client_name | 否 | H |  |
| 38 | corp_client_group | 否 | H |  |
| 39 | client_group | 否 | H |  |
| 40 | room_code | 否 | H |  |
| 41 | asset_prop | 否 | H |  |
| 42 | limit_flag | 否 | H |  |
| 43 | client_prop | 否 | H |  |
| 44 | asset_level | 否 | H |  |
| 45 | risk_level | 否 | H |  |
| 46 | corp_risk_level | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srp_fund_detail | ART | 是 | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |
| idx_srp_fund_detail_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_srpfunddetail | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpfunddetail_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpfunddetail_tolast | ART | 是 | date_clear, date_clear |
| idx_srp_fund_detail | ART | 是 | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |
| idx_srp_fund_detail_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_srpfunddetail | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_srpfunddetail_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_srpfunddetail_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srp_fund_detail | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |
| idx_srp_fund_detail | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:46:54 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 16:22:47 | V3.0.2.74 | 洪略 | 补充分区信息 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2026-03-09 14:46:54 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 16:22:47 | V3.0.2.74 | 洪略 | 补充分区信息 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |

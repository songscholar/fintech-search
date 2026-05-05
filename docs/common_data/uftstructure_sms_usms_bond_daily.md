# usms_bond_daily - 正回购每日情况表

**表对象ID**: 2854
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | uncome_balance | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | client_id | 否 | H |  |
| 9 | client_name | 否 | H |  |
| 10 | corp_client_group | 否 | H |  |
| 11 | client_group | 否 | H |  |
| 12 | room_code | 否 | H |  |
| 13 | asset_prop | 否 | H |  |
| 14 | limit_flag | 否 | H |  |
| 15 | client_prop | 否 | H |  |
| 16 | asset_level | 否 | H |  |
| 17 | risk_level | 否 | H |  |
| 18 | corp_risk_level | 否 | H |  |
| 19 | init_date | 否 |  |  |
| 20 | fund_account | 否 |  |  |
| 21 | stock_account | 否 |  |  |
| 22 | branch_no | 否 |  |  |
| 23 | uncome_balance | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | date_clear | 否 |  |  |
| 26 | client_id | 否 | H |  |
| 27 | client_name | 否 | H |  |
| 28 | corp_client_group | 否 | H |  |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | asset_prop | 否 | H |  |
| 32 | limit_flag | 否 | H |  |
| 33 | client_prop | 否 | H |  |
| 34 | asset_level | 否 | H |  |
| 35 | risk_level | 否 | H |  |
| 36 | corp_risk_level | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_bond_daily | 默认 | 是 | init_date, fund_account, stock_account, exchange_type, init_date, fund_account, stock_account, exchange_type |
| idx_rpt_usms_bond_daily | ART | 是 | init_date, fund_account, stock_account, exchange_type, init_date, fund_account, stock_account, exchange_type |
| idx_usms_bond_daily | 默认 | 是 | init_date, fund_account, stock_account, exchange_type, init_date, fund_account, stock_account, exchange_type |
| idx_rpt_usms_bond_daily | ART | 是 | init_date, fund_account, stock_account, exchange_type, init_date, fund_account, stock_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usms_bond_daily | init_date, fund_account, stock_account, exchange_type, init_date, fund_account, stock_account, exchange_type |
| idx_usms_bond_daily | init_date, fund_account, stock_account, exchange_type, init_date, fund_account, stock_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-08 12:21:41 | 3.0.2.6 | 洪略 | 历史表索引增加rtp前缀 |
| 2025-11-07 13:38:21 | 3.0.2.4 | 洪略 | 增加历史表 |
| 2025-08-22 14:36:55 | 3.0.2.3 | 陆良铠 | 新建表结构 |
| 2025-12-08 12:21:41 | 3.0.2.6 | 洪略 | 历史表索引增加rtp前缀 |
| 2025-11-07 13:38:21 | 3.0.2.4 | 洪略 | 增加历史表 |
| 2025-08-22 14:36:55 | 3.0.2.3 | 陆良铠 | 新建表结构 |

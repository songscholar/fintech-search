# usms_fundpend_jour - 资金待扣收流水表

**表对象ID**: 2849
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 104 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | business_flag | 否 |  |  |
| 6 | operator_no | 否 |  |  |
| 7 | op_branch_no | 否 |  |  |
| 8 | op_entrust_way | 否 |  |  |
| 9 | branch_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | report_account | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | stock_type | 否 |  |  |
| 17 | stock_name | 否 |  |  |
| 18 | money_type | 否 |  |  |
| 19 | entrust_bs | 否 |  |  |
| 20 | seat_no | 否 |  |  |
| 21 | business_no | 否 |  |  |
| 22 | business_id | 否 |  |  |
| 23 | business_type | 否 |  |  |
| 24 | business_amount | 否 |  |  |
| 25 | business_price | 否 |  |  |
| 26 | total_pend_fare | 否 |  |  |
| 27 | pend_fare | 否 |  |  |
| 28 | entrust_no | 否 |  |  |
| 29 | deal_date | 否 |  |  |
| 30 | deal_time | 否 |  |  |
| 31 | deal_flag | 否 |  |  |
| 32 | join_position_str | 否 |  |  |
| 33 | remark | 否 |  |  |
| 34 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 35 | fundpend_type | 否 |  |  |
| 36 | fare0 | 否 |  |  |
| 37 | fare1 | 否 |  |  |
| 38 | fare2 | 否 |  |  |
| 39 | fare3 | 否 |  |  |
| 40 | farex | 否 |  |  |
| 41 | end_date | 否 |  |  |
| 42 | force_pendfare_flag | 否 |  |  |
| 43 | client_group | 否 | H |  |
| 44 | room_code | 否 | H |  |
| 45 | limit_flag | 否 | H |  |
| 46 | asset_prop | 否 | H |  |
| 47 | risk_level | 否 | H |  |
| 48 | corp_client_group | 否 | H |  |
| 49 | corp_risk_level | 否 | H |  |
| 50 | asset_level | 否 | H |  |
| 51 | client_name | 否 | H |  |
| 52 | sub_stock_type | 否 | H |  |
| 53 | init_date | 否 |  |  |
| 54 | serial_no | 否 |  |  |
| 55 | curr_date | 否 |  |  |
| 56 | curr_time | 否 |  |  |
| 57 | business_flag | 否 |  |  |
| 58 | operator_no | 否 |  |  |
| 59 | op_branch_no | 否 |  |  |
| 60 | op_entrust_way | 否 |  |  |
| 61 | branch_no | 否 |  |  |
| 62 | fund_account | 否 |  |  |
| 63 | client_id | 否 |  |  |
| 64 | exchange_type | 否 |  |  |
| 65 | stock_account | 否 |  |  |
| 66 | report_account | 否 |  |  |
| 67 | stock_code | 否 |  |  |
| 68 | stock_type | 否 |  |  |
| 69 | stock_name | 否 |  |  |
| 70 | money_type | 否 |  |  |
| 71 | entrust_bs | 否 |  |  |
| 72 | seat_no | 否 |  |  |
| 73 | business_no | 否 |  |  |
| 74 | business_id | 否 |  |  |
| 75 | business_type | 否 |  |  |
| 76 | business_amount | 否 |  |  |
| 77 | business_price | 否 |  |  |
| 78 | total_pend_fare | 否 |  |  |
| 79 | pend_fare | 否 |  |  |
| 80 | entrust_no | 否 |  |  |
| 81 | deal_date | 否 |  |  |
| 82 | deal_time | 否 |  |  |
| 83 | deal_flag | 否 |  |  |
| 84 | join_position_str | 否 |  |  |
| 85 | remark | 否 |  |  |
| 86 | position_str | 否 |  | init_date(8)+branch_no(5)+serial_no(10) |
| 87 | fundpend_type | 否 |  |  |
| 88 | fare0 | 否 |  |  |
| 89 | fare1 | 否 |  |  |
| 90 | fare2 | 否 |  |  |
| 91 | fare3 | 否 |  |  |
| 92 | farex | 否 |  |  |
| 93 | end_date | 否 |  |  |
| 94 | force_pendfare_flag | 否 |  |  |
| 95 | client_group | 否 | H |  |
| 96 | room_code | 否 | H |  |
| 97 | limit_flag | 否 | H |  |
| 98 | asset_prop | 否 | H |  |
| 99 | risk_level | 否 | H |  |
| 100 | corp_client_group | 否 | H |  |
| 101 | corp_risk_level | 否 | H |  |
| 102 | asset_level | 否 | H |  |
| 103 | client_name | 否 | H |  |
| 104 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_fundpend_jour | ART | 是 | position_str, position_str |
| idx_rpt_usms_fundpend_jour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_usms_fundpend_jour_acct | ART | 是 | fund_account, fund_account |
| idx_rpt_usms_fundpend_jour_serialno | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_rpt_usms_fundpend_jour_deal | ART | 是 | deal_date, deal_date |
| idx_usms_fundpend_jour | ART | 是 | position_str, position_str |
| idx_rpt_usms_fundpend_jour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_rpt_usms_fundpend_jour_acct | ART | 是 | fund_account, fund_account |
| idx_rpt_usms_fundpend_jour_serialno | ART | 是 | serial_no, init_date, serial_no, init_date |
| idx_rpt_usms_fundpend_jour_deal | ART | 是 | deal_date, deal_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usms_fundpend_jour | position_str, position_str |
| idx_usms_fundpend_jour | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-08 12:21:35 | 3.0.2.6 | 洪略 | 历史表索引增加rtp前缀 |
| 2025-11-29 12:09:04 | 3.0.2.4 | 洪略 | 历史表补充sub_stock_type |
| 2025-11-24 10:40:42 | 3.0.2.3 | 洪略 | 增加历史表 |
| 2025-08-14 10:03:33 | 3.0.2.2 | 高志强 | 增加DB模式,避免写表失败 |
| 2025-12-08 12:21:35 | 3.0.2.6 | 洪略 | 历史表索引增加rtp前缀 |
| 2025-11-29 12:09:04 | 3.0.2.4 | 洪略 | 历史表补充sub_stock_type |
| 2025-11-24 10:40:42 | 3.0.2.3 | 洪略 | 增加历史表 |
| 2025-08-14 10:03:33 | 3.0.2.2 | 高志强 | 增加DB模式,避免写表失败 |

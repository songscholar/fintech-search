# uref_borrow_uncompact - 转融通借入合约在途表

**表对象ID**: 6110
**所属模块**: reftrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 70 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | refcompact_type | 否 |  |  |
| 3 | compact_id | 否 |  |  |
| 4 | orig_compact_id | 否 |  |  |
| 5 | company_no | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | refsrcgroup_id | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_account | 否 |  |  |
| 12 | stock_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | ref_type | 否 |  |  |
| 15 | money_type | 否 |  |  |
| 16 | compact_balance | 否 |  |  |
| 17 | compact_amount | 否 |  |  |
| 18 | ref_term | 否 |  |  |
| 19 | refbase_rate | 否 |  |  |
| 20 | valid_date | 否 |  |  |
| 21 | date_clear | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | client_name | 否 | H |  |
| 25 | asset_prop | 否 | H |  |
| 26 | client_group | 否 | H |  |
| 27 | room_code | 否 | H |  |
| 28 | limit_flag | 否 | H |  |
| 29 | client_prop | 否 | H |  |
| 30 | stock_name | 否 | H |  |
| 31 | sub_stock_type | 否 | H |  |
| 32 | corp_client_group | 否 | H |  |
| 33 | asset_level | 否 | H |  |
| 34 | risk_level | 否 | H |  |
| 35 | corp_risk_level | 否 | H |  |
| 36 | init_date | 否 |  |  |
| 37 | refcompact_type | 否 |  |  |
| 38 | compact_id | 否 |  |  |
| 39 | orig_compact_id | 否 |  |  |
| 40 | company_no | 否 |  |  |
| 41 | branch_no | 否 |  |  |
| 42 | refsrcgroup_id | 否 |  |  |
| 43 | fund_account | 否 |  |  |
| 44 | client_id | 否 |  |  |
| 45 | exchange_type | 否 |  |  |
| 46 | stock_account | 否 |  |  |
| 47 | stock_type | 否 |  |  |
| 48 | stock_code | 否 |  |  |
| 49 | ref_type | 否 |  |  |
| 50 | money_type | 否 |  |  |
| 51 | compact_balance | 否 |  |  |
| 52 | compact_amount | 否 |  |  |
| 53 | ref_term | 否 |  |  |
| 54 | refbase_rate | 否 |  |  |
| 55 | valid_date | 否 |  |  |
| 56 | date_clear | 否 |  |  |
| 57 | remark | 否 |  |  |
| 58 | position_str | 否 |  |  |
| 59 | client_name | 否 | H |  |
| 60 | asset_prop | 否 | H |  |
| 61 | client_group | 否 | H |  |
| 62 | room_code | 否 | H |  |
| 63 | limit_flag | 否 | H |  |
| 64 | client_prop | 否 | H |  |
| 65 | stock_name | 否 | H |  |
| 66 | sub_stock_type | 否 | H |  |
| 67 | corp_client_group | 否 | H |  |
| 68 | asset_level | 否 | H |  |
| 69 | risk_level | 否 | H |  |
| 70 | corp_risk_level | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_unrefbcompact | ART | 是 | compact_id, compact_id |
| idx_unrefbcompact_stk | ART | 是 | stock_code, exchange_type, refsrcgroup_id, valid_date, stock_code, exchange_type, refsrcgroup_id, valid_date |
| idx_unrefbcompact_id | ART | 是 | orig_compact_id, orig_compact_id |
| idx_unrefbcompact | ART | 是 | compact_id, compact_id |
| idx_unrefbcompact_stk | ART | 是 | stock_code, exchange_type, refsrcgroup_id, valid_date, stock_code, exchange_type, refsrcgroup_id, valid_date |
| idx_unrefbcompact_id | ART | 是 | orig_compact_id, orig_compact_id |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_unrefbcompact | compact_id, compact_id |
| uk_rpt_urefborrowuncompact | init_date, position_str, init_date, position_str |
| idx_unrefbcompact | compact_id, compact_id |
| uk_rpt_urefborrowuncompact | init_date, position_str, init_date, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-12 15:54:27 | V3.0.2.6 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_borrow_uncompact，添加了表字段(corp_client_g... |
| 2025-10-16 10:41:57 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |
| 2025-12-12 15:54:27 | V3.0.2.6 | 廖宏玮 | 历史表(归档表)rpt_(fil_)uref_borrow_uncompact，添加了表字段(corp_client_g... |
| 2025-10-16 10:41:57 | V3.0.2.2 | 廖宏玮 | 增加历史表索引与字段 |

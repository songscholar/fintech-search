# income_price_info - 固收非公开报价行情信息表

**表对象ID**: 2466
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 74 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | income_busi_type | 否 |  |  |
| 3 | entrust_prop | 否 |  |  |
| 4 | exch_order_id | 否 |  |  |
| 5 | cbpconfer_id | 否 |  |  |
| 6 | incopriinfo_status | 否 |  |  |
| 7 | quotingparty_name | 否 |  |  |
| 8 | trader_id | 否 |  |  |
| 9 | entrust_bs | 否 |  |  |
| 10 | income_price | 否 |  |  |
| 11 | repo_term | 否 |  |  |
| 12 | settle_start_date | 否 |  |  |
| 13 | back_end_date | 否 |  |  |
| 14 | settle_due_date | 否 |  |  |
| 15 | preend_date | 否 |  |  |
| 16 | fund_used_days | 否 |  |  |
| 17 | old_business_date | 否 |  |  |
| 18 | orig_cbp_business_id | 否 |  |  |
| 19 | basket_str | 否 |  |  |
| 20 | stock_account | 否 |  |  |
| 21 | seat_no | 否 |  |  |
| 22 | account_name | 否 |  |  |
| 23 | invester_name | 否 |  |  |
| 24 | prop_account_name | 否 |  |  |
| 25 | prop_invester_name | 否 |  |  |
| 26 | pledgee_name | 否 |  |  |
| 27 | product_consigner | 否 |  |  |
| 28 | deal_balance | 否 |  |  |
| 29 | settle_balance | 否 |  |  |
| 30 | profit | 否 |  |  |
| 31 | current_assure_value | 否 |  |  |
| 32 | lever_limit | 否 |  |  |
| 33 | extend_str | 否 |  |  |
| 34 | remark | 否 |  |  |
| 35 | position_str | 否 |  | init_date(8)+entrust_prop(3)+cbpconfer_id(10)+entrust_bs(1) |
| 36 | income_update_type | 否 |  |  |
| 37 | oppo_trader_id | 否 |  | 合并申报时为中间方交易员，其余时为空 |
| 38 | init_date | 否 |  |  |
| 39 | income_busi_type | 否 |  |  |
| 40 | entrust_prop | 否 |  |  |
| 41 | exch_order_id | 否 |  |  |
| 42 | cbpconfer_id | 否 |  |  |
| 43 | incopriinfo_status | 否 |  |  |
| 44 | quotingparty_name | 否 |  |  |
| 45 | trader_id | 否 |  |  |
| 46 | entrust_bs | 否 |  |  |
| 47 | income_price | 否 |  |  |
| 48 | repo_term | 否 |  |  |
| 49 | settle_start_date | 否 |  |  |
| 50 | back_end_date | 否 |  |  |
| 51 | settle_due_date | 否 |  |  |
| 52 | preend_date | 否 |  |  |
| 53 | fund_used_days | 否 |  |  |
| 54 | old_business_date | 否 |  |  |
| 55 | orig_cbp_business_id | 否 |  |  |
| 56 | basket_str | 否 |  |  |
| 57 | stock_account | 否 |  |  |
| 58 | seat_no | 否 |  |  |
| 59 | account_name | 否 |  |  |
| 60 | invester_name | 否 |  |  |
| 61 | prop_account_name | 否 |  |  |
| 62 | prop_invester_name | 否 |  |  |
| 63 | pledgee_name | 否 |  |  |
| 64 | product_consigner | 否 |  |  |
| 65 | deal_balance | 否 |  |  |
| 66 | settle_balance | 否 |  |  |
| 67 | profit | 否 |  |  |
| 68 | current_assure_value | 否 |  |  |
| 69 | lever_limit | 否 |  |  |
| 70 | extend_str | 否 |  |  |
| 71 | remark | 否 |  |  |
| 72 | position_str | 否 |  | init_date(8)+entrust_prop(3)+cbpconfer_id(10)+entrust_bs(1) |
| 73 | income_update_type | 否 |  |  |
| 74 | oppo_trader_id | 否 |  | 合并申报时为中间方交易员，其余时为空 |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_incomepriinfo_id | ART | 是 | init_date, entrust_prop, cbpconfer_id, init_date, entrust_prop, cbpconfer_id |
| idx_incomepriinfo_pos | ART | 是 | position_str, position_str |
| idx_rpt_incomepriinfo_id | ART | 是 | init_date, entrust_prop, cbpconfer_id, init_date, entrust_prop, cbpconfer_id |
| idx_rpt_incomepriinfo_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_incomepriinfo_id | ART | 是 | init_date, entrust_prop, cbpconfer_id, init_date, entrust_prop, cbpconfer_id |
| idx_incomepriinfo_pos | ART | 是 | position_str, position_str |
| idx_rpt_incomepriinfo_id | ART | 是 | init_date, entrust_prop, cbpconfer_id, init_date, entrust_prop, cbpconfer_id |
| idx_rpt_incomepriinfo_pos | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_incomepriinfo_pos | position_str, position_str |
| idx_incomepriinfo_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-08 13:57:07 | 3.0.2.98 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-06 14:41:53 | 3.0.2.98 | 洪略 | 增加历史表 |
| 2025-04-09 09:57:05 | 3.0.2.82 | 钟兆星 | 新增固收非公开行情信息表income_price_info |
| 2025-12-08 13:57:07 | 3.0.2.98 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-06 14:41:53 | 3.0.2.98 | 洪略 | 增加历史表 |
| 2025-04-09 09:57:05 | 3.0.2.82 | 钟兆星 | 新增固收非公开行情信息表income_price_info |

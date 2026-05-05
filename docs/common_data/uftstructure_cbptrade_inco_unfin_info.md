# inco_unfin_info - 固收未结算信息表

**表对象ID**: 2353
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 88 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | income_busi_type | 否 |  |  |
| 3 | business_date | 否 |  |  |
| 4 | cbp_business_id | 否 |  |  |
| 5 | income_due_status | 否 |  |  |
| 6 | operation_status | 否 |  |  |
| 7 | entrust_bs | 否 |  |  |
| 8 | repo_rate | 否 |  |  |
| 9 | back_end_date | 否 |  |  |
| 10 | settle_due_date | 否 |  |  |
| 11 | repo_term | 否 |  |  |
| 12 | fund_used_days | 否 |  |  |
| 13 | deal_balance | 否 |  |  |
| 14 | settle_balance | 否 |  |  |
| 15 | profit | 否 |  |  |
| 16 | impawn_total_value | 否 |  |  |
| 17 | current_assure_value | 否 |  |  |
| 18 | agency_no | 否 |  |  |
| 19 | agency_name | 否 |  |  |
| 20 | trader_id | 否 |  |  |
| 21 | stock_account | 否 |  |  |
| 22 | seat_no | 否 |  |  |
| 23 | oppo_agency | 否 |  |  |
| 24 | oppo_agency_name | 否 |  |  |
| 25 | oppo_trader_id | 否 |  |  |
| 26 | prop_stock_account | 否 |  |  |
| 27 | prop_seat_no | 否 |  |  |
| 28 | pledgee_name | 否 |  |  |
| 29 | account_name | 否 |  |  |
| 30 | invester_name | 否 |  |  |
| 31 | product_consigner | 否 |  |  |
| 32 | lever_limit | 否 |  |  |
| 33 | prop_account_name | 否 |  |  |
| 34 | prop_invester_name | 否 |  |  |
| 35 | prop_product_consigner | 否 |  |  |
| 36 | prop_lever_limit | 否 |  |  |
| 37 | income_treatmode | 否 |  |  |
| 38 | settle_no | 否 |  |  |
| 39 | basket_str | 否 |  |  |
| 40 | remark | 否 |  |  |
| 41 | position_str | 否 |  | init_date(8)+business_date(8)+income_busi_type(8)+cbp_busine |
| 42 | stock_code | 否 |  |  |
| 43 | impawn_amount | 否 |  |  |
| 44 | funder_ratio | 否 |  |  |
| 45 | init_date | 否 |  |  |
| 46 | income_busi_type | 否 |  |  |
| 47 | business_date | 否 |  |  |
| 48 | cbp_business_id | 否 |  |  |
| 49 | income_due_status | 否 |  |  |
| 50 | operation_status | 否 |  |  |
| 51 | entrust_bs | 否 |  |  |
| 52 | repo_rate | 否 |  |  |
| 53 | back_end_date | 否 |  |  |
| 54 | settle_due_date | 否 |  |  |
| 55 | repo_term | 否 |  |  |
| 56 | fund_used_days | 否 |  |  |
| 57 | deal_balance | 否 |  |  |
| 58 | settle_balance | 否 |  |  |
| 59 | profit | 否 |  |  |
| 60 | impawn_total_value | 否 |  |  |
| 61 | current_assure_value | 否 |  |  |
| 62 | agency_no | 否 |  |  |
| 63 | agency_name | 否 |  |  |
| 64 | trader_id | 否 |  |  |
| 65 | stock_account | 否 |  |  |
| 66 | seat_no | 否 |  |  |
| 67 | oppo_agency | 否 |  |  |
| 68 | oppo_agency_name | 否 |  |  |
| 69 | oppo_trader_id | 否 |  |  |
| 70 | prop_stock_account | 否 |  |  |
| 71 | prop_seat_no | 否 |  |  |
| 72 | pledgee_name | 否 |  |  |
| 73 | account_name | 否 |  |  |
| 74 | invester_name | 否 |  |  |
| 75 | product_consigner | 否 |  |  |
| 76 | lever_limit | 否 |  |  |
| 77 | prop_account_name | 否 |  |  |
| 78 | prop_invester_name | 否 |  |  |
| 79 | prop_product_consigner | 否 |  |  |
| 80 | prop_lever_limit | 否 |  |  |
| 81 | income_treatmode | 否 |  |  |
| 82 | settle_no | 否 |  |  |
| 83 | basket_str | 否 |  |  |
| 84 | remark | 否 |  |  |
| 85 | position_str | 否 |  | init_date(8)+business_date(8)+income_busi_type(8)+cbp_busine |
| 86 | stock_code | 否 |  |  |
| 87 | impawn_amount | 否 |  |  |
| 88 | funder_ratio | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_incounfininfo_pos | 默认 | 否 |  |
| idx_incounfininfo_id | ART | 是 | init_date, business_date, income_busi_type, cbp_business_id, init_date, business_date, income_busi_type, cbp_business_id |
| idx_incounfininfo_pos | ART | 是 | position_str, position_str |
| uk_rpt_incounfininfo | ART | 是 | init_date, position_str, init_date, position_str |
| idx_incounfininfo_pos | 默认 | 否 |  |
| idx_incounfininfo_id | ART | 是 | init_date, business_date, income_busi_type, cbp_business_id, init_date, business_date, income_busi_type, cbp_business_id |
| idx_incounfininfo_pos | ART | 是 | position_str, position_str |
| uk_rpt_incounfininfo | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_incounfininfo_pos | position_str, position_str |
| idx_incounfininfo_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:37:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-23 16:42:40 | V3.0.2.1007 | 张明月 | 新增 |
| 2026-03-04 15:37:46 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-09-23 16:42:40 | V3.0.2.1007 | 张明月 | 新增 |

# stk_res_stock - 券源股份表

**表对象ID**: 2863
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 88 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stkres_id | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | stkres_prop | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | current_amount | 否 |  |  |
| 7 | used_amount | 否 |  |  |
| 8 | interest | 否 |  |  |
| 9 | dividend_balance | 否 |  |  |
| 10 | recoup_bonus_balance | 否 |  |  |
| 11 | recoup_alloted_balance | 否 |  |  |
| 12 | recoup_other_balance | 否 |  |  |
| 13 | return_balance | 否 |  |  |
| 14 | other_balance | 否 |  |  |
| 15 | cost_balance | 否 |  |  |
| 16 | sum_current_amount | 否 |  |  |
| 17 | sum_used_amount | 否 |  |  |
| 18 | return_date | 否 |  |  |
| 19 | priority_level | 否 |  |  |
| 20 | create_date | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | stkres_id | 否 |  |  |
| 24 | stock_account | 否 |  |  |
| 25 | stkres_prop | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | stock_code | 否 |  |  |
| 28 | current_amount | 否 |  |  |
| 29 | used_amount | 否 |  |  |
| 30 | interest | 否 |  |  |
| 31 | dividend_balance | 否 |  |  |
| 32 | recoup_bonus_balance | 否 |  |  |
| 33 | recoup_alloted_balance | 否 |  |  |
| 34 | recoup_other_balance | 否 |  |  |
| 35 | return_balance | 否 |  |  |
| 36 | other_balance | 否 |  |  |
| 37 | cost_balance | 否 |  |  |
| 38 | sum_current_amount | 否 |  |  |
| 39 | sum_used_amount | 否 |  |  |
| 40 | return_date | 否 |  |  |
| 41 | priority_level | 否 |  |  |
| 42 | create_date | 否 |  |  |
| 43 | remark | 否 |  |  |
| 44 | position_str | 否 |  |  |
| 45 | stkres_id | 否 |  |  |
| 46 | stock_account | 否 |  |  |
| 47 | stkres_prop | 否 |  |  |
| 48 | exchange_type | 否 |  |  |
| 49 | stock_code | 否 |  |  |
| 50 | current_amount | 否 |  |  |
| 51 | used_amount | 否 |  |  |
| 52 | interest | 否 |  |  |
| 53 | dividend_balance | 否 |  |  |
| 54 | recoup_bonus_balance | 否 |  |  |
| 55 | recoup_alloted_balance | 否 |  |  |
| 56 | recoup_other_balance | 否 |  |  |
| 57 | return_balance | 否 |  |  |
| 58 | other_balance | 否 |  |  |
| 59 | cost_balance | 否 |  |  |
| 60 | sum_current_amount | 否 |  |  |
| 61 | sum_used_amount | 否 |  |  |
| 62 | return_date | 否 |  |  |
| 63 | priority_level | 否 |  |  |
| 64 | create_date | 否 |  |  |
| 65 | remark | 否 |  |  |
| 66 | position_str | 否 |  |  |
| 67 | stkres_id | 否 |  |  |
| 68 | stock_account | 否 |  |  |
| 69 | stkres_prop | 否 |  |  |
| 70 | exchange_type | 否 |  |  |
| 71 | stock_code | 否 |  |  |
| 72 | current_amount | 否 |  |  |
| 73 | used_amount | 否 |  |  |
| 74 | interest | 否 |  |  |
| 75 | dividend_balance | 否 |  |  |
| 76 | recoup_bonus_balance | 否 |  |  |
| 77 | recoup_alloted_balance | 否 |  |  |
| 78 | recoup_other_balance | 否 |  |  |
| 79 | return_balance | 否 |  |  |
| 80 | other_balance | 否 |  |  |
| 81 | cost_balance | 否 |  |  |
| 82 | sum_current_amount | 否 |  |  |
| 83 | sum_used_amount | 否 |  |  |
| 84 | return_date | 否 |  |  |
| 85 | priority_level | 否 |  |  |
| 86 | create_date | 否 |  |  |
| 87 | remark | 否 |  |  |
| 88 | position_str | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stk_res_stock | ART | 是 | stkres_id, stkres_id |
| idx_stk_res_stock | ART | 是 | stkres_id, stkres_id |
| idx_stkresstock_pos | ART | 是 | position_str, position_str |
| idx_stk_res_stock | ART | 是 | stkres_id, stkres_id |
| idx_stk_res_stock | ART | 是 | stkres_id, stkres_id |
| idx_stkresstock_pos | ART | 是 | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-24 10:05:37 | 8.26.2.96 | 徐世晗 | 添加表 |
| 2026-02-24 10:05:37 | 8.26.2.96 | 徐世晗 |  |
| 2026-02-24 10:05:37 | 8.26.2.96 | 徐世晗 | 添加表 |
| 2026-02-24 10:05:37 | 8.26.2.96 | 徐世晗 |  |

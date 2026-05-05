# settredo_uref_stock - 清算重做保证金股份表

**表对象ID**: 6060
**所属模块**: refmargin
**数据空间**: HS_UFT_DATA

## 字段列表（共 60 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | begin_amount | 否 |  |  |
| 2 | current_amount | 否 |  |  |
| 3 | frozen_amount | 否 |  |  |
| 4 | unfrozen_amount | 否 |  |  |
| 5 | entrust_sell_amount | 否 |  |  |
| 6 | real_buy_amount | 否 |  |  |
| 7 | real_sell_amount | 否 |  |  |
| 8 | deposit_amount | 否 |  |  |
| 9 | fetch_amount | 否 |  |  |
| 10 | csfc_use_amount | 否 |  |  |
| 11 | enable_amount | 否 |  |  |
| 12 | correct_amount | 否 |  |  |
| 13 | position_str | 否 |  |  |
| 14 | sett_dml_type | 否 |  |  |
| 15 | sett_batch_no | 否 |  |  |
| 16 | begin_amount | 否 |  |  |
| 17 | current_amount | 否 |  |  |
| 18 | frozen_amount | 否 |  |  |
| 19 | unfrozen_amount | 否 |  |  |
| 20 | entrust_sell_amount | 否 |  |  |
| 21 | real_buy_amount | 否 |  |  |
| 22 | real_sell_amount | 否 |  |  |
| 23 | deposit_amount | 否 |  |  |
| 24 | fetch_amount | 否 |  |  |
| 25 | csfc_use_amount | 否 |  |  |
| 26 | enable_amount | 否 |  |  |
| 27 | correct_amount | 否 |  |  |
| 28 | position_str | 否 |  |  |
| 29 | sett_dml_type | 否 |  |  |
| 30 | sett_batch_no | 否 |  |  |
| 31 | begin_amount | 否 |  |  |
| 32 | current_amount | 否 |  |  |
| 33 | frozen_amount | 否 |  |  |
| 34 | unfrozen_amount | 否 |  |  |
| 35 | entrust_sell_amount | 否 |  |  |
| 36 | real_buy_amount | 否 |  |  |
| 37 | real_sell_amount | 否 |  |  |
| 38 | deposit_amount | 否 |  |  |
| 39 | fetch_amount | 否 |  |  |
| 40 | csfc_use_amount | 否 |  |  |
| 41 | enable_amount | 否 |  |  |
| 42 | correct_amount | 否 |  |  |
| 43 | position_str | 否 |  |  |
| 44 | sett_dml_type | 否 |  |  |
| 45 | sett_batch_no | 否 |  |  |
| 46 | begin_amount | 否 |  |  |
| 47 | current_amount | 否 |  |  |
| 48 | frozen_amount | 否 |  |  |
| 49 | unfrozen_amount | 否 |  |  |
| 50 | entrust_sell_amount | 否 |  |  |
| 51 | real_buy_amount | 否 |  |  |
| 52 | real_sell_amount | 否 |  |  |
| 53 | deposit_amount | 否 |  |  |
| 54 | fetch_amount | 否 |  |  |
| 55 | csfc_use_amount | 否 |  |  |
| 56 | enable_amount | 否 |  |  |
| 57 | correct_amount | 否 |  |  |
| 58 | position_str | 否 |  |  |
| 59 | sett_dml_type | 否 |  |  |
| 60 | sett_batch_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_refstock | 默认 | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_refstock | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_refstock | 默认 | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_refstock | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_refstock | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_refstock | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-20 09:11:21 | V3.0.2.1 | 廖宏玮 | 添加表 |
| 2025-08-20 09:11:21 | V8.0.2.1 |  |  |
| 2025-08-20 09:11:21 | V3.0.2.1 | 廖宏玮 | 添加表 |
| 2025-08-20 09:11:21 | V8.0.2.1 |  |  |

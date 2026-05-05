# settredo_uref_fund - 清算重做保证金资金表

**表对象ID**: 6059
**所属模块**: refmargin
**数据空间**: HS_UFT_DATA

## 字段列表（共 72 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | begin_balance | 否 |  |  |
| 2 | current_balance | 否 |  |  |
| 3 | frozen_balance | 否 |  |  |
| 4 | unfrozen_balance | 否 |  |  |
| 5 | entrust_buy_balance | 否 |  |  |
| 6 | real_buy_balance | 否 |  |  |
| 7 | real_sell_balance | 否 |  |  |
| 8 | deposit_balance | 否 |  |  |
| 9 | fetch_balance | 否 |  |  |
| 10 | csfc_use_balance | 否 |  |  |
| 11 | enable_balance | 否 |  |  |
| 12 | correct_balance | 否 |  |  |
| 13 | integral_balance | 否 |  |  |
| 14 | interest | 否 |  |  |
| 15 | integral_update | 否 |  |  |
| 16 | position_str | 否 |  |  |
| 17 | sett_dml_type | 否 |  |  |
| 18 | sett_batch_no | 否 |  |  |
| 19 | begin_balance | 否 |  |  |
| 20 | current_balance | 否 |  |  |
| 21 | frozen_balance | 否 |  |  |
| 22 | unfrozen_balance | 否 |  |  |
| 23 | entrust_buy_balance | 否 |  |  |
| 24 | real_buy_balance | 否 |  |  |
| 25 | real_sell_balance | 否 |  |  |
| 26 | deposit_balance | 否 |  |  |
| 27 | fetch_balance | 否 |  |  |
| 28 | csfc_use_balance | 否 |  |  |
| 29 | enable_balance | 否 |  |  |
| 30 | correct_balance | 否 |  |  |
| 31 | integral_balance | 否 |  |  |
| 32 | interest | 否 |  |  |
| 33 | integral_update | 否 |  |  |
| 34 | position_str | 否 |  |  |
| 35 | sett_dml_type | 否 |  |  |
| 36 | sett_batch_no | 否 |  |  |
| 37 | begin_balance | 否 |  |  |
| 38 | current_balance | 否 |  |  |
| 39 | frozen_balance | 否 |  |  |
| 40 | unfrozen_balance | 否 |  |  |
| 41 | entrust_buy_balance | 否 |  |  |
| 42 | real_buy_balance | 否 |  |  |
| 43 | real_sell_balance | 否 |  |  |
| 44 | deposit_balance | 否 |  |  |
| 45 | fetch_balance | 否 |  |  |
| 46 | csfc_use_balance | 否 |  |  |
| 47 | enable_balance | 否 |  |  |
| 48 | correct_balance | 否 |  |  |
| 49 | integral_balance | 否 |  |  |
| 50 | interest | 否 |  |  |
| 51 | integral_update | 否 |  |  |
| 52 | position_str | 否 |  |  |
| 53 | sett_dml_type | 否 |  |  |
| 54 | sett_batch_no | 否 |  |  |
| 55 | begin_balance | 否 |  |  |
| 56 | current_balance | 否 |  |  |
| 57 | frozen_balance | 否 |  |  |
| 58 | unfrozen_balance | 否 |  |  |
| 59 | entrust_buy_balance | 否 |  |  |
| 60 | real_buy_balance | 否 |  |  |
| 61 | real_sell_balance | 否 |  |  |
| 62 | deposit_balance | 否 |  |  |
| 63 | fetch_balance | 否 |  |  |
| 64 | csfc_use_balance | 否 |  |  |
| 65 | enable_balance | 否 |  |  |
| 66 | correct_balance | 否 |  |  |
| 67 | integral_balance | 否 |  |  |
| 68 | interest | 否 |  |  |
| 69 | integral_update | 否 |  |  |
| 70 | position_str | 否 |  |  |
| 71 | sett_dml_type | 否 |  |  |
| 72 | sett_batch_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settrode_reffund | 默认 | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_reffund | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settrode_reffund | 默认 | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_reffund | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_reffund | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_reffund | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-20 09:10:48 | V3.0.2.1 | 廖宏玮 | 添加表 |
| 2025-08-20 09:10:48 | V8.0.2.1 |  |  |
| 2025-08-20 09:10:48 | V3.0.2.1 | 廖宏玮 | 添加表 |
| 2025-08-20 09:10:48 | V8.0.2.1 |  |  |

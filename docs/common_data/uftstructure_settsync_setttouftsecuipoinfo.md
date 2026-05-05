# setttouftsecuipoinfo - 清算证券新股申购信息表

**表对象ID**: 3025
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | sett_id | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | client_id | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | asset_prop | 是 |  |  |
| 8 | stock_account | 是 |  |  |
| 9 | stock_code | 是 |  |  |
| 10 | stock_type | 是 |  |  |
| 11 | order_no | 是 |  |  |
| 12 | ipo_lucky_amount | 是 |  |  |
| 13 | lucky_balance | 是 |  |  |
| 14 | ipo_accancel_amount | 是 |  |  |
| 15 | ipo_pacancel_amount | 是 |  |  |
| 16 | ipo_short_balance | 是 |  |  |
| 17 | unfrozen_balance | 是 |  |  |
| 18 | ipo_info_status | 是 |  |  |
| 19 | ipo_report_flag | 是 |  |  |
| 20 | date_clear | 是 |  |  |
| 21 | remark | 是 |  |  |
| 22 | position_str | 是 |  |  |
| 23 | total_temp_balance | 是 |  | 冗余字段 |
| 24 | uft_data_change_status | 是 |  |  |
| 25 | frozen_balance | 是 |  |  |
| 26 | entrust_date | 是 |  |  |
| 27 | entrust_no | 是 |  |  |
| 28 | frozen_balance_t1 | 是 |  |  |
| 29 | init_date | 是 |  |  |
| 30 | sett_id | 是 |  |  |
| 31 | exchange_type | 是 |  |  |
| 32 | branch_no | 是 |  |  |
| 33 | client_id | 是 |  |  |
| 34 | fund_account | 是 |  |  |
| 35 | asset_prop | 是 |  |  |
| 36 | stock_account | 是 |  |  |
| 37 | stock_code | 是 |  |  |
| 38 | stock_type | 是 |  |  |
| 39 | order_no | 是 |  |  |
| 40 | ipo_lucky_amount | 是 |  |  |
| 41 | lucky_balance | 是 |  |  |
| 42 | ipo_accancel_amount | 是 |  |  |
| 43 | ipo_pacancel_amount | 是 |  |  |
| 44 | ipo_short_balance | 是 |  |  |
| 45 | unfrozen_balance | 是 |  |  |
| 46 | ipo_info_status | 是 |  |  |
| 47 | ipo_report_flag | 是 |  |  |
| 48 | date_clear | 是 |  |  |
| 49 | remark | 是 |  |  |
| 50 | position_str | 是 |  |  |
| 51 | total_temp_balance | 是 |  | 冗余字段 |
| 52 | uft_data_change_status | 是 |  |  |
| 53 | frozen_balance | 是 |  |  |
| 54 | entrust_date | 是 |  |  |
| 55 | entrust_no | 是 |  |  |
| 56 | frozen_balance_t1 | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settsecuipoinfo_pos | 默认 | 是 | position_str, position_str |
| idx_settsecuipoinfo_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settsecuipoinfo_pos | position_str, position_str |
| idx_settsecuipoinfo_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-03-31 14:36 | 8.26.1.116 | 罗佳楠 | 增加字段frozen_balance_t1 |
| 2021-03-04 10:29 | 8.26.1.113 | 罗佳楠 | 增加字段entrust_date和entrust_no |
| 2018-08-31 09:25 | 8.26.1.42 | 王天成 | 增加字段frozen_balance,删除含lucky_balance的索引 |
| 2021-03-31 14:36 | 8.26.1.116 | 罗佳楠 | 增加字段frozen_balance_t1 |
| 2021-03-04 10:29 | 8.26.1.113 | 罗佳楠 | 增加字段entrust_date和entrust_no |
| 2018-08-31 09:25 | 8.26.1.42 | 王天成 | 增加字段frozen_balance,删除含lucky_balance的索引 |

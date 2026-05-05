# setttouftsoptreg - 清算自主行权股东名册表

**表对象ID**: 3086
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_account | 是 |  |  |
| 3 | holder_name | 是 |  |  |
| 4 | id_kind | 是 |  |  |
| 5 | id_no | 是 |  |  |
| 6 | sopt_code | 是 |  |  |
| 7 | register_amount | 是 |  |  |
| 8 | confirm_amount | 是 |  |  |
| 9 | used_amount | 是 |  |  |
| 10 | frozen_amount | 是 |  |  |
| 11 | sopttax_kind | 是 |  |  |
| 12 | seat_no | 是 |  |  |
| 13 | executives_flag | 是 |  |  |
| 14 | limitsell_days | 是 |  |  |
| 15 | soptmatch_flag | 是 |  |  |
| 16 | soptreg_status | 是 |  |  |
| 17 | tax_months | 是 |  |  |
| 18 | sum_payable_tax | 是 |  |  |
| 19 | sum_paid_tax | 是 |  |  |
| 20 | draw_tax | 是 |  |  |
| 21 | position_str | 是 |  |  |
| 22 | execv_lock_ratio | 是 |  |  |
| 23 | uft_data_change_status | 是 |  |  |
| 24 | exchange_type | 是 |  |  |
| 25 | stock_account | 是 |  |  |
| 26 | holder_name | 是 |  |  |
| 27 | id_kind | 是 |  |  |
| 28 | id_no | 是 |  |  |
| 29 | sopt_code | 是 |  |  |
| 30 | register_amount | 是 |  |  |
| 31 | confirm_amount | 是 |  |  |
| 32 | used_amount | 是 |  |  |
| 33 | frozen_amount | 是 |  |  |
| 34 | sopttax_kind | 是 |  |  |
| 35 | seat_no | 是 |  |  |
| 36 | executives_flag | 是 |  |  |
| 37 | limitsell_days | 是 |  |  |
| 38 | soptmatch_flag | 是 |  |  |
| 39 | soptreg_status | 是 |  |  |
| 40 | tax_months | 是 |  |  |
| 41 | sum_payable_tax | 是 |  |  |
| 42 | sum_paid_tax | 是 |  |  |
| 43 | draw_tax | 是 |  |  |
| 44 | position_str | 是 |  |  |
| 45 | execv_lock_ratio | 是 |  |  |
| 46 | uft_data_change_status | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settsoptregtotal | 默认 | 是 | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_settsoptregtotal | 默认 | 是 | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settsoptregtotal | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |
| idx_settsoptregtotal | stock_account, sopt_code, exchange_type, stock_account, sopt_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-07-06 16:57 | 8.26.2.1 | 徐开 | 新增股东名册汇总表 |
| 2021-07-06 16:57 | 8.26.2.1 | 徐开 | 新增股东名册汇总表 |

# uft_qms_szreduction - UFT深圳减持信息表

**表对象ID**: 1650
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 66 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | trustee_seat_no | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | stock_total_amount | 否 |  |  |
| 7 | frozen_amount | 否 |  |  |
| 8 | stock_amount1 | 否 |  |  |
| 9 | stock_amount2 | 否 |  |  |
| 10 | stock_amount3 | 否 |  |  |
| 11 | stock_amount4 | 否 |  |  |
| 12 | stock_amount5 | 否 |  |  |
| 13 | stock_amount6 | 否 |  |  |
| 14 | stock_amount1_ex | 否 |  |  |
| 15 | stock_amount2_ex | 否 |  |  |
| 16 | stock_amount3_ex | 否 |  |  |
| 17 | stock_amount4_ex | 否 |  |  |
| 18 | begin_enable_quota | 否 |  |  |
| 19 | block_enable_quota | 否 |  |  |
| 20 | block_enable_quota1 | 否 |  |  |
| 21 | pre_used_quota | 否 |  |  |
| 22 | preblock_used_quota | 否 |  |  |
| 23 | prereduce_used_quota | 否 |  |  |
| 24 | used_quota | 否 |  |  |
| 25 | block_used_quota | 否 |  |  |
| 26 | reduce_used_quota | 否 |  |  |
| 27 | remark | 否 |  |  |
| 28 | company_no | 否 |  |  |
| 29 | stock_amount3_t | 否 |  |  |
| 30 | position_str | 否 |  | init_date(8)+company_no(4)+seat_no(6)+exchange_type(4)+stock |
| 31 | modify_date | 否 |  |  |
| 32 | order_no | 否 |  |  |
| 33 | acode_account | 否 |  |  |
| 34 | init_date | 否 |  |  |
| 35 | exchange_type | 否 |  |  |
| 36 | stock_account | 否 |  |  |
| 37 | trustee_seat_no | 否 |  |  |
| 38 | stock_code | 否 |  |  |
| 39 | stock_total_amount | 否 |  |  |
| 40 | frozen_amount | 否 |  |  |
| 41 | stock_amount1 | 否 |  |  |
| 42 | stock_amount2 | 否 |  |  |
| 43 | stock_amount3 | 否 |  |  |
| 44 | stock_amount4 | 否 |  |  |
| 45 | stock_amount5 | 否 |  |  |
| 46 | stock_amount6 | 否 |  |  |
| 47 | stock_amount1_ex | 否 |  |  |
| 48 | stock_amount2_ex | 否 |  |  |
| 49 | stock_amount3_ex | 否 |  |  |
| 50 | stock_amount4_ex | 否 |  |  |
| 51 | begin_enable_quota | 否 |  |  |
| 52 | block_enable_quota | 否 |  |  |
| 53 | block_enable_quota1 | 否 |  |  |
| 54 | pre_used_quota | 否 |  |  |
| 55 | preblock_used_quota | 否 |  |  |
| 56 | prereduce_used_quota | 否 |  |  |
| 57 | used_quota | 否 |  |  |
| 58 | block_used_quota | 否 |  |  |
| 59 | reduce_used_quota | 否 |  |  |
| 60 | remark | 否 |  |  |
| 61 | company_no | 否 |  |  |
| 62 | stock_amount3_t | 否 |  |  |
| 63 | position_str | 否 |  | init_date(8)+company_no(4)+seat_no(6)+exchange_type(4)+stock |
| 64 | modify_date | 否 |  |  |
| 65 | order_no | 否 |  |  |
| 66 | acode_account | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uft_qms_szreduction | 默认 | 否 |  |
| uk_uft_qms_szreduction | ART | 是 | stock_account, stock_code, trustee_seat_no, exchange_type, company_no, stock_account, stock_code, trustee_seat_no, exchange_type, company_no |
| uk_uft_qms_szreduction | 默认 | 否 |  |
| uk_uft_qms_szreduction | ART | 是 | stock_account, stock_code, trustee_seat_no, exchange_type, company_no, stock_account, stock_code, trustee_seat_no, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_uft_qms_szreduction | stock_account, stock_code, trustee_seat_no, exchange_type, company_no, stock_account, stock_code, trustee_seat_no, exchange_type, company_no |
| uk_uft_qms_szreduction | stock_account, stock_code, trustee_seat_no, exchange_type, company_no, stock_account, stock_code, trustee_seat_no, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:48:40 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:50:57 | 3.0.2.14 | taocong45644 | 当前表uft_qms_szreduction，修改了索引uk_uft_qms_szreduction,索引字段修改为：(... |
| 2025-03-22 18:23:04 | 3.0.2.2002 | 高志强 | 调整对象号避免和feature_ses分支冲突 |
| 2025-03-11 11:09:11 | 3.0.2.2001 | 杨新照 | 新增表结构 |
| 2026-03-05 16:48:40 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:50:57 | 3.0.2.14 | taocong45644 | 当前表uft_qms_szreduction，修改了索引uk_uft_qms_szreduction,索引字段修改为：(... |
| 2025-03-22 18:23:04 | 3.0.2.2002 | 高志强 | 调整对象号避免和feature_ses分支冲突 |
| 2025-03-11 11:09:11 | 3.0.2.2001 | 杨新照 | 新增表结构 |

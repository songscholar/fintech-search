# uft_qms_shreduction - UFT上海减持信息表

**表对象ID**: 1651
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 56 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | seat_no | 否 |  |  |
| 6 | cognizancestock_amount1 | 否 |  |  |
| 7 | cognizancestock_amount2 | 否 |  |  |
| 8 | reducectrl_amount | 否 |  |  |
| 9 | blockreducectrl_amount | 否 |  |  |
| 10 | surplusstock_amount | 否 |  |  |
| 11 | blockrecectrl_amount | 否 |  |  |
| 12 | frozen_amount | 否 |  |  |
| 13 | begin_enable_quota | 否 |  |  |
| 14 | block_enable_quota | 否 |  |  |
| 15 | pre_used_quota | 否 |  |  |
| 16 | prereduce_used_quota | 否 |  |  |
| 17 | used_quota | 否 |  |  |
| 18 | reduce_used_quota | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | company_no | 否 |  |  |
| 21 | block_enable_quota1 | 否 |  |  |
| 22 | preblock_used_quota | 否 |  |  |
| 23 | block_used_quota | 否 |  |  |
| 24 | stock_circulate_amount | 否 |  |  |
| 25 | position_str | 否 |  | init_date(8)+company_no(4)+seat_no(6)+exchange_type(4)+stock |
| 26 | modify_date | 否 |  |  |
| 27 | order_no | 否 |  |  |
| 28 | acode_account | 否 |  |  |
| 29 | init_date | 否 |  |  |
| 30 | exchange_type | 否 |  |  |
| 31 | stock_account | 否 |  |  |
| 32 | stock_code | 否 |  |  |
| 33 | seat_no | 否 |  |  |
| 34 | cognizancestock_amount1 | 否 |  |  |
| 35 | cognizancestock_amount2 | 否 |  |  |
| 36 | reducectrl_amount | 否 |  |  |
| 37 | blockreducectrl_amount | 否 |  |  |
| 38 | surplusstock_amount | 否 |  |  |
| 39 | blockrecectrl_amount | 否 |  |  |
| 40 | frozen_amount | 否 |  |  |
| 41 | begin_enable_quota | 否 |  |  |
| 42 | block_enable_quota | 否 |  |  |
| 43 | pre_used_quota | 否 |  |  |
| 44 | prereduce_used_quota | 否 |  |  |
| 45 | used_quota | 否 |  |  |
| 46 | reduce_used_quota | 否 |  |  |
| 47 | remark | 否 |  |  |
| 48 | company_no | 否 |  |  |
| 49 | block_enable_quota1 | 否 |  |  |
| 50 | preblock_used_quota | 否 |  |  |
| 51 | block_used_quota | 否 |  |  |
| 52 | stock_circulate_amount | 否 |  |  |
| 53 | position_str | 否 |  | init_date(8)+company_no(4)+seat_no(6)+exchange_type(4)+stock |
| 54 | modify_date | 否 |  |  |
| 55 | order_no | 否 |  |  |
| 56 | acode_account | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uft_qms_shreduction | 默认 | 否 |  |
| uk_uft_qms_shreduction | ART | 是 | stock_account, stock_code, exchange_type, company_no, seat_no, stock_account, stock_code, exchange_type, company_no, seat_no |
| uk_uft_qms_shreduction | 默认 | 否 |  |
| uk_uft_qms_shreduction | ART | 是 | stock_account, stock_code, exchange_type, company_no, seat_no, stock_account, stock_code, exchange_type, company_no, seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_uft_qms_shreduction | stock_account, stock_code, exchange_type, company_no, seat_no, stock_account, stock_code, exchange_type, company_no, seat_no |
| uk_uft_qms_shreduction | stock_account, stock_code, exchange_type, company_no, seat_no, stock_account, stock_code, exchange_type, company_no, seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:49:11 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:49:21 | 3.0.2.14 | taocong45644 | 当前表uft_qms_shreduction，修改了索引uk_uft_qms_shreduction,索引字段修改为：(... |
| 2025-03-22 18:23:04 | 3.0.2.2002 | 高志强 | 调整对象号避免和feature_ses分支冲突 |
| 2025-03-11 11:09:37 | 3.0.2.2001 | 杨新照 | 新增表结构 |
| 2026-03-05 16:49:11 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 15:49:21 | 3.0.2.14 | taocong45644 | 当前表uft_qms_shreduction，修改了索引uk_uft_qms_shreduction,索引字段修改为：(... |
| 2025-03-22 18:23:04 | 3.0.2.2002 | 高志强 | 调整对象号避免和feature_ses分支冲突 |
| 2025-03-11 11:09:37 | 3.0.2.2001 | 杨新照 | 新增表结构 |

# ucrt_acct_assure_code - 个人担保证券信息表

**表对象ID**: 7021
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 68 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | float_ratio | 否 |  |  |
| 7 | fair_price_flag | 否 |  |  |
| 8 | fair_price | 否 |  |  |
| 9 | end_date | 否 |  |  |
| 10 | assure_status | 否 |  |  |
| 11 | fair_ratio | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | registration_flag | 否 |  |  |
| 14 | active_flag | 否 |  |  |
| 15 | branch_no | 否 |  |  |
| 16 | dyna_fair_price_flag | 否 |  |  |
| 17 | upper_assure_hold_amount | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_code(8)+stock_type(4 |
| 22 | tohis_date | 否 | H |  |
| 23 | client_name | 否 | H |  |
| 24 | corp_client_group | 否 | H |  |
| 25 | client_group | 否 | H |  |
| 26 | room_code | 否 | H |  |
| 27 | asset_prop | 否 | H |  |
| 28 | limit_flag | 否 | H |  |
| 29 | client_prop | 否 | H |  |
| 30 | asset_level | 否 | H |  |
| 31 | risk_level | 否 | H |  |
| 32 | corp_risk_level | 否 | H |  |
| 33 | stock_name | 否 | H |  |
| 34 | sub_stock_type | 否 | H |  |
| 35 | client_id | 否 |  |  |
| 36 | fund_account | 否 |  |  |
| 37 | exchange_type | 否 |  |  |
| 38 | stock_code | 否 |  |  |
| 39 | stock_type | 否 |  |  |
| 40 | float_ratio | 否 |  |  |
| 41 | fair_price_flag | 否 |  |  |
| 42 | fair_price | 否 |  |  |
| 43 | end_date | 否 |  |  |
| 44 | assure_status | 否 |  |  |
| 45 | fair_ratio | 否 |  |  |
| 46 | transaction_no | 否 |  |  |
| 47 | registration_flag | 否 |  |  |
| 48 | active_flag | 否 |  |  |
| 49 | branch_no | 否 |  |  |
| 50 | dyna_fair_price_flag | 否 |  |  |
| 51 | upper_assure_hold_amount | 否 |  |  |
| 52 | remark | 否 |  |  |
| 53 | update_date | 否 |  |  |
| 54 | update_time | 否 |  |  |
| 55 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_code(8)+stock_type(4 |
| 56 | tohis_date | 否 | H |  |
| 57 | client_name | 否 | H |  |
| 58 | corp_client_group | 否 | H |  |
| 59 | client_group | 否 | H |  |
| 60 | room_code | 否 | H |  |
| 61 | asset_prop | 否 | H |  |
| 62 | limit_flag | 否 | H |  |
| 63 | client_prop | 否 | H |  |
| 64 | asset_level | 否 | H |  |
| 65 | risk_level | 否 | H |  |
| 66 | corp_risk_level | 否 | H |  |
| 67 | stock_name | 否 | H |  |
| 68 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_acct_assure_code_uk | 默认 | 否 | registration_flag, registration_flag |
| idx_ucrt_acct_assure_code | ART | 是 | fund_account, stock_code, exchange_type, stock_type, registration_flag, fund_account, stock_code, exchange_type, stock_type, registration_flag |
| idx_ucrt_acct_assure_code_uk | ART | 是 | fund_account, exchange_type, stock_code, stock_type, registration_flag, fund_account, exchange_type, stock_code, stock_type, registration_flag |
| idx_rpt_ucrt_acct_assure_code | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_ucrt_acct_assure_code_uk | 默认 | 否 | registration_flag, registration_flag |
| idx_ucrt_acct_assure_code | ART | 是 | fund_account, stock_code, exchange_type, stock_type, registration_flag, fund_account, stock_code, exchange_type, stock_type, registration_flag |
| idx_ucrt_acct_assure_code_uk | ART | 是 | fund_account, exchange_type, stock_code, stock_type, registration_flag, fund_account, exchange_type, stock_code, stock_type, registration_flag |
| idx_rpt_ucrt_acct_assure_code | ART | 是 | tohis_date, position_str, tohis_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_acct_assure_code_uk | fund_account, exchange_type, stock_code, stock_type, registration_flag, fund_account, exchange_type, stock_code, stock_type, registration_flag |
| idx_ucrt_acct_assure_code_uk | fund_account, exchange_type, stock_code, stock_type, registration_flag, fund_account, exchange_type, stock_code, stock_type, registration_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-04 16:57:10 | V3.0.2.21 | 蒋浩宇 | 所有表ucrt_acct_assure_code，添加了表字段(upper_assure_hold_amount);
 |
| 2025-11-21 15:33:57 | 3.0.6.1068 | 袁文龙 | 所有表ucrt_acct_assure_code，添加了表字段(branch_no);
所有表ucrt_acct_as... |
| 2025-02-06 09:33:35 | 3.0.6.34 | 沈勋 | 物理表ucrt_acct_assure_code，删除了表字段(float_flag);
 |
| 2025-02-06 09:32:59 | 3.0.6.34 | 沈勋 | 物理表ucrt_acct_assure_code，添加了表字段(active_flag);
 |
| 2024-06-15 10:46:05 | 3.0.2.17 | 楼欣欣 | 物理表ucrt_acct_assure_code，增加索引字段(索引idx_ucrt_acct_assure_code_... |
| 2024-06-15 10:45:07 | 3.0.2.17 | 楼欣欣 | 物理表ucrt_acct_assure_code，添加了表字段(registration_flag);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 在索引idx_ucrt_acct_assure_code_uk中增加stock_type字段 |
| 2023-06-21 14:22 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2026-01-04 16:57:10 | V3.0.2.21 | 蒋浩宇 | 所有表ucrt_acct_assure_code，添加了表字段(upper_assure_hold_amount);
 |
| 2025-11-21 15:33:57 | 3.0.6.1068 | 袁文龙 | 所有表ucrt_acct_assure_code，添加了表字段(branch_no);
所有表ucrt_acct_as... |
| 2025-02-06 09:33:35 | 3.0.6.34 | 沈勋 | 物理表ucrt_acct_assure_code，删除了表字段(float_flag);
 |
| 2025-02-06 09:32:59 | 3.0.6.34 | 沈勋 | 物理表ucrt_acct_assure_code，添加了表字段(active_flag);
 |
| 2024-06-15 10:46:05 | 3.0.2.17 | 楼欣欣 | 物理表ucrt_acct_assure_code，增加索引字段(索引idx_ucrt_acct_assure_code_... |
| 2024-06-15 10:45:07 | 3.0.2.17 | 楼欣欣 | 物理表ucrt_acct_assure_code，添加了表字段(registration_flag);
 |

> 共 18 条修改记录，仅显示最近15条

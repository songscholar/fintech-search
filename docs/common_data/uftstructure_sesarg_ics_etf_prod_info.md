# ics_etf_prod_info - ETF产品信息表

**表对象ID**: 5010
**所属模块**: sesarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | stock_name | 否 |  |  |
| 4 | ics_etfcode_type | 否 |  |  |
| 5 | stock_code_0 | 否 |  |  |
| 6 | stock_code_2 | 否 |  |  |
| 7 | stock_code_3 | 否 |  |  |
| 8 | stock_code_5 | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | ics_replenish_seat_no | 否 |  |  |
| 11 | ics_repl_enable_mode | 否 |  |  |
| 12 | ics_stock_enable_mode | 否 |  |  |
| 13 | settle_account_fund | 否 |  |  |
| 14 | firm_id | 否 |  |  |
| 15 | ics_hkreplenish_seat_no | 否 |  |  |
| 16 | settle_style | 否 |  |  |
| 17 | ics_local_replenish_seat_no | 否 |  |  |
| 18 | channel_type | 否 |  |  |
| 19 | ics_bjreplenish_seat_no | 否 |  |  |
| 20 | dsfsettle_way | 否 |  |  |
| 21 | appredeem_type | 否 |  |  |
| 22 | estimated_cash_mode | 否 |  |  |
| 23 | redem_risk_rate | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | exchange_type(4)+stock_code(8)+channel_type(1) |
| 27 | transaction_no | 否 |  |  |
| 28 | exchange_type | 否 |  |  |
| 29 | stock_code | 否 |  |  |
| 30 | stock_name | 否 |  |  |
| 31 | ics_etfcode_type | 否 |  |  |
| 32 | stock_code_0 | 否 |  |  |
| 33 | stock_code_2 | 否 |  |  |
| 34 | stock_code_3 | 否 |  |  |
| 35 | stock_code_5 | 否 |  |  |
| 36 | fund_account | 否 |  |  |
| 37 | ics_replenish_seat_no | 否 |  |  |
| 38 | ics_repl_enable_mode | 否 |  |  |
| 39 | ics_stock_enable_mode | 否 |  |  |
| 40 | settle_account_fund | 否 |  |  |
| 41 | firm_id | 否 |  |  |
| 42 | ics_hkreplenish_seat_no | 否 |  |  |
| 43 | settle_style | 否 |  |  |
| 44 | ics_local_replenish_seat_no | 否 |  |  |
| 45 | channel_type | 否 |  |  |
| 46 | ics_bjreplenish_seat_no | 否 |  |  |
| 47 | dsfsettle_way | 否 |  |  |
| 48 | appredeem_type | 否 |  |  |
| 49 | estimated_cash_mode | 否 |  |  |
| 50 | redem_risk_rate | 否 |  |  |
| 51 | update_date | 否 |  |  |
| 52 | update_time | 否 |  |  |
| 53 | position_str | 否 |  | exchange_type(4)+stock_code(8)+channel_type(1) |
| 54 | transaction_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_icsetfprodinfo_acct | 默认 | 否 | fund_account, fund_account |
| idx_icsetfprodinfo | ART | 是 | exchange_type, stock_code, channel_type, exchange_type, stock_code, channel_type |
| idx_icsetfprodinfo_acct | ART | 是 | fund_account, fund_account |
| idx_icsetfprodinfo_acct | 默认 | 否 | fund_account, fund_account |
| idx_icsetfprodinfo | ART | 是 | exchange_type, stock_code, channel_type, exchange_type, stock_code, channel_type |
| idx_icsetfprodinfo_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_icsetfprodinfo | exchange_type, stock_code, channel_type, exchange_type, stock_code, channel_type |
| idx_icsetfprodinfo_acct | fund_account, fund_account |
| idx_icsetfprodinfo | exchange_type, stock_code, channel_type, exchange_type, stock_code, channel_type |
| idx_icsetfprodinfo_acct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:21:32 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-07-17 15:21:39 | 3.0.6.48 | 常行 | 物理表ics_etf_prod_info，增加索引(idx_icsetfprodinfo_acct:[fund_acco... |
| 2025-06-25 14:49:48 | 3.0.6.47 | 蒋浩 | 物理表ics_etf_prod_info，添加了表字段(transaction_no);
 |
| 2025-04-18 15:41:48 | 3.0.6.46 | 常行 | 物理表ics_etf_prod_info，添加了表字段(estimated_cash_mode);
物理表ics_et... |
| 2025-04-17 14:49:16 | 3.0.6.45 | 常行 | 物理表ics_etf_prod_info，添加了表字段(appredeem_type);
 |
| 2025-02-19 17:04:32 | 3.0.6.38 | 李想 | 物理表ics_etf_prod_info，添加了表字段(update_date);
物理表ics_etf_prod_i... |
| 2024-09-25 21:35:27 | 3.0.2.16 | 张明月 | 新增 |
| 2026-03-05 17:21:32 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-07-17 15:21:39 | 3.0.6.48 | 常行 | 物理表ics_etf_prod_info，增加索引(idx_icsetfprodinfo_acct:[fund_acco... |
| 2025-06-25 14:49:48 | 3.0.6.47 | 蒋浩 | 物理表ics_etf_prod_info，添加了表字段(transaction_no);
 |
| 2025-04-18 15:41:48 | 3.0.6.46 | 常行 | 物理表ics_etf_prod_info，添加了表字段(estimated_cash_mode);
物理表ics_et... |
| 2025-04-17 14:49:16 | 3.0.6.45 | 常行 | 物理表ics_etf_prod_info，添加了表字段(appredeem_type);
 |
| 2025-02-19 17:04:32 | 3.0.6.38 | 李想 | 物理表ics_etf_prod_info，添加了表字段(update_date);
物理表ics_etf_prod_i... |
| 2024-09-25 21:35:27 | 3.0.2.16 | 张明月 | 新增 |

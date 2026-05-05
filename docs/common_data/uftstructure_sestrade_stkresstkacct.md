# stkresstkacct - 股东账户证券限制表

**表对象ID**: 5533
**所属模块**: sestrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | res_exchange_type | 否 |  |  |
| 5 | res_stock_type | 否 |  |  |
| 6 | res_stock_code | 否 |  |  |
| 7 | res_sub_stock_type | 否 |  |  |
| 8 | res_entrust_bs | 否 |  |  |
| 9 | res_entrust_way | 否 |  |  |
| 10 | res_entrust_type | 否 |  |  |
| 11 | res_entrust_prop | 否 |  |  |
| 12 | begin_date | 否 |  |  |
| 13 | end_date | 否 |  |  |
| 14 | ordinal | 否 |  |  |
| 15 | anti_flag | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | branch_no | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  | fund_account(18)+stock_account(20)+ordinal(10) |
| 22 | restrict_str | 否 |  |  |
| 23 | tohis_date | 否 | H |  |
| 24 | client_id | 否 |  |  |
| 25 | fund_account | 否 |  |  |
| 26 | stock_account | 否 |  |  |
| 27 | res_exchange_type | 否 |  |  |
| 28 | res_stock_type | 否 |  |  |
| 29 | res_stock_code | 否 |  |  |
| 30 | res_sub_stock_type | 否 |  |  |
| 31 | res_entrust_bs | 否 |  |  |
| 32 | res_entrust_way | 否 |  |  |
| 33 | res_entrust_type | 否 |  |  |
| 34 | res_entrust_prop | 否 |  |  |
| 35 | begin_date | 否 |  |  |
| 36 | end_date | 否 |  |  |
| 37 | ordinal | 否 |  |  |
| 38 | anti_flag | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | transaction_no | 否 |  |  |
| 41 | branch_no | 否 |  |  |
| 42 | update_date | 否 |  |  |
| 43 | update_time | 否 |  |  |
| 44 | position_str | 否 |  | fund_account(18)+stock_account(20)+ordinal(10) |
| 45 | restrict_str | 否 |  |  |
| 46 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stkresstkacct | ART | 是 | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |
| uk_rpt_stkresstkacct | ART | 是 | tohis_date, fund_account, stock_account, ordinal, tohis_date, fund_account, stock_account, ordinal |
| idx_stkresstkacct | ART | 是 | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |
| uk_rpt_stkresstkacct | ART | 是 | tohis_date, fund_account, stock_account, ordinal, tohis_date, fund_account, stock_account, ordinal |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stkresstkacct | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |
| idx_stkresstkacct | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-08 14:39:23 | 3.0.2.43 | 洪略 | 补充资源 |
| 2025-07-25 14:20:57 | 3.0.6.1003 | 李奕轩 | 所有表stkresstkacct，添加了表字段(restrict_str);
 |
| 2025-02-14 14:26:11 | 3.0.6.7 | 常行 | 物理表stkresstkacct，添加了表字段(branch_no);
物理表stkresstkacct，添加了表字段... |
| 2024-09-09 11:14:49 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2025-11-08 14:39:23 | 3.0.2.43 | 洪略 | 补充资源 |
| 2025-07-25 14:20:57 | 3.0.6.1003 | 李奕轩 | 所有表stkresstkacct，添加了表字段(restrict_str);
 |
| 2025-02-14 14:26:11 | 3.0.6.7 | 常行 | 物理表stkresstkacct，添加了表字段(branch_no);
物理表stkresstkacct，添加了表字段... |
| 2024-09-09 11:14:49 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |

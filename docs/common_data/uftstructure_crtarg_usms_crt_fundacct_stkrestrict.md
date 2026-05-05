# usms_crt_fundacct_stkrestrict - 信用资产账户证券限制表

**表对象ID**: 7107
**所属模块**: crtarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | res_exchange_type | 否 |  |  |
| 4 | res_stock_type | 否 |  |  |
| 5 | res_sub_stock_type | 否 |  |  |
| 6 | res_stock_code | 否 |  |  |
| 7 | res_entrust_bs | 否 |  |  |
| 8 | res_entrust_way | 否 |  |  |
| 9 | res_entrust_type | 否 |  |  |
| 10 | res_entrust_prop | 否 |  |  |
| 11 | begin_date | 否 |  |  |
| 12 | end_date | 否 |  |  |
| 13 | ordinal | 否 |  |  |
| 14 | anti_flag | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | position_str | 否 |  | fund_account(18)+stock_account(20)+ordinal(10) |
| 22 | restrict_str | 否 |  |  |
| 23 | client_id | 否 |  |  |
| 24 | fund_account | 否 |  |  |
| 25 | res_exchange_type | 否 |  |  |
| 26 | res_stock_type | 否 |  |  |
| 27 | res_sub_stock_type | 否 |  |  |
| 28 | res_stock_code | 否 |  |  |
| 29 | res_entrust_bs | 否 |  |  |
| 30 | res_entrust_way | 否 |  |  |
| 31 | res_entrust_type | 否 |  |  |
| 32 | res_entrust_prop | 否 |  |  |
| 33 | begin_date | 否 |  |  |
| 34 | end_date | 否 |  |  |
| 35 | ordinal | 否 |  |  |
| 36 | anti_flag | 否 |  |  |
| 37 | stock_account | 否 |  |  |
| 38 | transaction_no | 否 |  |  |
| 39 | branch_no | 否 |  |  |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | remark | 否 |  |  |
| 43 | position_str | 否 |  | fund_account(18)+stock_account(20)+ordinal(10) |
| 44 | restrict_str | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_crt_fundacct_stkrestrict | 默认 | 否 |  |
| idx_uarg_crt_fundacct_stkrestrict_stock | 默认 | 否 | stock_account, stock_account |
| idx_usms_crt_fundacct_stkrestrict | 默认 | 是 | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |
| idx_usms_crt_fundacct_stkrestrict | 默认 | 否 |  |
| idx_uarg_crt_fundacct_stkrestrict_stock | 默认 | 否 | stock_account, stock_account |
| idx_usms_crt_fundacct_stkrestrict | 默认 | 是 | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_crt_fundacct_stkrestrict | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |
| idx_uarg_crt_fundacct_stkrestrict | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-24 10:19:14 | 3.0.6.1068 | 蒋浩 | 当前表usms_crt_fundacct_stkrestrict，重命名索引（idx_uarg_crt_fundacct... |
| 2025-07-25 14:23:05 | 3.0.6.117 | 李奕轩 | 所有表uarg_crt_fundacct_stkrestrict，添加了表字段(restrict_str);
 |
| 2025-03-13 13:52:50 | 3.0.6.95 | 李想 | 新增表 |
| 2025-10-24 10:19:14 | 3.0.6.1068 | 蒋浩 | 当前表usms_crt_fundacct_stkrestrict，重命名索引（idx_uarg_crt_fundacct... |
| 2025-07-25 14:23:05 | 3.0.6.117 | 李奕轩 | 所有表uarg_crt_fundacct_stkrestrict，添加了表字段(restrict_str);
 |
| 2025-03-13 13:52:50 | 3.0.6.95 | 李想 | 新增表 |

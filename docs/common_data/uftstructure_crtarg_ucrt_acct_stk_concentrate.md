# ucrt_acct_stk_concentrate - 个人集中度控制表

**表对象ID**: 7027
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | conc_ratio_type | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | market_forward_date_type | 否 |  |  |
| 7 | stockgroup_no | 否 |  |  |
| 8 | organ_flag | 否 |  |  |
| 9 | assurescale_value | 否 |  |  |
| 10 | stock_conc_ratio | 否 |  |  |
| 11 | registration_flag | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | end_date | 否 |  |  |
| 15 | followdate_flag | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | position_str | 否 |  | fund_account(18)+organ_flag(1)+market_forward_date_type(1)+s |
| 20 | fund_account | 否 |  |  |
| 21 | conc_ratio_type | 否 |  |  |
| 22 | exchange_type | 否 |  |  |
| 23 | stock_code | 否 |  |  |
| 24 | stock_type | 否 |  |  |
| 25 | market_forward_date_type | 否 |  |  |
| 26 | stockgroup_no | 否 |  |  |
| 27 | organ_flag | 否 |  |  |
| 28 | assurescale_value | 否 |  |  |
| 29 | stock_conc_ratio | 否 |  |  |
| 30 | registration_flag | 否 |  |  |
| 31 | transaction_no | 否 |  |  |
| 32 | branch_no | 否 |  |  |
| 33 | end_date | 否 |  |  |
| 34 | followdate_flag | 否 |  |  |
| 35 | remark | 否 |  |  |
| 36 | update_date | 否 |  |  |
| 37 | update_time | 否 |  |  |
| 38 | position_str | 否 |  | fund_account(18)+organ_flag(1)+market_forward_date_type(1)+s |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_acct_stk_concentrate | 默认 | 否 | conc_ratio_type, conc_ratio_type |
| idx_ucrt_acct_stk_concentrate | ART | 是 | fund_account, conc_ratio_type, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, fund_account, conc_ratio_type, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value |
| idx_ucrt_acct_stk_concentrate_flag | ART | 是 | fund_account, conc_ratio_type, market_forward_date_type, assurescale_value, stock_conc_ratio, fund_account, conc_ratio_type, market_forward_date_type, assurescale_value, stock_conc_ratio |
| idx_ucrt_acct_stk_concentrate | 默认 | 否 | conc_ratio_type, conc_ratio_type |
| idx_ucrt_acct_stk_concentrate | ART | 是 | fund_account, conc_ratio_type, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, fund_account, conc_ratio_type, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value |
| idx_ucrt_acct_stk_concentrate_flag | ART | 是 | fund_account, conc_ratio_type, market_forward_date_type, assurescale_value, stock_conc_ratio, fund_account, conc_ratio_type, market_forward_date_type, assurescale_value, stock_conc_ratio |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_acct_stk_concentrate_account | fund_account, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, conc_ratio_type, fund_account, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, conc_ratio_type |
| idx_ucrt_acct_stk_concentrate_account | fund_account, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, conc_ratio_type, fund_account, organ_flag, market_forward_date_type, stock_code, exchange_type, stock_type, stockgroup_no, registration_flag, assurescale_value, conc_ratio_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 10:28:31 | 3.0.6.71 | 李想 | 物理表ucrt_acct_stk_concentrate，添加了表字段(branch_no);
物理表ucrt_acc... |
| 2024-07-10 09:28:41 | 3.0.3.3 | 徐志坚 | 为了提升性能，将两个索引都改为分级索引，并删除两个*_account重复的索引 |
| 2024-05-08 13:23:23 | 3.0.2.7 | 叶慧军 | 新增两个分级索引用于优化个人集中度限额获取性能 |
| 2023-10-30 14:17:48 | V3.0.1.11 | 吴丽丽 | 物理表ucrt_acct_stk_concentrate，增加索引字段(索引idx_ucrt_acct_stk_conc... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2023-06-02 21:20 | 0.0.0.7 | 程猛 | 调整唯一索引 |
| 2025-02-18 10:28:31 | 3.0.6.71 | 李想 | 物理表ucrt_acct_stk_concentrate，添加了表字段(branch_no);
物理表ucrt_acc... |
| 2024-07-10 09:28:41 | 3.0.3.3 | 徐志坚 | 为了提升性能，将两个索引都改为分级索引，并删除两个*_account重复的索引 |
| 2024-05-08 13:23:23 | 3.0.2.7 | 叶慧军 | 新增两个分级索引用于优化个人集中度限额获取性能 |
| 2023-10-30 14:17:48 | V3.0.1.11 | 吴丽丽 | 物理表ucrt_acct_stk_concentrate，增加索引字段(索引idx_ucrt_acct_stk_conc... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2023-06-02 21:20 | 0.0.0.7 | 程猛 | 调整唯一索引 |

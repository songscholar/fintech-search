# ucrt_acct_underly_code - 个人标的证券信息表

**表对象ID**: 7023
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | fin_float_ratio | 否 |  |  |
| 7 | fin_status | 否 |  |  |
| 8 | slo_float_ratio | 否 |  |  |
| 9 | slo_status | 否 |  |  |
| 10 | end_date | 否 |  |  |
| 11 | slo_compact_end_date | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | registration_flag | 否 |  |  |
| 14 | active_flag | 否 |  |  |
| 15 | fin_active_flag | 否 |  |  |
| 16 | slo_active_flag | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_type(4)+stock_code(8 |
| 22 | client_id | 否 |  |  |
| 23 | fund_account | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | stock_type | 否 |  |  |
| 26 | stock_code | 否 |  |  |
| 27 | fin_float_ratio | 否 |  |  |
| 28 | fin_status | 否 |  |  |
| 29 | slo_float_ratio | 否 |  |  |
| 30 | slo_status | 否 |  |  |
| 31 | end_date | 否 |  |  |
| 32 | slo_compact_end_date | 否 |  |  |
| 33 | transaction_no | 否 |  |  |
| 34 | registration_flag | 否 |  |  |
| 35 | active_flag | 否 |  |  |
| 36 | fin_active_flag | 否 |  |  |
| 37 | slo_active_flag | 否 |  |  |
| 38 | branch_no | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_type(4)+stock_code(8 |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_acct_underly_code_uk | 默认 | 否 | registration_flag, registration_flag |
| idx_ucrt_acct_underly_code_uk | ART | 是 | fund_account, exchange_type, stock_type, stock_code, registration_flag, fund_account, exchange_type, stock_type, stock_code, registration_flag |
| idx_ucrt_acct_underly_code_uk | 默认 | 否 | registration_flag, registration_flag |
| idx_ucrt_acct_underly_code_uk | ART | 是 | fund_account, exchange_type, stock_type, stock_code, registration_flag, fund_account, exchange_type, stock_type, stock_code, registration_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_acct_underly_code_uk | fund_account, exchange_type, stock_type, stock_code, registration_flag, fund_account, exchange_type, stock_type, stock_code, registration_flag |
| idx_ucrt_acct_underly_code_uk | fund_account, exchange_type, stock_type, stock_code, registration_flag, fund_account, exchange_type, stock_type, stock_code, registration_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 11:06:52 | 3.0.6.1068 | 袁文龙 | 所有表ucrt_acct_underly_code，添加了表字段(branch_no);
所有表ucrt_acct_u... |
| 2025-08-22 10:52:28 | 3.0.6.1066 | 牟家乐 | 支持ucrt_acct_underly_code勾选不回库 |
| 2025-02-06 09:32:26 | 3.0.6.34 | 沈勋 | 物理表ucrt_acct_underly_code，删除了表字段(float_flag);
物理表ucrt_acct_... |
| 2025-02-06 09:28:56 | 3.0.6.34 | 沈勋 | 物理表ucrt_acct_underly_code，添加了表字段(active_flag);
物理表ucrt_acct... |
| 2024-06-11 17:10:38 | 3.0.2.15 | 楼欣欣 | 物理表ucrt_acct_underly_code，增加索引字段(索引idx_ucrt_acct_underly_cod... |
| 2024-06-11 17:08:42 | 3.0.2.15 | 楼欣欣 | 物理表ucrt_acct_underly_code，添加了表字段(registration_flag);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-11-21 11:06:52 | 3.0.6.1068 | 袁文龙 | 所有表ucrt_acct_underly_code，添加了表字段(branch_no);
所有表ucrt_acct_u... |
| 2025-08-22 10:52:28 | 3.0.6.1066 | 牟家乐 | 支持ucrt_acct_underly_code勾选不回库 |
| 2025-02-06 09:32:26 | 3.0.6.34 | 沈勋 | 物理表ucrt_acct_underly_code，删除了表字段(float_flag);
物理表ucrt_acct_... |
| 2025-02-06 09:28:56 | 3.0.6.34 | 沈勋 | 物理表ucrt_acct_underly_code，添加了表字段(active_flag);
物理表ucrt_acct... |
| 2024-06-11 17:10:38 | 3.0.2.15 | 楼欣欣 | 物理表ucrt_acct_underly_code，增加索引字段(索引idx_ucrt_acct_underly_cod... |
| 2024-06-11 17:08:42 | 3.0.2.15 | 楼欣欣 | 物理表ucrt_acct_underly_code，添加了表字段(registration_flag);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

> 共 16 条修改记录，仅显示最近15条

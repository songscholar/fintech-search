# uopt_comb_arg - 期权组合策略参数表

**表对象ID**: 9001
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | optcomb_code | 否 |  |  |
| 3 | optcomb_name | 否 |  |  |
| 4 | enddate_same_flag | 否 |  |  |
| 5 | underly_same_flag | 否 |  |  |
| 6 | unit_same_flag | 否 |  |  |
| 7 | component_count | 否 |  |  |
| 8 | first_option_type | 否 |  |  |
| 9 | first_opthold_type | 否 |  |  |
| 10 | first_exeprice_num | 否 |  |  |
| 11 | first_per_optamount | 否 |  |  |
| 12 | second_option_type | 否 |  |  |
| 13 | second_opthold_type | 否 |  |  |
| 14 | second_exeprice_num | 否 |  |  |
| 15 | second_per_optamount | 否 |  |  |
| 16 | first_enddate_num | 否 |  |  |
| 17 | second_enddate_num | 否 |  |  |
| 18 | near_split_days | 否 |  |  |
| 19 | standard_code_flag | 否 |  |  |
| 20 | update_date | 否 |  | 3.0 |
| 21 | update_time | 否 |  | 3.0独有，且字段名称就是更新时间 |
| 22 | transaction_no | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | optcomb_code | 否 |  |  |
| 26 | optcomb_name | 否 |  |  |
| 27 | enddate_same_flag | 否 |  |  |
| 28 | underly_same_flag | 否 |  |  |
| 29 | unit_same_flag | 否 |  |  |
| 30 | component_count | 否 |  |  |
| 31 | first_option_type | 否 |  |  |
| 32 | first_opthold_type | 否 |  |  |
| 33 | first_exeprice_num | 否 |  |  |
| 34 | first_per_optamount | 否 |  |  |
| 35 | second_option_type | 否 |  |  |
| 36 | second_opthold_type | 否 |  |  |
| 37 | second_exeprice_num | 否 |  |  |
| 38 | second_per_optamount | 否 |  |  |
| 39 | first_enddate_num | 否 |  |  |
| 40 | second_enddate_num | 否 |  |  |
| 41 | near_split_days | 否 |  |  |
| 42 | standard_code_flag | 否 |  |  |
| 43 | update_date | 否 |  | 3.0 |
| 44 | update_time | 否 |  | 3.0独有，且字段名称就是更新时间 |
| 45 | transaction_no | 否 |  |  |
| 46 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_comb_arg | 默认 | 是 | exchange_type, optcomb_code, exchange_type, optcomb_code |
| idx_uopt_comb_arg | 默认 | 是 | exchange_type, optcomb_code, exchange_type, optcomb_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optcombarg | exchange_type, optcomb_code, exchange_type, optcomb_code |
| idx_optcombarg | exchange_type, optcomb_code, exchange_type, optcomb_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-18 16:32:27 | V3.0.3.7 | 汪迎 | 物理表uopt_comb_arg，添加了表字段(transaction_no);
 |
| 2024-08-20 15:04:16 | V3.0.3.6 | 周君杰 | 不落redo、不回库、日初落redo |
| 2023-12-16 17:28:10 | 3.0.0.0 | wuxd |  |
| 2025-04-18 16:32:27 | V3.0.3.7 | 汪迎 | 物理表uopt_comb_arg，添加了表字段(transaction_no);
 |
| 2024-08-20 15:04:16 | V3.0.3.6 | 周君杰 | 不落redo、不回库、日初落redo |
| 2023-12-16 17:28:10 | 3.0.0.0 | wuxd |  |

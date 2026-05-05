# ref_underly_code - 转融通标的证券信息表

**表对象ID**: 6002
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 52 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_name | 否 |  |  |
| 6 | underly_status | 否 |  |  |
| 7 | one_low_app_amount | 否 |  |  |
| 8 | fair_price_flag | 否 |  |  |
| 9 | fair_price | 否 |  |  |
| 10 | end_date | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | confer_upper_lend_limit | 否 |  |  |
| 13 | confer_down_lend_limit | 否 |  |  |
| 14 | confer_lend_amount_unit | 否 |  |  |
| 15 | upper_lend_limit | 否 |  |  |
| 16 | down_lend_limit | 否 |  |  |
| 17 | lend_amount_unit | 否 |  |  |
| 18 | market_refflag | 否 |  |  |
| 19 | restri_lendflag | 否 |  |  |
| 20 | stock_name_long | 否 |  |  |
| 21 | ref_pause_flag | 否 |  |  |
| 22 | market_pause_flag | 否 |  |  |
| 23 | update_date | 否 |  |  |
| 24 | update_time | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 27 | init_date | 否 |  |  |
| 28 | exchange_type | 否 |  |  |
| 29 | stock_type | 否 |  |  |
| 30 | stock_code | 否 |  |  |
| 31 | stock_name | 否 |  |  |
| 32 | underly_status | 否 |  |  |
| 33 | one_low_app_amount | 否 |  |  |
| 34 | fair_price_flag | 否 |  |  |
| 35 | fair_price | 否 |  |  |
| 36 | end_date | 否 |  |  |
| 37 | remark | 否 |  |  |
| 38 | confer_upper_lend_limit | 否 |  |  |
| 39 | confer_down_lend_limit | 否 |  |  |
| 40 | confer_lend_amount_unit | 否 |  |  |
| 41 | upper_lend_limit | 否 |  |  |
| 42 | down_lend_limit | 否 |  |  |
| 43 | lend_amount_unit | 否 |  |  |
| 44 | market_refflag | 否 |  |  |
| 45 | restri_lendflag | 否 |  |  |
| 46 | stock_name_long | 否 |  |  |
| 47 | ref_pause_flag | 否 |  |  |
| 48 | market_pause_flag | 否 |  |  |
| 49 | update_date | 否 |  |  |
| 50 | update_time | 否 |  |  |
| 51 | transaction_no | 否 |  |  |
| 52 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_underly_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_ref_underly_code_pos | ART | 是 | position_str, position_str |
| idx_ref_underly_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_ref_underly_code_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_underly_code | stock_code, exchange_type, stock_code, exchange_type |
| idx_ref_underly_code | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 10:51:57 | 1.0.0.2 | 李想 | 新增表 |
| 2025-02-21 10:51:57 | 1.0.0.2 | 李想 | 新增表 |

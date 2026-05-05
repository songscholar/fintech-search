# ref_assure_code - 转融通担保证券信息表

**表对象ID**: 6001
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_name | 否 |  |  |
| 6 | assure_ratio | 否 |  |  |
| 7 | circulate_amount | 否 |  |  |
| 8 | capital_amount | 否 |  |  |
| 9 | fair_price | 否 |  |  |
| 10 | fair_price_flag | 否 |  |  |
| 11 | assure_status | 否 |  |  |
| 12 | modify_date | 否 |  |  |
| 13 | end_date | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 19 | init_date | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | stock_type | 否 |  |  |
| 22 | stock_code | 否 |  |  |
| 23 | stock_name | 否 |  |  |
| 24 | assure_ratio | 否 |  |  |
| 25 | circulate_amount | 否 |  |  |
| 26 | capital_amount | 否 |  |  |
| 27 | fair_price | 否 |  |  |
| 28 | fair_price_flag | 否 |  |  |
| 29 | assure_status | 否 |  |  |
| 30 | modify_date | 否 |  |  |
| 31 | end_date | 否 |  |  |
| 32 | remark | 否 |  |  |
| 33 | update_date | 否 |  |  |
| 34 | update_time | 否 |  |  |
| 35 | transaction_no | 否 |  |  |
| 36 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_assure_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_ref_assure_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_assure_code | stock_code, exchange_type, stock_code, exchange_type |
| idx_ref_assure_code | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 10:50:31 | 1.0.0.1 | 李想 | 新增表 |
| 2025-02-21 10:50:31 | 1.0.0.1 | 李想 | 新增表 |

# ref_pre_excharg - 转融通市场化约定申报参数表

**表对象ID**: 6013
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | ref_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | up_ref_term | 否 |  |  |
| 5 | down_ref_term | 否 |  |  |
| 6 | up_year_rate | 否 |  |  |
| 7 | down_year_rate | 否 |  |  |
| 8 | rate_diff | 否 |  |  |
| 9 | modify_date | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | init_date | 否 |  |  |
| 15 | ref_type | 否 |  |  |
| 16 | stock_type | 否 |  |  |
| 17 | up_ref_term | 否 |  |  |
| 18 | down_ref_term | 否 |  |  |
| 19 | up_year_rate | 否 |  |  |
| 20 | down_year_rate | 否 |  |  |
| 21 | rate_diff | 否 |  |  |
| 22 | modify_date | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_pre_excharg | ART | 是 | ref_type, stock_type, up_ref_term, down_ref_term, ref_type, stock_type, up_ref_term, down_ref_term |
| idx_ref_pre_excharg | ART | 是 | ref_type, stock_type, up_ref_term, down_ref_term, ref_type, stock_type, up_ref_term, down_ref_term |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_pre_excharg | ref_type, stock_type, up_ref_term, down_ref_term, ref_type, stock_type, up_ref_term, down_ref_term |
| idx_ref_pre_excharg | ref_type, stock_type, up_ref_term, down_ref_term, ref_type, stock_type, up_ref_term, down_ref_term |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 11:32:01 | 1.0.0.11 | 李想 | 新增表 |
| 2025-02-21 11:32:01 | 1.0.0.11 | 李想 | 新增表 |

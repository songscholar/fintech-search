# ref_csfc_rate - 转融通证金标准利率表

**表对象ID**: 6004
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | ref_type | 否 |  |  |
| 3 | ref_term | 否 |  |  |
| 4 | reflend_ratio | 否 |  |  |
| 5 | refborr_ratio | 否 |  |  |
| 6 | postpone_flag | 否 |  |  |
| 7 | preend_flag | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | position_str | 否 |  | ref_type(1)+ref_term(5) |
| 12 | init_date | 否 |  |  |
| 13 | ref_type | 否 |  |  |
| 14 | ref_term | 否 |  |  |
| 15 | reflend_ratio | 否 |  |  |
| 16 | refborr_ratio | 否 |  |  |
| 17 | postpone_flag | 否 |  |  |
| 18 | preend_flag | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | position_str | 否 |  | ref_type(1)+ref_term(5) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_csfc_rate | ART | 是 | ref_type, ref_term, ref_type, ref_term |
| idx_ref_csfc_rate | ART | 是 | ref_type, ref_term, ref_type, ref_term |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_csfc_rate | ref_type, ref_term, ref_type, ref_term |
| idx_ref_csfc_rate | ref_type, ref_term, ref_type, ref_term |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 10:53:56 | 1.0.0.3 | 李想 | 新增表 |
| 2025-02-21 10:53:56 | 1.0.0.3 | 李想 | 新增表 |

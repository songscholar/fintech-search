# uopt_init_date_model - 期权交易日期表

**表对象ID**: 9036
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | init_model | 否 |  |  |
| 3 | settle_flag | 否 |  |  |
| 4 | trade_flag | 否 |  |  |
| 5 | row_num | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | init_model | 否 |  |  |
| 9 | settle_flag | 否 |  |  |
| 10 | trade_flag | 否 |  |  |
| 11 | row_num | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | init_date | 否 |  |  |
| 14 | init_model | 否 |  |  |
| 15 | settle_flag | 否 |  |  |
| 16 | trade_flag | 否 |  |  |
| 17 | row_num | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | init_date | 否 |  |  |
| 20 | init_model | 否 |  |  |
| 21 | settle_flag | 否 |  |  |
| 22 | trade_flag | 否 |  |  |
| 23 | row_num | 否 |  |  |
| 24 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_init_date_model | ART | 是 | init_date, init_date |
| idx_uopt_init_date_model | ART | 是 | init_date, init_date |
| idx_uopt_init_date_model | ART | 是 | init_date, init_date |
| idx_uopt_init_date_model | ART | 是 | init_date, init_date |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_init_date_model | init_date, init_date |
| idx_uopt_init_date_model | init_date, init_date |
| idx_uopt_init_date_model | init_date, init_date |
| idx_uopt_init_date_model | init_date, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-18 10:19:07 | 3.0.2.99 |  | 调整表落redo |
| 2025-10-10 15:20:58 | 3.0.2.97 | wuxd | 添加表 |
| 2025-11-18 10:19:07 | 3.0.2.99 |  | 调整表落redo |
| 2025-10-10 15:20:58 | 3.0.2.97 | wuxd | 添加表 |

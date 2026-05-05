# settredo_usms_sdsjour - 清算重做限售扣税流水表

**表对象ID**: 2859
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 44 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | drawtax_balance | 否 |  |  |
| 2 | sum_drawtax_balance | 否 |  |  |
| 3 | sell_balance | 否 |  |  |
| 4 | order_id | 否 |  |  |
| 5 | entrust_no | 否 |  |  |
| 6 | deal_date | 否 |  |  |
| 7 | deal_time | 否 |  |  |
| 8 | deal_flag | 否 |  |  |
| 9 | position_str | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |
| 11 | sett_dml_type | 否 |  |  |
| 12 | drawtax_balance | 否 |  |  |
| 13 | sum_drawtax_balance | 否 |  |  |
| 14 | sell_balance | 否 |  |  |
| 15 | order_id | 否 |  |  |
| 16 | entrust_no | 否 |  |  |
| 17 | deal_date | 否 |  |  |
| 18 | deal_time | 否 |  |  |
| 19 | deal_flag | 否 |  |  |
| 20 | position_str | 否 |  |  |
| 21 | sett_batch_no | 否 |  |  |
| 22 | sett_dml_type | 否 |  |  |
| 23 | drawtax_balance | 否 |  |  |
| 24 | sum_drawtax_balance | 否 |  |  |
| 25 | sell_balance | 否 |  |  |
| 26 | order_id | 否 |  |  |
| 27 | entrust_no | 否 |  |  |
| 28 | deal_date | 否 |  |  |
| 29 | deal_time | 否 |  |  |
| 30 | deal_flag | 否 |  |  |
| 31 | position_str | 否 |  |  |
| 32 | sett_batch_no | 否 |  |  |
| 33 | sett_dml_type | 否 |  |  |
| 34 | drawtax_balance | 否 |  |  |
| 35 | sum_drawtax_balance | 否 |  |  |
| 36 | sell_balance | 否 |  |  |
| 37 | order_id | 否 |  |  |
| 38 | entrust_no | 否 |  |  |
| 39 | deal_date | 否 |  |  |
| 40 | deal_time | 否 |  |  |
| 41 | deal_flag | 否 |  |  |
| 42 | position_str | 否 |  |  |
| 43 | sett_batch_no | 否 |  |  |
| 44 | sett_dml_type | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sdsjour | 默认 | 否 | position_str, position_str |
| idx_sdsjour | 默认 | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_sdsjour | 默认 | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_sdsjour | 默认 | 否 | position_str, position_str |
| idx_sdsjour | 默认 | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_sdsjour | 默认 | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_sdsjour | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_sdsjour | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_sdsjour | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_sdsjour | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-05-08 09:45:47 | 3.0.6.86 | yangxz | 添加表 |
| 2025-05-08 09:45:47 | 3.0.6.86 |  | 物理表usms_sdsjour，增加索引(idx_sdsjour:[position_str]);
 |
| 2025-05-08 09:45:47 | 3.0.6.86 | yangxz | 添加表 |
| 2025-05-08 09:45:47 | 3.0.6.86 |  | 物理表usms_sdsjour，增加索引(idx_sdsjour:[position_str]);
 |

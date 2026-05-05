# income_pub_info - 固收公开报价行情信息表

**表对象ID**: 2464
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | income_busi_type | 否 |  |  |
| 3 | exch_order_id | 否 |  |  |
| 4 | quotingparty_name | 否 |  |  |
| 5 | trader_id | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | entrust_bs | 否 |  |  |
| 8 | income_price | 否 |  |  |
| 9 | entrust_amount | 否 |  |  |
| 10 | impawn_rate | 否 |  |  |
| 11 | repo_term | 否 |  |  |
| 12 | deal_balance | 否 |  |  |
| 13 | date_back | 否 |  |  |
| 14 | basket_str | 否 |  |  |
| 15 | relation_name | 否 |  |  |
| 16 | relation_way | 否 |  |  |
| 17 | quote_source | 否 |  |  |
| 18 | stock_code2 | 否 |  |  |
| 19 | settle_place | 否 |  |  |
| 20 | settle_efficiency | 否 |  |  |
| 21 | income_price_type | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | income_update_type | 否 |  |  |
| 25 | init_date | 否 |  |  |
| 26 | income_busi_type | 否 |  |  |
| 27 | exch_order_id | 否 |  |  |
| 28 | quotingparty_name | 否 |  |  |
| 29 | trader_id | 否 |  |  |
| 30 | stock_code | 否 |  |  |
| 31 | entrust_bs | 否 |  |  |
| 32 | income_price | 否 |  |  |
| 33 | entrust_amount | 否 |  |  |
| 34 | impawn_rate | 否 |  |  |
| 35 | repo_term | 否 |  |  |
| 36 | deal_balance | 否 |  |  |
| 37 | date_back | 否 |  |  |
| 38 | basket_str | 否 |  |  |
| 39 | relation_name | 否 |  |  |
| 40 | relation_way | 否 |  |  |
| 41 | quote_source | 否 |  |  |
| 42 | stock_code2 | 否 |  |  |
| 43 | settle_place | 否 |  |  |
| 44 | settle_efficiency | 否 |  |  |
| 45 | income_price_type | 否 |  |  |
| 46 | remark | 否 |  |  |
| 47 | position_str | 否 |  |  |
| 48 | income_update_type | 否 |  |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_incomepubinfo_id | 默认 | 否 |  |
| idx_incomepubinfo_pos | 默认 | 否 |  |
| idx_incomepubinfo_pos | 默认 | 否 |  |
| idx_incomepubinfo_id | ART | 是 | init_date, income_busi_type, exch_order_id, init_date, income_busi_type, exch_order_id |
| idx_incomepubinfo_pos | ART | 是 | position_str, position_str |
| idx_rpt_incomepubinfo_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_incomepubinfo_id | 默认 | 否 |  |
| idx_incomepubinfo_pos | 默认 | 否 |  |
| idx_incomepubinfo_pos | 默认 | 否 |  |
| idx_incomepubinfo_id | ART | 是 | init_date, income_busi_type, exch_order_id, init_date, income_busi_type, exch_order_id |
| idx_incomepubinfo_pos | ART | 是 | position_str, position_str |
| idx_rpt_incomepubinfo_pos | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_incomepubinfo_pos | position_str, position_str |
| idx_incomepubinfo_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-08 13:57:40 | 3.0.2.98 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-12-01 14:43:01 | 3.0.2.103 | taocong45644 | 当前表income_pub_info，修改了索引idx_incomepubinfo_id,索引字段修改为：(init_d... |
| 2025-11-06 15:07:57 | 3.2.0.98 | 洪略 | 增加历史表 |
| 2025-12-08 13:57:40 | 3.0.2.98 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-12-01 14:43:01 | 3.0.2.103 | taocong45644 | 当前表income_pub_info，修改了索引idx_incomepubinfo_id,索引字段修改为：(init_d... |
| 2025-11-06 15:07:57 | 3.2.0.98 | 洪略 | 增加历史表 |

# usms_limit_sell_daily - 限售股每日交易表

**表对象ID**: 2845
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | total_amount | 否 |  |  |
| 9 | circulate_amount | 否 |  |  |
| 10 | limit_ratio | 否 |  |  |
| 11 | sum_sell_amount | 否 |  |  |
| 12 | sum_sell_balance | 否 |  |  |
| 13 | blocktrade_flag | 否 |  |  |
| 14 | position_str_long | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | init_date | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | client_id | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | exchange_type | 否 |  |  |
| 21 | stock_account | 否 |  |  |
| 22 | stock_code | 否 |  |  |
| 23 | total_amount | 否 |  |  |
| 24 | circulate_amount | 否 |  |  |
| 25 | limit_ratio | 否 |  |  |
| 26 | sum_sell_amount | 否 |  |  |
| 27 | sum_sell_balance | 否 |  |  |
| 28 | blocktrade_flag | 否 |  |  |
| 29 | position_str_long | 否 |  |  |
| 30 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usms_limit_sell_daily | ART | 是 | position_str_long, position_str_long |
| idx_usms_limit_sell_daily | ART | 是 | position_str_long, position_str_long |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usms_limit_sell_daily | position_str_long, position_str_long |
| idx_usms_limit_sell_daily | position_str_long, position_str_long |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-14 10:01:40 | 3.0.2.2 | 高志强 | 增加DB模式,避免写表失败 |
| 2025-08-14 10:01:40 | 3.0.2.2 | 高志强 | 增加DB模式,避免写表失败 |

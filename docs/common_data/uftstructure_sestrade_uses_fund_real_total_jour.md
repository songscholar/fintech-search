# uses_fund_real_total_jour - 证券交易资金汇总流水表

**表对象ID**: 5990
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | curr_date | 否 |  |  |
| 5 | curr_time | 否 |  |  |
| 6 | settserial_no | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | current_balance | 否 |  |  |
| 9 | enable_balance | 否 |  |  |
| 10 | frozen_balance | 否 |  |  |
| 11 | unfrozen_balance | 否 |  |  |
| 12 | correct_balance | 否 |  |  |
| 13 | uncome_buy_balance | 否 |  |  |
| 14 | uncome_sell_balance | 否 |  |  |
| 15 | uncome_correct_balance | 否 |  |  |
| 16 | post_enable_balance | 否 |  |  |
| 17 | post_current_balance | 否 |  |  |
| 18 | flow_count | 否 |  |  |
| 19 | foregift_balance | 否 |  |  |
| 20 | init_date | 否 |  |  |
| 21 | serial_no | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | curr_date | 否 |  |  |
| 24 | curr_time | 否 |  |  |
| 25 | settserial_no | 否 |  |  |
| 26 | money_type | 否 |  |  |
| 27 | current_balance | 否 |  |  |
| 28 | enable_balance | 否 |  |  |
| 29 | frozen_balance | 否 |  |  |
| 30 | unfrozen_balance | 否 |  |  |
| 31 | correct_balance | 否 |  |  |
| 32 | uncome_buy_balance | 否 |  |  |
| 33 | uncome_sell_balance | 否 |  |  |
| 34 | uncome_correct_balance | 否 |  |  |
| 35 | post_enable_balance | 否 |  |  |
| 36 | post_current_balance | 否 |  |  |
| 37 | flow_count | 否 |  |  |
| 38 | foregift_balance | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usesfundrealtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_usesfundrealtotaljour_fund | 默认 | 否 | fund_account, money_type, fund_account, money_type |
| idx_rpt_usesfundrealtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_rpt_usesfundrealtotaljour_fund | ART | 是 | init_date, fund_account, money_type, init_date, fund_account, money_type |
| idx_usesfundrealtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_usesfundrealtotaljour_fund | 默认 | 否 | fund_account, money_type, fund_account, money_type |
| idx_rpt_usesfundrealtotaljour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_rpt_usesfundrealtotaljour_fund | ART | 是 | init_date, fund_account, money_type, init_date, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usesfundrealtotaljour | init_date, serial_no, init_date, serial_no |
| idx_usesfundrealtotaljour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:54:33 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-11 16:36:49 | V3.0.8.29 | 洪略 | idx_rpt_usesfundrealtotaljour调整为非唯一索引 |
| 2025-12-08 13:29:15 | V3.0.8.25 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-24 14:12:41 | V3.0.2.104 | 洪略 | 历史表的idx_usesfundrealtotaljour_fund索引调整为非唯一索引 |
| 2025-11-07 11:05:12 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2026-03-09 14:54:33 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-11 16:36:49 | V3.0.8.29 | 洪略 | idx_rpt_usesfundrealtotaljour调整为非唯一索引 |
| 2025-12-08 13:29:15 | V3.0.8.25 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-24 14:12:41 | V3.0.2.104 | 洪略 | 历史表的idx_usesfundrealtotaljour_fund索引调整为非唯一索引 |
| 2025-11-07 11:05:12 | V3.0.2.103 | 洪略 | 增加历史表 |

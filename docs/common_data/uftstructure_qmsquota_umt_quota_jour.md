# umt_quota_jour - 内存额度流水表

**表对象ID**: 1505
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | company_no | 否 |  |  |
| 6 | cbpacct_type | 否 |  |  |
| 7 | entrust_type | 否 |  |  |
| 8 | cancel_serialno | 否 |  |  |
| 9 | real_action | 否 |  |  |
| 10 | reverse_flag | 否 |  |  |
| 11 | occur_amount | 否 |  |  |
| 12 | occur_balance | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | position_str | 否 |  |  |
| 15 | init_date | 否 |  |  |
| 16 | serial_no | 否 |  |  |
| 17 | curr_date | 否 |  |  |
| 18 | curr_time | 否 |  |  |
| 19 | company_no | 否 |  |  |
| 20 | cbpacct_type | 否 |  |  |
| 21 | entrust_type | 否 |  |  |
| 22 | cancel_serialno | 否 |  |  |
| 23 | real_action | 否 |  |  |
| 24 | reverse_flag | 否 |  |  |
| 25 | occur_amount | 否 |  |  |
| 26 | occur_balance | 否 |  |  |
| 27 | remark | 否 |  |  |
| 28 | position_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_umtquotajour | 默认 | 否 |  |
| uk_umtquotajour | ART | 是 | init_date, cancel_serialno, reverse_flag, init_date, cancel_serialno, reverse_flag |
| uk_umtquotajour | 默认 | 否 |  |
| uk_umtquotajour | ART | 是 | init_date, cancel_serialno, reverse_flag, init_date, cancel_serialno, reverse_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_umt_quota_jour | init_date, cancel_serialno, reverse_flag, init_date, cancel_serialno, reverse_flag |
| uk_umt_quota_jour | init_date, cancel_serialno, reverse_flag, init_date, cancel_serialno, reverse_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:00:30 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:11:01 | 3.0.2.5 | taocong45644 | 当前表umt_quota_jour，修改了索引uk_umtquotajour,索引字段修改为：(init_date,ca... |
| 2025-04-03 22:19:26 | 3.0.2.2003 | 王云乾 | 新增 |
| 2026-03-05 17:00:30 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:11:01 | 3.0.2.5 | taocong45644 | 当前表umt_quota_jour，修改了索引uk_umtquotajour,索引字段修改为：(init_date,ca... |
| 2025-04-03 22:19:26 | 3.0.2.2003 | 王云乾 | 新增 |

# uses_fundrealfrozendetailjour - 交易资金汇总流水表

**表对象ID**: 5581
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | business_flag | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | curr_date | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | money_type | 否 |  |  |
| 9 | frozen_balance | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | position_str | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | serial_no | 否 |  |  |
| 14 | business_flag | 否 |  |  |
| 15 | curr_time | 否 |  |  |
| 16 | curr_date | 否 |  |  |
| 17 | client_id | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | money_type | 否 |  |  |
| 20 | frozen_balance | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | position_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fundrealfrozendetailjour | ART | 是 | position_str, position_str |
| idx_rpt_fundrealfrozendetailjour | ART | 是 | init_date, position_str, init_date, position_str |
| idx_fundrealfrozendetailjour | ART | 是 | position_str, position_str |
| idx_rpt_fundrealfrozendetailjour | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fundrealfrozendetailjour | position_str, position_str |
| idx_fundrealfrozendetailjour | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:31:35 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:27:57 | V3.0.8.18 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-07 10:51:07 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2025-08-22 10:30:42 | 3.0.6.1019 | 吴威 | 新增 |
| 2026-03-09 14:31:35 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:27:57 | V3.0.8.18 | 洪略 | 历史表索引加rpt前缀 |
| 2025-11-07 10:51:07 | V3.0.2.103 | 洪略 | 增加历史表 |
| 2025-08-22 10:30:42 | 3.0.6.1019 | 吴威 | 新增 |

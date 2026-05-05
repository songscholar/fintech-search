# frozen_total - 冻结汇总表

**表对象ID**: 5585
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | ordinal | 否 |  | 自增字段 |
| 2 | init_date | 否 |  |  |
| 3 | judifrozen_type | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | branch_no | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | seat_no | 否 |  |  |
| 11 | frozen_amount | 否 |  |  |
| 12 | csdc_sellfro_flag | 否 |  |  |
| 13 | end_date | 否 |  |  |
| 14 | judifrozen_id | 否 |  |  |
| 15 | judirefrozen_id | 否 |  |  |
| 16 | frozen_serial_id | 否 |  |  |
| 17 | frozen_organname | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | file_type | 否 |  |  |
| 20 | file_kind | 否 |  |  |
| 21 | set_seat_no | 否 |  |  |
| 22 | principal | 否 |  |  |
| 23 | dividend | 否 |  |  |
| 24 | ordinal | 否 |  | 自增字段 |
| 25 | init_date | 否 |  |  |
| 26 | judifrozen_type | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | client_id | 否 |  |  |
| 29 | branch_no | 否 |  |  |
| 30 | stock_account | 否 |  |  |
| 31 | exchange_type | 否 |  |  |
| 32 | stock_code | 否 |  |  |
| 33 | seat_no | 否 |  |  |
| 34 | frozen_amount | 否 |  |  |
| 35 | csdc_sellfro_flag | 否 |  |  |
| 36 | end_date | 否 |  |  |
| 37 | judifrozen_id | 否 |  |  |
| 38 | judirefrozen_id | 否 |  |  |
| 39 | frozen_serial_id | 否 |  |  |
| 40 | frozen_organname | 否 |  |  |
| 41 | remark | 否 |  |  |
| 42 | file_type | 否 |  |  |
| 43 | file_kind | 否 |  |  |
| 44 | set_seat_no | 否 |  |  |
| 45 | principal | 否 |  |  |
| 46 | dividend | 否 |  |  |

## 索引（共 24 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_frozen_total | 默认 | 否 |  |
| idx_frozen_total_acct | 默认 | 否 |  |
| idx_frozen_total_code | 默认 | 否 |  |
| idx_frozen_total
 | 默认 | 否 |  |
| idx_frozen_total_acct | 默认 | 否 |  |
| idx_frozen_total_code | 默认 | 否 |  |
| idx_frozen_total | ART | 是 | ordinal, ordinal |
| idx_frozen_total_acct | ART | 是 | branch_no, fund_account, stock_account, branch_no, fund_account, stock_account |
| idx_frozen_total_code | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_rpt_frozen_total
 | ART | 是 | init_date, ordinal, init_date, ordinal |
| idx_rpt_frozen_total_acct | ART | 是 | init_date, branch_no, fund_account, stock_account, init_date, branch_no, fund_account, stock_account |
| idx_rpt_frozen_total_code | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_frozen_total | 默认 | 否 |  |
| idx_frozen_total_acct | 默认 | 否 |  |
| idx_frozen_total_code | 默认 | 否 |  |
| idx_frozen_total
 | 默认 | 否 |  |
| idx_frozen_total_acct | 默认 | 否 |  |
| idx_frozen_total_code | 默认 | 否 |  |
| idx_frozen_total | ART | 是 | ordinal, ordinal |
| idx_frozen_total_acct | ART | 是 | branch_no, fund_account, stock_account, branch_no, fund_account, stock_account |
| idx_frozen_total_code | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_rpt_frozen_total
 | ART | 是 | init_date, ordinal, init_date, ordinal |
| idx_rpt_frozen_total_acct | ART | 是 | init_date, branch_no, fund_account, stock_account, init_date, branch_no, fund_account, stock_account |
| idx_rpt_frozen_total_code | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_frozen_total | ordinal, ordinal |
| idx_frozen_total_acct | branch_no, fund_account, stock_account, branch_no, fund_account, stock_account |
| idx_frozen_total_code | exchange_type, stock_code, exchange_type, stock_code |
| idx_frozen_total | ordinal, ordinal |
| idx_frozen_total_acct | branch_no, fund_account, stock_account, branch_no, fund_account, stock_account |
| idx_frozen_total_code | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:33:08 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:28:05 | V3.0.8.19 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:21:50 | 3.0.2.105 | taocong45644 | 当前表frozen_total，修改了索引idx_frozen_total,索引字段修改为：(ordinal),索引唯一... |
| 2025-11-05 15:23:39 | V3.0.2.103 | 洪略 | 支持历史表 |
| 2025-10-16 18:39:59 | 3.0.2.102 | 陆良铠 | 新增 |
| 2026-03-09 14:33:08 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-08 13:28:05 | V3.0.8.19 | 洪略 | 历史表索引加rpt前缀 |
| 2025-12-01 16:21:50 | 3.0.2.105 | taocong45644 | 当前表frozen_total，修改了索引idx_frozen_total,索引字段修改为：(ordinal),索引唯一... |
| 2025-11-05 15:23:39 | V3.0.2.103 | 洪略 | 支持历史表 |
| 2025-10-16 18:39:59 | 3.0.2.102 | 陆良铠 | 新增 |

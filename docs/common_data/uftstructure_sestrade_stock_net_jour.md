# stock_net_jour - 股份轧差流水表

**表对象ID**: 5525
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 62 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | stock_account | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | stock_type | 否 |  |  |
| 12 | stocknet_kind | 否 |  |  |
| 13 | begin_gap_amount | 否 |  |  |
| 14 | buy_real_amount1 | 否 |  |  |
| 15 | buy_real_amount2 | 否 |  |  |
| 16 | prev_amount | 否 |  |  |
| 17 | position_str | 否 |  | curr_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 18 | remark | 否 |  |  |
| 19 | trustee_seat_no | 否 |  |  |
| 20 | client_name | 否 | H |  |
| 21 | corp_client_group | 否 | H |  |
| 22 | client_group | 否 | H |  |
| 23 | room_code | 否 | H |  |
| 24 | asset_prop | 否 | H |  |
| 25 | limit_flag | 否 | H |  |
| 26 | client_prop | 否 | H |  |
| 27 | asset_level | 否 | H |  |
| 28 | risk_level | 否 | H |  |
| 29 | corp_risk_level | 否 | H |  |
| 30 | stock_name | 否 | H |  |
| 31 | sub_stock_type | 否 | H |  |
| 32 | init_date | 否 |  |  |
| 33 | serial_no | 否 |  |  |
| 34 | curr_date | 否 |  |  |
| 35 | curr_microtime | 否 |  |  |
| 36 | stock_account | 否 |  |  |
| 37 | stock_code | 否 |  |  |
| 38 | branch_no | 否 |  |  |
| 39 | exchange_type | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | client_id | 否 |  |  |
| 42 | stock_type | 否 |  |  |
| 43 | stocknet_kind | 否 |  |  |
| 44 | begin_gap_amount | 否 |  |  |
| 45 | buy_real_amount1 | 否 |  |  |
| 46 | buy_real_amount2 | 否 |  |  |
| 47 | prev_amount | 否 |  |  |
| 48 | position_str | 否 |  | curr_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 49 | remark | 否 |  |  |
| 50 | trustee_seat_no | 否 |  |  |
| 51 | client_name | 否 | H |  |
| 52 | corp_client_group | 否 | H |  |
| 53 | client_group | 否 | H |  |
| 54 | room_code | 否 | H |  |
| 55 | asset_prop | 否 | H |  |
| 56 | limit_flag | 否 | H |  |
| 57 | client_prop | 否 | H |  |
| 58 | asset_level | 否 | H |  |
| 59 | risk_level | 否 | H |  |
| 60 | corp_risk_level | 否 | H |  |
| 61 | stock_name | 否 | H |  |
| 62 | sub_stock_type | 否 | H |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stock_net_jour_unique | 默认 | 否 | fund_account, fund_account |
| idx_stock_net_jour | ART | 是 | serial_no, init_date, fund_account, serial_no, init_date, fund_account |
| uk_rpt_stocknetjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_stocknetjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_stock_net_jour_unique | 默认 | 否 | fund_account, fund_account |
| idx_stock_net_jour | ART | 是 | serial_no, init_date, fund_account, serial_no, init_date, fund_account |
| uk_rpt_stocknetjour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_stocknetjour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stock_net_jour_unique | init_date, serial_no, fund_account, init_date, serial_no, fund_account |
| idx_stock_net_jour_unique | init_date, serial_no, fund_account, init_date, serial_no, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:46:36 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，idx_stock_net_jour修改为全局唯一索引，删去无用的idx_stock_net_jour_u... |
| 2024-05-21 21:19:36 | 3.0.2.10 | 乐闽庭 | 物理表stock_net_jour，增加索引字段(索引idx_stock_net_jour_unique:增加了索引字段... |
| 2026-03-09 13:46:36 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，idx_stock_net_jour修改为全局唯一索引，删去无用的idx_stock_net_jour_u... |
| 2024-05-21 21:19:36 | 3.0.2.10 | 乐闽庭 | 物理表stock_net_jour，增加索引字段(索引idx_stock_net_jour_unique:增加了索引字段... |

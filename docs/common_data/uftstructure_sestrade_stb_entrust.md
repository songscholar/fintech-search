# stb_entrust - 三板报价订单表

**表对象ID**: 5716
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | prop_seat_no | 否 |  |  |
| 6 | prop_stock_account | 否 |  |  |
| 7 | entrust_amount2 | 否 |  |  |
| 8 | entrust_price2 | 否 |  |  |
| 9 | position_str | 否 |  | curr_date(8) + partition_no(2) + curr_milltime(9) + branch_n |
| 10 | deal_flag | 否 |  |  |
| 11 | prev_balance | 否 |  |  |
| 12 | join_serial_no | 否 |  |  |
| 13 | agency_no | 否 |  |  |
| 14 | trader_id | 否 |  |  |
| 15 | client_name | 否 | H |  |
| 16 | corp_client_group | 否 | H |  |
| 17 | branch_no | 否 | H |  |
| 18 | client_group | 否 | H |  |
| 19 | room_code | 否 | H |  |
| 20 | asset_prop | 否 | H |  |
| 21 | limit_flag | 否 | H |  |
| 22 | client_prop | 否 | H |  |
| 23 | asset_level | 否 | H |  |
| 24 | risk_level | 否 | H |  |
| 25 | corp_risk_level | 否 | H |  |
| 26 | init_date | 否 |  |  |
| 27 | entrust_no | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | client_id | 否 |  |  |
| 30 | prop_seat_no | 否 |  |  |
| 31 | prop_stock_account | 否 |  |  |
| 32 | entrust_amount2 | 否 |  |  |
| 33 | entrust_price2 | 否 |  |  |
| 34 | position_str | 否 |  | curr_date(8) + partition_no(2) + curr_milltime(9) + branch_n |
| 35 | deal_flag | 否 |  |  |
| 36 | prev_balance | 否 |  |  |
| 37 | join_serial_no | 否 |  |  |
| 38 | agency_no | 否 |  |  |
| 39 | trader_id | 否 |  |  |
| 40 | client_name | 否 | H |  |
| 41 | corp_client_group | 否 | H |  |
| 42 | branch_no | 否 | H |  |
| 43 | client_group | 否 | H |  |
| 44 | room_code | 否 | H |  |
| 45 | asset_prop | 否 | H |  |
| 46 | limit_flag | 否 | H |  |
| 47 | client_prop | 否 | H |  |
| 48 | asset_level | 否 | H |  |
| 49 | risk_level | 否 | H |  |
| 50 | corp_risk_level | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stb_entrust | ART | 是 | fund_account, entrust_no, init_date, fund_account, entrust_no, init_date |
| idx_stb_entrust_fund | ART | 是 | fund_account, fund_account |
| idx_stb_entrust_id | ART | 是 | client_id, client_id |
| idx_stb_entrust_pos | ART | 是 | position_str, position_str |
| uk_rpt_stbentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_stbentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_stb_entrust | ART | 是 | fund_account, entrust_no, init_date, fund_account, entrust_no, init_date |
| idx_stb_entrust_fund | ART | 是 | fund_account, fund_account |
| idx_stb_entrust_id | ART | 是 | client_id, client_id |
| idx_stb_entrust_pos | ART | 是 | position_str, position_str |
| uk_rpt_stbentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_stbentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stb_entrust_pos | position_str, position_str |
| idx_stb_entrust_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:36:34 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-03 17:00:38 | 3.0.5.1063 | 张训华 | 修改备注信息 |
| 2024-12-03 09:14:48 | 3.0.5.1061 | 阮善宏 | 定位串规则调整，增加备注信息 |
| 2024-06-14 10:30:37 | 3.0.2.19 | 乐闽庭 | 物理表stb_entrust，删除了表字段(branch_no);
内存表索引idx_stb_entrust 删除索引... |
| 2026-03-09 14:36:34 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-03 17:00:38 | 3.0.5.1063 | 张训华 | 修改备注信息 |
| 2024-12-03 09:14:48 | 3.0.5.1061 | 阮善宏 | 定位串规则调整，增加备注信息 |
| 2024-06-14 10:30:37 | 3.0.2.19 | 乐闽庭 | 物理表stb_entrust，删除了表字段(branch_no);
内存表索引idx_stb_entrust 删除索引... |

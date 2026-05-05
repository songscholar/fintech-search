# etf_ustock_entrust - 网下股份认购流水表

**表对象ID**: 5543
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 82 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | entrust_no | 否 |  |  |
| 4 | op_branch_no | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_entrust_way | 否 |  |  |
| 7 | op_station | 否 |  |  |
| 8 | batch_no | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_account | 否 |  |  |
| 13 | report_account | 否 |  |  |
| 14 | join_stock_account | 否 |  |  |
| 15 | join_report_account | 否 |  |  |
| 16 | join_seat_no | 否 |  |  |
| 17 | seat_no | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | component_code | 否 |  |  |
| 20 | component_name | 否 |  |  |
| 21 | stock_type | 否 |  |  |
| 22 | entrust_bs | 否 |  |  |
| 23 | entrust_amount | 否 |  |  |
| 24 | fund_flag | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 27 | curr_microtime | 否 |  |  |
| 28 | cancel_serial_no | 否 |  |  |
| 29 | stock_name | 否 |  |  |
| 30 | client_name | 否 | H |  |
| 31 | corp_client_group | 否 | H |  |
| 32 | branch_no | 否 | H |  |
| 33 | client_group | 否 | H |  |
| 34 | room_code | 否 | H |  |
| 35 | asset_prop | 否 | H |  |
| 36 | limit_flag | 否 | H |  |
| 37 | client_prop | 否 | H |  |
| 38 | asset_level | 否 | H |  |
| 39 | risk_level | 否 | H |  |
| 40 | corp_risk_level | 否 | H |  |
| 41 | sub_stock_type | 否 | H |  |
| 42 | init_date | 否 |  |  |
| 43 | curr_date | 否 |  |  |
| 44 | entrust_no | 否 |  |  |
| 45 | op_branch_no | 否 |  |  |
| 46 | operator_no | 否 |  |  |
| 47 | op_entrust_way | 否 |  |  |
| 48 | op_station | 否 |  |  |
| 49 | batch_no | 否 |  |  |
| 50 | fund_account | 否 |  |  |
| 51 | client_id | 否 |  |  |
| 52 | exchange_type | 否 |  |  |
| 53 | stock_account | 否 |  |  |
| 54 | report_account | 否 |  |  |
| 55 | join_stock_account | 否 |  |  |
| 56 | join_report_account | 否 |  |  |
| 57 | join_seat_no | 否 |  |  |
| 58 | seat_no | 否 |  |  |
| 59 | stock_code | 否 |  |  |
| 60 | component_code | 否 |  |  |
| 61 | component_name | 否 |  |  |
| 62 | stock_type | 否 |  |  |
| 63 | entrust_bs | 否 |  |  |
| 64 | entrust_amount | 否 |  |  |
| 65 | fund_flag | 否 |  |  |
| 66 | remark | 否 |  |  |
| 67 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 68 | curr_microtime | 否 |  |  |
| 69 | cancel_serial_no | 否 |  |  |
| 70 | stock_name | 否 |  |  |
| 71 | client_name | 否 | H |  |
| 72 | corp_client_group | 否 | H |  |
| 73 | branch_no | 否 | H |  |
| 74 | client_group | 否 | H |  |
| 75 | room_code | 否 | H |  |
| 76 | asset_prop | 否 | H |  |
| 77 | limit_flag | 否 | H |  |
| 78 | client_prop | 否 | H |  |
| 79 | asset_level | 否 | H |  |
| 80 | risk_level | 否 | H |  |
| 81 | corp_risk_level | 否 | H |  |
| 82 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etf_ustock_entrust | ART | 是 | position_str, position_str |
| idx_etf_ustock_entrust_acct | ART | 是 | fund_account, fund_account |
| idx_etf_ustock_entrust_id | ART | 是 | client_id, client_id |
| uk_rpt_etfustockentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_etfustockentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_etf_ustock_entrust | ART | 是 | position_str, position_str |
| idx_etf_ustock_entrust_acct | ART | 是 | fund_account, fund_account |
| idx_etf_ustock_entrust_id | ART | 是 | client_id, client_id |
| uk_rpt_etfustockentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_etfustockentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etf_ustock_entrust | position_str, position_str |
| idx_etf_ustock_entrust | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:57:24 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-01-22 10:54:47 | 3.0.2.56 | 李江霖 | 将position_str中的sysnode_id调整为partition_no |
| 2024-12-27 14:28:13 | 3.0.2.55 | 李江霖 | 增加position_str的备注 |
| 2024-12-25 16:23:53 | 3.0.2.54 | 雷玄 | 物理表etf_ustock_entrust，添加了表字段(stock_name);
 |
| 2024-07-04 13:26:52 | 3.0.2.27 | 谢宗艺 | 物理表etf_ustock_entrust，添加了表字段(curr_microtime);
物理表etf_ustock... |
| 2024-07-04 13:26:15 | 3.0.2.27 | 谢宗艺 | 物理表etf_ustock_entrust，删除了表字段(curr_time);
物理表etf_ustock_entr... |
| 2024-07-02 19:33:33 | 3.0.2.26 | 谢宗艺 | 新增 |
| 2026-03-09 13:57:24 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-01-22 10:54:47 | 3.0.2.56 | 李江霖 | 将position_str中的sysnode_id调整为partition_no |
| 2024-12-27 14:28:13 | 3.0.2.55 | 李江霖 | 增加position_str的备注 |
| 2024-12-25 16:23:53 | 3.0.2.54 | 雷玄 | 物理表etf_ustock_entrust，添加了表字段(stock_name);
 |
| 2024-07-04 13:26:52 | 3.0.2.27 | 谢宗艺 | 物理表etf_ustock_entrust，添加了表字段(curr_microtime);
物理表etf_ustock... |
| 2024-07-04 13:26:15 | 3.0.2.27 | 谢宗艺 | 物理表etf_ustock_entrust，删除了表字段(curr_time);
物理表etf_ustock_entr... |

> 共 16 条修改记录，仅显示最近15条

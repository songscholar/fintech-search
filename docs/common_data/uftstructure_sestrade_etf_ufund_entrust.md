# etf_ufund_entrust - 网下现金认购流水表

**表对象ID**: 5542
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 78 个）

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
| 14 | seat_no | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | stock_type | 否 |  |  |
| 17 | entrust_bs | 否 |  |  |
| 18 | entrust_amount | 否 |  |  |
| 19 | entrust_price | 否 |  |  |
| 20 | frozen_balance | 否 |  |  |
| 21 | frozen_fare | 否 |  |  |
| 22 | fund_flag | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 25 | curr_microtime | 否 |  |  |
| 26 | cancel_serial_no | 否 |  |  |
| 27 | client_name | 否 | H |  |
| 28 | corp_client_group | 否 | H |  |
| 29 | branch_no | 否 | H |  |
| 30 | client_group | 否 | H |  |
| 31 | room_code | 否 | H |  |
| 32 | asset_prop | 否 | H |  |
| 33 | limit_flag | 否 | H |  |
| 34 | client_prop | 否 | H |  |
| 35 | asset_level | 否 | H |  |
| 36 | risk_level | 否 | H |  |
| 37 | corp_risk_level | 否 | H |  |
| 38 | stock_name | 否 | H |  |
| 39 | sub_stock_type | 否 | H |  |
| 40 | init_date | 否 |  |  |
| 41 | curr_date | 否 |  |  |
| 42 | entrust_no | 否 |  |  |
| 43 | op_branch_no | 否 |  |  |
| 44 | operator_no | 否 |  |  |
| 45 | op_entrust_way | 否 |  |  |
| 46 | op_station | 否 |  |  |
| 47 | batch_no | 否 |  |  |
| 48 | fund_account | 否 |  |  |
| 49 | client_id | 否 |  |  |
| 50 | exchange_type | 否 |  |  |
| 51 | stock_account | 否 |  |  |
| 52 | report_account | 否 |  |  |
| 53 | seat_no | 否 |  |  |
| 54 | stock_code | 否 |  |  |
| 55 | stock_type | 否 |  |  |
| 56 | entrust_bs | 否 |  |  |
| 57 | entrust_amount | 否 |  |  |
| 58 | entrust_price | 否 |  |  |
| 59 | frozen_balance | 否 |  |  |
| 60 | frozen_fare | 否 |  |  |
| 61 | fund_flag | 否 |  |  |
| 62 | remark | 否 |  |  |
| 63 | position_str | 否 |  | init_date(8)+partition_no(2)+branch_no(5)+serial_no(10) |
| 64 | curr_microtime | 否 |  |  |
| 65 | cancel_serial_no | 否 |  |  |
| 66 | client_name | 否 | H |  |
| 67 | corp_client_group | 否 | H |  |
| 68 | branch_no | 否 | H |  |
| 69 | client_group | 否 | H |  |
| 70 | room_code | 否 | H |  |
| 71 | asset_prop | 否 | H |  |
| 72 | limit_flag | 否 | H |  |
| 73 | client_prop | 否 | H |  |
| 74 | asset_level | 否 | H |  |
| 75 | risk_level | 否 | H |  |
| 76 | corp_risk_level | 否 | H |  |
| 77 | stock_name | 否 | H |  |
| 78 | sub_stock_type | 否 | H |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etf_ufund_entrust | ART | 是 | position_str, position_str |
| idx_etf_ufund_entrust_acct | ART | 是 | fund_account, fund_account |
| idx_etf_ufund_entrust_id | ART | 是 | client_id, client_id |
| uk_rpt_etfufundentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_etfufundentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_etf_ufund_entrust | ART | 是 | position_str, position_str |
| idx_etf_ufund_entrust_acct | ART | 是 | fund_account, fund_account |
| idx_etf_ufund_entrust_id | ART | 是 | client_id, client_id |
| uk_rpt_etfufundentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_etfufundentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etf_ufund_entrust | position_str, position_str |
| idx_etf_ufund_entrust | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:55:09 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-01-22 10:54:47 | 3.0.2.29 | 李江霖 | 将position_str中的sysnode_id调整为partition_no |
| 2024-12-27 14:28:13 | 3.0.2.28 | 李江霖 | 增加position_str的备注 |
| 2024-07-04 13:25:12 | 3.0.2.27 | 谢宗艺 | 物理表etf_ufund_entrust，添加了表字段(curr_microtime);
物理表etf_ufund_e... |
| 2024-07-04 13:22:52 | 3.0.2.27 | 谢宗艺 | 物理表etf_ufund_entrust，删除了表字段(branch_no);
物理表etf_ufund_entrus... |
| 2024-07-01 17:14:28 | 3.0.2.24 | 谢宗艺 | 新增 |
| 2026-03-09 13:55:09 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-01-22 10:54:47 | 3.0.2.29 | 李江霖 | 将position_str中的sysnode_id调整为partition_no |
| 2024-12-27 14:28:13 | 3.0.2.28 | 李江霖 | 增加position_str的备注 |
| 2024-07-04 13:25:12 | 3.0.2.27 | 谢宗艺 | 物理表etf_ufund_entrust，添加了表字段(curr_microtime);
物理表etf_ufund_e... |
| 2024-07-04 13:22:52 | 3.0.2.27 | 谢宗艺 | 物理表etf_ufund_entrust，删除了表字段(branch_no);
物理表etf_ufund_entrus... |
| 2024-07-01 17:14:28 | 3.0.2.24 | 谢宗艺 | 新增 |

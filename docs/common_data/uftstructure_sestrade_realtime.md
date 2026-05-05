# realtime - 实时成交表

**表对象ID**: 5523
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 92 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_microtime | 否 |  |  |
| 4 | serial_no | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | seat_no | 否 |  |  |
| 9 | stock_account | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | entrust_bs | 否 |  |  |
| 12 | entrust_prop | 否 |  |  |
| 13 | entrust_no | 否 |  |  |
| 14 | business_amount | 否 |  |  |
| 15 | business_price | 否 |  |  |
| 16 | business_balance | 否 |  |  |
| 17 | opp_account | 否 |  |  |
| 18 | business_no | 否 |  |  |
| 19 | business_id | 否 |  |  |
| 20 | business_microtime | 否 |  |  |
| 21 | real_type | 否 |  |  |
| 22 | real_status | 否 |  |  |
| 23 | cancel_serial_no | 否 |  |  |
| 24 | order_id | 否 |  |  |
| 25 | orig_order_id | 否 |  |  |
| 26 | secu_stock_type | 否 |  |  |
| 27 | exch_return_time | 否 |  |  |
| 28 | position_str | 否 |  | init_date(8)+curr_milltime(9)+branch_no(5)+serial_no(10) |
| 29 | report_no | 否 |  |  |
| 30 | comb_hold_flag | 否 |  |  |
| 31 | op_entrust_way | 否 |  |  |
| 32 | ext_order_id | 否 |  |  |
| 33 | client_name | 否 | H |  |
| 34 | corp_client_group | 否 | H |  |
| 35 | branch_no | 否 | H |  |
| 36 | client_group | 否 | H |  |
| 37 | room_code | 否 | H |  |
| 38 | asset_prop | 否 | H |  |
| 39 | limit_flag | 否 | H |  |
| 40 | client_prop | 否 | H |  |
| 41 | asset_level | 否 | H |  |
| 42 | risk_level | 否 | H |  |
| 43 | corp_risk_level | 否 | H |  |
| 44 | stock_name | 否 | H |  |
| 45 | stock_type | 否 | H |  |
| 46 | sub_stock_type | 否 | H |  |
| 47 | init_date | 否 |  |  |
| 48 | curr_date | 否 |  |  |
| 49 | curr_microtime | 否 |  |  |
| 50 | serial_no | 否 |  |  |
| 51 | fund_account | 否 |  |  |
| 52 | client_id | 否 |  |  |
| 53 | exchange_type | 否 |  |  |
| 54 | seat_no | 否 |  |  |
| 55 | stock_account | 否 |  |  |
| 56 | stock_code | 否 |  |  |
| 57 | entrust_bs | 否 |  |  |
| 58 | entrust_prop | 否 |  |  |
| 59 | entrust_no | 否 |  |  |
| 60 | business_amount | 否 |  |  |
| 61 | business_price | 否 |  |  |
| 62 | business_balance | 否 |  |  |
| 63 | opp_account | 否 |  |  |
| 64 | business_no | 否 |  |  |
| 65 | business_id | 否 |  |  |
| 66 | business_microtime | 否 |  |  |
| 67 | real_type | 否 |  |  |
| 68 | real_status | 否 |  |  |
| 69 | cancel_serial_no | 否 |  |  |
| 70 | order_id | 否 |  |  |
| 71 | orig_order_id | 否 |  |  |
| 72 | secu_stock_type | 否 |  |  |
| 73 | exch_return_time | 否 |  |  |
| 74 | position_str | 否 |  | init_date(8)+curr_milltime(9)+branch_no(5)+serial_no(10) |
| 75 | report_no | 否 |  |  |
| 76 | comb_hold_flag | 否 |  |  |
| 77 | op_entrust_way | 否 |  |  |
| 78 | ext_order_id | 否 |  |  |
| 79 | client_name | 否 | H |  |
| 80 | corp_client_group | 否 | H |  |
| 81 | branch_no | 否 | H |  |
| 82 | client_group | 否 | H |  |
| 83 | room_code | 否 | H |  |
| 84 | asset_prop | 否 | H |  |
| 85 | limit_flag | 否 | H |  |
| 86 | client_prop | 否 | H |  |
| 87 | asset_level | 否 | H |  |
| 88 | risk_level | 否 | H |  |
| 89 | corp_risk_level | 否 | H |  |
| 90 | stock_name | 否 | H |  |
| 91 | stock_type | 否 | H |  |
| 92 | sub_stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_realtime_fund_acct | 默认 | 否 | fund_account, fund_account |
| idx_realtime_id | 默认 | 否 | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| idx_realtime_serialno | ART | 是 | order_id, business_no, order_id, business_no |
| idx_realtime_id | ART | 是 | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| idx_realtime_pos | ART | 是 | position_str, position_str |
| uk_rpt_realtime | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_realtime_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_realtime_fund_acct | 默认 | 否 | fund_account, fund_account |
| idx_realtime_id | 默认 | 否 | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| idx_realtime_serialno | ART | 是 | order_id, business_no, order_id, business_no |
| idx_realtime_id | ART | 是 | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| idx_realtime_pos | ART | 是 | position_str, position_str |
| uk_rpt_realtime | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_realtime_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_realtime_id | fund_account, serial_no, init_date, fund_account, serial_no, init_date |
| idx_realtime_id | fund_account, serial_no, init_date, fund_account, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:45:40 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 16:13:24 | 3.0.2.74 | 洪略 | 补充分区信息 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-27 19:39:53 | 3.0.2.73 | 全春辉 | 数据导出相关表增加定位串查询索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-21 21:21:03 | 3.0.2.64 | 周富安 | 物理表realtime，添加了表字段(op_entrust_way);
物理表realtime，添加了表字段(ext_... |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，增加全局唯一索引idx_realtime_id |
| 2024-12-27 14:28:13 | 3.0.2.53 | 李江霖 | 修改position_str的备注，与代码中用法保持一致 |
| 2024-12-17 15:59:44 | 3.0.2.52 | 张云焘 | 物理表realtime，添加了表字段(comb_hold_flag);
 |
| 2024-11-04 15:27:54 | 3.0.5.1057 | 雷玄 | 物理表realtime，增加索引(idx_realtime_fund_acct:[fund_account]);
 |
| 2024-09-16 11:14:07 | 3.0.2.47 | 杨森峰 | 物理表realtime，添加了表字段(report_no);
 |
| 2024-05-04 13:57:45 | 3.0.2.4 | 乐闽庭 | 物理表realtime，增加索引字段(索引idx_realtime_id:删除了索引字段：client_id;增加了索引... |
| 2026-03-09 13:45:40 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 16:13:24 | 3.0.2.74 | 洪略 | 补充分区信息 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |

> 共 24 条修改记录，仅显示最近15条

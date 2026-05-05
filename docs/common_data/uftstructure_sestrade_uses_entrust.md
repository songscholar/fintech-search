# uses_entrust - 证券实时订单表

**表对象ID**: 5505
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 152 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | batch_no | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | business_amount | 否 |  |  |
| 4 | business_balance | 否 |  |  |
| 5 | business_price | 否 |  |  |
| 6 | business_microtime | 否 |  |  |
| 7 | cancel_serial_no | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | curr_date | 否 |  |  |
| 10 | curr_microtime | 否 |  |  |
| 11 | dispart_fare | 否 |  |  |
| 12 | entrust_amount | 否 |  |  |
| 13 | entrust_bs | 否 |  |  |
| 14 | entrust_no | 否 |  |  |
| 15 | entrust_price | 否 |  |  |
| 16 | entrust_prop | 否 |  |  |
| 17 | entrust_reference | 否 |  |  |
| 18 | entrust_status | 否 |  |  |
| 19 | entrust_type | 否 |  |  |
| 20 | return_code | 否 |  |  |
| 21 | exchange_type | 否 |  |  |
| 22 | fare_kind | 否 |  |  |
| 23 | fund_account | 否 |  |  |
| 24 | init_date | 否 |  |  |
| 25 | login_pbu | 否 |  |  |
| 26 | money_type | 否 |  |  |
| 27 | op_branch_no | 否 |  |  |
| 28 | op_entrust_way | 否 |  |  |
| 29 | op_station | 否 |  |  |
| 30 | operator_no | 否 |  |  |
| 31 | order_id | 否 |  |  |
| 32 | orig_order_id | 否 |  |  |
| 33 | prev_balance | 否 |  |  |
| 34 | real_seat_no | 否 |  |  |
| 35 | record_no | 否 |  |  |
| 36 | report_account | 否 |  |  |
| 37 | report_bs | 否 |  |  |
| 38 | report_microtime | 否 |  |  |
| 39 | report_unit | 否 |  |  |
| 40 | seat_no | 否 |  |  |
| 41 | stock_account | 否 |  |  |
| 42 | stock_code | 否 |  |  |
| 43 | stock_type | 否 |  |  |
| 44 | store_unit | 否 |  |  |
| 45 | sub_stock_type | 否 |  |  |
| 46 | trustee_seat_no | 否 |  |  |
| 47 | withdraw_amount | 否 |  |  |
| 48 | owner_type | 否 |  |  |
| 49 | secu_stock_type | 否 |  |  |
| 50 | exch_return_time | 否 |  |  |
| 51 | extend_field | 否 |  |  |
| 52 | partition_no | 否 |  |  |
| 53 | clear_balance | 否 |  |  |
| 54 | position_str | 否 |  | curr_date(8) + partition_no(2) + curr_milltime(9) + branch_n |
| 55 | enable_polling | 否 |  |  |
| 56 | report_no | 否 |  |  |
| 57 | strategyfare_id | 否 |  |  |
| 58 | json_data | 否 |  |  |
| 59 | polling_level | 否 |  |  |
| 60 | join_stock_account | 否 |  |  |
| 61 | join_seat_no | 否 |  |  |
| 62 | appredeem_type | 否 |  |  |
| 63 | client_group | 否 |  |  |
| 64 | offer_userinfo | 否 |  |  |
| 65 | exec_id | 否 |  |  |
| 66 | client_name | 否 | H |  |
| 67 | corp_client_group | 否 | H |  |
| 68 | room_code | 否 | H |  |
| 69 | asset_prop | 否 | H |  |
| 70 | limit_flag | 否 | H |  |
| 71 | client_prop | 否 | H |  |
| 72 | asset_level | 否 | H |  |
| 73 | risk_level | 否 | H |  |
| 74 | corp_risk_level | 否 | H |  |
| 75 | stock_name | 否 | H |  |
| 76 | return_info | 否 |  |  |
| 77 | batch_no | 否 |  |  |
| 78 | branch_no | 否 |  |  |
| 79 | business_amount | 否 |  |  |
| 80 | business_balance | 否 |  |  |
| 81 | business_price | 否 |  |  |
| 82 | business_microtime | 否 |  |  |
| 83 | cancel_serial_no | 否 |  |  |
| 84 | client_id | 否 |  |  |
| 85 | curr_date | 否 |  |  |
| 86 | curr_microtime | 否 |  |  |
| 87 | dispart_fare | 否 |  |  |
| 88 | entrust_amount | 否 |  |  |
| 89 | entrust_bs | 否 |  |  |
| 90 | entrust_no | 否 |  |  |
| 91 | entrust_price | 否 |  |  |
| 92 | entrust_prop | 否 |  |  |
| 93 | entrust_reference | 否 |  |  |
| 94 | entrust_status | 否 |  |  |
| 95 | entrust_type | 否 |  |  |
| 96 | return_code | 否 |  |  |
| 97 | exchange_type | 否 |  |  |
| 98 | fare_kind | 否 |  |  |
| 99 | fund_account | 否 |  |  |
| 100 | init_date | 否 |  |  |
| 101 | login_pbu | 否 |  |  |
| 102 | money_type | 否 |  |  |
| 103 | op_branch_no | 否 |  |  |
| 104 | op_entrust_way | 否 |  |  |
| 105 | op_station | 否 |  |  |
| 106 | operator_no | 否 |  |  |
| 107 | order_id | 否 |  |  |
| 108 | orig_order_id | 否 |  |  |
| 109 | prev_balance | 否 |  |  |
| 110 | real_seat_no | 否 |  |  |
| 111 | record_no | 否 |  |  |
| 112 | report_account | 否 |  |  |
| 113 | report_bs | 否 |  |  |
| 114 | report_microtime | 否 |  |  |
| 115 | report_unit | 否 |  |  |
| 116 | seat_no | 否 |  |  |
| 117 | stock_account | 否 |  |  |
| 118 | stock_code | 否 |  |  |
| 119 | stock_type | 否 |  |  |
| 120 | store_unit | 否 |  |  |
| 121 | sub_stock_type | 否 |  |  |
| 122 | trustee_seat_no | 否 |  |  |
| 123 | withdraw_amount | 否 |  |  |
| 124 | owner_type | 否 |  |  |
| 125 | secu_stock_type | 否 |  |  |
| 126 | exch_return_time | 否 |  |  |
| 127 | extend_field | 否 |  |  |
| 128 | partition_no | 否 |  |  |
| 129 | clear_balance | 否 |  |  |
| 130 | position_str | 否 |  | curr_date(8) + partition_no(2) + curr_milltime(9) + branch_n |
| 131 | enable_polling | 否 |  |  |
| 132 | report_no | 否 |  |  |
| 133 | strategyfare_id | 否 |  |  |
| 134 | json_data | 否 |  |  |
| 135 | polling_level | 否 |  |  |
| 136 | join_stock_account | 否 |  |  |
| 137 | join_seat_no | 否 |  |  |
| 138 | appredeem_type | 否 |  |  |
| 139 | client_group | 否 |  |  |
| 140 | offer_userinfo | 否 |  |  |
| 141 | exec_id | 否 |  |  |
| 142 | client_name | 否 | H |  |
| 143 | corp_client_group | 否 | H |  |
| 144 | room_code | 否 | H |  |
| 145 | asset_prop | 否 | H |  |
| 146 | limit_flag | 否 | H |  |
| 147 | client_prop | 否 | H |  |
| 148 | asset_level | 否 | H |  |
| 149 | risk_level | 否 | H |  |
| 150 | corp_risk_level | 否 | H |  |
| 151 | stock_name | 否 | H |  |
| 152 | return_info | 否 |  |  |

## 索引（共 24 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_entrust_pos | 默认 | 否 |  |
| idx_uses_entrust_orig | 默认 | 否 | orig_order_id, init_date, orig_order_id, init_date |
| idx_uses_entrust_code | ART | 是 | fund_account, stock_code, entrust_bs, fund_account, stock_code, entrust_bs |
| idx_uses_entrust_polling | ART | 是 | exchange_type, enable_polling, polling_level, curr_date, curr_microtime, entrust_no, exchange_type, enable_polling, polling_level, curr_date, curr_microtime, entrust_no |
| idx_uses_entrust_rpt | ART | 是 | order_id, init_date, entrust_no, branch_no, order_id, init_date, entrust_no, branch_no |
| idx_uses_entrust | ART | 是 | fund_account, entrust_no, init_date, fund_account, entrust_no, init_date |
| idx_uses_entrust_orig | ART | 是 | orig_order_id, init_date, orig_order_id, init_date |
| idx_uses_entrust_no | ART | 是 | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_uses_entrust_pos | ART | 是 | fund_account, position_str, fund_account, position_str |
| uk_rpt_usesentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_uses_entrust_position | ART | 是 | position_str, position_str |
| idx_uses_entrust_pos | 默认 | 否 |  |
| idx_uses_entrust_orig | 默认 | 否 | orig_order_id, init_date, orig_order_id, init_date |
| idx_uses_entrust_code | ART | 是 | fund_account, stock_code, entrust_bs, fund_account, stock_code, entrust_bs |
| idx_uses_entrust_polling | ART | 是 | exchange_type, enable_polling, polling_level, curr_date, curr_microtime, entrust_no, exchange_type, enable_polling, polling_level, curr_date, curr_microtime, entrust_no |
| idx_uses_entrust_rpt | ART | 是 | order_id, init_date, entrust_no, branch_no, order_id, init_date, entrust_no, branch_no |
| idx_uses_entrust | ART | 是 | fund_account, entrust_no, init_date, fund_account, entrust_no, init_date |
| idx_uses_entrust_orig | ART | 是 | orig_order_id, init_date, orig_order_id, init_date |
| idx_uses_entrust_no | ART | 是 | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_uses_entrust_pos | ART | 是 | fund_account, position_str, fund_account, position_str |
| uk_rpt_usesentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_usesentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_uses_entrust_position | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_entrust | fund_account, entrust_no, init_date, fund_account, entrust_no, init_date |
| idx_uses_entrust | fund_account, entrust_no, init_date, fund_account, entrust_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 11:20:12 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-18 14:56:58 | V3.0.8.30 | 洪略 | 维护分区信息 |
| 2025-12-09 10:17:20 | V3.0.8.28 | 洪略 | 维护资源 |
| 2025-11-26 17:32:48 | V3.0.8.11 | 马天宇 | 当前表uses_entrust，修改了索引idx_uses_entrust_pos,索引字段修改为：(fund_acco... |
| 2025-07-27 19:41:53 | 3.0.2.73 | 全春辉 | 数据导出相关表增加定位串查询索引 |
| 2025-07-17 20:33:52 | 3.0.6.13 | 张华佳 | 物理表uses_entrust，添加了表字段(exec_id);
 |
| 2025-07-12 10:16:57 | 3.0.2.72 | 全春辉 | 物理表uses_entrust，添加了表字段(offer_userinfo);
 |
| 2025-06-26 15:13:45 | 3.0.2.71 | 钟兆星 | 增加索引idx_uses_entrust_no |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-03-19 11:34:01 | 3.0.6.12 | 卢杰 | 物理表uses_entrust，添加了表字段(client_group);
 |
| 2025-02-21 10:06:56 | 3.0.2.59 | 华曌 | 物理表uses_entrust，添加了表字段(client_group);
 |
| 2025-01-22 14:28:10 | 3.0.2.58 | 杨涛 | 物理表uses_entrust，添加了表字段(join_stock_account);
物理表uses_entrust... |
| 2025-01-15 20:16:05 | 3.0.2.57 | 乐闽庭 | 物理表uses_entrust，添加了表字段(polling_level);
 |
| 2024-12-25 16:25:42 | 3.0.2.54 | 雷玄 | 物理表uses_entrust，添加了表字段(strategyfare_id);
物理表uses_entrust，添加... |
| 2024-12-03 16:49:02 | 3.0.5.1062 | 张训华 | uses_entrust的备注信息修改 |

> 共 62 条修改记录，仅显示最近15条

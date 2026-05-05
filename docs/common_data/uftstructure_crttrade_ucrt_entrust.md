# ucrt_entrust - 融资融券实时订单表

**表对象ID**: 7531
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 158 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | batch_no | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | business_amount | 否 |  |  |
| 4 | business_balance | 否 |  |  |
| 5 | business_price | 否 |  |  |
| 6 | business_microtime | 否 |  |  |
| 7 | clear_balance | 否 |  |  |
| 8 | cancel_serial_no | 否 |  |  |
| 9 | cashgroup_prop | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | compact_id | 否 |  |  |
| 12 | curr_date | 否 |  |  |
| 13 | curr_microtime | 否 |  |  |
| 14 | dispart_fare | 否 |  |  |
| 15 | entrust_amount | 否 |  |  |
| 16 | entrust_bs | 否 |  |  |
| 17 | entrust_no | 否 |  |  |
| 18 | entrust_price | 否 |  |  |
| 19 | entrust_prop | 否 |  |  |
| 20 | entrust_reference | 否 |  |  |
| 21 | entrust_status | 否 |  |  |
| 22 | entrust_type | 否 |  |  |
| 23 | return_info | 否 |  |  |
| 24 | return_code | 否 |  |  |
| 25 | exchange_type | 否 |  |  |
| 26 | fare_kind | 否 |  |  |
| 27 | fund_account | 否 |  |  |
| 28 | init_date | 否 |  |  |
| 29 | login_pbu | 否 |  |  |
| 30 | money_type | 否 |  |  |
| 31 | op_branch_no | 否 |  |  |
| 32 | op_entrust_way | 否 |  |  |
| 33 | op_station | 否 |  |  |
| 34 | operator_no | 否 |  |  |
| 35 | order_id | 否 |  |  |
| 36 | orig_order_id | 否 |  |  |
| 37 | prev_balance | 否 |  |  |
| 38 | real_seat_no | 否 |  |  |
| 39 | record_no | 否 |  |  |
| 40 | report_account | 否 |  |  |
| 41 | report_bs | 否 |  |  |
| 42 | report_microtime | 否 |  |  |
| 43 | report_unit | 否 |  |  |
| 44 | seat_no | 否 |  |  |
| 45 | stock_account | 否 |  |  |
| 46 | stock_code | 否 |  |  |
| 47 | stock_type | 否 |  |  |
| 48 | store_unit | 否 |  |  |
| 49 | sub_stock_type | 否 |  |  |
| 50 | trustee_seat_no | 否 |  |  |
| 51 | withdraw_amount | 否 |  |  |
| 52 | owner_type | 否 |  |  |
| 53 | secu_stock_type | 否 |  |  |
| 54 | exch_return_time | 否 |  |  |
| 55 | extend_field | 否 |  |  |
| 56 | partition_no | 否 |  |  |
| 57 | prop_seat_no | 否 |  |  |
| 58 | prop_stock_account | 否 |  |  |
| 59 | cbpconfer_id | 否 |  |  |
| 60 | agency_no | 否 |  |  |
| 61 | trader_id | 否 |  |  |
| 62 | oppo_agency | 否 |  |  |
| 63 | oppo_trader_id | 否 |  |  |
| 64 | report_no | 否 |  |  |
| 65 | position_str | 否 |  |  |
| 66 | json_data | 否 |  |  |
| 67 | combentrust_no | 是 |  |  |
| 68 | client_group | 否 | H |  |
| 69 | room_code | 否 | H |  |
| 70 | asset_prop | 否 | H |  |
| 71 | limit_flag | 否 | H |  |
| 72 | risk_level | 否 | H |  |
| 73 | corp_client_group | 否 | H |  |
| 74 | corp_risk_level | 否 | H |  |
| 75 | asset_level | 否 | H |  |
| 76 | client_name | 否 | H |  |
| 77 | stock_name | 否 | H |  |
| 78 | error_info | 否 | H |  |
| 79 | client_prop | 否 | H |  |
| 80 | batch_no | 否 |  |  |
| 81 | branch_no | 否 |  |  |
| 82 | business_amount | 否 |  |  |
| 83 | business_balance | 否 |  |  |
| 84 | business_price | 否 |  |  |
| 85 | business_microtime | 否 |  |  |
| 86 | clear_balance | 否 |  |  |
| 87 | cancel_serial_no | 否 |  |  |
| 88 | cashgroup_prop | 否 |  |  |
| 89 | client_id | 否 |  |  |
| 90 | compact_id | 否 |  |  |
| 91 | curr_date | 否 |  |  |
| 92 | curr_microtime | 否 |  |  |
| 93 | dispart_fare | 否 |  |  |
| 94 | entrust_amount | 否 |  |  |
| 95 | entrust_bs | 否 |  |  |
| 96 | entrust_no | 否 |  |  |
| 97 | entrust_price | 否 |  |  |
| 98 | entrust_prop | 否 |  |  |
| 99 | entrust_reference | 否 |  |  |
| 100 | entrust_status | 否 |  |  |
| 101 | entrust_type | 否 |  |  |
| 102 | return_info | 否 |  |  |
| 103 | return_code | 否 |  |  |
| 104 | exchange_type | 否 |  |  |
| 105 | fare_kind | 否 |  |  |
| 106 | fund_account | 否 |  |  |
| 107 | init_date | 否 |  |  |
| 108 | login_pbu | 否 |  |  |
| 109 | money_type | 否 |  |  |
| 110 | op_branch_no | 否 |  |  |
| 111 | op_entrust_way | 否 |  |  |
| 112 | op_station | 否 |  |  |
| 113 | operator_no | 否 |  |  |
| 114 | order_id | 否 |  |  |
| 115 | orig_order_id | 否 |  |  |
| 116 | prev_balance | 否 |  |  |
| 117 | real_seat_no | 否 |  |  |
| 118 | record_no | 否 |  |  |
| 119 | report_account | 否 |  |  |
| 120 | report_bs | 否 |  |  |
| 121 | report_microtime | 否 |  |  |
| 122 | report_unit | 否 |  |  |
| 123 | seat_no | 否 |  |  |
| 124 | stock_account | 否 |  |  |
| 125 | stock_code | 否 |  |  |
| 126 | stock_type | 否 |  |  |
| 127 | store_unit | 否 |  |  |
| 128 | sub_stock_type | 否 |  |  |
| 129 | trustee_seat_no | 否 |  |  |
| 130 | withdraw_amount | 否 |  |  |
| 131 | owner_type | 否 |  |  |
| 132 | secu_stock_type | 否 |  |  |
| 133 | exch_return_time | 否 |  |  |
| 134 | extend_field | 否 |  |  |
| 135 | partition_no | 否 |  |  |
| 136 | prop_seat_no | 否 |  |  |
| 137 | prop_stock_account | 否 |  |  |
| 138 | cbpconfer_id | 否 |  |  |
| 139 | agency_no | 否 |  |  |
| 140 | trader_id | 否 |  |  |
| 141 | oppo_agency | 否 |  |  |
| 142 | oppo_trader_id | 否 |  |  |
| 143 | report_no | 否 |  |  |
| 144 | position_str | 否 |  |  |
| 145 | json_data | 否 |  |  |
| 146 | combentrust_no | 是 |  |  |
| 147 | client_group | 否 | H |  |
| 148 | room_code | 否 | H |  |
| 149 | asset_prop | 否 | H |  |
| 150 | limit_flag | 否 | H |  |
| 151 | risk_level | 否 | H |  |
| 152 | corp_client_group | 否 | H |  |
| 153 | corp_risk_level | 否 | H |  |
| 154 | asset_level | 否 | H |  |
| 155 | client_name | 否 | H |  |
| 156 | stock_name | 否 | H |  |
| 157 | error_info | 否 | H |  |
| 158 | client_prop | 否 | H |  |

## 索引（共 28 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_entrust_pos | 默认 | 否 | position_str, position_str |
| idx_ucrt_entrust_no | ART | 是 | fund_account, entrust_no, init_date, fund_account, entrust_no, init_date |
| idx_ucrt_entrust | ART | 是 | init_date, entrust_no, fund_account, init_date, entrust_no, fund_account |
| idx_ucrt_entrust_code | ART | 是 | fund_account, stock_code, entrust_bs, fund_account, stock_code, entrust_bs |
| idx_ucrt_entrust_polling | ART | 是 | exchange_type, entrust_status, curr_date, curr_microtime, entrust_no, exchange_type, entrust_status, curr_date, curr_microtime, entrust_no |
| idx_ucrt_entrust_query | ART | 是 | fund_account, init_date, exchange_type, stock_account, stock_code, entrust_bs, entrust_prop, entrust_type, fund_account, init_date, exchange_type, stock_account, stock_code, entrust_bs, entrust_prop, entrust_type |
| idx_ucrt_entrust_rpt | ART | 是 | order_id, init_date, branch_no, order_id, init_date, branch_no |
| idx_ucrt_entrust_query_globle | ART | 是 | report_account, stock_code, report_account, stock_code |
| idx_ucrt_entrust_total | ART | 是 | init_date, branch_no, batch_no, init_date, branch_no, batch_no |
| idx_ucrt_entrust_orig | ART | 是 | orig_order_id, init_date, orig_order_id, init_date |
| idx_ucrt_entrust_pos | ART | 是 | position_str, position_str |
| idx_ucrt_entrust_fundpos | ART | 是 | fund_account, position_str, fund_account, position_str |
| uk_rpt_ucrtentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucrt_entrust_pos | 默认 | 否 | position_str, position_str |
| idx_ucrt_entrust_no | ART | 是 | fund_account, entrust_no, init_date, fund_account, entrust_no, init_date |
| idx_ucrt_entrust | ART | 是 | init_date, entrust_no, fund_account, init_date, entrust_no, fund_account |
| idx_ucrt_entrust_code | ART | 是 | fund_account, stock_code, entrust_bs, fund_account, stock_code, entrust_bs |
| idx_ucrt_entrust_polling | ART | 是 | exchange_type, entrust_status, curr_date, curr_microtime, entrust_no, exchange_type, entrust_status, curr_date, curr_microtime, entrust_no |
| idx_ucrt_entrust_query | ART | 是 | fund_account, init_date, exchange_type, stock_account, stock_code, entrust_bs, entrust_prop, entrust_type, fund_account, init_date, exchange_type, stock_account, stock_code, entrust_bs, entrust_prop, entrust_type |
| idx_ucrt_entrust_rpt | ART | 是 | order_id, init_date, branch_no, order_id, init_date, branch_no |
| idx_ucrt_entrust_query_globle | ART | 是 | report_account, stock_code, report_account, stock_code |
| idx_ucrt_entrust_total | ART | 是 | init_date, branch_no, batch_no, init_date, branch_no, batch_no |
| idx_ucrt_entrust_orig | ART | 是 | orig_order_id, init_date, orig_order_id, init_date |
| idx_ucrt_entrust_pos | ART | 是 | position_str, position_str |
| idx_ucrt_entrust_fundpos | ART | 是 | fund_account, position_str, fund_account, position_str |
| uk_rpt_ucrtentrust | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucrtentrust_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_entrust | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |
| idx_ucrt_entrust | entrust_no, init_date, fund_account, entrust_no, init_date, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-26 20:11:50 | 3.0.6.1064 | 袁文龙 | 所有表ucrt_entrust，添加了表字段(combentrust_no);
 |
| 2025-03-31 15:46:46 | 3.0.6.52 | 袁文龙 | 物理表ucrt_entrust，添加了表字段(json_data);
 |
| 2025-03-12 20:09:59 | 3.0.6.42 | 徐世晗 | 物理表ucrt_entrust，增加索引(idx_ucrt_entrust_pos:[position_str]);
 |
| 2025-03-12 10:51:50 | 3.0.6.42 | 徐世晗 | 物理表ucrt_entrust，添加了表字段(position_str);
 |
| 2025-02-21 14:23:57 | 3.0.6.38 | 汪杰 | 物理表ucrt_entrust，添加了表字段(report_no);
 |
| 2024-07-23 15:50:36 | 3.0.3.5 | 刘景锋 | 修复关联索引是全局索引问题 |
| 2024-01-19 10:32:13 | V3.0.1.26 | huangzh | idx_ucrt_entrust_code调整为分级索引 |
| 2023-12-31 13:59:08 | V3.0.1.25 | 吴丽丽 | 物理表ucrt_entrust，添加了表字段(agency_no);
物理表ucrt_entrust，添加了表字段(t... |
| 2023-11-17 09:42:22 | V3.0.1.20 | 徐世晗 | idx_entrust调整为分级索引 |
| 2023-09-15 10:22:33 | V3.0.1.2 | 许琮擎 | 表索引重命名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-29 10:50 | 0.3.3.114 | 程猛 | 新增全局非唯一索引ucrt_entrust.idx_ucrt_entrust_orig_order_id（orig_or... |
| 2023-06-28 17:03 | 0.3.3.112 | 程猛 | 索引ucrt_entrust.idx_ucrt_entrust_rpt由唯一索引调整为非唯一索引 |
| 2023-06-20 20:13 | 0.3.3.108 | 程猛 | 分片号由partition_id-HsChar10调整为partition_no-HsNum |
| 2025-08-26 20:11:50 | 3.0.6.1064 | 袁文龙 | 所有表ucrt_entrust，添加了表字段(combentrust_no);
 |

> 共 28 条修改记录，仅显示最近15条

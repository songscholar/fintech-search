# uqms_bpr_info - 额度管理协议回购行情信息表

**表对象ID**: 1620
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 90 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | cbpconfer_id | 否 |  |  |
| 3 | entrust_no | 否 |  |  |
| 4 | bpr_hq_type | 否 |  |  |
| 5 | entrust_prop | 否 |  |  |
| 6 | entrust_bs | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | expire_year_rate | 否 |  |  |
| 11 | repo_term | 否 |  |  |
| 12 | fund_used_days | 否 |  |  |
| 13 | first_exchdate | 否 |  |  |
| 14 | date_back | 否 |  |  |
| 15 | settle_end_date | 否 |  |  |
| 16 | component_num | 否 |  |  |
| 17 | old_impawn_code | 否 |  |  |
| 18 | impawn_amount | 否 |  |  |
| 19 | funder_ratio | 否 |  |  |
| 20 | impawn_balance | 否 |  |  |
| 21 | prev_impawn_balance | 否 |  |  |
| 22 | profit | 否 |  |  |
| 23 | settle_balance | 否 |  |  |
| 24 | asset_net_value | 否 |  |  |
| 25 | bprsrc_status | 否 |  |  |
| 26 | orig_entrust_date | 否 |  |  |
| 27 | orig_cbpconfer_id | 否 |  |  |
| 28 | agency_no | 否 |  |  |
| 29 | trader_id | 否 |  |  |
| 30 | stock_account | 否 |  |  |
| 31 | seat_no | 否 |  |  |
| 32 | oppo_agency | 否 |  |  |
| 33 | oppo_trader_id | 否 |  |  |
| 34 | prop_stock_account | 否 |  |  |
| 35 | prop_seat_no | 否 |  |  |
| 36 | agency_name | 否 |  |  |
| 37 | hq_status | 否 |  |  |
| 38 | position_str | 否 |  |  |
| 39 | oppo_agency_name | 否 |  |  |
| 40 | prop_account_name | 否 |  |  |
| 41 | remark | 否 |  |  |
| 42 | serial_no | 否 |  |  |
| 43 | modify_time | 否 |  |  |
| 44 | stock_name | 否 | H |  |
| 45 | sub_stock_type | 否 | H |  |
| 46 | init_date | 否 |  |  |
| 47 | cbpconfer_id | 否 |  |  |
| 48 | entrust_no | 否 |  |  |
| 49 | bpr_hq_type | 否 |  |  |
| 50 | entrust_prop | 否 |  |  |
| 51 | entrust_bs | 否 |  |  |
| 52 | exchange_type | 否 |  |  |
| 53 | stock_type | 否 |  |  |
| 54 | stock_code | 否 |  |  |
| 55 | expire_year_rate | 否 |  |  |
| 56 | repo_term | 否 |  |  |
| 57 | fund_used_days | 否 |  |  |
| 58 | first_exchdate | 否 |  |  |
| 59 | date_back | 否 |  |  |
| 60 | settle_end_date | 否 |  |  |
| 61 | component_num | 否 |  |  |
| 62 | old_impawn_code | 否 |  |  |
| 63 | impawn_amount | 否 |  |  |
| 64 | funder_ratio | 否 |  |  |
| 65 | impawn_balance | 否 |  |  |
| 66 | prev_impawn_balance | 否 |  |  |
| 67 | profit | 否 |  |  |
| 68 | settle_balance | 否 |  |  |
| 69 | asset_net_value | 否 |  |  |
| 70 | bprsrc_status | 否 |  |  |
| 71 | orig_entrust_date | 否 |  |  |
| 72 | orig_cbpconfer_id | 否 |  |  |
| 73 | agency_no | 否 |  |  |
| 74 | trader_id | 否 |  |  |
| 75 | stock_account | 否 |  |  |
| 76 | seat_no | 否 |  |  |
| 77 | oppo_agency | 否 |  |  |
| 78 | oppo_trader_id | 否 |  |  |
| 79 | prop_stock_account | 否 |  |  |
| 80 | prop_seat_no | 否 |  |  |
| 81 | agency_name | 否 |  |  |
| 82 | hq_status | 否 |  |  |
| 83 | position_str | 否 |  |  |
| 84 | oppo_agency_name | 否 |  |  |
| 85 | prop_account_name | 否 |  |  |
| 86 | remark | 否 |  |  |
| 87 | serial_no | 否 |  |  |
| 88 | modify_time | 否 |  |  |
| 89 | stock_name | 否 | H |  |
| 90 | sub_stock_type | 否 | H |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_bprinfo_pos | ART | 是 | position_str, position_str |
| idx_uqms_bprinfo | ART | 是 | bpr_hq_type, cbpconfer_id, init_date, bpr_hq_type, cbpconfer_id, init_date |
| uk_rpt_uqmsbprinfo | ART | 是 | init_date, position_str, init_date, position_str |
| idx_uqms_bprinfo_pos | ART | 是 | position_str, position_str |
| idx_uqms_bprinfo | ART | 是 | bpr_hq_type, cbpconfer_id, init_date, bpr_hq_type, cbpconfer_id, init_date |
| uk_rpt_uqmsbprinfo | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_bprinfo_pos | position_str, position_str |
| idx_uqms_bprinfo_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:47:03 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-05-06 10:43:12 | 3.0.2.13 | 周富安 | 新增 |
| 2026-03-05 16:47:03 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-05-06 10:43:12 | 3.0.2.13 | 周富安 | 新增 |

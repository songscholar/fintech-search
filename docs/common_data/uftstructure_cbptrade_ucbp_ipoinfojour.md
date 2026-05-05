# ucbp_ipoinfojour - 新股申购信息流水表

**表对象ID**: 2310
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 84 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | op_branch_no | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_station | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | serial_no | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | asset_prop | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | ipo_lucky_amount | 否 |  |  |
| 16 | lucky_balance | 否 |  |  |
| 17 | ipo_accancel_amount | 否 |  |  |
| 18 | ipo_pacancel_amount | 否 |  |  |
| 19 | ipo_short_balance | 否 |  |  |
| 20 | unfrozen_balance | 否 |  |  |
| 21 | ipo_info_status | 否 |  |  |
| 22 | ipo_report_flag | 否 |  |  |
| 23 | date_clear | 否 |  |  |
| 24 | remark | 否 |  |  |
| 25 | position_str | 否 |  | init_date(8)+branch_no(5)+asset_prop(1)+stock_account(10)+st |
| 26 | order_no | 否 |  |  |
| 27 | stock_type | 否 |  |  |
| 28 | frozen_balance | 否 |  |  |
| 29 | frozen_balance_t1 | 否 |  |  |
| 30 | business_frozen_balance | 否 |  |  |
| 31 | branch_no | 否 | H |  |
| 32 | client_name | 否 | H |  |
| 33 | corp_client_group | 否 | H |  |
| 34 | client_group | 否 | H |  |
| 35 | room_code | 否 | H |  |
| 36 | limit_flag | 否 | H |  |
| 37 | client_prop | 否 | H |  |
| 38 | asset_level | 否 | H |  |
| 39 | risk_level | 否 | H |  |
| 40 | corp_risk_level | 否 | H |  |
| 41 | stock_name | 否 | H |  |
| 42 | sub_stock_type | 否 | H |  |
| 43 | init_date | 否 |  |  |
| 44 | curr_date | 否 |  |  |
| 45 | curr_time | 否 |  |  |
| 46 | op_branch_no | 否 |  |  |
| 47 | operator_no | 否 |  |  |
| 48 | op_station | 否 |  |  |
| 49 | op_entrust_way | 否 |  |  |
| 50 | exchange_type | 否 |  |  |
| 51 | serial_no | 否 |  |  |
| 52 | client_id | 否 |  |  |
| 53 | fund_account | 否 |  |  |
| 54 | asset_prop | 否 |  |  |
| 55 | stock_account | 否 |  |  |
| 56 | stock_code | 否 |  |  |
| 57 | ipo_lucky_amount | 否 |  |  |
| 58 | lucky_balance | 否 |  |  |
| 59 | ipo_accancel_amount | 否 |  |  |
| 60 | ipo_pacancel_amount | 否 |  |  |
| 61 | ipo_short_balance | 否 |  |  |
| 62 | unfrozen_balance | 否 |  |  |
| 63 | ipo_info_status | 否 |  |  |
| 64 | ipo_report_flag | 否 |  |  |
| 65 | date_clear | 否 |  |  |
| 66 | remark | 否 |  |  |
| 67 | position_str | 否 |  | init_date(8)+branch_no(5)+asset_prop(1)+stock_account(10)+st |
| 68 | order_no | 否 |  |  |
| 69 | stock_type | 否 |  |  |
| 70 | frozen_balance | 否 |  |  |
| 71 | frozen_balance_t1 | 否 |  |  |
| 72 | business_frozen_balance | 否 |  |  |
| 73 | branch_no | 否 | H |  |
| 74 | client_name | 否 | H |  |
| 75 | corp_client_group | 否 | H |  |
| 76 | client_group | 否 | H |  |
| 77 | room_code | 否 | H |  |
| 78 | limit_flag | 否 | H |  |
| 79 | client_prop | 否 | H |  |
| 80 | asset_level | 否 | H |  |
| 81 | risk_level | 否 | H |  |
| 82 | corp_risk_level | 否 | H |  |
| 83 | stock_name | 否 | H |  |
| 84 | sub_stock_type | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucbp_ipoinfojour_serial_no | 默认 | 否 |  |
| idx_ucbp_ipoinfojour_serial_no | 默认 | 否 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| idx_ucbp_ipoinfojour | ART | 是 | fund_account, stock_code, exchange_type, init_date, fund_account, stock_code, exchange_type, init_date |
| idx_ucbp_ipoinfojour_serial_no | ART | 是 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| uk_rpt_ucbpipoinfojour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucbpipoinfojour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_ucbp_ipoinfojour_serial_no | 默认 | 否 |  |
| idx_ucbp_ipoinfojour_serial_no | 默认 | 否 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| idx_ucbp_ipoinfojour | ART | 是 | fund_account, stock_code, exchange_type, init_date, fund_account, stock_code, exchange_type, init_date |
| idx_ucbp_ipoinfojour_serial_no | ART | 是 | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| uk_rpt_ucbpipoinfojour | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucbpipoinfojour_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucbp_ipoinfojour_serial_no | init_date, fund_account, serial_no, init_date, fund_account, serial_no |
| idx_ucbp_ipoinfojour_serial_no | init_date, fund_account, serial_no, init_date, fund_account, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:15:06 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-18 16:23:25 | V3.0.2.59 | 钟兆星 | 删除索引idx_ucbp_ipoinfojour_stock_account |
| 2024-12-27 14:28:13 | V3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-10-04 17:02:20 | V3.0.3.8 | 黄佳平 | 物理表ucbp_ipoinfojour，添加了表字段(business_frozen_balance);
 |
| 2024-05-21 21:21:52 | V3.0.1.9 | 乐闽庭 | 删除内存表索引 idx_ucbp_ipoinfojour_stock_account |
| 2023-09-30 10:51:36 | V3.0.1.5 | huangzh | 物理表ucbp_ipoinfojour，增加索引(idx_ucbp_ipoinfojour_serial_no:[ini... |
| 2026-03-04 15:15:06 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-18 16:23:25 | V3.0.2.59 | 钟兆星 | 删除索引idx_ucbp_ipoinfojour_stock_account |
| 2024-12-27 14:28:13 | V3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-10-04 17:02:20 | V3.0.3.8 | 黄佳平 | 物理表ucbp_ipoinfojour，添加了表字段(business_frozen_balance);
 |
| 2024-05-21 21:21:52 | V3.0.1.9 | 乐闽庭 | 删除内存表索引 idx_ucbp_ipoinfojour_stock_account |
| 2023-09-30 10:51:36 | V3.0.1.5 | huangzh | 物理表ucbp_ipoinfojour，增加索引(idx_ucbp_ipoinfojour_serial_no:[ini... |

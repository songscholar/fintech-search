# ucbp_ipoinfo - 新股申购信息表

**表对象ID**: 2309
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 74 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | asset_prop | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | ipo_lucky_amount | 否 |  |  |
| 9 | lucky_balance | 否 |  |  |
| 10 | ipo_accancel_amount | 否 |  |  |
| 11 | ipo_pacancel_amount | 否 |  |  |
| 12 | ipo_short_balance | 否 |  |  |
| 13 | unfrozen_balance | 否 |  |  |
| 14 | ipo_info_status | 否 |  |  |
| 15 | ipo_report_flag | 否 |  |  |
| 16 | date_clear | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | order_no | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | frozen_balance | 否 |  |  |
| 21 | entrust_date | 否 |  |  |
| 22 | entrust_no | 否 |  |  |
| 23 | frozen_balance_t1 | 否 |  |  |
| 24 | business_frozen_balance | 否 |  |  |
| 25 | position_str | 否 |  | 拼串规则：init_date(8位,不足前补0)+@branch_no(5位,不足前补0)+asset_prop+sto |
| 26 | branch_no | 否 | H |  |
| 27 | stock_name | 否 | H |  |
| 28 | sub_stock_type | 否 | H |  |
| 29 | client_group | 否 | H |  |
| 30 | room_code | 否 | H |  |
| 31 | limit_flag | 否 | H |  |
| 32 | risk_level | 否 | H |  |
| 33 | corp_client_group | 否 | H |  |
| 34 | corp_risk_level | 否 | H |  |
| 35 | asset_level | 否 | H |  |
| 36 | client_name | 否 | H |  |
| 37 | client_prop | 否 | H |  |
| 38 | init_date | 否 |  |  |
| 39 | exchange_type | 否 |  |  |
| 40 | client_id | 否 |  |  |
| 41 | fund_account | 否 |  |  |
| 42 | asset_prop | 否 |  |  |
| 43 | stock_account | 否 |  |  |
| 44 | stock_code | 否 |  |  |
| 45 | ipo_lucky_amount | 否 |  |  |
| 46 | lucky_balance | 否 |  |  |
| 47 | ipo_accancel_amount | 否 |  |  |
| 48 | ipo_pacancel_amount | 否 |  |  |
| 49 | ipo_short_balance | 否 |  |  |
| 50 | unfrozen_balance | 否 |  |  |
| 51 | ipo_info_status | 否 |  |  |
| 52 | ipo_report_flag | 否 |  |  |
| 53 | date_clear | 否 |  |  |
| 54 | remark | 否 |  |  |
| 55 | order_no | 否 |  |  |
| 56 | stock_type | 否 |  |  |
| 57 | frozen_balance | 否 |  |  |
| 58 | entrust_date | 否 |  |  |
| 59 | entrust_no | 否 |  |  |
| 60 | frozen_balance_t1 | 否 |  |  |
| 61 | business_frozen_balance | 否 |  |  |
| 62 | position_str | 否 |  | 拼串规则：init_date(8位,不足前补0)+@branch_no(5位,不足前补0)+asset_prop+sto |
| 63 | branch_no | 否 | H |  |
| 64 | stock_name | 否 | H |  |
| 65 | sub_stock_type | 否 | H |  |
| 66 | client_group | 否 | H |  |
| 67 | room_code | 否 | H |  |
| 68 | limit_flag | 否 | H |  |
| 69 | risk_level | 否 | H |  |
| 70 | corp_client_group | 否 | H |  |
| 71 | corp_risk_level | 否 | H |  |
| 72 | asset_level | 否 | H |  |
| 73 | client_name | 否 | H |  |
| 74 | client_prop | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucbp_ipoinfo | 默认 | 否 |  |
| idx_ucbp_ipoinfo | 默认 | 否 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucbp_ipoinfo | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucbp_ipoinfo_stock_account | ART | 是 | stock_account, stock_code, stock_account, stock_code |
| uk_rpt_ucbpipoinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucbpipoinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucbpipoinfo_tolast | ART | 是 | date_clear, date_clear |
| idx_ucbp_ipoinfo | 默认 | 否 |  |
| idx_ucbp_ipoinfo | 默认 | 否 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucbp_ipoinfo | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucbp_ipoinfo_stock_account | ART | 是 | stock_account, stock_code, stock_account, stock_code |
| uk_rpt_ucbpipoinfo | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_ucbpipoinfo_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_rpt_ucbpipoinfo_tolast | ART | 是 | date_clear, date_clear |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucbp_ipoinfo | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucbp_ipoinfo | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:13:24 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.8.9 | 周兆军 | 维护历史表 |
| 2025-04-17 16:10:33 | V3.0.2.56 | 董乾坤 | 物理表ucbp_ipoinfo，添加了表字段(position_str);
 |
| 2024-10-04 16:30:48 | V3.0.3.8 | 黄佳平 | 物理表ucbp_ipoinfo，添加了表字段(business_frozen_balance);
 |
| 2023-10-17 09:42:54 | V3.0.1.7 | 阮善宏 | 物理表ucbp_ipoinfo，增加分级索引(idx_ucbp_ipoinfo:[fund_account|][stoc... |
| 2023-09-30 10:44:49 | V3.0.1.5 | huangzh | 物理表ucbp_ipoinfo，增加索引(idx_ucbp_ipoinfo:[fund_account,stock_co... |
| 2026-03-04 15:13:24 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-11-21 19:56:55 | V3.0.8.9 | 周兆军 | 维护历史表 |
| 2025-04-17 16:10:33 | V3.0.2.56 | 董乾坤 | 物理表ucbp_ipoinfo，添加了表字段(position_str);
 |
| 2024-10-04 16:30:48 | V3.0.3.8 | 黄佳平 | 物理表ucbp_ipoinfo，添加了表字段(business_frozen_balance);
 |
| 2023-10-17 09:42:54 | V3.0.1.7 | 阮善宏 | 物理表ucbp_ipoinfo，增加分级索引(idx_ucbp_ipoinfo:[fund_account|][stoc... |
| 2023-09-30 10:44:49 | V3.0.1.5 | huangzh | 物理表ucbp_ipoinfo，增加索引(idx_ucbp_ipoinfo:[fund_account,stock_co... |

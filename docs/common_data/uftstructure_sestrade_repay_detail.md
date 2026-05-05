# repay_detail - 卖券还款明细表

**表对象ID**: 5734
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 68 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | contract_id | 否 |  |  |
| 4 | join_contract_id | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | stock_sell_type | 否 |  |  |
| 10 | entrust_amount | 否 |  |  |
| 11 | business_amount | 否 |  |  |
| 12 | business_balance | 否 |  |  |
| 13 | business_price | 否 |  |  |
| 14 | entrust_status | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+entrust_no(10) |
| 17 | join_busin_id | 否 |  |  |
| 18 | join_report_id | 否 |  |  |
| 19 | entrust_prop | 否 |  |  |
| 20 | clear_balance | 否 |  |  |
| 21 | position_num | 否 |  |  |
| 22 | client_id | 否 | H |  |
| 23 | client_name | 否 | H |  |
| 24 | corp_client_group | 否 | H |  |
| 25 | client_group | 否 | H |  |
| 26 | room_code | 否 | H |  |
| 27 | limit_flag | 否 | H |  |
| 28 | client_prop | 否 | H |  |
| 29 | asset_level | 否 | H |  |
| 30 | risk_level | 否 | H |  |
| 31 | corp_risk_level | 否 | H |  |
| 32 | stock_name | 否 | H |  |
| 33 | stock_type | 否 | H |  |
| 34 | sub_stock_type | 否 | H |  |
| 35 | init_date | 否 |  |  |
| 36 | entrust_no | 否 |  |  |
| 37 | contract_id | 否 |  |  |
| 38 | join_contract_id | 否 |  |  |
| 39 | branch_no | 否 |  |  |
| 40 | fund_account | 否 |  |  |
| 41 | exchange_type | 否 |  |  |
| 42 | stock_code | 否 |  |  |
| 43 | stock_sell_type | 否 |  |  |
| 44 | entrust_amount | 否 |  |  |
| 45 | business_amount | 否 |  |  |
| 46 | business_balance | 否 |  |  |
| 47 | business_price | 否 |  |  |
| 48 | entrust_status | 否 |  |  |
| 49 | remark | 否 |  |  |
| 50 | position_str | 否 |  | init_date(8)+node_id(2)+branch_no(5)+entrust_no(10) |
| 51 | join_busin_id | 否 |  |  |
| 52 | join_report_id | 否 |  |  |
| 53 | entrust_prop | 否 |  |  |
| 54 | clear_balance | 否 |  |  |
| 55 | position_num | 否 |  |  |
| 56 | client_id | 否 | H |  |
| 57 | client_name | 否 | H |  |
| 58 | corp_client_group | 否 | H |  |
| 59 | client_group | 否 | H |  |
| 60 | room_code | 否 | H |  |
| 61 | limit_flag | 否 | H |  |
| 62 | client_prop | 否 | H |  |
| 63 | asset_level | 否 | H |  |
| 64 | risk_level | 否 | H |  |
| 65 | corp_risk_level | 否 | H |  |
| 66 | stock_name | 否 | H |  |
| 67 | stock_type | 否 | H |  |
| 68 | sub_stock_type | 否 | H |  |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_repay_detail | ART | 是 | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |
| idx_repay_detail_cont | ART | 是 | contract_id, contract_id |
| idx_repay_detail_acct | ART | 是 | fund_account, fund_account |
| idx_repay_detail_rpt | ART | 是 | join_report_id, init_date, join_report_id, init_date |
| uk_rpt_repaydetail | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_repaydetail_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |
| idx_repay_detail | ART | 是 | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |
| idx_repay_detail_cont | ART | 是 | contract_id, contract_id |
| idx_repay_detail_acct | ART | 是 | fund_account, fund_account |
| idx_repay_detail_rpt | ART | 是 | join_report_id, init_date, join_report_id, init_date |
| uk_rpt_repaydetail | ART | 是 | init_date, branch_no, position_str, init_date, branch_no, position_str |
| idx_rpt_repaydetail_cid | ART | 是 | init_date, client_id, fund_account, position_str, init_date, client_id, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_repay_detail | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |
| idx_repay_detail | entrust_no, branch_no, init_date, entrust_no, branch_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:39:52 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-17 15:53:18 | 3.0.2.66 | 於达 | 内存表repay_detail，添加了表字段(position_num);
 |
| 2025-04-17 15:50:14 | 3.0.2.66 | 於达 | 内存表repay_detail，删除了表字段(position_int);
 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2026-03-09 14:39:52 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-09 09:35:46 | V3.0.2.2003 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-17 15:53:18 | 3.0.2.66 | 於达 | 内存表repay_detail，添加了表字段(position_num);
 |
| 2025-04-17 15:50:14 | 3.0.2.66 | 於达 | 内存表repay_detail，删除了表字段(position_int);
 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |

# settredo_etf_ustock - 清算重做网下股份认购信息表

**表对象ID**: 5998
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | component_code | 否 |  |  |
| 2 | entrust_status | 否 |  |  |
| 3 | prev_status | 否 |  |  |
| 4 | confirm_amount | 否 |  |  |
| 5 | report_date | 否 |  |  |
| 6 | remark | 否 |  |  |
| 7 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 8 | sett_batch_no | 否 |  |  |
| 9 | component_code | 否 |  |  |
| 10 | entrust_status | 否 |  |  |
| 11 | prev_status | 否 |  |  |
| 12 | confirm_amount | 否 |  |  |
| 13 | report_date | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 16 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_etf_ustock_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_etf_ustock_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_etf_ustock_pos | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_etf_ustock_pos | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:57:42 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:42:04 | 3.0.6.1004 | yangxz |  |
| 2026-03-09 14:57:42 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:42:04 | 3.0.6.1004 | yangxz |  |

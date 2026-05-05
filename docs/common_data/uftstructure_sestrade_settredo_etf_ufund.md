# settredo_etf_ufund - 清算重做网下现金认购信息表

**表对象ID**: 5999
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | entrust_status | 否 |  |  |
| 2 | prev_status | 否 |  |  |
| 3 | remark | 否 |  |  |
| 4 | report_date | 否 |  |  |
| 5 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 6 | sett_batch_no | 否 |  |  |
| 7 | entrust_status | 否 |  |  |
| 8 | prev_status | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | report_date | 否 |  |  |
| 11 | position_str | 否 |  | branch_no(5)+exchange_type(4)+stock_account(10)+stock_code(6 |
| 12 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_etf_ufund_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_etf_ufund_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_etf_ufund_pos | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_etf_ufund_pos | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:58:06 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:47:02 | 3.0.6.1010 | yangxz |  |
| 2026-03-09 14:58:06 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:47:02 | 3.0.6.1010 | yangxz |  |

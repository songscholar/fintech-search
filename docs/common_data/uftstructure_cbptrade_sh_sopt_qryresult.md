# sh_sopt_qryresult - 上海现金担保品指令查询结果表

**表对象ID**: 2488
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | reserve_account | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | entrust_prop | 否 |  |  |
| 9 | entrust_amount | 否 |  |  |
| 10 | business_amount | 否 |  |  |
| 11 | return_serial_no | 否 |  |  |
| 12 | position_str | 否 |  | init_date(8)+entrust_no(10)+return_serial_no(16) |
| 13 | return_code | 否 |  |  |
| 14 | return_info | 否 |  |  |
| 15 | init_date | 否 |  |  |
| 16 | entrust_no | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | client_id | 否 |  |  |
| 20 | reserve_account | 否 |  |  |
| 21 | stock_account | 否 |  |  |
| 22 | entrust_prop | 否 |  |  |
| 23 | entrust_amount | 否 |  |  |
| 24 | business_amount | 否 |  |  |
| 25 | return_serial_no | 否 |  |  |
| 26 | position_str | 否 |  | init_date(8)+entrust_no(10)+return_serial_no(16) |
| 27 | return_code | 否 |  |  |
| 28 | return_info | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_shsoptqryresult | ART | 是 | init_date, entrust_no, return_serial_no, branch_no, init_date, entrust_no, return_serial_no, branch_no |
| idx_shsoptqryresult_if | ART | 是 | init_date, fund_account, init_date, fund_account |
| idx_shsoptqryresult_pos | ART | 是 | init_date, position_str, init_date, position_str |
| idx_shsoptqryresult | ART | 是 | init_date, entrust_no, return_serial_no, branch_no, init_date, entrust_no, return_serial_no, branch_no |
| idx_shsoptqryresult_if | ART | 是 | init_date, fund_account, init_date, fund_account |
| idx_shsoptqryresult_pos | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_shsoptqryresult | init_date, entrust_no, return_serial_no, branch_no, init_date, entrust_no, return_serial_no, branch_no |
| idx_shsoptqryresult | init_date, entrust_no, return_serial_no, branch_no, init_date, entrust_no, return_serial_no, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:48:06 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-11-28 10:22:47 | 3.0.2.48 | 王云乾 | 新增 |
| 2026-03-04 15:48:06 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-11-28 10:22:47 | 3.0.2.48 | 王云乾 | 新增 |

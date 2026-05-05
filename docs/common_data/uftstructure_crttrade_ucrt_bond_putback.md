# ucrt_bond_putback - 债券回售业务表

**表对象ID**: 7515
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | trustee_seat_no | 否 |  |  |
| 7 | revocable_amount | 否 |  |  |
| 8 | begin_amount | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | order_no | 是 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | trustee_seat_no | 否 |  |  |
| 17 | revocable_amount | 否 |  |  |
| 18 | begin_amount | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | order_no | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_bond_putback | ART | 是 | fund_account, stock_account, stock_code, exchange_type, trustee_seat_no, fund_account, stock_account, stock_code, exchange_type, trustee_seat_no |
| idx_ucrt_bond_putback | ART | 是 | fund_account, stock_account, stock_code, exchange_type, trustee_seat_no, fund_account, stock_account, stock_code, exchange_type, trustee_seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_bond_putback | fund_account, stock_account, stock_code, exchange_type, trustee_seat_no, fund_account, stock_account, stock_code, exchange_type, trustee_seat_no |
| idx_ucrt_bond_putback | fund_account, stock_account, stock_code, exchange_type, trustee_seat_no, fund_account, stock_account, stock_code, exchange_type, trustee_seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-12 15:55:35 | 3.0.8.16 | xucq | 所有表ucrt_bond_putback，添加了表字段(order_no);
 |
| 2025-05-09 13:45:41 | 3.0.6.54 | 袁文龙 | 修改内存表索引idx_ucrt_bond_putback为分级索引 |
| 2025-02-18 20:47:33 | 3.0.6.37 | 牟家乐 | 物理表ucrt_bond_putback，添加了表字段(remark);
 |
| 2024-07-22 13:25:27 | 3.0.3.4 | 袁文龙 | 修复关联字段和关联索引字段重复 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-12 15:55:35 | 3.0.8.16 | xucq | 所有表ucrt_bond_putback，添加了表字段(order_no);
 |
| 2025-05-09 13:45:41 | 3.0.6.54 | 袁文龙 | 修改内存表索引idx_ucrt_bond_putback为分级索引 |
| 2025-02-18 20:47:33 | 3.0.6.37 | 牟家乐 | 物理表ucrt_bond_putback，添加了表字段(remark);
 |
| 2024-07-22 13:25:27 | 3.0.3.4 | 袁文龙 | 修复关联字段和关联索引字段重复 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

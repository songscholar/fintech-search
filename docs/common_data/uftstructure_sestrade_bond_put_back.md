# bond_put_back - 证券债券回售业务表

**表对象ID**: 5522
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | trustee_seat_no | 否 |  |  |
| 7 | revocable_amount | 否 |  |  |
| 8 | begin_amount | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | order_no | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | stock_account | 否 |  |  |
| 14 | client_id | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | trustee_seat_no | 否 |  |  |
| 17 | revocable_amount | 否 |  |  |
| 18 | begin_amount | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | order_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bond_put_back | ART | 是 | fund_account, stock_account, stock_code, exchange_type, trustee_seat_no, fund_account, stock_account, stock_code, exchange_type, trustee_seat_no |
| idx_bond_put_back | ART | 是 | fund_account, stock_account, stock_code, exchange_type, trustee_seat_no, fund_account, stock_account, stock_code, exchange_type, trustee_seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bond_put_back | fund_account, stock_account, stock_code, exchange_type, trustee_seat_no, fund_account, stock_account, stock_code, exchange_type, trustee_seat_no |
| idx_bond_put_back | fund_account, stock_account, stock_code, exchange_type, trustee_seat_no, fund_account, stock_account, stock_code, exchange_type, trustee_seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:45:14 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-04-25 22:22:38 | 3.0.1.429 | 阮善宏 | 表名调整为证券债券回售业务表 |
| 2026-03-09 13:45:14 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-04-25 22:22:38 | 3.0.1.429 | 阮善宏 | 表名调整为证券债券回售业务表 |

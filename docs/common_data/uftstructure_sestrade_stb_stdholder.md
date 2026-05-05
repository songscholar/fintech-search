# stb_stdholder - 三板合规证券账户表

**表对象ID**: 5831
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | sub_risk_status | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | position_str | 否 |  | stock_code(8)+stock_account(20)+exchange_type(4) |
| 7 | stock_code | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | sub_risk_status | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | position_str | 否 |  | stock_code(8)+stock_account(20)+exchange_type(4) |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stb_stdholder | ART | 是 | stock_code, stock_account, exchange_type, stock_code, stock_account, exchange_type |
| idx_stb_stdholder_acct | ART | 是 | stock_account, stock_account |
| idx_stb_stdholder_pos | ART | 是 | position_str, position_str |
| idx_stb_stdholder | ART | 是 | stock_code, stock_account, exchange_type, stock_code, stock_account, exchange_type |
| idx_stb_stdholder_acct | ART | 是 | stock_account, stock_account |
| idx_stb_stdholder_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stb_stdholder | stock_code, stock_account, exchange_type, stock_code, stock_account, exchange_type |
| idx_stb_stdholder | stock_code, stock_account, exchange_type, stock_code, stock_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:45:49 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-27 20:23:22 | 3.0.2.74 | 全春辉 | 物理表stb_stdholder，添加了表字段(position_str);
 |
| 2024-06-18 10:27:24 | 3.0.2.21 | 吴威 | 物理表stb_stdholder，添加了表字段(transaction_no);
支持不回库 |
| 2024-06-14 10:46:23 | 3.0.2.19 | 乐闽庭 | 物理表stb_stdholder，删除了表字段(seat_no);
物理表stb_stdholder，删除了表字段(i... |
| 2026-03-09 14:45:49 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-27 20:23:22 | 3.0.2.74 | 全春辉 | 物理表stb_stdholder，添加了表字段(position_str);
 |
| 2024-06-18 10:27:24 | 3.0.2.21 | 吴威 | 物理表stb_stdholder，添加了表字段(transaction_no);
支持不回库 |
| 2024-06-14 10:46:23 | 3.0.2.19 | 乐闽庭 | 物理表stb_stdholder，删除了表字段(seat_no);
物理表stb_stdholder，删除了表字段(i... |

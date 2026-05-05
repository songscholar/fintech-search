# bond_rateinf - 国债折算率通知表

**表对象ID**: 313
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | begin_date | 否 |  |  |
| 4 | end_date | 否 |  |  |
| 5 | impawn_rate | 否 |  |  |
| 6 | impawn_code | 否 |  |  |
| 7 | modify_date | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | stock_code(8)+exchange_type(4)+begin_date(8) |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | begin_date | 否 |  |  |
| 15 | end_date | 否 |  |  |
| 16 | impawn_rate | 否 |  |  |
| 17 | impawn_code | 否 |  |  |
| 18 | modify_date | 否 |  |  |
| 19 | transaction_no | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | stock_code(8)+exchange_type(4)+begin_date(8) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bond_rateinf | 默认 | 否 | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |
| idx_bond_rateinf | ART | 是 | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |
| idx_bond_rateinf | 默认 | 否 | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |
| idx_bond_rateinf | ART | 是 | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bond_rateinf | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |
| idx_bond_rateinf | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 17:04:48 | 3.0.6.68 | 李想 | 物理表bond_rateinf，添加了表字段(update_date);
物理表bond_rateinf，添加了表字段... |
| 2024-07-18 11:12:46 | 3.0.2.23 | 张云焘 | 物理表bond_rateinf，添加了表字段(transaction_no);
 |
| 2023-12-17 20:30:07 | 3.0.1.18 | 全春辉 | 物理表增加索引 |
| 2025-02-18 17:04:48 | 3.0.6.68 | 李想 | 物理表bond_rateinf，添加了表字段(update_date);
物理表bond_rateinf，添加了表字段... |
| 2024-07-18 11:12:46 | 3.0.2.23 | 张云焘 | 物理表bond_rateinf，添加了表字段(transaction_no);
 |
| 2023-12-17 20:30:07 | 3.0.1.18 | 全春辉 | 物理表增加索引 |

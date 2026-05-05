# bond_impawn_arg - 债券回购参数表

**表对象ID**: 5557
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | old_client_conc_ratio | 否 |  |  |
| 5 | new_client_conc_ratio | 否 |  |  |
| 6 | trustee_amount | 否 |  |  |
| 7 | par_ratio | 否 |  |  |
| 8 | company_conc_ratio | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | old_client_conc_ratio | 否 |  |  |
| 17 | new_client_conc_ratio | 否 |  |  |
| 18 | trustee_amount | 否 |  |  |
| 19 | par_ratio | 否 |  |  |
| 20 | company_conc_ratio | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bondimpawnarg | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_bondimpawnarg | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bondimpawnarg | stock_code, exchange_type, stock_code, exchange_type |
| idx_bondimpawnarg | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-20 11:44:29 | 3.0.6.16 | 李想 | 物理表bond_impawn_arg，添加了表字段(update_date);
物理表bond_impawn_arg，... |
| 2024-07-18 11:21:00 | 3.0.2.29 | 张云焘 | 物理表bond_impawn_arg，添加了表字段(transaction_no);
 |
| 2025-02-20 11:44:29 | 3.0.6.16 | 李想 | 物理表bond_impawn_arg，添加了表字段(update_date);
物理表bond_impawn_arg，... |
| 2024-07-18 11:21:00 | 3.0.2.29 | 张云焘 | 物理表bond_impawn_arg，添加了表字段(transaction_no);
 |

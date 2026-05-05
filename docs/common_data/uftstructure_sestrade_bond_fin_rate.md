# bond_fin_rate - 债券融资折算信息表

**表对象ID**: 5551
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | organ_flag | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | fin_rate | 否 |  |  |
| 5 | en_bond_level | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |
| 11 | fund_account | 否 |  |  |
| 12 | organ_flag | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | fin_rate | 否 |  |  |
| 15 | en_bond_level | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | update_date | 否 |  |  |
| 19 | update_time | 否 |  |  |
| 20 | position_str | 否 |  | init_date(8)+branch_no(6)+serial_no(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bond_fin_rate | ART | 是 | fund_account, organ_flag, exchange_type, en_bond_level, fund_account, organ_flag, exchange_type, en_bond_level |
| idx_bond_fin_rate | ART | 是 | fund_account, organ_flag, exchange_type, en_bond_level, fund_account, organ_flag, exchange_type, en_bond_level |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bond_fin_rate | fund_account, organ_flag, exchange_type, en_bond_level, fund_account, organ_flag, exchange_type, en_bond_level |
| idx_bond_fin_rate | fund_account, organ_flag, exchange_type, en_bond_level, fund_account, organ_flag, exchange_type, en_bond_level |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:03:31 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 13:40:54 | 3.0.6.21 | 李想 | 物理表bond_fin_rate，添加了表字段(branch_no);
物理表bond_fin_rate，添加了表字段... |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |
| 2026-03-09 14:03:31 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 13:40:54 | 3.0.6.21 | 李想 | 物理表bond_fin_rate，添加了表字段(branch_no);
物理表bond_fin_rate，添加了表字段... |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |

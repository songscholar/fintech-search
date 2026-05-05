# usps_farestandard - 规费设置表

**表对象ID**: 55
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | index_field | 否 |  |  |
| 3 | en_exchange_type | 否 |  |  |
| 4 | en_stock_type | 否 |  |  |
| 5 | en_money_type | 否 |  |  |
| 6 | standard_ratio | 否 |  |  |
| 7 | max_ratio | 否 |  |  |
| 8 | entrust_type | 否 |  |  |
| 9 | sub_stock_type | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | index_field | 否 |  |  |
| 13 | en_exchange_type | 否 |  |  |
| 14 | en_stock_type | 否 |  |  |
| 15 | en_money_type | 否 |  |  |
| 16 | standard_ratio | 否 |  |  |
| 17 | max_ratio | 否 |  |  |
| 18 | entrust_type | 否 |  |  |
| 19 | sub_stock_type | 否 |  |  |
| 20 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sps_farestandard | ART | 是 | entrust_type, sub_stock_type, index_field, entrust_type, sub_stock_type, index_field |
| idx_usps_farestandard_uk | ART | 是 | branch_no, index_field, branch_no, index_field |
| idx_sps_farestandard | ART | 是 | entrust_type, sub_stock_type, index_field, entrust_type, sub_stock_type, index_field |
| idx_usps_farestandard_uk | ART | 是 | branch_no, index_field, branch_no, index_field |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_farestandard_uk | branch_no, index_field, branch_no, index_field |
| idx_usps_farestandard_uk | branch_no, index_field, branch_no, index_field |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段，并增加唯一索引idx_usps_farestandard_uk |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段，并增加唯一索引idx_usps_farestandard_uk |

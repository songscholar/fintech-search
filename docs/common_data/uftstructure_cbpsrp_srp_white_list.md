# srp_white_list - 股票质押白名单表

**表对象ID**: 2614
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | registe_date | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | branch_no(6)+client_id(18)+exchange_type(4) |
| 10 | branch_no | 否 |  |  |
| 11 | client_id | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | registe_date | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | branch_no(6)+client_id(18)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpwhitelist | ART | 是 | branch_no, client_id, exchange_type, branch_no, client_id, exchange_type |
| idx_srpwhitelist | ART | 是 | branch_no, client_id, exchange_type, branch_no, client_id, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpwhitelist | branch_no, client_id, exchange_type, branch_no, client_id, exchange_type |
| idx_srpwhitelist | branch_no, client_id, exchange_type, branch_no, client_id, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:49:35 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 17:20:33 | 3.0.3.5 | 李想 | 物理表srp_white_list，添加了表字段(update_date);
物理表srp_white_list，添加... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:28 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:49:35 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 17:20:33 | 3.0.3.5 | 李想 | 物理表srp_white_list，添加了表字段(update_date);
物理表srp_white_list，添加... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:28 | 3.0.3.1 | wuxd | 新增 |

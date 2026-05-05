# usps_srp_rate - 股票质押质押比例表

**表对象ID**: 351
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | impawn_rate | 否 |  |  |
| 4 | modify_date | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_code | 否 |  |  |
| 8 | impawn_rate | 否 |  |  |
| 9 | modify_date | 否 |  |  |
| 10 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srprate | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_srprate | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srprate | exchange_type, stock_code, exchange_type, stock_code |
| idx_srprate | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-17 17:36:51 | 3.0.2.96 | taocong45644 | 物理表usps_srp_rate；去掉不回库的勾选 |
| 2024-12-05 16:39:54 | 3.0.2.33 | 范文浩 | 物理表usps_srp_rate，添加了表字段(transaction_no);
勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.32 | 范文浩 | 补充物理表索引 |
| 2024-10-23 14:44:28 | 3.0.4.3 | wuxd | 新增 |
| 2025-09-17 17:36:51 | 3.0.2.96 | taocong45644 | 物理表usps_srp_rate；去掉不回库的勾选 |
| 2024-12-05 16:39:54 | 3.0.2.33 | 范文浩 | 物理表usps_srp_rate，添加了表字段(transaction_no);
勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.32 | 范文浩 | 补充物理表索引 |
| 2024-10-23 14:44:28 | 3.0.4.3 | wuxd | 新增 |

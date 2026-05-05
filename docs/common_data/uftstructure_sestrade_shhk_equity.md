# shhk_equity - 沪港通权益表

**表对象ID**: 5570
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | entrust_amount | 否 |  |  |
| 7 | hkdc_circulate_type | 否 |  |  |
| 8 | hkdc_authority_type | 否 |  |  |
| 9 | hkdc_authority_times | 否 |  |  |
| 10 | hkdc_market_year | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | frozen_amount | 否 |  |  |
| 13 | position_str | 否 |  |  |
| 14 | init_date | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | entrust_amount | 否 |  |  |
| 20 | hkdc_circulate_type | 否 |  |  |
| 21 | hkdc_authority_type | 否 |  |  |
| 22 | hkdc_authority_times | 否 |  |  |
| 23 | hkdc_market_year | 否 |  |  |
| 24 | seat_no | 否 |  |  |
| 25 | frozen_amount | 否 |  |  |
| 26 | position_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_shhkequity | ART | 是 | fund_account, stock_code, fund_account, stock_code |
| idx_shhkequity_pos | ART | 是 | position_str, position_str |
| idx_shhkequity | ART | 是 | fund_account, stock_code, fund_account, stock_code |
| idx_shhkequity_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_shhkequity_pos | position_str, position_str |
| idx_shhkequity_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:20:35 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:17:49 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-08-01 10:21:51 | 3.0.2.31 | 张云焘 | 新增 |
| 2026-03-09 14:20:35 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-09-09 11:17:49 | 3.0.2.43 | 杨森峰 | 表属性调整为不回库 |
| 2024-08-01 10:21:51 | 3.0.2.31 | 张云焘 | 新增 |

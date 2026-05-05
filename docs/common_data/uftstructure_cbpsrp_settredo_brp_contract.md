# settredo_brp_contract - 清算重做债券质押协议回购合约表

**表对象ID**: 12350
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | stock_type | 否 |  |  |
| 3 | real_year_rate | 否 |  |  |
| 4 | real_back_balance | 否 |  |  |
| 5 | real_date_back | 否 |  |  |
| 6 | brp_contract_status | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | position_str | 否 |  |  |
| 10 | stock_property | 否 |  |  |
| 11 | sett_batch_no | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | stock_type | 否 |  |  |
| 14 | real_year_rate | 否 |  |  |
| 15 | real_back_balance | 否 |  |  |
| 16 | real_date_back | 否 |  |  |
| 17 | brp_contract_status | 否 |  |  |
| 18 | date_clear | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | position_str | 否 |  |  |
| 21 | stock_property | 否 |  |  |
| 22 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_brpcontract_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_brpcontract_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_brpcontract_pos | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_brpcontract_pos | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:03:36 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-04 16:15:06 | V3.0.2.4 | taocong45644 | 新增表 |
| 2026-03-06 17:03:36 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-04 16:15:06 | V3.0.2.4 | taocong45644 | 新增表 |

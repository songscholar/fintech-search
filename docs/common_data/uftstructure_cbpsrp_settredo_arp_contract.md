# settredo_arp_contract - 清算重做约定购回合同表

**表对象ID**: 2652
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | contract_id | 否 |  |  |
| 2 | arp_contract_status | 否 |  |  |
| 3 | bonus_amount | 否 |  |  |
| 4 | bonus_balance | 否 |  |  |
| 5 | date_clear | 否 |  |  |
| 6 | cbp_business_id | 否 |  |  |
| 7 | sett_batch_no | 否 |  |  |
| 8 | contract_id | 否 |  |  |
| 9 | arp_contract_status | 否 |  |  |
| 10 | bonus_amount | 否 |  |  |
| 11 | bonus_balance | 否 |  |  |
| 12 | date_clear | 否 |  |  |
| 13 | cbp_business_id | 否 |  |  |
| 14 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_arpcontract | ART | 是 | sett_batch_no, contract_id, sett_batch_no, contract_id |
| idx_settredo_arpcontract | ART | 是 | sett_batch_no, contract_id, sett_batch_no, contract_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_arpcontract | sett_batch_no, contract_id, sett_batch_no, contract_id |
| idx_settredo_arpcontract | sett_batch_no, contract_id, sett_batch_no, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:01:15 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:52:55 | 3.0.3.17 | yangxz |  |
| 2026-03-06 17:01:15 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:52:55 | 3.0.3.17 | yangxz |  |

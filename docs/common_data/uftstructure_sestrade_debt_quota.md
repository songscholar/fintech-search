# debt_quota - 账户融资回购额度表

**表对象ID**: 5559
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | total_max_quota | 否 |  |  |
| 3 | today_actual_quota | 否 |  |  |
| 4 | used_quota | 否 |  |  |
| 5 | surplus_quota | 否 |  |  |
| 6 | begin_date | 否 |  |  |
| 7 | end_date | 否 |  |  |
| 8 | backdebtquota_type | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | total_max_quota | 否 |  |  |
| 12 | today_actual_quota | 否 |  |  |
| 13 | used_quota | 否 |  |  |
| 14 | surplus_quota | 否 |  |  |
| 15 | begin_date | 否 |  |  |
| 16 | end_date | 否 |  |  |
| 17 | backdebtquota_type | 否 |  |  |
| 18 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_backdebt_quota | ART | 是 | fund_account, backdebtquota_type, fund_account, backdebtquota_type |
| idx_backdebt_quota | ART | 是 | fund_account, backdebtquota_type, fund_account, backdebtquota_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_backdebt_quota | fund_account, backdebtquota_type, fund_account, backdebtquota_type |
| idx_backdebt_quota | fund_account, backdebtquota_type, fund_account, backdebtquota_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:10:12 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-07-18 14:08:28 | 3.0.2.29 | 张云焘 | 物理表debt_quota，添加了表字段(transaction_no);
 |
| 2026-03-09 14:10:12 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-07-18 14:08:28 | 3.0.2.29 | 张云焘 | 物理表debt_quota，添加了表字段(transaction_no);
 |

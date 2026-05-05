# fcssvrfare - 服务费率表

**表对象ID**: 391
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 48 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | svrfare_kind | 否 |  |  |
| 2 | scope_id | 否 |  |  |
| 3 | fare_type | 否 |  |  |
| 4 | fare_cal_mode | 否 |  |  |
| 5 | fare_deal_mode | 否 |  |  |
| 6 | fare_coexist_mode | 否 |  |  |
| 7 | fare_balance_ratio | 否 |  |  |
| 8 | par_balance_ratio | 否 |  |  |
| 9 | fixed_fare | 否 |  |  |
| 10 | max_fare | 否 |  |  |
| 11 | min_fare | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | svrfare_kind | 否 |  |  |
| 14 | scope_id | 否 |  |  |
| 15 | fare_type | 否 |  |  |
| 16 | fare_cal_mode | 否 |  |  |
| 17 | fare_deal_mode | 否 |  |  |
| 18 | fare_coexist_mode | 否 |  |  |
| 19 | fare_balance_ratio | 否 |  |  |
| 20 | par_balance_ratio | 否 |  |  |
| 21 | fixed_fare | 否 |  |  |
| 22 | max_fare | 否 |  |  |
| 23 | min_fare | 否 |  |  |
| 24 | transaction_no | 否 |  |  |
| 25 | svrfare_kind | 否 |  |  |
| 26 | scope_id | 否 |  |  |
| 27 | fare_type | 否 |  |  |
| 28 | fare_cal_mode | 否 |  |  |
| 29 | fare_deal_mode | 否 |  |  |
| 30 | fare_coexist_mode | 否 |  |  |
| 31 | fare_balance_ratio | 否 |  |  |
| 32 | par_balance_ratio | 否 |  |  |
| 33 | fixed_fare | 否 |  |  |
| 34 | max_fare | 否 |  |  |
| 35 | min_fare | 否 |  |  |
| 36 | transaction_no | 否 |  |  |
| 37 | svrfare_kind | 否 |  |  |
| 38 | scope_id | 否 |  |  |
| 39 | fare_type | 否 |  |  |
| 40 | fare_cal_mode | 否 |  |  |
| 41 | fare_deal_mode | 否 |  |  |
| 42 | fare_coexist_mode | 否 |  |  |
| 43 | fare_balance_ratio | 否 |  |  |
| 44 | par_balance_ratio | 否 |  |  |
| 45 | fixed_fare | 否 |  |  |
| 46 | max_fare | 否 |  |  |
| 47 | min_fare | 否 |  |  |
| 48 | transaction_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fcssvrfare | ART | 是 | svrfare_kind, scope_id, svrfare_kind, scope_id |
| idx_fcssvrfare | ART | 是 | svrfare_kind, scope_id, svrfare_kind, scope_id |
| idx_fcssvrfare_mode | ART | 是 | svrfare_kind, fare_coexist_mode, svrfare_kind, fare_coexist_mode |
| idx_fcssvrfare | ART | 是 | svrfare_kind, scope_id, svrfare_kind, scope_id |
| idx_fcssvrfare | ART | 是 | svrfare_kind, scope_id, svrfare_kind, scope_id |
| idx_fcssvrfare_mode | ART | 是 | svrfare_kind, fare_coexist_mode, svrfare_kind, fare_coexist_mode |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_fcssvrfare | svrfare_kind, scope_id, svrfare_kind, scope_id |
| idx_fcssvrfare | svrfare_kind, scope_id, svrfare_kind, scope_id |
| idx_fcssvrfare | svrfare_kind, scope_id, svrfare_kind, scope_id |
| idx_fcssvrfare | svrfare_kind, scope_id, svrfare_kind, scope_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-10 15:06:09 | 3.0.8.4 | 徐世晗 | 添加表 |
| 2025-09-10 15:06:09 | 8.26.2.94 |  |  |
| 2025-09-10 15:06:09 | 3.0.8.4 | 徐世晗 | 添加表 |
| 2025-09-10 15:06:09 | 8.26.2.94 |  |  |

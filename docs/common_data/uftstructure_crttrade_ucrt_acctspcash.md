# ucrt_acctspcash - 客户专项头寸账户表

**表对象ID**: 7510
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | cashgroup_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | crdt_fare_str | 否 |  |  |
| 5 | fare_main_flag | 否 |  |  |
| 6 | bonusalloc_flag | 否 |  |  |
| 7 | spcash_status | 否 |  |  |
| 8 | spcash_cost_fare | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | fin_refcost_fare | 是 |  |  |
| 11 | slo_refcost_fare | 是 |  |  |
| 12 | cashgroup_no | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | crdt_fare_str | 否 |  |  |
| 16 | fare_main_flag | 否 |  |  |
| 17 | bonusalloc_flag | 否 |  |  |
| 18 | spcash_status | 否 |  |  |
| 19 | spcash_cost_fare | 否 |  |  |
| 20 | transaction_no | 否 |  |  |
| 21 | fin_refcost_fare | 是 |  |  |
| 22 | slo_refcost_fare | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_ucrt_acctspcash | ART | 是 | cashgroup_no, cashgroup_no |
| idx_ucrt_ucrt_fundspcash | ART | 是 | fund_account, fund_account |
| idx_ucrt_ucrt_acctspcash | ART | 是 | cashgroup_no, cashgroup_no |
| idx_ucrt_ucrt_fundspcash | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_ucrt_acctspcash | cashgroup_no, cashgroup_no |
| idx_ucrt_ucrt_acctspcash | cashgroup_no, cashgroup_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-10 09:42:40 | 3.0.2.2017 | huangzh | 所有表ucrt_acctspcash，添加了表字段(fin_refcost_fare);
所有表ucrt_acctsp... |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-10-10 09:42:40 | 3.0.2.2017 | huangzh | 所有表ucrt_acctspcash，添加了表字段(fin_refcost_fare);
所有表ucrt_acctsp... |
| 2023-08-23 18:39:36 | 0.3.3.142 | 徐志坚 | 增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

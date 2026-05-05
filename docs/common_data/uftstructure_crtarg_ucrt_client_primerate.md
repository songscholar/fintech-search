# ucrt_client_primerate - 客户优惠利率信息表

**表对象ID**: 7032
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | compact_type | 否 |  |  |
| 4 | primerate_begin_date | 否 |  |  |
| 5 | primerate_end_date | 否 |  |  |
| 6 | primerate_id | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | compact_type | 否 |  |  |
| 11 | primerate_begin_date | 否 |  |  |
| 12 | primerate_end_date | 否 |  |  |
| 13 | primerate_id | 否 |  |  |
| 14 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_client_primerate_type | 默认 | 否 | fund_account, compact_type, fund_account, compact_type |
| idx_ucrt_client_primerate_type | ART | 是 | fund_account, compact_type, fund_account, compact_type |
| idx_ucrt_client_primerate_type | 默认 | 否 | fund_account, compact_type, fund_account, compact_type |
| idx_ucrt_client_primerate_type | ART | 是 | fund_account, compact_type, fund_account, compact_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_client_primerate_type | fund_account, compact_type, fund_account, compact_type |
| idx_ucrt_client_primerate_type | fund_account, compact_type, fund_account, compact_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-02-28 09:27:55 | 3.0.6.1075 | 袁文龙 | 当前表ucrt_client_primerate，修改了索引idx_ucrt_client_primerate_type... |
| 2023-08-22 13:49:52 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.137 | 徐世晗 | 根据内存表索引增加物理表索引 |
| 2026-02-28 09:27:55 | 3.0.6.1075 | 袁文龙 | 当前表ucrt_client_primerate，修改了索引idx_ucrt_client_primerate_type... |
| 2023-08-22 13:49:52 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.137 | 徐世晗 | 根据内存表索引增加物理表索引 |

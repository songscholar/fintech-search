# ucrt_compact_repay_order - 融资融券负债了结表

**表对象ID**: 7505
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | compact_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | back_date | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | compact_type | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | compact_postpone_status | 否 |  |  |
| 8 | compact_source | 否 |  |  |
| 9 | compact_id | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | back_date | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | compact_type | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | compact_postpone_status | 否 |  |  |
| 16 | compact_source | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_compact_repay_order_compact | ART | 是 | fund_account, compact_id, fund_account, compact_id |
| idx_ucrt_compact_repay_order_date | ART | 是 | fund_account, back_date, compact_id, fund_account, back_date, compact_id |
| idx_ucrt_compact_repay_order_compact | ART | 是 | fund_account, compact_id, fund_account, compact_id |
| idx_ucrt_compact_repay_order_date | ART | 是 | fund_account, back_date, compact_id, fund_account, back_date, compact_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_compact_repay_order | fund_account, compact_id, fund_account, compact_id |
| idx_ucrt_compact_repay_order | fund_account, compact_id, fund_account, compact_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-02 09:28 | 0.0.0.3 | lift | 调整索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-02 09:28 | 0.0.0.3 | lift | 调整索引名 |

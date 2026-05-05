# ucrt_total_stk_entrust - 证券委托汇总表

**表对象ID**: 7502
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | crdt_prev_balance | 否 |  |  |
| 5 | assure_back_prev_amount | 否 |  |  |
| 6 | assure_submit_prev_amount | 否 |  |  |
| 7 | assure_submit_report_amount | 否 |  |  |
| 8 | crdt_prev_amount | 否 |  |  |
| 9 | crdt_prev_value | 否 |  |  |
| 10 | crdt_noprice_amount | 否 |  |  |
| 11 | fin_buy_prev_amount | 否 |  |  |
| 12 | fin_buy_prev_value | 否 |  |  |
| 13 | fin_buy_noprice_amount | 否 |  |  |
| 14 | secureturn_prev_amount | 否 |  |  |
| 15 | slo_buy_prev_amount | 否 |  |  |
| 16 | slo_buy_prev_balance | 否 |  |  |
| 17 | slo_buy_prev_value | 否 |  |  |
| 18 | slo_buy_noprice_prev_amount | 否 |  |  |
| 19 | crdt_sell_prev_amount | 否 |  |  |
| 20 | crdt_sell_prev_value | 否 |  |  |
| 21 | crdt_sell_noprice_prev_amount | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | crdt_prev_balance | 否 |  |  |
| 26 | assure_back_prev_amount | 否 |  |  |
| 27 | assure_submit_prev_amount | 否 |  |  |
| 28 | assure_submit_report_amount | 否 |  |  |
| 29 | crdt_prev_amount | 否 |  |  |
| 30 | crdt_prev_value | 否 |  |  |
| 31 | crdt_noprice_amount | 否 |  |  |
| 32 | fin_buy_prev_amount | 否 |  |  |
| 33 | fin_buy_prev_value | 否 |  |  |
| 34 | fin_buy_noprice_amount | 否 |  |  |
| 35 | secureturn_prev_amount | 否 |  |  |
| 36 | slo_buy_prev_amount | 否 |  |  |
| 37 | slo_buy_prev_balance | 否 |  |  |
| 38 | slo_buy_prev_value | 否 |  |  |
| 39 | slo_buy_noprice_prev_amount | 否 |  |  |
| 40 | crdt_sell_prev_amount | 否 |  |  |
| 41 | crdt_sell_prev_value | 否 |  |  |
| 42 | crdt_sell_noprice_prev_amount | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_total_stk_entrust_code | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucrt_total_stk_entrust_code | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_total_stk_entrust | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucrt_total_stk_entrust | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-06 11:00:56 | 3.0.6.1063 | 许琮擎 | crdt_prev_value、crdt_sell_prev_value调整为HsHighQuantity |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2025-08-06 11:00:56 | 3.0.6.1063 | 许琮擎 | crdt_prev_value、crdt_sell_prev_value调整为HsHighQuantity |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

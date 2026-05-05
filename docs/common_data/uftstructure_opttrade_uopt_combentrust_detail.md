# uopt_combentrust_detail - 期权组合委托明细表

**表对象ID**: 9611
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | trace_id | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | entrust_no | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | optcomb_code | 否 |  |  |
| 9 | opthold_type | 否 |  |  |
| 10 | option_code | 否 |  |  |
| 11 | report_amount | 否 |  |  |
| 12 | leg_order | 否 |  |  |
| 13 | cancel_serial_no | 否 |  |  |
| 14 | init_date | 否 |  |  |
| 15 | trace_id | 否 |  |  |
| 16 | client_id | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | entrust_no | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_account | 否 |  |  |
| 21 | optcomb_code | 否 |  |  |
| 22 | opthold_type | 否 |  |  |
| 23 | option_code | 否 |  |  |
| 24 | report_amount | 否 |  |  |
| 25 | leg_order | 否 |  |  |
| 26 | cancel_serial_no | 否 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_combentrust_detail | 默认 | 否 | init_date, init_date |
| idx_uopt_combentrust_detail | 默认 | 否 | init_date, entrust_no, leg_order, init_date, entrust_no, leg_order |
| idx_uopt_combentrustdetail_acct | 默认 | 是 | fund_account, fund_account |
| idx_uopt_combentrust_global | 默认 | 是 | init_date, fund_account, exchange_type, entrust_no, leg_order, init_date, fund_account, exchange_type, entrust_no, leg_order |
| idx_uopt_combentrust_detail_temp | 默认 | 是 | init_date, fund_account, entrust_no, exchange_type, stock_account, leg_order, init_date, fund_account, entrust_no, exchange_type, stock_account, leg_order |
| idx_uopt_combentrust_detail | 默认 | 否 | init_date, init_date |
| idx_uopt_combentrust_detail | 默认 | 否 | init_date, entrust_no, leg_order, init_date, entrust_no, leg_order |
| idx_uopt_combentrustdetail_acct | 默认 | 是 | fund_account, fund_account |
| idx_uopt_combentrust_global | 默认 | 是 | init_date, fund_account, exchange_type, entrust_no, leg_order, init_date, fund_account, exchange_type, entrust_no, leg_order |
| idx_uopt_combentrust_detail_temp | 默认 | 是 | init_date, fund_account, entrust_no, exchange_type, stock_account, leg_order, init_date, fund_account, entrust_no, exchange_type, stock_account, leg_order |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_combentrust_detail | init_date, fund_account, entrust_no, exchange_type, stock_account, leg_order, init_date, fund_account, entrust_no, exchange_type, stock_account, leg_order |
| idx_uopt_combentrust_detail | init_date, fund_account, entrust_no, exchange_type, stock_account, leg_order, init_date, fund_account, entrust_no, exchange_type, stock_account, leg_order |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-07 11:34:13 | V3.0.2.3 | 吴笑东 | 物理表uopt_combentrust_detail，增加索引字段(索引idx_uopt_combentrust_det... |
| 2025-08-07 11:34:13 | V3.0.2.3 | 吴笑东 | 物理表uopt_combentrust_detail，增加索引字段(索引idx_uopt_combentrust_det... |

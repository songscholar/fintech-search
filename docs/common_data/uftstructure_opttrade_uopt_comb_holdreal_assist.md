# uopt_comb_holdreal_assist - 组合策略持仓实时交易辅助表

**表对象ID**: 9625
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | stock_account | 否 |  | this is uft2.0 |
| 3 | exchange_type | 否 |  | this is uft2.0 |
| 4 | optcomb_id | 否 |  | this is uft2.0 |
| 5 | margin_ratio1 | 否 |  | this is uft2.0 |
| 6 | near_final_ratio_kind1 | 否 |  | this is uft2.0 |
| 7 | margin_ratio2 | 否 |  | this is uft2.0 |
| 8 | near_final_ratio_kind2 | 否 |  | this is uft2.0 |
| 9 | margin_ratio_comb | 否 |  | this is uft2.0 |
| 10 | comb_upbail_balance | 否 |  | this is uft2.0 |
| 11 | near_final_days | 否 |  | this is uft2.0 |
| 12 | near_final_time | 否 |  | this is uft2.0 |
| 13 | fund_account | 否 |  |  |
| 14 | stock_account | 否 |  | this is uft2.0 |
| 15 | exchange_type | 否 |  | this is uft2.0 |
| 16 | optcomb_id | 否 |  | this is uft2.0 |
| 17 | margin_ratio1 | 否 |  | this is uft2.0 |
| 18 | near_final_ratio_kind1 | 否 |  | this is uft2.0 |
| 19 | margin_ratio2 | 否 |  | this is uft2.0 |
| 20 | near_final_ratio_kind2 | 否 |  | this is uft2.0 |
| 21 | margin_ratio_comb | 否 |  | this is uft2.0 |
| 22 | comb_upbail_balance | 否 |  | this is uft2.0 |
| 23 | near_final_days | 否 |  | this is uft2.0 |
| 24 | near_final_time | 否 |  | this is uft2.0 |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uopt_comb_holdreal_assist_temp | 默认 | 是 | stock_account, exchange_type, fund_account, optcomb_id, stock_account, exchange_type, fund_account, optcomb_id |
| uopt_comb_holdreal_assist_temp | 默认 | 是 | stock_account, exchange_type, fund_account, optcomb_id, stock_account, exchange_type, fund_account, optcomb_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_comb_holdreal_assist | stock_account, exchange_type, fund_account, optcomb_id, stock_account, exchange_type, fund_account, optcomb_id |
| idx_uopt_comb_holdreal_assist | stock_account, exchange_type, fund_account, optcomb_id, stock_account, exchange_type, fund_account, optcomb_id |

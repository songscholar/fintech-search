# upbs_elig_busi_arg - 业务风险参数表

**表对象ID**: 84
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | busi_svr_kind | 否 |  |  |
| 2 | busi_risk_level | 否 |  |  |
| 3 | entrust_type | 否 |  |  |
| 4 | entrust_bs | 否 |  |  |
| 5 | en_exchange_type | 否 |  |  |
| 6 | en_stock_type | 否 |  |  |
| 7 | en_busi_type | 否 |  |  |
| 8 | invest_term | 否 |  |  |
| 9 | invest_type | 否 |  |  |
| 10 | elig_ctrlstr | 否 |  |  |
| 11 | income_type | 否 |  |  |
| 12 | elig_match_rule | 否 |  |  |
| 13 | en_sub_stock_type | 否 |  |  |
| 14 | elig_matchstr | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | busi_svr_kind | 否 |  |  |
| 17 | busi_risk_level | 否 |  |  |
| 18 | entrust_type | 否 |  |  |
| 19 | entrust_bs | 否 |  |  |
| 20 | en_exchange_type | 否 |  |  |
| 21 | en_stock_type | 否 |  |  |
| 22 | en_busi_type | 否 |  |  |
| 23 | invest_term | 否 |  |  |
| 24 | invest_type | 否 |  |  |
| 25 | elig_ctrlstr | 否 |  |  |
| 26 | income_type | 否 |  |  |
| 27 | elig_match_rule | 否 |  |  |
| 28 | en_sub_stock_type | 否 |  |  |
| 29 | elig_matchstr | 否 |  |  |
| 30 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_elig_busi_arg | ART | 是 | busi_svr_kind, busi_svr_kind |
| idx_upbs_elig_busi_type | ART | 是 | entrust_type, en_sub_stock_type, entrust_type, en_sub_stock_type |
| idx_upbs_elig_busi_arg | ART | 是 | busi_svr_kind, busi_svr_kind |
| idx_upbs_elig_busi_type | ART | 是 | entrust_type, en_sub_stock_type, entrust_type, en_sub_stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_elig_busi_arg | busi_svr_kind, busi_svr_kind |
| idx_upbs_elig_busi_arg | busi_svr_kind, busi_svr_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-11-10 10:18:15 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |
| 2023-11-10 10:18:15 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |

# uref_svrfare - 转融通出借服务费用表

**表对象ID**: 6015
**所属模块**: refarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | refsvrfare_kind | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | ref_term | 否 |  |  |
| 5 | refbalance_type | 否 |  |  |
| 6 | balance_ratio | 否 |  |  |
| 7 | balance_fare | 否 |  |  |
| 8 | max_fare | 否 |  |  |
| 9 | min_fare | 否 |  |  |
| 10 | refsvrfare_kind | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | ref_term | 否 |  |  |
| 14 | refbalance_type | 否 |  |  |
| 15 | balance_ratio | 否 |  |  |
| 16 | balance_fare | 否 |  |  |
| 17 | max_fare | 否 |  |  |
| 18 | min_fare | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refsvrfare | ART | 是 | refsvrfare_kind, ref_term, exchange_type, stock_code, refsvrfare_kind, ref_term, exchange_type, stock_code |
| idx_refsvrfare | ART | 是 | refsvrfare_kind, ref_term, exchange_type, stock_code, refsvrfare_kind, ref_term, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refsvrfare | refsvrfare_kind, ref_term, exchange_type, stock_code, refsvrfare_kind, ref_term, exchange_type, stock_code |
| idx_refsvrfare | refsvrfare_kind, ref_term, exchange_type, stock_code, refsvrfare_kind, ref_term, exchange_type, stock_code |

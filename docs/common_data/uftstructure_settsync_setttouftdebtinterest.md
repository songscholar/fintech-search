# setttouftdebtinterest - 清算国债利息表

**表对象ID**: 3096
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_code | 是 |  |  |
| 3 | init_date | 是 |  |  |
| 4 | ratio | 是 |  |  |
| 5 | interest_period | 是 |  |  |
| 6 | stock_interest | 是 |  |  |
| 7 | remark | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | stock_code | 是 |  |  |
| 10 | init_date | 是 |  |  |
| 11 | ratio | 是 |  |  |
| 12 | interest_period | 是 |  |  |
| 13 | stock_interest | 是 |  |  |
| 14 | remark | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_debtinterest | 默认 | 否 | exchange_type, stock_code, exchange_type, stock_code |
| idx_settdebtinterest | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_debtinterest | 默认 | 否 | exchange_type, stock_code, exchange_type, stock_code |
| idx_settdebtinterest | 默认 | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_debtinterest | exchange_type, stock_code, exchange_type, stock_code |
| idx_debtinterest | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-21 15:19:03 | 8.26.2.88 |  | 物理表setttouftdebtinterest，增加索引(idx_debtinterest:[exchange_typ... |
| 2025-04-21 15:19:03 | 8.26.2.88 |  | 物理表setttouftdebtinterest，增加索引(idx_debtinterest:[exchange_typ... |

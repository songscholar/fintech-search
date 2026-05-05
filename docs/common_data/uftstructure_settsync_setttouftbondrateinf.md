# setttouftbondrateinf - 清算国债折算率通知表

**表对象ID**: 3095
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_code | 是 |  |  |
| 3 | begin_date | 是 |  |  |
| 4 | end_date | 是 |  |  |
| 5 | impawn_rate | 是 |  |  |
| 6 | impawn_code | 是 |  |  |
| 7 | modify_date | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | stock_code | 是 |  |  |
| 10 | begin_date | 是 |  |  |
| 11 | end_date | 是 |  |  |
| 12 | impawn_rate | 是 |  |  |
| 13 | impawn_code | 是 |  |  |
| 14 | modify_date | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bondrateinf | 默认 | 否 | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |
| idx_settbondrateinf | 默认 | 是 | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |
| idx_bondrateinf | 默认 | 否 | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |
| idx_settbondrateinf | 默认 | 是 | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bondrateinf | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |
| idx_bondrateinf | stock_code, exchange_type, begin_date, stock_code, exchange_type, begin_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-21 15:19:10 | 8.26.2.89 |  | 物理表setttouftbondrateinf，增加索引(idx_bondrateinf:[stock_code,exc... |
| 2025-04-21 15:19:10 | 8.26.2.89 |  | 物理表setttouftbondrateinf，增加索引(idx_bondrateinf:[stock_code,exc... |

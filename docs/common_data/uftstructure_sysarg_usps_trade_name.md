# usps_trade_name - 交易说明表

**表对象ID**: 24
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | entrust_bs | 否 |  |  |
| 3 | entrust_type | 否 |  |  |
| 4 | entrust_prop | 否 |  |  |
| 5 | trade_type | 否 |  |  |
| 6 | trade_name | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | entrust_bs | 否 |  |  |
| 9 | entrust_type | 否 |  |  |
| 10 | entrust_prop | 否 |  |  |
| 11 | trade_type | 否 |  |  |
| 12 | trade_name | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tradename | ART | 是 | exchange_type, entrust_bs, entrust_type, entrust_prop, exchange_type, entrust_bs, entrust_type, entrust_prop |
| idx_tradename | ART | 是 | exchange_type, entrust_bs, entrust_type, entrust_prop, exchange_type, entrust_bs, entrust_type, entrust_prop |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tradename | exchange_type, entrust_bs, entrust_type, entrust_prop, exchange_type, entrust_bs, entrust_type, entrust_prop |
| idx_tradename | exchange_type, entrust_bs, entrust_type, entrust_prop, exchange_type, entrust_bs, entrust_type, entrust_prop |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-09 11:03:08 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-03-23 09:16 | 0.0.0.1 | 吴丽丽 | 新增tradename表 |
| 2024-09-09 11:03:08 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-03-23 09:16 | 0.0.0.1 | 吴丽丽 | 新增tradename表 |

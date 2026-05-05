# usps_spread_type - 价差类别表

**表对象ID**: 76
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | spread_type | 否 |  |  |
| 2 | begin_price | 否 |  |  |
| 3 | end_price | 否 |  |  |
| 4 | step_price | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | position_str | 否 |  | spread_type(1)+begin_price(20) |
| 9 | spread_type | 否 |  |  |
| 10 | begin_price | 否 |  |  |
| 11 | end_price | 否 |  |  |
| 12 | step_price | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | spread_type(1)+begin_price(20) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_spread_type | ART | 是 | spread_type, begin_price, spread_type, begin_price |
| idx_usps_spread_type | ART | 是 | spread_type, begin_price, spread_type, begin_price |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_spread_type | spread_type, begin_price, spread_type, begin_price |
| idx_usps_spread_type | spread_type, begin_price, spread_type, begin_price |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-21 15:05:25 | 3.0.2.87 | 童程凯 | 调整position_str备注，position_str统一凭借规则为拼接为规则为spread_type(1)+beg... |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-19 11:35:15 | 3.0.6.81 | 李想 | 物理表usps_spread_type，添加了表字段(update_date);
物理表usps_spread_typ... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-10-21 15:05:25 | 3.0.2.87 | 童程凯 | 调整position_str备注，position_str统一凭借规则为拼接为规则为spread_type(1)+beg... |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-19 11:35:15 | 3.0.6.81 | 李想 | 物理表usps_spread_type，添加了表字段(update_date);
物理表usps_spread_typ... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

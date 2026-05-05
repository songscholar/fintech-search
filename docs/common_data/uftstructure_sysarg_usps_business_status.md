# usps_business_status - 业务委托申报状态表

**表对象ID**: 13
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_type | 否 |  |  |
| 3 | entrust_prop | 否 |  |  |
| 4 | sub_stock_type | 否 |  |  |
| 5 | withdraw | 否 |  | 1：撤单委托；0：非撤单委托 |
| 6 | report_status | 否 |  | 1：当前允许申报；0：当前不允许申报 |
| 7 | entrust_status | 否 |  | 1：当前允许委托；0：当前不允许委托 |
| 8 | time_order | 否 |  | 低8位存放申报对应time_order;高8位存放委托对应time_order |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_type | 否 |  |  |
| 11 | entrust_prop | 否 |  |  |
| 12 | sub_stock_type | 否 |  |  |
| 13 | withdraw | 否 |  | 1：撤单委托；0：非撤单委托 |
| 14 | report_status | 否 |  | 1：当前允许申报；0：当前不允许申报 |
| 15 | entrust_status | 否 |  | 1：当前允许委托；0：当前不允许委托 |
| 16 | time_order | 否 |  | 低8位存放申报对应time_order;高8位存放委托对应time_order |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_business_status | ART | 是 | exchange_type, stock_type, entrust_prop, sub_stock_type, withdraw, exchange_type, stock_type, entrust_prop, sub_stock_type, withdraw |
| idx_usps_business_status | ART | 是 | exchange_type, stock_type, entrust_prop, sub_stock_type, withdraw, exchange_type, stock_type, entrust_prop, sub_stock_type, withdraw |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_business_status | exchange_type, stock_type, entrust_prop, sub_stock_type, withdraw, exchange_type, stock_type, entrust_prop, sub_stock_type, withdraw |
| idx_usps_business_status | exchange_type, stock_type, entrust_prop, sub_stock_type, withdraw, exchange_type, stock_type, entrust_prop, sub_stock_type, withdraw |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-09 11:01:45 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2024-09-09 11:01:45 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

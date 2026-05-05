# uref_iestock_info - 信息交互平台关联证券信息表

**表对象ID**: 6223
**所属模块**: refinex
**数据空间**: HS_UFT_DATA

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | create_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | serial_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | stock_name | 否 |  |  |
| 7 | entrust_amount | 否 |  |  |
| 8 | position_str | 否 |  |  |
| 9 | info_type | 否 |  |  |
| 10 | intent_status | 否 |  |  |
| 11 | create_date | 否 |  |  |
| 12 | entrust_no | 否 |  |  |
| 13 | serial_no | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | stock_name | 否 |  |  |
| 17 | entrust_amount | 否 |  |  |
| 18 | position_str | 否 |  |  |
| 19 | info_type | 否 |  |  |
| 20 | intent_status | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_iestockinfo | ART | 是 | position_str, position_str |
| idx_iestockinfo_esno | ART | 是 | entrust_no, serial_no, create_date, entrust_no, serial_no, create_date |
| idx_iestockinfo | ART | 是 | position_str, position_str |
| idx_iestockinfo_esno | ART | 是 | entrust_no, serial_no, create_date, entrust_no, serial_no, create_date |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_iestockinfo | position_str, position_str |
| idx_iestockinfo_esno | entrust_no, serial_no, create_date, entrust_no, serial_no, create_date |
| idx_iestockinfo | position_str, position_str |
| idx_iestockinfo_esno | entrust_no, serial_no, create_date, entrust_no, serial_no, create_date |

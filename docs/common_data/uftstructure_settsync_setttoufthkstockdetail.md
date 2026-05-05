# setttoufthkstockdetail - 清算港股证券余额信息表

**表对象ID**: 3052
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_account | 是 |  |  |
| 3 | seat_no | 是 |  |  |
| 4 | stock_code | 是 |  |  |
| 5 | hkdc_stock_type | 是 |  |  |
| 6 | hkdc_stock_property | 是 |  |  |
| 7 | hkdc_circulate_type | 是 |  |  |
| 8 | hkdc_authority_type | 是 |  |  |
| 9 | hkdc_market_year | 是 |  |  |
| 10 | hkdc_authority_times | 是 |  |  |
| 11 | szhk_authority_id | 是 |  |  |
| 12 | current_amount | 是 |  |  |
| 13 | uncome_amount | 是 |  |  |
| 14 | frozen_amount | 是 |  |  |
| 15 | position_str | 是 |  |  |
| 16 | exchange_type | 是 |  |  |
| 17 | stock_account | 是 |  |  |
| 18 | seat_no | 是 |  |  |
| 19 | stock_code | 是 |  |  |
| 20 | hkdc_stock_type | 是 |  |  |
| 21 | hkdc_stock_property | 是 |  |  |
| 22 | hkdc_circulate_type | 是 |  |  |
| 23 | hkdc_authority_type | 是 |  |  |
| 24 | hkdc_market_year | 是 |  |  |
| 25 | hkdc_authority_times | 是 |  |  |
| 26 | szhk_authority_id | 是 |  |  |
| 27 | current_amount | 是 |  |  |
| 28 | uncome_amount | 是 |  |  |
| 29 | frozen_amount | 是 |  |  |
| 30 | position_str | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_hkstockdetail | 默认 | 是 | position_str, position_str |
| idx_hkstockdetail_code | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| uk_hkstockdetail | 默认 | 是 | position_str, position_str |
| idx_hkstockdetail_code | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_hkstockdetail | position_str, position_str |
| uk_hkstockdetail | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2022-08-12 16:32 | 8.26.2.33 | 徐开 | 新增索引 |
| 2021-08-05 14:06 | 8.26.2.6 | 张明林 | 新增表结构hkstockdetail |
| 2022-08-12 16:32 | 8.26.2.33 | 徐开 | 新增索引 |
| 2021-08-05 14:06 | 8.26.2.6 | 张明林 | 新增表结构hkstockdetail |

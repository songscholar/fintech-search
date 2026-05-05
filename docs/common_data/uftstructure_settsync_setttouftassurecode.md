# setttouftassurecode - 清算担保证券信息表

**表对象ID**: 3087
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 50 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | stock_code | 是 |  |  |
| 4 | assure_ratio | 是 |  |  |
| 5 | assure_std_ratio | 是 |  |  |
| 6 | circulate_amount | 是 |  |  |
| 7 | capital_amount | 是 |  |  |
| 8 | upper_assure_hold_amount | 是 |  |  |
| 9 | fair_price | 是 |  |  |
| 10 | fair_price_flag | 是 |  |  |
| 11 | fair_ratio | 是 |  |  |
| 12 | end_date | 是 |  |  |
| 13 | assure_status | 是 |  |  |
| 14 | modify_date | 是 |  |  |
| 15 | remark | 是 |  |  |
| 16 | slo_sellbuy_status | 是 |  |  |
| 17 | old_assure_ratio | 是 |  |  |
| 18 | old_assure_std_ratio | 是 |  |  |
| 19 | static_pe_ratio | 是 |  |  |
| 20 | ensurescale_value | 是 |  |  |
| 21 | init_ensurescale_value | 是 |  |  |
| 22 | allow_blocktrade_flag | 是 |  |  |
| 23 | short_ensurescale_value | 是 |  |  |
| 24 | short_init_ensurescale_value | 是 |  |  |
| 25 | uft_data_change_status | 是 |  |  |
| 26 | init_date | 是 |  |  |
| 27 | exchange_type | 是 |  |  |
| 28 | stock_code | 是 |  |  |
| 29 | assure_ratio | 是 |  |  |
| 30 | assure_std_ratio | 是 |  |  |
| 31 | circulate_amount | 是 |  |  |
| 32 | capital_amount | 是 |  |  |
| 33 | upper_assure_hold_amount | 是 |  |  |
| 34 | fair_price | 是 |  |  |
| 35 | fair_price_flag | 是 |  |  |
| 36 | fair_ratio | 是 |  |  |
| 37 | end_date | 是 |  |  |
| 38 | assure_status | 是 |  |  |
| 39 | modify_date | 是 |  |  |
| 40 | remark | 是 |  |  |
| 41 | slo_sellbuy_status | 是 |  |  |
| 42 | old_assure_ratio | 是 |  |  |
| 43 | old_assure_std_ratio | 是 |  |  |
| 44 | static_pe_ratio | 是 |  |  |
| 45 | ensurescale_value | 是 |  |  |
| 46 | init_ensurescale_value | 是 |  |  |
| 47 | allow_blocktrade_flag | 是 |  |  |
| 48 | short_ensurescale_value | 是 |  |  |
| 49 | short_init_ensurescale_value | 是 |  |  |
| 50 | uft_data_change_status | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settassurecode | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_settassurecode | 默认 | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settassurecode | stock_code, stock_code |
| idx_settassurecode | stock_code, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-01-08 15:23 | 8.26.2.6 | 张军 | 新增 |
| 2024-01-08 15:23 | 8.26.2.6 | 张军 | 新增 |

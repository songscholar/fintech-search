# setttouftsellfrozenstock - 清算可售冻结股份表

**表对象ID**: 3073
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | stock_account | 是 |  |  |
| 3 | stock_code | 是 |  |  |
| 4 | exchange_type | 是 |  |  |
| 5 | stock_type | 是 |  |  |
| 6 | available_amount | 是 |  |  |
| 7 | seat_no | 是 |  |  |
| 8 | stock_property | 是 |  |  |
| 9 | hkdc_circulate_type | 是 |  | 0-无限售流通；N-限售或非流通 |
| 10 | date_clear | 是 |  |  |
| 11 | position_str | 是 |  | stock_account(20) + exchange_type(4) + stock_code(6) + seat_ |
| 12 | uft_data_change_status | 是 |  |  |
| 13 | init_date | 是 |  |  |
| 14 | stock_account | 是 |  |  |
| 15 | stock_code | 是 |  |  |
| 16 | exchange_type | 是 |  |  |
| 17 | stock_type | 是 |  |  |
| 18 | available_amount | 是 |  |  |
| 19 | seat_no | 是 |  |  |
| 20 | stock_property | 是 |  |  |
| 21 | hkdc_circulate_type | 是 |  | 0-无限售流通；N-限售或非流通 |
| 22 | date_clear | 是 |  |  |
| 23 | position_str | 是 |  | stock_account(20) + exchange_type(4) + stock_code(6) + seat_ |
| 24 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settsellfrozenstock | 默认 | 是 | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| idx_settsellfrozenstock_pos | 默认 | 是 | position_str, position_str |
| idx_settsellfrozenstock | 默认 | 是 | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| idx_settsellfrozenstock_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settsellfrozenstock | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |
| idx_settsellfrozenstock | stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type, stock_account, stock_code, exchange_type, seat_no, stock_property, hkdc_circulate_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-03-28 18:44 | 8.26.2.37 | 丁界成 | 新增 |
| 2023-03-28 18:44 | 8.26.2.37 | 丁界成 | 新增 |

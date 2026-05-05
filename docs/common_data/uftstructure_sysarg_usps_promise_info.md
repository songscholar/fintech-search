# usps_promise_info - 要约信息表

**表对象ID**: 23
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | begin_date | 否 |  |  |
| 2 | end_date | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | purchase_code | 否 |  |  |
| 5 | purchase_id | 否 |  |  |
| 6 | purchase_name | 否 |  |  |
| 7 | purchase_price | 否 |  |  |
| 8 | purchase_ratio | 否 |  |  |
| 9 | purchase_type | 否 |  |  |
| 10 | report_code | 否 |  |  |
| 11 | status | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | stock_name | 否 |  |  |
| 14 | stock_type | 否 |  |  |
| 15 | target_price | 否 |  |  |
| 16 | purchase_amount | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  | stock_code(8)+exchange_type(4)+purchase_id(64) |
| 22 | begin_date | 否 |  |  |
| 23 | end_date | 否 |  |  |
| 24 | exchange_type | 否 |  |  |
| 25 | purchase_code | 否 |  |  |
| 26 | purchase_id | 否 |  |  |
| 27 | purchase_name | 否 |  |  |
| 28 | purchase_price | 否 |  |  |
| 29 | purchase_ratio | 否 |  |  |
| 30 | purchase_type | 否 |  |  |
| 31 | report_code | 否 |  |  |
| 32 | status | 否 |  |  |
| 33 | stock_code | 否 |  |  |
| 34 | stock_name | 否 |  |  |
| 35 | stock_type | 否 |  |  |
| 36 | target_price | 否 |  |  |
| 37 | purchase_amount | 否 |  |  |
| 38 | transaction_no | 否 |  |  |
| 39 | remark | 否 |  |  |
| 40 | update_date | 否 |  |  |
| 41 | update_time | 否 |  |  |
| 42 | position_str | 否 |  | stock_code(8)+exchange_type(4)+purchase_id(64) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_promise_info_exch | ART | 是 | exchange_type, exchange_type |
| idx_usps_promise_info | ART | 是 | stock_code, exchange_type, purchase_id, stock_code, exchange_type, purchase_id |
| idx_usps_promise_info_exch | ART | 是 | exchange_type, exchange_type |
| idx_usps_promise_info | ART | 是 | stock_code, exchange_type, purchase_id, stock_code, exchange_type, purchase_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_promise_info | stock_code, exchange_type, purchase_id, stock_code, exchange_type, purchase_id |
| idx_usps_promise_info | stock_code, exchange_type, purchase_id, stock_code, exchange_type, purchase_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 16:51:56 | 3.0.6.63 | 李想 | 物理表usps_promise_info，添加了表字段(update_date);
物理表usps_promise_i... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-22 17:44 | 0.0.0.11 | 侯璇 | 取消非唯一索引的【删除时检查】 |
| 2023-06-19 17:10 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2025-02-18 16:51:56 | 3.0.6.63 | 李想 | 物理表usps_promise_info，添加了表字段(update_date);
物理表usps_promise_i... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-22 17:44 | 0.0.0.11 | 侯璇 | 取消非唯一索引的【删除时检查】 |
| 2023-06-19 17:10 | 0.0.0.9 | 吴威 | 新增transaction_no |

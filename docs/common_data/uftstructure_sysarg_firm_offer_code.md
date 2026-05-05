# firm_offer_code - 个人投顾标的表

**表对象ID**: 323
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | adproduct_id | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | start_date | 否 |  |  |
| 6 | end_date | 否 |  |  |
| 7 | begin_time | 否 |  |  |
| 8 | end_time | 否 |  |  |
| 9 | sign_status | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | data_src | 否 |  |  |
| 12 | adviser_buy_price | 否 |  |  |
| 13 | adviser_sell_price | 否 |  |  |
| 14 | folbuy_end_date | 否 |  |  |
| 15 | date_clear | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | adproduct_id | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | start_date | 否 |  |  |
| 22 | end_date | 否 |  |  |
| 23 | begin_time | 否 |  |  |
| 24 | end_time | 否 |  |  |
| 25 | sign_status | 否 |  |  |
| 26 | position_str | 否 |  |  |
| 27 | data_src | 否 |  |  |
| 28 | adviser_buy_price | 否 |  |  |
| 29 | adviser_sell_price | 否 |  |  |
| 30 | folbuy_end_date | 否 |  |  |
| 31 | date_clear | 否 |  |  |
| 32 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_firmoffercode_id | ART | 是 | fund_account, exchange_type, stock_code, adproduct_id, fund_account, exchange_type, stock_code, adproduct_id |
| idx_firmoffercode_pos | ART | 是 | position_str, position_str |
| idx_firmoffercode_id | ART | 是 | fund_account, exchange_type, stock_code, adproduct_id, fund_account, exchange_type, stock_code, adproduct_id |
| idx_firmoffercode_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_firmoffercode_pos | position_str, position_str |
| idx_firmoffercode_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-06 14:31:01 | 3.0.2.98 | 洪略 | 增加历史表 |
| 2025-08-14 10:09:59 | 3.0.2.91 | 高志强 | 增加DB模式,避免写表失败 |
| 2024-09-24 13:33:37 | 3.0.2.29 | 范文浩 | 物理表firm_offer_code，添加了表字段(fund_account);
物理表firm_offer_code... |
| 2025-11-06 14:31:01 | 3.0.2.98 | 洪略 | 增加历史表 |
| 2025-08-14 10:09:59 | 3.0.2.91 | 高志强 | 增加DB模式,避免写表失败 |
| 2024-09-24 13:33:37 | 3.0.2.29 | 范文浩 | 物理表firm_offer_code，添加了表字段(fund_account);
物理表firm_offer_code... |

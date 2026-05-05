# adviser_product - 投顾产品信息

**表对象ID**: 320
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | adproduct_id | 否 |  |  |
| 3 | adproduct_name | 否 |  |  |
| 4 | investadv_name | 否 |  |  |
| 5 | follow_buy_rate | 否 |  |  |
| 6 | period_buy_rate | 否 |  |  |
| 7 | follow_sell_rate | 否 |  |  |
| 8 | period_sell_rate | 否 |  |  |
| 9 | follow_days | 否 |  |  |
| 10 | min_fare | 否 |  |  |
| 11 | min_profit_ratio | 否 |  |  |
| 12 | adproduct_status | 否 |  |  |
| 13 | main_adproduct_id | 否 |  |  |
| 14 | adv_module | 否 |  |  |
| 15 | profit_pay_flag | 否 |  |  |
| 16 | fare_get_type | 否 |  |  |
| 17 | end_date | 否 |  |  |
| 18 | persell_fixed_fare0 | 否 |  |  |
| 19 | perbuy_fixed_fare0 | 否 |  |  |
| 20 | folsell_fixed_fare0 | 否 |  |  |
| 21 | folbuy_fixed_fare0 | 否 |  |  |
| 22 | buy_follow_days | 否 |  |  |
| 23 | adv_position_flag | 否 |  |  |
| 24 | adv_prestock_flag | 否 |  |  |
| 25 | buy_min_fare | 否 |  |  |
| 26 | transaction_no | 否 |  |  |
| 27 | remark | 否 |  |  |
| 28 | init_date | 否 |  |  |
| 29 | adproduct_id | 否 |  |  |
| 30 | adproduct_name | 否 |  |  |
| 31 | investadv_name | 否 |  |  |
| 32 | follow_buy_rate | 否 |  |  |
| 33 | period_buy_rate | 否 |  |  |
| 34 | follow_sell_rate | 否 |  |  |
| 35 | period_sell_rate | 否 |  |  |
| 36 | follow_days | 否 |  |  |
| 37 | min_fare | 否 |  |  |
| 38 | min_profit_ratio | 否 |  |  |
| 39 | adproduct_status | 否 |  |  |
| 40 | main_adproduct_id | 否 |  |  |
| 41 | adv_module | 否 |  |  |
| 42 | profit_pay_flag | 否 |  |  |
| 43 | fare_get_type | 否 |  |  |
| 44 | end_date | 否 |  |  |
| 45 | persell_fixed_fare0 | 否 |  |  |
| 46 | perbuy_fixed_fare0 | 否 |  |  |
| 47 | folsell_fixed_fare0 | 否 |  |  |
| 48 | folbuy_fixed_fare0 | 否 |  |  |
| 49 | buy_follow_days | 否 |  |  |
| 50 | adv_position_flag | 否 |  |  |
| 51 | adv_prestock_flag | 否 |  |  |
| 52 | buy_min_fare | 否 |  |  |
| 53 | transaction_no | 否 |  |  |
| 54 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_adviserproduct_id | ART | 是 | adproduct_id, adproduct_id |
| idx_adviserproduct_id | ART | 是 | adproduct_id, adproduct_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_adviserproduct_id | adproduct_id, adproduct_id |
| idx_adviserproduct_id | adproduct_id, adproduct_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-10-06 09:51:45 | 3.0.2.31 | 李海洋 | 变长字段顺序调整，修复插入记录乱码问题 |
| 2024-09-24 11:16:52 | 3.0.2.29 | 范文浩 | 物理表adviser_product，添加了表字段(init_date);
物理表adviser_product，添加... |
| 2024-10-06 09:51:45 | 3.0.2.31 | 李海洋 | 变长字段顺序调整，修复插入记录乱码问题 |
| 2024-09-24 11:16:52 | 3.0.2.29 | 范文浩 | 物理表adviser_product，添加了表字段(init_date);
物理表adviser_product，添加... |

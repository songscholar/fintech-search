# usps_discount_model - 折扣模板表

**表对象ID**: 305
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | discount_model | 否 |  |  |
| 3 | entrust_way | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | discount_rate | 否 |  |  |
| 7 | modify_date | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | position_str | 否 |  | branch_no(6)+discount_model(10)+entrust_way(1)+stock_type(4) |
| 13 | branch_no | 否 |  |  |
| 14 | discount_model | 否 |  |  |
| 15 | entrust_way | 否 |  |  |
| 16 | stock_type | 否 |  |  |
| 17 | money_type | 否 |  |  |
| 18 | discount_rate | 否 |  |  |
| 19 | modify_date | 否 |  |  |
| 20 | transaction_no | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | branch_no(6)+discount_model(10)+entrust_way(1)+stock_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_discountmodel | ART | 是 | branch_no, discount_model, entrust_way, stock_type, money_type, branch_no, discount_model, entrust_way, stock_type, money_type |
| idx_discountmodel | ART | 是 | branch_no, discount_model, entrust_way, stock_type, money_type, branch_no, discount_model, entrust_way, stock_type, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_discountmodel | branch_no, discount_model, entrust_way, stock_type, money_type, branch_no, discount_model, entrust_way, stock_type, money_type |
| idx_discountmodel | branch_no, discount_model, entrust_way, stock_type, money_type, branch_no, discount_model, entrust_way, stock_type, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 15:57:10 | 3.0.6.35 | 李想 | 物理表usps_discount_model，添加了表字段(remark);
物理表usps_discount_mod... |
| 2024-05-18 14:07:34 | 3.0.2.8 | 祝丁恺 | 物理表usps_discount_model，添加了表字段(transaction_no);
 |
| 2024-04-30 22:34:33 | 3.0.2.7 | 乐闽庭 | 新增表 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 15:57:10 | 3.0.6.35 | 李想 | 物理表usps_discount_model，添加了表字段(remark);
物理表usps_discount_mod... |
| 2024-05-18 14:07:34 | 3.0.2.8 | 祝丁恺 | 物理表usps_discount_model，添加了表字段(transaction_no);
 |
| 2024-04-30 22:34:33 | 3.0.2.7 | 乐闽庭 | 新增表 |

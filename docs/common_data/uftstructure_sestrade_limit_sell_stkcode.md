# limit_sell_stkcode - 限售代码信息表

**表对象ID**: 5532
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | stock_name | 否 |  |  |
| 4 | total_amount | 否 |  |  |
| 5 | circulate_amount | 否 |  |  |
| 6 | month_limit_ratio | 否 |  |  |
| 7 | total_limit_ratio | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_flag | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | stock_name | 否 |  |  |
| 13 | total_amount | 否 |  |  |
| 14 | circulate_amount | 否 |  |  |
| 15 | month_limit_ratio | 否 |  |  |
| 16 | total_limit_ratio | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_flag | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_limit_sell_stkcode | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_limit_sell_stkcode | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_limit_sell_stkcode | stock_code, exchange_type, stock_code, exchange_type |
| idx_limit_sell_stkcode | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:50:07 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-11-23 14:01:01 | 3.0.5.1061 | 全春辉 | 表limit_sell_stkcode删除transaction_no字段 |
| 2024-05-29 21:28:11 | 3.0.2.16 | 祝丁恺 | 勾选不回库选项 |
| 2026-03-09 13:50:07 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-11-23 14:01:01 | 3.0.5.1061 | 全春辉 | 表limit_sell_stkcode删除transaction_no字段 |
| 2024-05-29 21:28:11 | 3.0.2.16 | 祝丁恺 | 勾选不回库选项 |

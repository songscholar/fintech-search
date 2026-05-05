# upbs_business_flag - 业务标志

**表对象ID**: 498
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | business_flag | 否 |  |  |
| 2 | business_name | 否 |  |  |
| 3 | business_subject | 否 |  |  |
| 4 | business_kind | 否 |  |  |
| 5 | business_group | 否 |  |  |
| 6 | borrow_lend | 否 |  |  |
| 7 | business_group_user | 否 |  |  |
| 8 | join_business_flag | 否 |  |  |
| 9 | opp_business_flag | 否 |  |  |
| 10 | transaction_no | 是 |  |  |
| 11 | business_flag | 否 |  |  |
| 12 | business_name | 否 |  |  |
| 13 | business_subject | 否 |  |  |
| 14 | business_kind | 否 |  |  |
| 15 | business_group | 否 |  |  |
| 16 | borrow_lend | 否 |  |  |
| 17 | business_group_user | 否 |  |  |
| 18 | join_business_flag | 否 |  |  |
| 19 | opp_business_flag | 否 |  |  |
| 20 | transaction_no | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_businflag | ART | 是 | business_flag, business_flag |
| idx_businflag | ART | 是 | business_flag, business_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_businflag | business_flag, business_flag |
| idx_businflag | business_flag, business_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-18 16:14:02 | 8.26.2.93 | 蒋浩宇 | 所有表upbs_business_flag，添加了表字段(transaction_no);
 |
| 2025-03-24 13:24:13 | 3.0.2.80 | 彭雪锋 | 调整表空间为HS_UFT_DATA |
| 2024-07-03 21:37:02 | 3.0.2.15 | 丁录荣 | 增加upbs_business_flag表 |
| 2025-09-18 16:14:02 | 8.26.2.93 | 蒋浩宇 | 所有表upbs_business_flag，添加了表字段(transaction_no);
 |
| 2025-03-24 13:24:13 | 3.0.2.80 | 彭雪锋 | 调整表空间为HS_UFT_DATA |
| 2024-07-03 21:37:02 | 3.0.2.15 | 丁录荣 | 增加upbs_business_flag表 |

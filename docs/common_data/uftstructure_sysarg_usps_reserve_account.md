# usps_reserve_account - 备付金账户信息表

**表对象ID**: 499
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | reserve_account_type | 否 |  |  |
| 3 | reserve_account_long | 否 |  |  |
| 4 | shdc_settle_no | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | company_no | 否 |  |  |
| 9 | reserve_account_type | 否 |  |  |
| 10 | reserve_account_long | 否 |  |  |
| 11 | shdc_settle_no | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reserveaccount | ART | 是 | company_no, reserve_account_type, company_no, reserve_account_type |
| idx_reserveaccount | ART | 是 | company_no, reserve_account_type, company_no, reserve_account_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_reserveaccount | company_no, reserve_account_type, company_no, reserve_account_type |
| idx_reserveaccount | company_no, reserve_account_type, company_no, reserve_account_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 14:02:54 | 3.0.6.88 | 李想 | 物理表usps_reserve_account，添加了表字段(update_date);
物理表usps_reserv... |
| 2024-11-28 10:22:47 | 3.0.2.48 | 王云乾 | 新增 |
| 2025-02-19 14:02:54 | 3.0.6.88 | 李想 | 物理表usps_reserve_account，添加了表字段(update_date);
物理表usps_reserv... |
| 2024-11-28 10:22:47 | 3.0.2.48 | 王云乾 | 新增 |

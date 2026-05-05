# credit_quotas - 分级授信额度

**表对象ID**: 1594
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | en_inv_client_grade | 否 |  |  |
| 2 | total_credit_quota | 否 |  |  |
| 3 | used_quota | 否 |  |  |
| 4 | surplus_quota | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | en_inv_client_grade | 否 |  |  |
| 7 | total_credit_quota | 否 |  |  |
| 8 | used_quota | 否 |  |  |
| 9 | surplus_quota | 否 |  |  |
| 10 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_credit_quota | ART | 是 | en_inv_client_grade, en_inv_client_grade |
| idx_credit_quota | ART | 是 | en_inv_client_grade, en_inv_client_grade |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_credit_quota | en_inv_client_grade, en_inv_client_grade |
| idx_credit_quota | en_inv_client_grade, en_inv_client_grade |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:01:43 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2024-11-21 13:57:39 | 3.0.5.1001 | 杨涛 | 分组授信额度不回库 |
| 2024-09-28 19:04:29 | 3.0.2.4 | 范文浩 | 物理表credit_quotas，添加了表字段(transaction_no);
 |
| 2026-03-05 17:01:43 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2024-11-21 13:57:39 | 3.0.5.1001 | 杨涛 | 分组授信额度不回库 |
| 2024-09-28 19:04:29 | 3.0.2.4 | 范文浩 | 物理表credit_quotas，添加了表字段(transaction_no);
 |

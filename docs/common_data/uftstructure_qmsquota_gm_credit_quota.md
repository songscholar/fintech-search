# gm_credit_quota - 分组授信额度表

**表对象ID**: 1596
**所属模块**: qmsquota
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | inv_client_group | 否 |  |  |
| 2 | total_credit_quota | 否 |  |  |
| 3 | used_quota | 否 |  |  |
| 4 | surplus_quota | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | inv_client_group | 否 |  |  |
| 7 | total_credit_quota | 否 |  |  |
| 8 | used_quota | 否 |  |  |
| 9 | surplus_quota | 否 |  |  |
| 10 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_gm_credit_quota | ART | 是 | inv_client_group, inv_client_group |
| idx_gm_credit_quota | ART | 是 | inv_client_group, inv_client_group |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_gm_credit_quota | inv_client_group, inv_client_group |
| idx_gm_credit_quota | inv_client_group, inv_client_group |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:02:29 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2024-11-21 13:57:39 | 3.0.5.1001 | 杨涛 | 分组授信额度表不回库 |
| 2024-09-28 19:06:28 | 3.0.2.4 | 范文浩 | 物理表gm_credit_quota，添加了表字段(transaction_no);
 |
| 2026-03-05 17:02:29 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2024-11-21 13:57:39 | 3.0.5.1001 | 杨涛 | 分组授信额度表不回库 |
| 2024-09-28 19:06:28 | 3.0.2.4 | 范文浩 | 物理表gm_credit_quota，添加了表字段(transaction_no);
 |

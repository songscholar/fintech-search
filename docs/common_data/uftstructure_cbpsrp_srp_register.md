# srp_register - 股票质押融资登记表

**表对象ID**: 2613
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | funder_no | 否 |  |  |
| 5 | papercont_id | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | funder_no | 否 |  |  |
| 11 | papercont_id | 否 |  |  |
| 12 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srpregister | ART | 是 | fund_account, funder_no, fund_account, funder_no |
| idx_srpregister | ART | 是 | fund_account, funder_no, fund_account, funder_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srpregister | fund_account, funder_no, fund_account, funder_no |
| idx_srpregister | fund_account, funder_no, fund_account, funder_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:49:11 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-05-08 20:40:07 | 3.0.2.3 | 余世泽 | 勾选全局版本号 |
| 2024-12-05 17:42:45 | 3.0.2.2 | 范文浩 | 物理表srp_register，添加了表字段(transaction_no);
勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:35 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:49:11 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-05-08 20:40:07 | 3.0.2.3 | 余世泽 | 勾选全局版本号 |
| 2024-12-05 17:42:45 | 3.0.2.2 | 范文浩 | 物理表srp_register，添加了表字段(transaction_no);
勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:26:35 | 3.0.3.1 | wuxd | 新增 |

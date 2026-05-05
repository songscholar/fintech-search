# arp_register - 约定购回协议登记表

**表对象ID**: 2534
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | funder_no | 否 |  |  |
| 5 | agree_version | 否 |  |  |
| 6 | papercont_id | 否 |  |  |
| 7 | branch_no | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | funder_no | 否 |  |  |
| 11 | agree_version | 否 |  |  |
| 12 | papercont_id | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpregister | ART | 是 | fund_account, funder_no, fund_account, funder_no |
| idx_arpregister | ART | 是 | fund_account, funder_no, fund_account, funder_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpregister | fund_account, funder_no, fund_account, funder_no |
| idx_arpregister | fund_account, funder_no, fund_account, funder_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:22:00 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2026-03-04 16:22:00 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |

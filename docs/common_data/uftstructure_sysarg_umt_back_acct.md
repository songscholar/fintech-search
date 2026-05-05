# umt_back_acct - 回切账户表

**表对象ID**: 97
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | asset_prop | 否 |  |  |
| 4 | umt_acct_status | 否 |  |  |
| 5 | partition_no | 否 |  |  |
| 6 | sysnode_id | 否 |  |  |
| 7 | transaction_str | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | client_id | 否 |  |  |
| 10 | asset_prop | 否 |  |  |
| 11 | umt_acct_status | 否 |  |  |
| 12 | partition_no | 否 |  |  |
| 13 | sysnode_id | 否 |  |  |
| 14 | transaction_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_umt_back_acct | ART | 是 | fund_account, fund_account |
| idx_umt_back_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_umt_back_acct | fund_account, fund_account |
| idx_umt_back_acct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-16 19:23:26 | 3.0.2.96 | 韦子晗 | 所有表umt_back_acct，添加了表字段(transaction_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-15 14:43:28 | 3.0.2.55 | 赵良梓 | 表不回库 |
| 2025-01-16 20:28:03 | 3.0.2.50 | 程猛 | 新增 |
| 2025-09-16 19:23:26 | 3.0.2.96 | 韦子晗 | 所有表umt_back_acct，添加了表字段(transaction_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-15 14:43:28 | 3.0.2.55 | 赵良梓 | 表不回库 |
| 2025-01-16 20:28:03 | 3.0.2.50 | 程猛 | 新增 |

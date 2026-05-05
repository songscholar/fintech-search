# crdt_acct_relationship - 账户关系信息控制表

**表对象ID**: 7555
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | main_acct | 否 |  |  |
| 2 | match_busin_type | 否 |  |  |
| 3 | relationship_acct | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | main_acct | 否 |  |  |
| 6 | match_busin_type | 否 |  |  |
| 7 | relationship_acct | 否 |  |  |
| 8 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_acct_relationship | ART | 是 | main_acct, match_busin_type, main_acct, match_busin_type |
| idx_crdt_acct_relationship | ART | 是 | main_acct, match_busin_type, main_acct, match_busin_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_acct_relationship | main_acct, match_busin_type, main_acct, match_busin_type |
| idx_crdt_acct_relationship | main_acct, match_busin_type, main_acct, match_busin_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-18 10:17:31 | 3.0.6.1062 | 袁文龙 | 勾选不回库 |
| 2024-03-20 16:06:22 | V3.0.2.4 | 程效 | 新增crdt_acct_relationship表 |
| 2025-07-18 10:17:31 | 3.0.6.1062 | 袁文龙 | 勾选不回库 |
| 2024-03-20 16:06:22 | V3.0.2.4 | 程效 | 新增crdt_acct_relationship表 |

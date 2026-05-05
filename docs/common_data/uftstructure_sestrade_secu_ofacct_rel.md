# secu_ofacct_rel - 证券基金账户关系对应表

**表对象ID**: 5544
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | organ_flag | 否 |  |  |
| 5 | holder_kind | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | otcholder_kind | 否 |  |  |
| 8 | ofund_account | 否 |  |  |
| 9 | sign_status | 否 |  |  |
| 10 | sign_date | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | acode_account | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | organ_flag | 否 |  |  |
| 16 | holder_kind | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | otcholder_kind | 否 |  |  |
| 19 | ofund_account | 否 |  |  |
| 20 | sign_status | 否 |  |  |
| 21 | sign_date | 否 |  |  |
| 22 | transaction_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secu_ofacct_rel | 默认 | 否 | stock_account, ofund_account, stock_account, ofund_account |
| idx_secu_ofacct_rel | ART | 是 | stock_account, ofund_account, stock_account, ofund_account |
| idx_secu_ofacct_rel_ofund | ART | 是 | ofund_account, ofund_account |
| idx_secu_ofacct_rel | 默认 | 否 | stock_account, ofund_account, stock_account, ofund_account |
| idx_secu_ofacct_rel | ART | 是 | stock_account, ofund_account, stock_account, ofund_account |
| idx_secu_ofacct_rel_ofund | ART | 是 | ofund_account, ofund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_secu_ofacct_rel | stock_account, ofund_account, stock_account, ofund_account |
| idx_secu_ofacct_rel | stock_account, ofund_account, stock_account, ofund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:57:50 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-08-09 14:33:28 | 3.0.2.34 | 骆鹏程 | 新增事务号 |
| 2024-07-02 16:47:19 | 3.0.2.27 | 张训华 | 物理表secu_ofacct_rel，增加索引(idx_secu_ofacct_rel:[stock_account,o... |
| 2026-03-09 13:57:50 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-08-09 14:33:28 | 3.0.2.34 | 骆鹏程 | 新增事务号 |
| 2024-07-02 16:47:19 | 3.0.2.27 | 张训华 | 物理表secu_ofacct_rel，增加索引(idx_secu_ofacct_rel:[stock_account,o... |

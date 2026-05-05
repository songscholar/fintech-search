# crdt_settle_jour - 融资融券清算流水表

**表对象ID**: 7999
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | settle_no | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | curr_date | 否 |  |  |
| 9 | curr_time | 否 |  |  |
| 10 | settle_no | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | fund_account | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_settle_jour | ART | 是 | settle_no, init_date, settle_no, init_date |
| idx_crdt_settle_jour | ART | 是 | settle_no, init_date, settle_no, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_settle_jour | settle_no, init_date, settle_no, init_date |
| idx_crdt_settle_jour | settle_no, init_date, settle_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-05-26 13:48:09 | V3.0.2.2003 | 马明智 | 新增字段fund_account |
| 2025-03-24 10:00:26 | 3.0.2.2002 | 马明智 | 新增表结构 |
| 2025-05-26 13:48:09 | V3.0.2.2003 | 马明智 | 新增字段fund_account |
| 2025-03-24 10:00:26 | 3.0.2.2002 | 马明智 | 新增表结构 |

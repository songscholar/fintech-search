# crdt_report_abstract - 虚拟股东申报账号控制表

**表对象ID**: 7580
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | abstract_account | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | report_account | 否 |  |  |
| 5 | fund_account | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | holder_level | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | abstract_account | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | report_account | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | holder_level | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtreportabstract | ART | 是 | abstract_account, branch_no, exchange_type, abstract_account, branch_no, exchange_type |
| idx_crdtreportabstract | ART | 是 | abstract_account, branch_no, exchange_type, abstract_account, branch_no, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtreportabstract | abstract_account, branch_no, exchange_type, abstract_account, branch_no, exchange_type |
| idx_crdtreportabstract | abstract_account, branch_no, exchange_type, abstract_account, branch_no, exchange_type |

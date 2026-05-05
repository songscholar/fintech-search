# uref_risk_acctlist - 转融通风险客户名单表

**表对象ID**: 6037
**所属模块**: refacct
**数据空间**: HS_UFT_DATA

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_name | 否 |  |  |
| 2 | refrisk_type | 否 |  | 0-出借黑名单 1-监控黑名单 2-警戒名单 |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | client_name | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | id_kind | 否 |  |  |
| 9 | id_no | 否 |  |  |
| 10 | seat_no | 否 |  |  |
| 11 | refsrc_type | 否 |  | 0-系统生成 1-业务部门确认 2-行业通报 |
| 12 | create_date | 否 |  | 发生日期 |
| 13 | remark | 否 |  |  |
| 14 | company_name | 否 |  |  |
| 15 | refrisk_type | 否 |  | 0-出借黑名单 1-监控黑名单 2-警戒名单 |
| 16 | branch_no | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | client_id | 否 |  |  |
| 19 | client_name | 否 |  |  |
| 20 | stock_account | 否 |  |  |
| 21 | id_kind | 否 |  |  |
| 22 | id_no | 否 |  |  |
| 23 | seat_no | 否 |  |  |
| 24 | refsrc_type | 否 |  | 0-系统生成 1-业务部门确认 2-行业通报 |
| 25 | create_date | 否 |  | 发生日期 |
| 26 | remark | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refriskacctlist | ART | 是 | id_no, id_kind, id_no, id_kind |
| idx_refriskacctlist_type | ART | 是 | refrisk_type, refrisk_type |
| idx_refriskacctlist_acct | ART | 是 | fund_account, fund_account |
| idx_refriskacctlist | ART | 是 | id_no, id_kind, id_no, id_kind |
| idx_refriskacctlist_type | ART | 是 | refrisk_type, refrisk_type |
| idx_refriskacctlist_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refriskacctlist | id_no, id_kind, id_no, id_kind |
| idx_refriskacctlist | id_no, id_kind, id_no, id_kind |

# uarg_crt_client_svrfare - 信用客户特殊服务佣金表

**表对象ID**: 7109
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | svr_fare_kind | 否 |  |  |
| 5 | begin_date | 否 |  |  |
| 6 | end_date | 否 |  |  |
| 7 | sign_time | 否 |  |  |
| 8 | sign_date | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | fund_account(18)+svr_fare_kind(10) |
| 14 | fund_account | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | branch_no | 否 |  |  |
| 17 | svr_fare_kind | 否 |  |  |
| 18 | begin_date | 否 |  |  |
| 19 | end_date | 否 |  |  |
| 20 | sign_time | 否 |  |  |
| 21 | sign_date | 否 |  |  |
| 22 | transaction_no | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | fund_account(18)+svr_fare_kind(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_crt_client_svrfare | ART | 是 | fund_account, svr_fare_kind, fund_account, svr_fare_kind |
| idx_uarg_crt_client_svrfare | ART | 是 | fund_account, svr_fare_kind, fund_account, svr_fare_kind |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_crt_client_svrfare | fund_account, svr_fare_kind, fund_account, svr_fare_kind |
| idx_uarg_crt_client_svrfare_acct | fund_account, fund_account |
| idx_uarg_crt_client_svrfare_client | client_id, client_id |
| idx_uarg_crt_client_svrfare | fund_account, svr_fare_kind, fund_account, svr_fare_kind |
| idx_uarg_crt_client_svrfare_acct | fund_account, fund_account |
| idx_uarg_crt_client_svrfare_client | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-13 14:30:37 | 3.0.6.97 | 李想 | 新增表 |
| 2025-03-13 14:30:37 | 3.0.6.97 | 李想 | 新增表 |

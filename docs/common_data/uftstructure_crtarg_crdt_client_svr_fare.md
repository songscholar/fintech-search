# crdt_client_svr_fare - 信用账户特殊服务佣金表

**表对象ID**: 7045
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | svr_fare_kind | 否 |  |  |
| 4 | begin_date | 否 |  |  |
| 5 | end_date | 否 |  |  |
| 6 | sign_time | 否 |  |  |
| 7 | sign_date | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | client_id | 否 |  |  |
| 11 | svr_fare_kind | 否 |  |  |
| 12 | begin_date | 否 |  |  |
| 13 | end_date | 否 |  |  |
| 14 | sign_time | 否 |  |  |
| 15 | sign_date | 否 |  |  |
| 16 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_client_svr_fare | ART | 是 | fund_account, svr_fare_kind, fund_account, svr_fare_kind |
| idx_crdt_client_svr_fare | ART | 是 | fund_account, svr_fare_kind, fund_account, svr_fare_kind |

## 数据库索引（共 6 个）

| 索引名 | 字段 |
|--------|------|
| idx_client_svr_fare | fund_account, svr_fare_kind, fund_account, svr_fare_kind |
| idx_client_svr_fare_acct | fund_account, fund_account |
| idx_client_svr_fare_client | client_id, client_id |
| idx_client_svr_fare | fund_account, svr_fare_kind, fund_account, svr_fare_kind |
| idx_client_svr_fare_acct | fund_account, fund_account |
| idx_client_svr_fare_client | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-11-06 10:11:24 | 3.0.6.13 | 许琮擎 | 物理表crdt_client_svr_fare，添加了表字段(sign_date);
 |
| 2024-05-21 16:25:26 | 3.0.2.13 | 楼欣欣 | 支持crdtclientsvrfare参数同步内存 |
| 2024-11-06 10:11:24 | 3.0.6.13 | 许琮擎 | 物理表crdt_client_svr_fare，添加了表字段(sign_date);
 |
| 2024-05-21 16:25:26 | 3.0.2.13 | 楼欣欣 | 支持crdtclientsvrfare参数同步内存 |

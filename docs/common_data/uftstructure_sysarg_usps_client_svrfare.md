# usps_client_svrfare - 账户特殊服务佣金表

**表对象ID**: 33
**所属模块**: sysarg
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
| 7 | transaction_no | 否 |  |  |
| 8 | sign_time | 否 |  |  |
| 9 | sign_date | 否 |  |  |
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
| 20 | transaction_no | 否 |  |  |
| 21 | sign_time | 否 |  |  |
| 22 | sign_date | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | fund_account(18)+svr_fare_kind(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_client_svrfare | ART | 是 | fund_account, svr_fare_kind, fund_account, svr_fare_kind |
| idx_usps_client_svrfare | ART | 是 | fund_account, svr_fare_kind, fund_account, svr_fare_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_client_svrfare | fund_account, svr_fare_kind, fund_account, svr_fare_kind |
| idx_usps_client_svrfare | fund_account, svr_fare_kind, fund_account, svr_fare_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 15:27:02 | 3.0.6.12 | 常行 | 物理表usps_client_svrfare，添加了表字段(client_id);
物理表usps_client_sv... |
| 2024-09-27 15:08:21 | 3.0.2.30 | yusz | 物理表usps_client_svrfare，添加了表字段(sign_time);
物理表usps_client_sv... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-02-14 15:27:02 | 3.0.6.12 | 常行 | 物理表usps_client_svrfare，添加了表字段(client_id);
物理表usps_client_sv... |
| 2024-09-27 15:08:21 | 3.0.2.30 | yusz | 物理表usps_client_svrfare，添加了表字段(sign_time);
物理表usps_client_sv... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

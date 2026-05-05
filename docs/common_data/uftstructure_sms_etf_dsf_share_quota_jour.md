# etf_dsf_share_quota_jour - ETF代收代付共享额度流水表

**表对象ID**: 2842
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | group_no | 是 |  |  |
| 4 | total_quota | 是 |  |  |
| 5 | used_quota | 是 |  |  |
| 6 | enable_quota | 是 |  |  |
| 7 | occur_quota | 是 |  |  |
| 8 | set_seat_no | 是 |  |  |
| 9 | file_type | 是 |  |  |
| 10 | file_kind | 是 |  |  |
| 11 | exchange_type | 是 |  |  |
| 12 | status | 是 |  |  |
| 13 | remark | 是 |  |  |
| 14 | init_date | 是 |  |  |
| 15 | serial_no | 是 |  |  |
| 16 | group_no | 是 |  |  |
| 17 | total_quota | 是 |  |  |
| 18 | used_quota | 是 |  |  |
| 19 | enable_quota | 是 |  |  |
| 20 | occur_quota | 是 |  |  |
| 21 | set_seat_no | 是 |  |  |
| 22 | file_type | 是 |  |  |
| 23 | file_kind | 是 |  |  |
| 24 | exchange_type | 是 |  |  |
| 25 | status | 是 |  |  |
| 26 | remark | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etf_dsf_share_quota_jour_cid | 默认 | 是 | init_date, serial_no, init_date, serial_no |
| idx_etf_dsf_share_quota_jour | 默认 | 否 | set_seat_no, file_type, file_kind, exchange_type, set_seat_no, file_type, file_kind, exchange_type |
| idx_etf_dsf_share_quota_jour_cid | 默认 | 是 | init_date, serial_no, init_date, serial_no |
| idx_etf_dsf_share_quota_jour | 默认 | 否 | set_seat_no, file_type, file_kind, exchange_type, set_seat_no, file_type, file_kind, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etf_dsf_share_quota_jour_cid | init_date, serial_no, init_date, serial_no |
| idx_etf_dsf_share_quota_jour_cid | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-06-23 10:53:47 | 3.0.2.2005 | 马明智 | ETF代收代付可用资金更新-初始化后业务处理 |
| 2025-06-23 10:53:47 | 3.0.2.2005 | 马明智 | ETF代收代付可用资金更新-初始化后业务处理 |

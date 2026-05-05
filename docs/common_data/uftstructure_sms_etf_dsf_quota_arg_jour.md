# etf_dsf_quota_arg_jour - ETF代收代付个人额度参数流水表

**表对象ID**: 2841
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | serial_no | 是 |  |  |
| 3 | fund_account | 是 |  |  |
| 4 | group_no | 是 |  |  |
| 5 | total_quota | 是 |  |  |
| 6 | used_quota | 是 |  |  |
| 7 | enable_quota | 是 |  |  |
| 8 | occur_quota | 是 |  |  |
| 9 | set_seat_no | 是 |  |  |
| 10 | file_type | 是 |  |  |
| 11 | file_kind | 是 |  |  |
| 12 | exchange_type | 是 |  |  |
| 13 | status | 是 |  |  |
| 14 | remark | 是 |  |  |
| 15 | init_date | 是 |  |  |
| 16 | serial_no | 是 |  |  |
| 17 | fund_account | 是 |  |  |
| 18 | group_no | 是 |  |  |
| 19 | total_quota | 是 |  |  |
| 20 | used_quota | 是 |  |  |
| 21 | enable_quota | 是 |  |  |
| 22 | occur_quota | 是 |  |  |
| 23 | set_seat_no | 是 |  |  |
| 24 | file_type | 是 |  |  |
| 25 | file_kind | 是 |  |  |
| 26 | exchange_type | 是 |  |  |
| 27 | status | 是 |  |  |
| 28 | remark | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etf_dsf_quota_arg_jour_cid | 默认 | 是 | init_date, serial_no, init_date, serial_no |
| idx_etf_dsf_quota_arg_jour | 默认 | 否 | set_seat_no, file_type, file_kind, exchange_type, set_seat_no, file_type, file_kind, exchange_type |
| idx_etf_dsf_quota_arg_jour_cid | 默认 | 是 | init_date, serial_no, init_date, serial_no |
| idx_etf_dsf_quota_arg_jour | 默认 | 否 | set_seat_no, file_type, file_kind, exchange_type, set_seat_no, file_type, file_kind, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etf_dsf_quota_arg_jour_cid | init_date, serial_no, init_date, serial_no |
| idx_etf_dsf_quota_arg_jour_cid | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-06-23 10:53:47 | 3.0.2.2005 | 马明智 | ETF代收代付可用资金更新-初始化后业务处理 |
| 2025-06-23 10:53:47 | 3.0.2.2005 | 马明智 | ETF代收代付可用资金更新-初始化后业务处理 |

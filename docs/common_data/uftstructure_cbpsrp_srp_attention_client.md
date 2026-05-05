# srp_attention_client - 股票质押特别关注客户信息表

**表对象ID**: 2650
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | srp_attention_type | 否 |  |  |
| 4 | fine_balance_person | 否 |  |  |
| 5 | srp_attention_status | 否 |  |  |
| 6 | open_date | 否 |  |  |
| 7 | cancel_date | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | position_str | 否 |  | client_id(18)+srp_attention_type(2) |
| 14 | branch_no | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | srp_attention_type | 否 |  |  |
| 17 | fine_balance_person | 否 |  |  |
| 18 | srp_attention_status | 否 |  |  |
| 19 | open_date | 否 |  |  |
| 20 | cancel_date | 否 |  |  |
| 21 | date_clear | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | update_date | 否 |  |  |
| 24 | update_time | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | position_str | 否 |  | client_id(18)+srp_attention_type(2) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_srp_attention_client | 默认 | 否 |  |
| idx_srp_attention_client | ART | 是 | client_id, srp_attention_type, client_id, srp_attention_type |
| idx_srp_attention_client | 默认 | 否 |  |
| idx_srp_attention_client | ART | 是 | client_id, srp_attention_type, client_id, srp_attention_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_srp_attention_client | client_id, srp_attention_type, client_id, srp_attention_type |
| idx_srp_attention_client | client_id, srp_attention_type, client_id, srp_attention_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:00:02 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:35:42 | 3.0.2.6 | taocong45644 | 当前表srp_attention_client，修改了索引idx_srp_attention_client,索引字段修改... |
| 2025-02-19 17:23:18 | 3.0.3.6 | 李想 | 新增表 |
| 2026-03-06 17:00:02 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:35:42 | 3.0.2.6 | taocong45644 | 当前表srp_attention_client，修改了索引idx_srp_attention_client,索引字段修改... |
| 2025-02-19 17:23:18 | 3.0.3.6 | 李想 | 新增表 |

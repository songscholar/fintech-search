# uft_crdt_dictate - UFT信用账户指令信息表

**表对象ID**: 7988
**所属模块**: crttrade
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB

## 字段列表（共 58 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | op_branch_no | 否 |  |  |
| 4 | operator_no | 否 |  |  |
| 5 | op_entrust_way | 否 |  |  |
| 6 | op_station | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | branch_no | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | assure_asset | 否 |  |  |
| 11 | total_debit | 否 |  |  |
| 12 | assurescale_value | 否 |  |  |
| 13 | dictate_applicant | 否 |  |  |
| 14 | apply_date | 否 |  |  |
| 15 | apply_time | 否 |  |  |
| 16 | dictate_sender | 否 |  |  |
| 17 | send_date | 否 |  |  |
| 18 | send_time | 否 |  |  |
| 19 | dictate_closer | 否 |  |  |
| 20 | close_date | 否 |  |  |
| 21 | close_time | 否 |  |  |
| 22 | dictate_type | 否 |  |  |
| 23 | dictate_status | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | limit_days | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | position_str | 否 |  |  |
| 28 | order_no | 否 |  |  |
| 29 | en_payoff_reason | 否 |  |  |
| 30 | init_date | 否 |  |  |
| 31 | serial_no | 否 |  |  |
| 32 | op_branch_no | 否 |  |  |
| 33 | operator_no | 否 |  |  |
| 34 | op_entrust_way | 否 |  |  |
| 35 | op_station | 否 |  |  |
| 36 | client_id | 否 |  |  |
| 37 | branch_no | 否 |  |  |
| 38 | fund_account | 否 |  |  |
| 39 | assure_asset | 否 |  |  |
| 40 | total_debit | 否 |  |  |
| 41 | assurescale_value | 否 |  |  |
| 42 | dictate_applicant | 否 |  |  |
| 43 | apply_date | 否 |  |  |
| 44 | apply_time | 否 |  |  |
| 45 | dictate_sender | 否 |  |  |
| 46 | send_date | 否 |  |  |
| 47 | send_time | 否 |  |  |
| 48 | dictate_closer | 否 |  |  |
| 49 | close_date | 否 |  |  |
| 50 | close_time | 否 |  |  |
| 51 | dictate_type | 否 |  |  |
| 52 | dictate_status | 否 |  |  |
| 53 | date_clear | 否 |  |  |
| 54 | limit_days | 否 |  |  |
| 55 | remark | 否 |  |  |
| 56 | position_str | 否 |  |  |
| 57 | order_no | 否 |  |  |
| 58 | en_payoff_reason | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_crdt_dictate_acct | ART | 是 | fund_account, fund_account |
| idx_uft_crdt_dictate_pos | ART | 是 | position_str, position_str |
| idx_uft_crdt_dictate_acct | ART | 是 | fund_account, fund_account |
| idx_uft_crdt_dictate_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_crdt_dictate_pos | position_str, position_str |
| idx_uft_crdt_dictate_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-17 16:36:42 | 3.0.2.21 | 常行 | uft_crdt_dictate表空间改为HS_USMS_DATA，存储介质改为DB+MDB |
| 2025-10-17 16:36:42 | 3.0.2.21 | 常行 | uft_crdt_dictate表空间改为HS_USMS_DATA，存储介质改为DB+MDB |

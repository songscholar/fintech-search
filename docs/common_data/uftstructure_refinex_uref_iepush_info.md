# uref_iepush_info - 信息交互平台推送信息表

**表对象ID**: 6226
**所属模块**: refinex
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | iereport_id | 否 |  |  |
| 3 | topic_name | 否 |  |  |
| 4 | ie_busin_type | 否 |  |  |
| 5 | opp_organ_code | 否 |  |  |
| 6 | opp_borrower_code | 否 |  |  |
| 7 | message_id | 否 |  |  |
| 8 | message_no | 否 |  |  |
| 9 | deal_status | 否 |  |  |
| 10 | csfc_organ_code | 否 |  |  |
| 11 | csfc_borrower_code | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | iereport_id | 否 |  |  |
| 14 | topic_name | 否 |  |  |
| 15 | ie_busin_type | 否 |  |  |
| 16 | opp_organ_code | 否 |  |  |
| 17 | opp_borrower_code | 否 |  |  |
| 18 | message_id | 否 |  |  |
| 19 | message_no | 否 |  |  |
| 20 | deal_status | 否 |  |  |
| 21 | csfc_organ_code | 否 |  |  |
| 22 | csfc_borrower_code | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_iepushinfo | ART | 是 | message_id, csfc_organ_code, csfc_borrower_code, message_id, csfc_organ_code, csfc_borrower_code |
| idx_iepushinfo | ART | 是 | message_id, csfc_organ_code, csfc_borrower_code, message_id, csfc_organ_code, csfc_borrower_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_iepushinfo | message_id, csfc_organ_code, csfc_borrower_code, message_id, csfc_organ_code, csfc_borrower_code |
| idx_iepushinfo | message_id, csfc_organ_code, csfc_borrower_code, message_id, csfc_organ_code, csfc_borrower_code |

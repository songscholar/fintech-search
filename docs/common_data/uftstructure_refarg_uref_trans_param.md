# uref_trans_param - 转融通报盘参数表

**表对象ID**: 6019
**所属模块**: refarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | clear_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | operator_no | 否 |  |  |
| 4 | trans_name | 否 |  |  |
| 5 | login_pbu | 否 |  |  |
| 6 | trans_config | 否 |  |  |
| 7 | report_status | 否 |  |  |
| 8 | order_num | 否 |  |  |
| 9 | business_num | 否 |  |  |
| 10 | confirm_num | 否 |  |  |
| 11 | other_config | 否 |  |  |
| 12 | en_seat_no | 否 |  |  |
| 13 | clear_date | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | operator_no | 否 |  |  |
| 16 | trans_name | 否 |  |  |
| 17 | login_pbu | 否 |  |  |
| 18 | trans_config | 否 |  |  |
| 19 | report_status | 否 |  |  |
| 20 | order_num | 否 |  |  |
| 21 | business_num | 否 |  |  |
| 22 | confirm_num | 否 |  |  |
| 23 | other_config | 否 |  |  |
| 24 | en_seat_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reftransparam | ART | 是 | operator_no, trans_name, operator_no, trans_name |
| idx_reftransparam | ART | 是 | operator_no, trans_name, operator_no, trans_name |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_reftransparam | operator_no, trans_name, operator_no, trans_name |
| idx_reftransparam | operator_no, trans_name, operator_no, trans_name |

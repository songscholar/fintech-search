# limit_client - 受限客户名单表

**表对象ID**: 141
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | busiwhite_kind | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | holder_name | 否 |  |  |
| 6 | internal_account | 否 |  |  |
| 7 | corp_id | 否 |  |  |
| 8 | post_type | 否 |  |  |
| 9 | post_ratio | 否 |  |  |
| 10 | post_status | 否 |  |  |
| 11 | post_date | 否 |  |  |
| 12 | leave_date | 否 |  |  |
| 13 | report_firm_code | 否 |  |  |
| 14 | company_no | 否 |  |  |
| 15 | end_date | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | position_str | 否 |  | exchange_type(4)+stock_account(20)+stock_code(8)+busiwhite_k |
| 20 | exchange_type | 否 |  |  |
| 21 | stock_account | 否 |  |  |
| 22 | busiwhite_kind | 否 |  |  |
| 23 | stock_code | 否 |  |  |
| 24 | holder_name | 否 |  |  |
| 25 | internal_account | 否 |  |  |
| 26 | corp_id | 否 |  |  |
| 27 | post_type | 否 |  |  |
| 28 | post_ratio | 否 |  |  |
| 29 | post_status | 否 |  |  |
| 30 | post_date | 否 |  |  |
| 31 | leave_date | 否 |  |  |
| 32 | report_firm_code | 否 |  |  |
| 33 | company_no | 否 |  |  |
| 34 | end_date | 否 |  |  |
| 35 | update_date | 否 |  |  |
| 36 | update_time | 否 |  |  |
| 37 | transaction_no | 否 |  |  |
| 38 | position_str | 否 |  | exchange_type(4)+stock_account(20)+stock_code(8)+busiwhite_k |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_limit_client_pos | 默认 | 否 |  |
| idx_limit_client_pos | ART | 是 | position_str, position_str |
| uk_rpt_limitclient | ART | 是 | end_date, position_str, end_date, position_str |
| idx_limit_client_pos | 默认 | 否 |  |
| idx_limit_client_pos | ART | 是 | position_str, position_str |
| uk_rpt_limitclient | ART | 是 | end_date, position_str, end_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_limit_client_pos | position_str, position_str |
| idx_limit_client_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-15 18:48:44 | 3.0.2.103 | 洪略 | 补充历史资源 |
| 2025-12-01 14:46:18 | 3.0.2.103 | taocong45644 | 当前表limit_client，修改了索引idx_limit_client_pos,索引字段修改为：(position_... |
| 2025-02-22 15:07:30 | 3.0.6.120 | 李想 | 新增表 |
| 2025-12-15 18:48:44 | 3.0.2.103 | 洪略 | 补充历史资源 |
| 2025-12-01 14:46:18 | 3.0.2.103 | taocong45644 | 当前表limit_client，修改了索引idx_limit_client_pos,索引字段修改为：(position_... |
| 2025-02-22 15:07:30 | 3.0.6.120 | 李想 | 新增表 |

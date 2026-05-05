# crdt_busi_whitelist - 融资融券业务白名单表

**表对象ID**: 7123
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | crdtwhite_type | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | stock_type | 否 |  |  |
| 7 | remark | 否 |  |  |
| 8 | compact_type | 否 |  |  |
| 9 | end_date | 否 |  |  |
| 10 | create_date | 否 |  |  |
| 11 | en_compact_source | 否 |  |  |
| 12 | en_crdt_busi_type | 否 |  |  |
| 13 | en_crdtrisk_no | 否 |  |  |
| 14 | acode_account | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+crdtwhite_type(1)+stock_code(8)+exchange_ty |
| 19 | tohis_date | 否 | H |  |
| 20 | fund_account | 否 |  |  |
| 21 | branch_no | 否 |  |  |
| 22 | crdtwhite_type | 否 |  |  |
| 23 | exchange_type | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | stock_type | 否 |  |  |
| 26 | remark | 否 |  |  |
| 27 | compact_type | 否 |  |  |
| 28 | end_date | 否 |  |  |
| 29 | create_date | 否 |  |  |
| 30 | en_compact_source | 否 |  |  |
| 31 | en_crdt_busi_type | 否 |  |  |
| 32 | en_crdtrisk_no | 否 |  |  |
| 33 | acode_account | 否 |  |  |
| 34 | update_date | 否 |  |  |
| 35 | update_time | 否 |  |  |
| 36 | transaction_no | 否 |  |  |
| 37 | position_str | 否 |  | fund_account(18)+crdtwhite_type(1)+stock_code(8)+exchange_ty |
| 38 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdtbusiwhitelist | ART | 是 | fund_account, crdtwhite_type, stock_code, exchange_type, stock_type, compact_type, fund_account, crdtwhite_type, stock_code, exchange_type, stock_type, compact_type |
| uk_rpt_crdtbusiwhitelist | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_crdtbusiwhitelist | ART | 是 | fund_account, crdtwhite_type, stock_code, exchange_type, stock_type, compact_type, fund_account, crdtwhite_type, stock_code, exchange_type, stock_type, compact_type |
| uk_rpt_crdtbusiwhitelist | ART | 是 | tohis_date, position_str, tohis_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdtbusiwhitelist | fund_account, crdtwhite_type, stock_code, exchange_type, stock_type, compact_type, fund_account, crdtwhite_type, stock_code, exchange_type, stock_type, compact_type |
| idx_crdtbusiwhitelist | fund_account, crdtwhite_type, stock_code, exchange_type, stock_type, compact_type, fund_account, crdtwhite_type, stock_code, exchange_type, stock_type, compact_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-05-08 16:50:43 | 3.0.6.109 | 常行 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-05-08 16:50:43 | 3.0.6.109 | 常行 | 新增表 |

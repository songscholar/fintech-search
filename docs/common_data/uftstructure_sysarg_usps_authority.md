# usps_authority - 权益登记表

**表对象ID**: 61
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | business_type | 否 |  |  |
| 5 | authority_code | 否 |  |  |
| 6 | register_date | 否 |  |  |
| 7 | distribute_rate | 否 |  |  |
| 8 | pay_begin_date | 否 |  |  |
| 9 | pay_end_date | 否 |  |  |
| 10 | authority_type | 否 |  |  |
| 11 | onetax_rate | 否 |  |  |
| 12 | orgtax_rate | 否 |  |  |
| 13 | arp_onetax_rate | 否 |  |  |
| 14 | pretax_balance | 否 |  |  |
| 15 | hkdc_corpbehavior_code | 否 |  |  |
| 16 | placard_id | 否 |  |  |
| 17 | info_kind | 否 |  |  |
| 18 | issue_price | 否 |  |  |
| 19 | round_type | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | exchange_type(4)+business_type(1)+authority_code(8)+register |
| 25 | stock_name | 否 | H |  |
| 26 | sub_stock_type | 否 | H |  |
| 27 | stock_type | 否 | H |  |
| 28 | init_date | 否 |  |  |
| 29 | exchange_type | 否 |  |  |
| 30 | stock_code | 否 |  |  |
| 31 | business_type | 否 |  |  |
| 32 | authority_code | 否 |  |  |
| 33 | register_date | 否 |  |  |
| 34 | distribute_rate | 否 |  |  |
| 35 | pay_begin_date | 否 |  |  |
| 36 | pay_end_date | 否 |  |  |
| 37 | authority_type | 否 |  |  |
| 38 | onetax_rate | 否 |  |  |
| 39 | orgtax_rate | 否 |  |  |
| 40 | arp_onetax_rate | 否 |  |  |
| 41 | pretax_balance | 否 |  |  |
| 42 | hkdc_corpbehavior_code | 否 |  |  |
| 43 | placard_id | 否 |  |  |
| 44 | info_kind | 否 |  |  |
| 45 | issue_price | 否 |  |  |
| 46 | round_type | 否 |  |  |
| 47 | remark | 否 |  |  |
| 48 | transaction_no | 否 |  |  |
| 49 | update_date | 否 |  |  |
| 50 | update_time | 否 |  |  |
| 51 | position_str | 否 |  | exchange_type(4)+business_type(1)+authority_code(8)+register |
| 52 | stock_name | 否 | H |  |
| 53 | sub_stock_type | 否 | H |  |
| 54 | stock_type | 否 | H |  |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_authority_code | 默认 | 否 | exchange_type, business_type, info_kind, placard_id, stock_code, exchange_type, business_type, info_kind, placard_id, stock_code |
| idx_usps_authority | ART | 是 | exchange_type, business_type, authority_code, register_date, stock_code, placard_id, info_kind, exchange_type, business_type, authority_code, register_date, stock_code, placard_id, info_kind |
| idx_usps_authority_type | ART | 是 | exchange_type, business_type, authority_code, register_date, exchange_type, business_type, authority_code, register_date |
| idx_usps_authority_code | ART | 是 | exchange_type, business_type, info_kind, placard_id, stock_code, exchange_type, business_type, info_kind, placard_id, stock_code |
| idx_authority_pos | ART | 是 | position_str, position_str |
| uk_rpt_uspsauthority | ART | 是 | position_str, position_str |
| idx_rpt_uspsauthority_reg | ART | 是 | register_date, register_date |
| idx_usps_authority_code | 默认 | 否 | exchange_type, business_type, info_kind, placard_id, stock_code, exchange_type, business_type, info_kind, placard_id, stock_code |
| idx_usps_authority | ART | 是 | exchange_type, business_type, authority_code, register_date, stock_code, placard_id, info_kind, exchange_type, business_type, authority_code, register_date, stock_code, placard_id, info_kind |
| idx_usps_authority_type | ART | 是 | exchange_type, business_type, authority_code, register_date, exchange_type, business_type, authority_code, register_date |
| idx_usps_authority_code | ART | 是 | exchange_type, business_type, info_kind, placard_id, stock_code, exchange_type, business_type, info_kind, placard_id, stock_code |
| idx_authority_pos | ART | 是 | position_str, position_str |
| uk_rpt_uspsauthority | ART | 是 | position_str, position_str |
| idx_rpt_uspsauthority_reg | ART | 是 | register_date, register_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_authority | position_str, position_str |
| idx_usps_authority | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-22 15:16:50 | 3.0.2.101 | 常行 | 所有表usps_authority，添加了表字段(issue_price);
所有表usps_authority，添加... |
| 2025-02-14 17:27:33 | 3.0.6.12 | 常行 | 物理表usps_authority，添加了表字段(update_date);
物理表usps_authority，添加... |
| 2024-10-30 17:28:22 | 3.0.5.1002 | 雷玄 | 物理表usps_authority，增加索引(idx_usps_authority_code:[exchange_typ... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:12 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2023-05-26 13:33 | 0.0.0.3 | 徐世晗 | 新增 |
| 2025-11-22 15:16:50 | 3.0.2.101 | 常行 | 所有表usps_authority，添加了表字段(issue_price);
所有表usps_authority，添加... |
| 2025-02-14 17:27:33 | 3.0.6.12 | 常行 | 物理表usps_authority，添加了表字段(update_date);
物理表usps_authority，添加... |
| 2024-10-30 17:28:22 | 3.0.5.1002 | 雷玄 | 物理表usps_authority，增加索引(idx_usps_authority_code:[exchange_typ... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:12 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2023-05-26 13:33 | 0.0.0.3 | 徐世晗 | 新增 |

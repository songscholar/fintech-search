# settredo_usps_authority - 清算重做权益登记表

**表对象ID**: 161
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | position_str | 否 |  |  |
| 2 | sett_dml_type | 否 |  |  |
| 3 | sett_batch_no | 否 |  |  |
| 4 | init_date | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_code | 是 |  |  |
| 7 | business_type | 是 |  |  |
| 8 | authority_code | 是 |  |  |
| 9 | register_date | 是 |  |  |
| 10 | distribute_rate | 是 |  |  |
| 11 | pay_begin_date | 是 |  |  |
| 12 | pay_end_date | 是 |  |  |
| 13 | authority_type | 是 |  |  |
| 14 | onetax_rate | 是 |  |  |
| 15 | orgtax_rate | 是 |  |  |
| 16 | arp_onetax_rate | 是 |  |  |
| 17 | pretax_balance | 是 |  |  |
| 18 | hkdc_corpbehavior_code | 是 |  |  |
| 19 | placard_id | 是 |  |  |
| 20 | info_kind | 是 |  |  |
| 21 | remark | 是 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | sett_dml_type | 否 |  |  |
| 24 | sett_batch_no | 否 |  |  |
| 25 | init_date | 是 |  |  |
| 26 | exchange_type | 是 |  |  |
| 27 | stock_code | 是 |  |  |
| 28 | business_type | 是 |  |  |
| 29 | authority_code | 是 |  |  |
| 30 | register_date | 是 |  |  |
| 31 | distribute_rate | 是 |  |  |
| 32 | pay_begin_date | 是 |  |  |
| 33 | pay_end_date | 是 |  |  |
| 34 | authority_type | 是 |  |  |
| 35 | onetax_rate | 是 |  |  |
| 36 | orgtax_rate | 是 |  |  |
| 37 | arp_onetax_rate | 是 |  |  |
| 38 | pretax_balance | 是 |  |  |
| 39 | hkdc_corpbehavior_code | 是 |  |  |
| 40 | placard_id | 是 |  |  |
| 41 | info_kind | 是 |  |  |
| 42 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_authority_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_authority_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_authority_pos | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_settredo_authority_pos | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-09 14:38:58 | 8.26.2.93 |  | 所有表settredo_usps_authority，添加了表字段(init_date);
所有表settredo_u... |
| 2025-10-09 14:38:58 | 8.26.2.93 |  | 所有表settredo_usps_authority，添加了表字段(init_date);
所有表settredo_u... |

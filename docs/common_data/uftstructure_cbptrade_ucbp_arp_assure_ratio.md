# ucbp_arp_assure_ratio - 约定购回折算率表

**表对象ID**: 2530
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | arp_assure_ratio | 否 |  |  |
| 7 | begin_date | 否 |  |  |
| 8 | end_date | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_code(8)+begin_date(1 |
| 14 | branch_no | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | arp_assure_ratio | 否 |  |  |
| 20 | begin_date | 否 |  |  |
| 21 | end_date | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_code(8)+begin_date(1 |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_arpassureratio_id | 默认 | 否 | client_id, client_id |
| idx_arpassureratio | ART | 是 | fund_account, exchange_type, stock_code, begin_date, fund_account, exchange_type, stock_code, begin_date |
| idx_arpassureratio_acct | ART | 是 | fund_account, fund_account |
| idx_arpassureratio_id | ART | 是 | client_id, client_id |
| idx_arpassureratio_id | 默认 | 否 | client_id, client_id |
| idx_arpassureratio | ART | 是 | fund_account, exchange_type, stock_code, begin_date, fund_account, exchange_type, stock_code, begin_date |
| idx_arpassureratio_acct | ART | 是 | fund_account, fund_account |
| idx_arpassureratio_id | ART | 是 | client_id, client_id |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_arpassureratio | fund_account, exchange_type, stock_code, begin_date, fund_account, exchange_type, stock_code, begin_date |
| idx_arpassureratio_id | client_id, client_id |
| idx_arpassureratio | fund_account, exchange_type, stock_code, begin_date, fund_account, exchange_type, stock_code, begin_date |
| idx_arpassureratio_id | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:20:05 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-07-16 17:47:15 | V3.0.6.13 | 常行 | 物理表ucbp_arp_assure_ratio，增加索引(idx_arpassureratio_id:[client_... |
| 2025-04-21 16:24:58 | V3.0.5.1027 | 常行 | 物理表ucbp_arp_assure_ratio，添加了表字段(update_date);
物理表ucbp_arp_a... |
| 2026-03-04 16:20:05 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-07-16 17:47:15 | V3.0.6.13 | 常行 | 物理表ucbp_arp_assure_ratio，增加索引(idx_arpassureratio_id:[client_... |
| 2025-04-21 16:24:58 | V3.0.5.1027 | 常行 | 物理表ucbp_arp_assure_ratio，添加了表字段(update_date);
物理表ucbp_arp_a... |

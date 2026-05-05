# business_white_list - 证券业务白名单表

**表对象ID**: 5528
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | busiwhite_kind | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_account(10)+stock_co |
| 7 | stock_type | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | end_date | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | fund_account | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | busiwhite_kind | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_account(10)+stock_co |
| 20 | stock_type | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | end_date | 否 |  |  |
| 23 | transaction_no | 否 |  |  |
| 24 | branch_no | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_business_white_list_uk | 默认 | 否 | stock_code, stock_code |
| idx_business_white_list | ART | 是 | fund_account, exchange_type, stock_account, busiwhite_kind, fund_account, exchange_type, stock_account, busiwhite_kind |
| idx_business_white_list_uk | ART | 是 | busiwhite_kind, fund_account, exchange_type, stock_account, stock_code, busiwhite_kind, fund_account, exchange_type, stock_account, stock_code |
| uk_rpt_businesswhitelist | ART | 是 | position_str, end_date, position_str, end_date |
| idx_business_white_list_uk | 默认 | 否 | stock_code, stock_code |
| idx_business_white_list | ART | 是 | fund_account, exchange_type, stock_account, busiwhite_kind, fund_account, exchange_type, stock_account, busiwhite_kind |
| idx_business_white_list_uk | ART | 是 | busiwhite_kind, fund_account, exchange_type, stock_account, stock_code, busiwhite_kind, fund_account, exchange_type, stock_account, stock_code |
| uk_rpt_businesswhitelist | ART | 是 | position_str, end_date, position_str, end_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_business_white_list_uk | busiwhite_kind, fund_account, exchange_type, stock_account, stock_code, busiwhite_kind, fund_account, exchange_type, stock_account, stock_code |
| idx_business_white_list_uk | busiwhite_kind, fund_account, exchange_type, stock_account, stock_code, busiwhite_kind, fund_account, exchange_type, stock_account, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:48:11 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-15 16:42:48 | 3.0.2.78 | 洪略 | 补齐历史资源 |
| 2025-08-26 17:14:59 | 3.0.2.78 | 高志强 | 数据存储介质改为DB+MDB |
| 2025-07-21 09:59:09 | 3.0.2.72 | 杨涛 | 物理表business_white_list，添加了表字段(branch_no);
物理表business_white... |
| 2024-05-18 15:41:29 | 3.0.2.8 | 祝丁恺 | 物理表business_white_list，增加索引字段(索引idx_business_white_list_uk:增... |
| 2026-03-09 13:48:11 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-12-15 16:42:48 | 3.0.2.78 | 洪略 | 补齐历史资源 |
| 2025-08-26 17:14:59 | 3.0.2.78 | 高志强 | 数据存储介质改为DB+MDB |
| 2025-07-21 09:59:09 | 3.0.2.72 | 杨涛 | 物理表business_white_list，添加了表字段(branch_no);
物理表business_white... |
| 2024-05-18 15:41:29 | 3.0.2.8 | 祝丁恺 | 物理表business_white_list，增加索引字段(索引idx_business_white_list_uk:增... |

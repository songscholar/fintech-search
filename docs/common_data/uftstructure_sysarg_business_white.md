# business_white - 证券持仓业务白名单表

**表对象ID**: 301
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | busiwhite_kind | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | position_str | 否 |  | branch_no(5)+fund_account(18)+exchange_type(4)+stock_account |
| 8 | stock_type | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | crdtwhite_type | 否 |  |  |
| 11 | compact_type | 否 |  |  |
| 12 | end_date | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | stock_account | 否 |  |  |
| 20 | busiwhite_kind | 否 |  |  |
| 21 | stock_code | 否 |  |  |
| 22 | position_str | 否 |  | branch_no(5)+fund_account(18)+exchange_type(4)+stock_account |
| 23 | stock_type | 否 |  |  |
| 24 | remark | 否 |  |  |
| 25 | crdtwhite_type | 否 |  |  |
| 26 | compact_type | 否 |  |  |
| 27 | end_date | 否 |  |  |
| 28 | transaction_no | 否 |  |  |
| 29 | update_date | 否 |  |  |
| 30 | update_time | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_business_white_acct | 默认 | 否 | fund_account, fund_account |
| idx_business_white_pos | ART | 是 | position_str, position_str |
| idx_business_white_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_busiwhite | ART | 是 | end_date, position_str, end_date, position_str |
| idx_business_white_acct | 默认 | 否 | fund_account, fund_account |
| idx_business_white_pos | ART | 是 | position_str, position_str |
| idx_business_white_acct | ART | 是 | fund_account, fund_account |
| uk_rpt_busiwhite | ART | 是 | end_date, position_str, end_date, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_business_white_pos | position_str, position_str |
| idx_business_white_acct | fund_account, fund_account |
| idx_business_white_pos | position_str, position_str |
| idx_business_white_acct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-03 14:25:07 | 3.0.2.104 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-17 14:18:14 | 3.0.6.1017 | 常行 | 物理表business_white，增加索引(idx_business_white_acct:[fund_account... |
| 2025-02-19 15:47:42 | 3.0.6.95 | 李想 | 物理表business_white，添加了表字段(update_date);
物理表business_white，添加... |
| 2024-09-09 11:08:08 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |
| 2025-12-03 14:25:07 | 3.0.2.104 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-07-17 14:18:14 | 3.0.6.1017 | 常行 | 物理表business_white，增加索引(idx_business_white_acct:[fund_account... |
| 2025-02-19 15:47:42 | 3.0.6.95 | 李想 | 物理表business_white，添加了表字段(update_date);
物理表business_white，添加... |
| 2024-09-09 11:08:08 | 3.0.2.28 | 杨森峰 | 表属性调整为不回库 |

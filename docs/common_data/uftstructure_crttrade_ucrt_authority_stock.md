# ucrt_authority_stock - 融资融券权益份额表

**表对象ID**: 7547
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | authority_str | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | current_amount | 否 |  |  |
| 9 | uncome_buy_amount | 否 |  |  |
| 10 | uncome_sell_amount | 否 |  |  |
| 11 | business_type | 否 |  |  |
| 12 | init_date | 否 |  |  |
| 13 | authority_str | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | stock_type | 否 |  |  |
| 19 | current_amount | 否 |  |  |
| 20 | uncome_buy_amount | 否 |  |  |
| 21 | uncome_sell_amount | 否 |  |  |
| 22 | business_type | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_authority_stock | ART | 是 | authority_str, exchange_type, stock_account, stock_code, fund_account, authority_str, exchange_type, stock_account, stock_code, fund_account |
| idx_ucrt_authority_stktype | ART | 是 | exchange_type, stock_account, stock_code, fund_account, business_type, exchange_type, stock_account, stock_code, fund_account, business_type |
| idx_ucrt_authority_stock | ART | 是 | authority_str, exchange_type, stock_account, stock_code, fund_account, authority_str, exchange_type, stock_account, stock_code, fund_account |
| idx_ucrt_authority_stktype | ART | 是 | exchange_type, stock_account, stock_code, fund_account, business_type, exchange_type, stock_account, stock_code, fund_account, business_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_authority_stock | authority_str, exchange_type, stock_account, stock_code, fund_account, authority_str, exchange_type, stock_account, stock_code, fund_account |
| idx_ucrt_authority_stock | authority_str, exchange_type, stock_account, stock_code, fund_account, authority_str, exchange_type, stock_account, stock_code, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-05-26 13:32 | 0.0.0.1 | 徐世晗 | 新增 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-05-26 13:32 | 0.0.0.1 | 徐世晗 | 新增 |

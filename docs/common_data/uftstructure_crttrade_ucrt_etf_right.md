# ucrt_etf_right - 融资融券ETF权限控制表

**表对象ID**: 7507
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | client_id | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | stock_code | 否 |  |  |
| 10 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_etf_right_code | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucrt_etf_right_code | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_etf_right | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucrt_etf_right | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-04-25 15:58:54 | 3.0.2.8 | 楼欣欣 | 物理表ucrt_etf_right，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2024-04-25 15:58:54 | 3.0.2.8 | 楼欣欣 | 物理表ucrt_etf_right，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

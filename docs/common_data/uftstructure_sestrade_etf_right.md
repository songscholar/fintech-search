# etf_right - ETF权限控制表

**表对象ID**: 5730
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | branch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etf_rightctrl_acct | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_etf_rightctrl_acct | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etf_rightctrl_acct | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_etf_rightctrl_acct | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:38:33 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2024-09-23 10:22:14 | 3.0.2.48 | 张明月 | 物理表etf_right，添加了表字段(branch_no);
 |
| 2024-06-20 15:59:22 | 3.0.2.20 | 泮新国 | 物理表etf_right，删除了表字段(branch_no);
物理表etf_right，删除了表字段(client_... |
| 2024-05-18 14:08:58 | 3.0.2.7 | 祝丁恺 | 物理表etf_right，添加了表字段(transaction_no);
 |
| 2026-03-09 14:38:33 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2024-09-23 10:22:14 | 3.0.2.48 | 张明月 | 物理表etf_right，添加了表字段(branch_no);
 |
| 2024-06-20 15:59:22 | 3.0.2.20 | 泮新国 | 物理表etf_right，删除了表字段(branch_no);
物理表etf_right，删除了表字段(client_... |
| 2024-05-18 14:08:58 | 3.0.2.7 | 祝丁恺 | 物理表etf_right，添加了表字段(transaction_no);
 |

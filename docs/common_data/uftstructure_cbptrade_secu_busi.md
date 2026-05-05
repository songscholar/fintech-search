# secu_busi - 交易业务控制信息表

**表对象ID**: 2311
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | stkholder_ctrlstr | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | exchange_type | 否 |  |  |
| 8 | stock_account | 否 |  |  |
| 9 | stkholder_ctrlstr | 否 |  |  |
| 10 | transaction_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secu_busi | 默认 | 否 |  |
| idx_secu_busi | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| idx_secu_busi_stkacc | ART | 是 | stock_account, stock_account |
| idx_secu_busi | 默认 | 否 |  |
| idx_secu_busi | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| idx_secu_busi_stkacc | ART | 是 | stock_account, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_secu_busi | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| idx_secu_busi | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:15:48 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-06-21 14:16:05 | V3.0.1.11 | 吴威 | 物理表secu_busi，添加了表字段(transaction_no);
 |
| 2024-06-20 14:33:22 | V3.0.1.10 | 祝丁恺 | 物理表secu_busi，添加了表字段(fund_account);
物理表secu_busi，添加了表字段(exch... |
| 2026-03-04 15:15:48 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-06-21 14:16:05 | V3.0.1.11 | 吴威 | 物理表secu_busi，添加了表字段(transaction_no);
 |
| 2024-06-20 14:33:22 | V3.0.1.10 | 祝丁恺 | 物理表secu_busi，添加了表字段(fund_account);
物理表secu_busi，添加了表字段(exch... |

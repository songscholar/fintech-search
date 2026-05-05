# setttouftstbstdholder - 清算三板合规证券账户表

**表对象ID**: 3047
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | seat_no | 是 |  |  |
| 2 | stock_code | 是 |  |  |
| 3 | stock_account | 是 |  |  |
| 4 | exchange_type | 是 |  |  |
| 5 | id_no | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | sub_risk_status | 是 |  |  |
| 8 | uft_data_change_status | 是 |  |  |
| 9 | seat_no | 是 |  |  |
| 10 | stock_code | 是 |  |  |
| 11 | stock_account | 是 |  |  |
| 12 | exchange_type | 是 |  |  |
| 13 | id_no | 是 |  |  |
| 14 | fund_account | 是 |  |  |
| 15 | sub_risk_status | 是 |  |  |
| 16 | uft_data_change_status | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settstbstdholder | 默认 | 是 | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |
| idx_settstbstdholder | 默认 | 是 | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settstbstdholder | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |
| idx_settstbstdholder | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-06-12 13:50 | 8.26.1.85 | 罗佳楠 | 新增settstbstdholder表 |
| 2020-06-12 13:50 | 8.26.1.85 | 罗佳楠 | 新增settstbstdholder表 |

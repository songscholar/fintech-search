# usps_farefundacct - 资产账户佣金类别表

**表对象ID**: 56
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | money_type | 否 |  |  |
| 3 | fare_sort | 否 |  |  |
| 4 | unen_stock_type | 否 |  |  |
| 5 | unen_entrust_way | 否 |  |  |
| 6 | consultative_flag | 否 |  |  |
| 7 | begin_date | 否 |  |  |
| 8 | end_date | 否 |  |  |
| 9 | valid_date | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | fund_account | 否 |  |  |
| 12 | money_type | 否 |  |  |
| 13 | fare_sort | 否 |  |  |
| 14 | unen_stock_type | 否 |  |  |
| 15 | unen_entrust_way | 否 |  |  |
| 16 | consultative_flag | 否 |  |  |
| 17 | begin_date | 否 |  |  |
| 18 | end_date | 否 |  |  |
| 19 | valid_date | 否 |  |  |
| 20 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_farefundacct | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_usps_farefundacct | ART | 是 | fund_account, money_type, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_farefundacct | fund_account, money_type, fund_account, money_type |
| idx_usps_farefundacct | fund_account, money_type, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

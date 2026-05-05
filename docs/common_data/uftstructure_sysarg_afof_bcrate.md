# afof_bcrate - 基金盘后业务分成费用表

**表对象ID**: 119
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | business_flag | 否 |  |  |
| 5 | money_type | 否 |  |  |
| 6 | rate | 否 |  |  |
| 7 | return_rate | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | position_str | 否 |  | exchange_type(4)+stock_code(8)+branch_no(6)+business_flag(10 |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | branch_no | 否 |  |  |
| 15 | business_flag | 否 |  |  |
| 16 | money_type | 否 |  |  |
| 17 | rate | 否 |  |  |
| 18 | return_rate | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | position_str | 否 |  | exchange_type(4)+stock_code(8)+branch_no(6)+business_flag(10 |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_afof_bcrate | 默认 | 否 |  |
| idx_afof_bcrate | ART | 是 | exchange_type, stock_code, branch_no, business_flag, money_type, exchange_type, stock_code, branch_no, business_flag, money_type |
| idx_afof_bcrate | 默认 | 否 |  |
| idx_afof_bcrate | ART | 是 | exchange_type, stock_code, branch_no, business_flag, money_type, exchange_type, stock_code, branch_no, business_flag, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_afof_bcrate | exchange_type, stock_code, branch_no, business_flag, money_type, exchange_type, stock_code, branch_no, business_flag, money_type |
| idx_afof_bcrate | exchange_type, stock_code, branch_no, business_flag, money_type, exchange_type, stock_code, branch_no, business_flag, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:34:15 | 3.0.2.103 | taocong45644 | 当前表afof_bcrate，修改了索引idx_afof_bcrate,索引字段修改为：(exchange_type,s... |
| 2025-02-14 16:37:11 | 3.0.6.38 | 李想 | 新增表 |
| 2025-12-01 14:34:15 | 3.0.2.103 | taocong45644 | 当前表afof_bcrate，修改了索引idx_afof_bcrate,索引字段修改为：(exchange_type,s... |
| 2025-02-14 16:37:11 | 3.0.6.38 | 李想 | 新增表 |

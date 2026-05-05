# crdt_ratio_loginfo - 融资融券保证金比例变化日志表

**表对象ID**: 7100
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | registration_flag | 否 |  |  |
| 7 | underly_package_kind | 否 |  |  |
| 8 | crdt_type | 否 |  |  |
| 9 | crdt_level | 否 |  |  |
| 10 | organ_flag | 否 |  |  |
| 11 | init_date | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | registration_flag | 否 |  |  |
| 17 | underly_package_kind | 否 |  |  |
| 18 | crdt_type | 否 |  |  |
| 19 | crdt_level | 否 |  |  |
| 20 | organ_flag | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_ratio_loginfo | ART | 是 | init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag, underly_package_kind, crdt_type, crdt_level, organ_flag, init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag, underly_package_kind, crdt_type, crdt_level, organ_flag |
| uk_rpt_crdtratiologinfo | ART | 是 | init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag, init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag |
| idx_crdt_ratio_loginfo | ART | 是 | init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag, underly_package_kind, crdt_type, crdt_level, organ_flag, init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag, underly_package_kind, crdt_type, crdt_level, organ_flag |
| uk_rpt_crdtratiologinfo | ART | 是 | init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag, init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_ratio_loginfo | init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag, underly_package_kind, crdt_type, crdt_level, organ_flag, init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag, underly_package_kind, crdt_type, crdt_level, organ_flag |
| idx_crdt_ratio_loginfo | init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag, underly_package_kind, crdt_type, crdt_level, organ_flag, init_date, fund_account, exchange_type, stock_code, stock_type, registration_flag, underly_package_kind, crdt_type, crdt_level, organ_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-18 13:58:18 | 3.0.6.86 | 李想 | 新增表 |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-18 13:58:18 | 3.0.6.86 | 李想 | 新增表 |

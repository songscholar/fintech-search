# ucrt_risk_params - 特定证券风控参数表

**表对象ID**: 7126
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | crdtriskparam_no | 否 |  |  |
| 4 | crdtrisk_type | 否 |  |  |
| 5 | crdtriskparam_value | 否 |  |  |
| 6 | crdtrisk_color | 否 |  |  |
| 7 | crdtrisk_status | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | index_kind | 否 |  |  |
| 11 | component_flag | 否 |  |  |
| 12 | stock_type | 否 |  |  |
| 13 | registration_flag | 否 |  |  |
| 14 | end_date | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | crdtriskparam_no | 否 |  |  |
| 18 | crdtrisk_type | 否 |  |  |
| 19 | crdtriskparam_value | 否 |  |  |
| 20 | crdtrisk_color | 否 |  |  |
| 21 | crdtrisk_status | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | fund_account | 否 |  |  |
| 24 | index_kind | 否 |  |  |
| 25 | component_flag | 否 |  |  |
| 26 | stock_type | 否 |  |  |
| 27 | registration_flag | 否 |  |  |
| 28 | end_date | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crtriskparams | ART | 是 | exchange_type, stock_code, crdtriskparam_no, crdtrisk_type, fund_account, index_kind, component_flag, stock_type, registration_flag, exchange_type, stock_code, crdtriskparam_no, crdtrisk_type, fund_account, index_kind, component_flag, stock_type, registration_flag |
| idx_crtriskparams | ART | 是 | exchange_type, stock_code, crdtriskparam_no, crdtrisk_type, fund_account, index_kind, component_flag, stock_type, registration_flag, exchange_type, stock_code, crdtriskparam_no, crdtrisk_type, fund_account, index_kind, component_flag, stock_type, registration_flag |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_crtriskparams | exchange_type, stock_code, crdtriskparam_no, crdtrisk_type, fund_account, index_kind, component_flag, stock_type, registration_flag, exchange_type, stock_code, crdtriskparam_no, crdtrisk_type, fund_account, index_kind, component_flag, stock_type, registration_flag |
| idx_crtriskparams | exchange_type, stock_code, crdtriskparam_no, crdtrisk_type, fund_account, index_kind, component_flag, stock_type, registration_flag, exchange_type, stock_code, crdtriskparam_no, crdtrisk_type, fund_account, index_kind, component_flag, stock_type, registration_flag |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-11 14:53:54 | 3.0.6.1067 | 冯元栋 | 新建表 |
| 2025-10-11 14:53:54 | 3.0.6.1067 | 冯元栋 | 新建表 |

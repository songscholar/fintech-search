# ucrt_risk_parameter - 风险监控参数表

**表对象ID**: 7030
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | crdtrisk_no | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | crdtrisk_value | 否 |  |  |
| 5 | crdtrisk_status | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | crdtrisk_no | 否 |  |  |
| 8 | stock_code | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | crdtrisk_value | 否 |  |  |
| 11 | crdtrisk_status | 否 |  |  |
| 12 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_risk_parameter | ART | 是 | crdtrisk_no, stock_code, exchange_type, crdtrisk_no, stock_code, exchange_type |
| idx_ucrt_risk_parameter | ART | 是 | crdtrisk_no, stock_code, exchange_type, crdtrisk_no, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_risk_parameter | crdtrisk_no, stock_code, exchange_type, crdtrisk_no, stock_code, exchange_type |
| idx_ucrt_risk_parameter | crdtrisk_no, stock_code, exchange_type, crdtrisk_no, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

# underly_package - 融资融券标的套餐参数表

**表对象ID**: 7052
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | underly_package_kind | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | fin_ratio | 否 |  |  |
| 6 | slo_ratio | 否 |  |  |
| 7 | float_flag | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | position_str | 否 |  | underly_package_kind(10)+stock_code(8)+exchange_type(4)+stoc |
| 13 | underly_package_kind | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_code | 否 |  |  |
| 16 | stock_type | 否 |  |  |
| 17 | fin_ratio | 否 |  |  |
| 18 | slo_ratio | 否 |  |  |
| 19 | float_flag | 否 |  |  |
| 20 | transaction_no | 否 |  |  |
| 21 | remark | 否 |  |  |
| 22 | update_date | 否 |  |  |
| 23 | update_time | 否 |  |  |
| 24 | position_str | 否 |  | underly_package_kind(10)+stock_code(8)+exchange_type(4)+stoc |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_underly_package | ART | 是 | underly_package_kind, stock_code, exchange_type, stock_type, underly_package_kind, stock_code, exchange_type, stock_type |
| idx_underly_package | ART | 是 | underly_package_kind, stock_code, exchange_type, stock_type, underly_package_kind, stock_code, exchange_type, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_underly_package | underly_package_kind, stock_code, exchange_type, stock_type, underly_package_kind, stock_code, exchange_type, stock_type |
| idx_underly_package | underly_package_kind, stock_code, exchange_type, stock_type, underly_package_kind, stock_code, exchange_type, stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 13:53:24 | 3.0.6.84 | 李想 | 物理表underly_package，添加了表字段(remark);
物理表underly_package，添加了表字... |
| 2024-12-24 11:12:24 | 3.0.6.23 | 沈勋 | 新增表 |
| 2025-02-18 13:53:24 | 3.0.6.84 | 李想 | 物理表underly_package，添加了表字段(remark);
物理表underly_package，添加了表字... |
| 2024-12-24 11:12:24 | 3.0.6.23 | 沈勋 | 新增表 |

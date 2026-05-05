# assure_package - 融资融券担保套餐参数表

**表对象ID**: 7051
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | assure_package_kind | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | stock_type | 否 |  |  |
| 5 | assure_ratio | 否 |  |  |
| 6 | float_flag | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | update_date | 否 |  |  |
| 10 | update_time | 否 |  |  |
| 11 | position_str | 否 |  | assure_package_kind(10)+stock_code(8)+exchange_type(4)+stock |
| 12 | assure_package_kind | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | stock_code | 否 |  |  |
| 15 | stock_type | 否 |  |  |
| 16 | assure_ratio | 否 |  |  |
| 17 | float_flag | 否 |  |  |
| 18 | transaction_no | 否 |  |  |
| 19 | remark | 否 |  |  |
| 20 | update_date | 否 |  |  |
| 21 | update_time | 否 |  |  |
| 22 | position_str | 否 |  | assure_package_kind(10)+stock_code(8)+exchange_type(4)+stock |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assure_package | ART | 是 | assure_package_kind, stock_code, exchange_type, stock_type, assure_package_kind, stock_code, exchange_type, stock_type |
| idx_assure_package | ART | 是 | assure_package_kind, stock_code, exchange_type, stock_type, assure_package_kind, stock_code, exchange_type, stock_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_assure_package | assure_package_kind, stock_code, exchange_type, stock_type, assure_package_kind, stock_code, exchange_type, stock_type |
| idx_assure_package | assure_package_kind, stock_code, exchange_type, stock_type, assure_package_kind, stock_code, exchange_type, stock_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-24 15:12:27 | 3.0.6.54 | 袁文龙 | 对象号7053修改为7051 |
| 2025-02-18 13:50:37 | 3.0.6.83 | 李想 | 物理表assure_package，添加了表字段(remark);
物理表assure_package，添加了表字段(... |
| 2024-12-24 11:12:10 | 3.0.6.23 | 沈勋 | 新增表 |
| 2025-04-24 15:12:27 | 3.0.6.54 | 袁文龙 | 对象号7053修改为7051 |
| 2025-02-18 13:50:37 | 3.0.6.83 | 李想 | 物理表assure_package，添加了表字段(remark);
物理表assure_package，添加了表字段(... |
| 2024-12-24 11:12:10 | 3.0.6.23 | 沈勋 | 新增表 |

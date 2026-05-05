# ucrt_ploy_template - 平仓策略模板表

**表对象ID**: 7019
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | payoffploy_no | 否 |  |  |
| 2 | poptarget_value | 否 |  |  |
| 3 | payoffploy_type | 否 |  |  |
| 4 | popdebit_order | 否 |  |  |
| 5 | fin_popover_rate | 否 |  |  |
| 6 | slo_popfund_flag | 否 |  |  |
| 7 | overdue_days | 否 |  |  |
| 8 | is_stib_priority | 否 |  |  |
| 9 | poly_default | 否 |  |  |
| 10 | popassure_rule | 否 |  |  |
| 11 | popassure_order | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | payoffploy_name | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | payoffploy_no | 否 |  |  |
| 17 | poptarget_value | 否 |  |  |
| 18 | payoffploy_type | 否 |  |  |
| 19 | popdebit_order | 否 |  |  |
| 20 | fin_popover_rate | 否 |  |  |
| 21 | slo_popfund_flag | 否 |  |  |
| 22 | overdue_days | 否 |  |  |
| 23 | is_stib_priority | 否 |  |  |
| 24 | poly_default | 否 |  |  |
| 25 | popassure_rule | 否 |  |  |
| 26 | popassure_order | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | payoffploy_name | 否 |  |  |
| 29 | update_date | 否 |  |  |
| 30 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_ploy_template | ART | 是 | payoffploy_no, payoffploy_no |
| idx_ucrt_ploy_template | ART | 是 | payoffploy_no, payoffploy_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_ploy_template | payoffploy_no, payoffploy_no |
| idx_ucrt_ploy_template | payoffploy_no, payoffploy_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-29 22:45:26 | 3.0.6.108 | 李奕轩 | 物理表ucrt_ploy_template，添加了表字段(payoffploy_name);
物理表ucrt_ploy... |
| 2024-12-19 10:47:35 | 3.0.6.27 | 刘景锋 | poptarget_value数据类型由HsAmount(19,2)调整为HsProportion(21,4) |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-04-29 22:45:26 | 3.0.6.108 | 李奕轩 | 物理表ucrt_ploy_template，添加了表字段(payoffploy_name);
物理表ucrt_ploy... |
| 2024-12-19 10:47:35 | 3.0.6.27 | 刘景锋 | poptarget_value数据类型由HsAmount(19,2)调整为HsProportion(21,4) |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

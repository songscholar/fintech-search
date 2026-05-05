# assunderly_arg - 担保标的一站式参数表

**表对象ID**: 7091
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | assunderlyarg_type | 否 |  |  |
| 2 | curr_sys_status | 否 |  |  |
| 3 | std_status | 否 |  |  |
| 4 | com_status | 否 |  |  |
| 5 | pre_status | 否 |  |  |
| 6 | en_per_crdtinfo_type | 否 |  |  |
| 7 | order_no | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | assunderlyarg_type | 否 |  |  |
| 13 | curr_sys_status | 否 |  |  |
| 14 | std_status | 否 |  |  |
| 15 | com_status | 否 |  |  |
| 16 | pre_status | 否 |  |  |
| 17 | en_per_crdtinfo_type | 否 |  |  |
| 18 | order_no | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | position_str | 否 |  |  |
| 22 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assunderly_arg | ART | 是 | order_no, order_no |
| idx_assunderly_arg | ART | 是 | order_no, order_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_assunderly_arg | order_no, order_no |
| idx_assunderly_arg | order_no, order_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-04 15:04:49 | V3.0.6.1069 | 童程凯 | 所有表assunderly_arg，添加了表字段(position_str);
所有表assunderly_arg，添... |
| 2025-02-17 21:32:08 | 3.0.6.61 | 李想 | 新增表 |
| 2025-12-04 15:04:49 | V3.0.6.1069 | 童程凯 | 所有表assunderly_arg，添加了表字段(position_str);
所有表assunderly_arg，添... |
| 2025-02-17 21:32:08 | 3.0.6.61 | 李想 | 新增表 |

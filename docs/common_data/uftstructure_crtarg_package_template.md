# package_template - 融资融券套餐参数模板表2

**表对象ID**: 7099
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | package_no | 否 |  |  |
| 2 | package_name_t | 否 |  |  |
| 3 | package_kind_str | 否 |  |  |
| 4 | max_debit_balance | 否 |  |  |
| 5 | min_debit_balance | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | package_no | 否 |  |  |
| 10 | package_name_t | 否 |  |  |
| 11 | package_kind_str | 否 |  |  |
| 12 | max_debit_balance | 否 |  |  |
| 13 | min_debit_balance | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_package_template | ART | 是 | package_no, package_no |
| idx_package_templet_up | ART | 是 | min_debit_balance, min_debit_balance |
| idx_package_template | ART | 是 | package_no, package_no |
| idx_package_templet_up | ART | 是 | min_debit_balance, min_debit_balance |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_package_template | package_no, package_no |
| idx_package_template | package_no, package_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-16 14:02:13 | 3.0.6.1066 | 周兆军 | 新增索引idx_package_templet_up |
| 2025-02-18 13:56:10 | 3.0.6.85 | 李想 | 新增表 |
| 2025-09-16 14:02:13 | 3.0.6.1066 | 周兆军 | 新增索引idx_package_templet_up |
| 2025-02-18 13:56:10 | 3.0.6.85 | 李想 | 新增表 |

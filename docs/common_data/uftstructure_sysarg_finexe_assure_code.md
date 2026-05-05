# finexe_assure_code - 融资行权担保标的表

**表对象ID**: 318
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | assure_ratio | 否 |  |  |
| 6 | lift_limit_ratio | 否 |  |  |
| 7 | execv_assure_ratio | 否 |  |  |
| 8 | assure_price | 否 |  |  |
| 9 | capital_amount | 否 |  |  |
| 10 | assure_capital_ratio | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | fair_price | 否 |  |  |
| 13 | fair_price_flag | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | stock_code(8)+exchange_type(4)+company_no(4) |
| 17 | company_no | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | stock_code | 否 |  |  |
| 21 | assure_ratio | 否 |  |  |
| 22 | lift_limit_ratio | 否 |  |  |
| 23 | execv_assure_ratio | 否 |  |  |
| 24 | assure_price | 否 |  |  |
| 25 | capital_amount | 否 |  |  |
| 26 | assure_capital_ratio | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | fair_price | 否 |  |  |
| 29 | fair_price_flag | 否 |  |  |
| 30 | update_date | 否 |  |  |
| 31 | update_time | 否 |  |  |
| 32 | position_str | 否 |  | stock_code(8)+exchange_type(4)+company_no(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexe_assure_code | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_finexe_assure_code | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexe_assure_code | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_finexe_assure_code | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-19 19:53:04 | 3.0.6.110 | 李想 | 物理表finexe_assure_code，添加了表字段(update_date);
物理表finexe_assure... |
| 2024-10-22 19:16:58 | 3.0.4.3 | wuxd | 新增表字段fair_price,fair_price_flag |
| 2024-08-09 16:14:42 | 3.0.2.27 | 骆鹏程 | 新增事务号 |
| 2024-08-09 13:16:21 | 3.0.2.26 | 骆鹏程 | 修改对象号为318 |
| 2024-05-29 21:27:13 | 3.0.2.11 | 祝丁恺 | 勾选不回库选项 |
| 2024-04-29 10:39:22 | 3.0.2.7 | 汪林 | 新增融资行权担保标的表 |
| 2025-02-19 19:53:04 | 3.0.6.110 | 李想 | 物理表finexe_assure_code，添加了表字段(update_date);
物理表finexe_assure... |
| 2024-10-22 19:16:58 | 3.0.4.3 | wuxd | 新增表字段fair_price,fair_price_flag |
| 2024-08-09 16:14:42 | 3.0.2.27 | 骆鹏程 | 新增事务号 |
| 2024-08-09 13:16:21 | 3.0.2.26 | 骆鹏程 | 修改对象号为318 |
| 2024-05-29 21:27:13 | 3.0.2.11 | 祝丁恺 | 勾选不回库选项 |
| 2024-04-29 10:39:22 | 3.0.2.7 | 汪林 | 新增融资行权担保标的表 |

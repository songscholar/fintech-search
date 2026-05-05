# settredo_uqms_sopt_reg - 清算重做额度管理自主行权股东名册表

**表对象ID**: 1654
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | sopt_code | 否 |  |  |
| 4 | register_amount | 否 |  |  |
| 5 | confirm_amount | 否 |  |  |
| 6 | used_amount | 否 |  |  |
| 7 | frozen_amount | 否 |  |  |
| 8 | seat_no | 否 |  |  |
| 9 | sum_payable_tax | 否 |  |  |
| 10 | sum_paid_tax | 否 |  |  |
| 11 | use_date | 否 |  |  |
| 12 | sett_dml_type | 否 |  |  |
| 13 | sett_batch_no | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | sopt_code | 否 |  |  |
| 17 | register_amount | 否 |  |  |
| 18 | confirm_amount | 否 |  |  |
| 19 | used_amount | 否 |  |  |
| 20 | frozen_amount | 否 |  |  |
| 21 | seat_no | 否 |  |  |
| 22 | sum_payable_tax | 否 |  |  |
| 23 | sum_paid_tax | 否 |  |  |
| 24 | use_date | 否 |  |  |
| 25 | sett_dml_type | 否 |  |  |
| 26 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_uqms_soptreg | ART | 是 | sett_batch_no, stock_account, sopt_code, exchange_type, sett_batch_no, stock_account, sopt_code, exchange_type |
| idx_settredo_uqms_soptreg | ART | 是 | sett_batch_no, stock_account, sopt_code, exchange_type, sett_batch_no, stock_account, sopt_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_uqms_soptreg | sett_batch_no, stock_account, sopt_code, exchange_type, sett_batch_no, stock_account, sopt_code, exchange_type |
| idx_settredo_uqms_soptreg | sett_batch_no, stock_account, sopt_code, exchange_type, sett_batch_no, stock_account, sopt_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:50:37 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-10-22 11:32:06 | 8.26.2.91 | yangxz | 所有表settredo_uqms_sopt_reg，添加了表字段(use_date);
 |
| 2025-08-04 15:55:24 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2026-03-05 16:50:37 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-10-22 11:32:06 | 8.26.2.91 | yangxz | 所有表settredo_uqms_sopt_reg，添加了表字段(use_date);
 |
| 2025-08-04 15:55:24 | 8.26.2.91 | 马天宇 | 新建表结构 |

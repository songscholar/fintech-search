# ref_risk - 转融通风险监控参数表

**表对象ID**: 6016
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | refrisk_no | 否 |  |  |
| 3 | refrisk_type | 否 |  |  |
| 4 | refrisk_value | 否 |  |  |
| 5 | refrisk_color | 否 |  |  |
| 6 | refrisk_status | 否 |  |  |
| 7 | remark | 否 |  |  |
| 8 | csfc_borrow_accttype | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | stock_code | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | company_no | 否 |  |  |
| 15 | refrisk_no | 否 |  |  |
| 16 | refrisk_type | 否 |  |  |
| 17 | refrisk_value | 否 |  |  |
| 18 | refrisk_color | 否 |  |  |
| 19 | refrisk_status | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | csfc_borrow_accttype | 否 |  |  |
| 22 | exchange_type | 否 |  |  |
| 23 | stock_code | 否 |  |  |
| 24 | transaction_no | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_risk | ART | 是 | refrisk_no, refrisk_type, company_no, csfc_borrow_accttype, stock_code, exchange_type, refrisk_no, refrisk_type, company_no, csfc_borrow_accttype, stock_code, exchange_type |
| idx_ref_risk_com | ART | 是 | company_no, company_no |
| idx_ref_risk | ART | 是 | refrisk_no, refrisk_type, company_no, csfc_borrow_accttype, stock_code, exchange_type, refrisk_no, refrisk_type, company_no, csfc_borrow_accttype, stock_code, exchange_type |
| idx_ref_risk_com | ART | 是 | company_no, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_risk | refrisk_no, refrisk_type, company_no, csfc_borrow_accttype, stock_code, exchange_type, refrisk_no, refrisk_type, company_no, csfc_borrow_accttype, stock_code, exchange_type |
| idx_ref_risk | refrisk_no, refrisk_type, company_no, csfc_borrow_accttype, stock_code, exchange_type, refrisk_no, refrisk_type, company_no, csfc_borrow_accttype, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-06-16 16:13:08 | 1.0.0.14 | 李奕轩 | 物理表ref_risk，添加了表字段(transaction_no);
物理表ref_risk，添加了表字段(upda... |
| 2025-02-21 11:43:57 | 1.0.0.12 | 李想 | 新增表 |
| 2025-06-16 16:13:08 | 1.0.0.14 | 李奕轩 | 物理表ref_risk，添加了表字段(transaction_no);
物理表ref_risk，添加了表字段(upda... |
| 2025-02-21 11:43:57 | 1.0.0.12 | 李想 | 新增表 |

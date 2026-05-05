# optmarginacctinfo - 衍生品保证金账户信息导出表

**表对象ID**: 3201
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | optmargin_account | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | seat_no | 是 |  |  |
| 6 | e_mail_str | 是 |  |  |
| 7 | mobile_tel_str | 是 |  |  |
| 8 | en_clear_no | 是 |  |  |
| 9 | company_no | 是 |  |  |
| 10 | exchange_type | 是 |  |  |
| 11 | optmargin_account | 是 |  |  |
| 12 | branch_no | 是 |  |  |
| 13 | seat_no | 是 |  |  |
| 14 | e_mail_str | 是 |  |  |
| 15 | mobile_tel_str | 是 |  |  |
| 16 | en_clear_no | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optmarginacctinfo | 默认 | 是 | exchange_type, company_no, exchange_type, company_no |
| idx_optmarginacctinfo | 默认 | 是 | exchange_type, company_no, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optmarginacctinfo | exchange_type, company_no, exchange_type, company_no |
| idx_optmarginacctinfo | exchange_type, company_no, exchange_type, company_no |

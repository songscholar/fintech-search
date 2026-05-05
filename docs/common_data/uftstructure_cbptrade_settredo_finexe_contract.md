# settredo_finexe_contract - 清算重做融资行权合约表

**表对象ID**: 2647
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | finexe_contract_status | 否 |  |  |
| 2 | sopt_tax | 否 |  |  |
| 3 | self_balance | 否 |  |  |
| 4 | entrust_balance | 否 |  |  |
| 5 | back_balance | 否 |  |  |
| 6 | remark | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | contract_id | 否 |  |  |
| 9 | sett_batch_no | 否 |  |  |
| 10 | finexe_contract_status | 否 |  |  |
| 11 | sopt_tax | 否 |  |  |
| 12 | self_balance | 否 |  |  |
| 13 | entrust_balance | 否 |  |  |
| 14 | back_balance | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | date_clear | 否 |  |  |
| 17 | contract_id | 否 |  |  |
| 18 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_finexe_contract | ART | 是 | sett_batch_no, contract_id, sett_batch_no, contract_id |
| idx_settredo_finexe_contract | ART | 是 | sett_batch_no, contract_id, sett_batch_no, contract_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_finexe_contract | sett_batch_no, contract_id, sett_batch_no, contract_id |
| idx_settredo_finexe_contract | sett_batch_no, contract_id, sett_batch_no, contract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:31:03 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2026-03-04 16:31:03 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-08-06 13:50:34 | 8.26.2.91 | 马天宇 | 新建表结构 |

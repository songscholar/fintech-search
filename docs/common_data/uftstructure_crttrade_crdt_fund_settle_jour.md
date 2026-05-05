# crdt_fund_settle_jour - 融资融券资金交易清算流水表

**表对象ID**: 7582
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | finance_type | 否 |  |  |
| 5 | settle_no | 否 |  |  |
| 6 | remark | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | init_date | 否 |  |  |
| 9 | curr_date | 否 |  |  |
| 10 | curr_time | 否 |  |  |
| 11 | finance_type | 否 |  |  |
| 12 | settle_no | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | fund_account | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uqms_fund_settle_jour | ART | 是 | settle_no, finance_type, init_date, settle_no, finance_type, init_date |
| idx_uqms_fund_settle_jour | ART | 是 | settle_no, finance_type, init_date, settle_no, finance_type, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_fund_settle_jour | settle_no, finance_type, init_date, settle_no, finance_type, init_date |
| idx_uqms_fund_settle_jour | settle_no, finance_type, init_date, settle_no, finance_type, init_date |

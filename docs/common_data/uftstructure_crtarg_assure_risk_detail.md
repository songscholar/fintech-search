# assure_risk_detail - 维持担保比例控制明细表

**表对象ID**: 7119
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | create_date | 否 |  |  |
| 2 | company_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | assurescale_in | 否 |  |  |
| 5 | assurescale_out | 否 |  |  |
| 6 | risk_restriction | 否 |  |  |
| 7 | date_clear | 否 |  |  |
| 8 | create_date | 否 |  |  |
| 9 | company_no | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | assurescale_in | 否 |  |  |
| 12 | assurescale_out | 否 |  |  |
| 13 | risk_restriction | 否 |  |  |
| 14 | date_clear | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assureriskdetail | ART | 是 | company_no, fund_account, assurescale_in, assurescale_out, company_no, fund_account, assurescale_in, assurescale_out |
| idx_assureriskdetail | ART | 是 | company_no, fund_account, assurescale_in, assurescale_out, company_no, fund_account, assurescale_in, assurescale_out |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_assureriskdetail | company_no, fund_account, assurescale_in, assurescale_out, company_no, fund_account, assurescale_in, assurescale_out |
| idx_assureriskdetail | company_no, fund_account, assurescale_in, assurescale_out, company_no, fund_account, assurescale_in, assurescale_out |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-23 16:58:36 | 3.0.6.107 | 常行 | 新增表 |
| 2025-04-23 16:58:36 | 3.0.6.107 | 常行 | 新增表 |

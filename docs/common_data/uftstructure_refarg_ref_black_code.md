# ref_black_code - 转融通标的黑名单表

**表对象ID**: 6010
**所属模块**: refarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | ref_bs | 否 |  |  |
| 3 | ref_term | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | create_date | 否 |  |  |
| 7 | remark | 否 |  |  |
| 8 | en_refbusi_code | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | position_str | 否 |  | ref_bs(1)+stock_code(8)+exchange_type(4)+ref_term(5)+company |
| 14 | company_no | 否 |  |  |
| 15 | ref_bs | 否 |  |  |
| 16 | ref_term | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | create_date | 否 |  |  |
| 20 | remark | 否 |  |  |
| 21 | en_refbusi_code | 否 |  |  |
| 22 | fund_account | 否 |  |  |
| 23 | update_date | 否 |  |  |
| 24 | update_time | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | position_str | 否 |  | ref_bs(1)+stock_code(8)+exchange_type(4)+ref_term(5)+company |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ref_black_code | ART | 是 | ref_bs, stock_code, exchange_type, ref_term, company_no, fund_account, ref_bs, stock_code, exchange_type, ref_term, company_no, fund_account |
| idx_ref_black_code | ART | 是 | ref_bs, stock_code, exchange_type, ref_term, company_no, fund_account, ref_bs, stock_code, exchange_type, ref_term, company_no, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ref_black_code | ref_bs, stock_code, exchange_type, ref_term, company_no, fund_account, ref_bs, stock_code, exchange_type, ref_term, company_no, fund_account |
| idx_ref_black_code | ref_bs, stock_code, exchange_type, ref_term, company_no, fund_account, ref_bs, stock_code, exchange_type, ref_term, company_no, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-21 11:07:32 | 1.0.0.9 | 李想 | 新增表 |
| 2025-02-21 11:07:32 | 1.0.0.9 | 李想 | 新增表 |

# ucrt_fundacct_stkrestrict - 融资融券资产账户证券限制表

**表对象ID**: 7007
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | res_exchange_type | 否 |  |  |
| 4 | res_stock_type | 否 |  |  |
| 5 | res_sub_stock_type | 否 |  |  |
| 6 | res_stock_code | 否 |  |  |
| 7 | res_entrust_bs | 否 |  |  |
| 8 | res_entrust_way | 否 |  |  |
| 9 | res_entrust_type | 否 |  |  |
| 10 | res_entrust_prop | 否 |  |  |
| 11 | begin_date | 否 |  |  |
| 12 | end_date | 否 |  |  |
| 13 | ordinal | 否 |  |  |
| 14 | anti_flag | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | transaction_no | 否 |  |  |
| 17 | client_id | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | res_exchange_type | 否 |  |  |
| 20 | res_stock_type | 否 |  |  |
| 21 | res_sub_stock_type | 否 |  |  |
| 22 | res_stock_code | 否 |  |  |
| 23 | res_entrust_bs | 否 |  |  |
| 24 | res_entrust_way | 否 |  |  |
| 25 | res_entrust_type | 否 |  |  |
| 26 | res_entrust_prop | 否 |  |  |
| 27 | begin_date | 否 |  |  |
| 28 | end_date | 否 |  |  |
| 29 | ordinal | 否 |  |  |
| 30 | anti_flag | 否 |  |  |
| 31 | stock_account | 否 |  |  |
| 32 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_fundacct_stkrestrict | ART | 是 | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |
| idx_ucrt_fundacct_stkrestrict | ART | 是 | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_fundacct_stkrestrict | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |
| idx_ucrt_fundacct_stkrestrict | fund_account, stock_account, ordinal, fund_account, stock_account, ordinal |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

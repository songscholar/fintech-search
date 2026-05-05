# ucrt_cpy_stock_info - 融资融券公司单只证券信息

**表对象ID**: 7551
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | fin_total_balance | 否 |  |  |
| 5 | slo_sell_balance | 否 |  |  |
| 6 | total_hold_amount | 否 |  |  |
| 7 | assure_return_amount | 否 |  |  |
| 8 | assure_submit_amount | 否 |  |  |
| 9 | crdt_buy_uncome_amount | 否 |  |  |
| 10 | fin_uncome_amount | 否 |  |  |
| 11 | company_no | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | exchange_type | 否 |  |  |
| 14 | fin_total_balance | 否 |  |  |
| 15 | slo_sell_balance | 否 |  |  |
| 16 | total_hold_amount | 否 |  |  |
| 17 | assure_return_amount | 否 |  |  |
| 18 | assure_submit_amount | 否 |  |  |
| 19 | crdt_buy_uncome_amount | 否 |  |  |
| 20 | fin_uncome_amount | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_cpy_stock_info | ART | 是 | company_no, stock_code, exchange_type, company_no, stock_code, exchange_type |
| idx_ucrt_cpy_stock_info | ART | 是 | company_no, stock_code, exchange_type, company_no, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_cpy_stock_info | company_no, stock_code, exchange_type, company_no, stock_code, exchange_type |
| idx_ucrt_cpy_stock_info | company_no, stock_code, exchange_type, company_no, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-12 12:28 | 0.3.3.130 | 雷玄 | 新增表结构 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-12 12:28 | 0.3.3.130 | 雷玄 | 新增表结构 |

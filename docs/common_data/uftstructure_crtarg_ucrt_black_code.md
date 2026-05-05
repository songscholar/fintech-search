# ucrt_black_code - 融资融券代码黑名单

**表对象ID**: 7016
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | create_date | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | remark | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | position_str | 否 |  | stock_code(8)+exchange_type(4)+company_no(4) |
| 10 | company_no | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | stock_code | 否 |  |  |
| 13 | create_date | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | stock_code(8)+exchange_type(4)+company_no(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_black_code | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_ucrt_black_code | ART | 是 | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_black_code | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |
| idx_ucrt_black_code | stock_code, exchange_type, company_no, stock_code, exchange_type, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-18 10:00:12 | 3.0.6.67 | 李想 | 物理表ucrt_black_code，添加了表字段(remark);
物理表ucrt_black_code，添加了表字... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-02-18 10:00:12 | 3.0.6.67 | 李想 | 物理表ucrt_black_code，添加了表字段(remark);
物理表ucrt_black_code，添加了表字... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

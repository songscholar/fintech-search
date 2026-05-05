# ucrt_crdt_limit_sell - 融资融券限售股份控制表

**表对象ID**: 7503
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | limitsell_type | 否 |  |  |
| 7 | limitsell_flag | 否 |  |  |
| 8 | limitsell_source | 否 |  |  |
| 9 | lift_date | 否 |  |  |
| 10 | acode_account | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | client_id | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | limitsell_type | 否 |  |  |
| 18 | limitsell_flag | 否 |  |  |
| 19 | limitsell_source | 否 |  |  |
| 20 | lift_date | 否 |  |  |
| 21 | acode_account | 否 |  |  |
| 22 | remark | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_crdt_limit_sell_uk | ART | 是 | client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source, client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source |
| idx_ucrt_crdt_limit_sell_code | ART | 是 | acode_account, exchange_type, stock_code, acode_account, exchange_type, stock_code |
| idx_ucrt_crdt_limit_sell_uk | ART | 是 | client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source, client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source |
| idx_ucrt_crdt_limit_sell_code | ART | 是 | acode_account, exchange_type, stock_code, acode_account, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_crdt_limit_sell_uk | client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source, client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source |
| idx_ucrt_crdt_limit_sell_uk | client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source, client_id, stock_code, exchange_type, limitsell_type, stock_account, limitsell_source |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-11-11 16:33:22 | 3.0.6.16 | 沈勋 | 物理表ucrt_crdt_limit_sell，添加了表字段(remark);
 |
| 2024-11-01 13:14:59 | 3.0.6.12 | 董瑞辉 | 修改内存索引 |
| 2023-11-08 14:39:48 | V3.0.1.14 | 吴威 | 物理表ucrt_crdt_limit_sell，添加了表字段(acode_account);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2024-11-11 16:33:22 | 3.0.6.16 | 沈勋 | 物理表ucrt_crdt_limit_sell，添加了表字段(remark);
 |
| 2024-11-01 13:14:59 | 3.0.6.12 | 董瑞辉 | 修改内存索引 |
| 2023-11-08 14:39:48 | V3.0.1.14 | 吴威 | 物理表ucrt_crdt_limit_sell，添加了表字段(acode_account);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

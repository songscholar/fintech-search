# etb_bond_price - 互联互通债券行情表

**表对象ID**: 131
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code_long | 否 |  |  |
| 3 | init_date | 否 |  |  |
| 4 | closing_price | 否 |  |  |
| 5 | spot_full_price | 否 |  |  |
| 6 | stock_interest | 否 |  |  |
| 7 | money_type | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | position_str | 否 |  | stock_code_long(32)+exchange_type(4)+init_date(8) |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code_long | 否 |  |  |
| 14 | init_date | 否 |  |  |
| 15 | closing_price | 否 |  |  |
| 16 | spot_full_price | 否 |  |  |
| 17 | stock_interest | 否 |  |  |
| 18 | money_type | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | position_str | 否 |  | stock_code_long(32)+exchange_type(4)+init_date(8) |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etb_bond_price | 默认 | 否 |  |
| idx_etb_bond_price | ART | 是 | stock_code_long, exchange_type, init_date, stock_code_long, exchange_type, init_date |
| uk_rpt_etbbondprice | ART | 是 | init_date, stock_code_long, exchange_type, init_date, stock_code_long, exchange_type |
| idx_etb_bond_price | 默认 | 否 |  |
| idx_etb_bond_price | ART | 是 | stock_code_long, exchange_type, init_date, stock_code_long, exchange_type, init_date |
| uk_rpt_etbbondprice | ART | 是 | init_date, stock_code_long, exchange_type, init_date, stock_code_long, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etb_bond_price | stock_code_long, exchange_type, init_date, stock_code_long, exchange_type, init_date |
| idx_etb_bond_price | stock_code_long, exchange_type, init_date, stock_code_long, exchange_type, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 14:39:52 | 3.0.2.103 | taocong45644 | 当前表etb_bond_price，修改了索引idx_etb_bond_price,索引字段修改为：(stock_cod... |
| 2025-02-18 17:40:38 | 3.0.6.75 | 李想 | 新增表 |
| 2025-12-09 09:35:46 | V3.0.2.2006 | 陆良铠 | 新增历史表的字段和索引 |
| 2025-12-01 14:39:52 | 3.0.2.103 | taocong45644 | 当前表etb_bond_price，修改了索引idx_etb_bond_price,索引字段修改为：(stock_cod... |
| 2025-02-18 17:40:38 | 3.0.6.75 | 李想 | 新增表 |

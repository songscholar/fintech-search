# settredo_ucbp_dividend_tax - 清算重做股息红利差别化扣税信息表

**表对象ID**: 2648
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | date_clear | 否 |  |  |
| 4 | dividendtax_status | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | serial_no | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | dividendtax_status | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredocbp_dividendtax | 默认 | 否 |  |
| idx_settredocbp_dividendtax | ART | 是 | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |
| idx_settredocbp_dividendtax | 默认 | 否 |  |
| idx_settredocbp_dividendtax | ART | 是 | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredocbp_dividendtax | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |
| idx_settredocbp_dividendtax | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:31:51 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:50:58 | 3.0.2.75 | taocong45644 | 当前表settredo_ucbp_dividend_tax，修改了索引idx_settredocbp_dividendt... |
| 2025-02-20 10:57:43 | 3.0.2.2001 | 高志强 | 新增表结构 |
| 2026-03-04 16:31:51 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:50:58 | 3.0.2.75 | taocong45644 | 当前表settredo_ucbp_dividend_tax，修改了索引idx_settredocbp_dividendt... |
| 2025-02-20 10:57:43 | 3.0.2.2001 | 高志强 | 新增表结构 |

# settredo_usms_dividend_tax - 清算重做股息红利差别化扣税信息表(交易管理)

**表对象ID**: 2857
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

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

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredosms_dividendtax | 默认 | 是 | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |
| idx_settredosms_dividendtax | 默认 | 是 | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredosms_dividendtax | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |
| idx_settredosms_dividendtax | sett_batch_no, init_date, serial_no, sett_batch_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-20 10:57:43 | 3.0.2.2001 | yangxz | 新增表结构 |
| 2025-02-20 10:57:43 | 3.0.2.2001 | yangxz | 新增表结构 |

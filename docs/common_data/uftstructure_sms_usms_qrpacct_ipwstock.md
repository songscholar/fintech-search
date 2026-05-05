# usms_qrpacct_ipwstock - 报价回购未开户质押国债表

**表对象ID**: 2815
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | store_amount | 否 |  |  |
| 5 | tohis_date | 否 | H |  |
| 6 | stock_name | 否 | H |  |
| 7 | stock_type | 否 | H |  |
| 8 | sub_stock_type | 否 | H |  |
| 9 | stock_account | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | store_amount | 否 |  |  |
| 13 | tohis_date | 否 | H |  |
| 14 | stock_name | 否 | H |  |
| 15 | stock_type | 否 | H |  |
| 16 | sub_stock_type | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrpacct_ipwstock | 默认 | 是 | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |
| idx_rpt_qrpacct_ipwstock | ART | 是 | stock_account, exchange_type, stock_code, tohis_date, stock_account, exchange_type, stock_code, tohis_date |
| idx_qrpacct_ipwstock | 默认 | 是 | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |
| idx_rpt_qrpacct_ipwstock | ART | 是 | stock_account, exchange_type, stock_code, tohis_date, stock_account, exchange_type, stock_code, tohis_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrpacct_ipwstock | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |
| idx_qrpacct_ipwstock | stock_account, exchange_type, stock_code, stock_account, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-08 12:20:21 | 3.0.2.4 | 洪略 | 历史表索引增加rtp前缀 |
| 2025-11-07 14:32:31 | 3.0.2.4 | 洪略 | 新增历史表 |
| 2025-04-27 15:54:32 | 3.0.6.84 | 吴昊 | 新增表结构 |
| 2025-12-08 12:20:21 | 3.0.2.4 | 洪略 | 历史表索引增加rtp前缀 |
| 2025-11-07 14:32:31 | 3.0.2.4 | 洪略 | 新增历史表 |
| 2025-04-27 15:54:32 | 3.0.6.84 | 吴昊 | 新增表结构 |

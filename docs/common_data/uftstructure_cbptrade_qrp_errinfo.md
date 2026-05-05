# qrp_errinfo - 报价回购超限信息

**表对象ID**: 2338
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | company_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | entrust_type | 否 |  |  |
| 9 | entrust_prop | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | error_info | 否 |  |  |
| 12 | error_pathinfo | 否 |  |  |
| 13 | position_str | 否 |  | init_date(8)+serial_no(10) |
| 14 | init_date | 否 |  |  |
| 15 | serial_no | 否 |  |  |
| 16 | exchange_type | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | company_no | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | stock_account | 否 |  |  |
| 21 | entrust_type | 否 |  |  |
| 22 | entrust_prop | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | error_info | 否 |  |  |
| 25 | error_pathinfo | 否 |  |  |
| 26 | position_str | 否 |  | init_date(8)+serial_no(10) |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_qrp_errinfo | 默认 | 否 |  |
| idx_qrp_errinfo | ART | 是 | serial_no, init_date, serial_no, init_date |
| uk_rpt_qrperrinfo | ART | 是 | init_date, position_str, init_date, position_str |
| idx_qrp_errinfo | 默认 | 否 |  |
| idx_qrp_errinfo | ART | 是 | serial_no, init_date, serial_no, init_date |
| uk_rpt_qrperrinfo | ART | 是 | init_date, position_str, init_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_qrp_errinfo | serial_no, init_date, serial_no, init_date |
| idx_qrp_errinfo | serial_no, init_date, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:30:41 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-08-15 15:31:40 | V3.0.2.1005 | weill | 新增表结构 |
| 2026-03-04 15:30:41 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-03 14:25:07 | 3.0.2.76 | 陆良铠 | 新增历史表的字段和索引 |
| 2024-12-27 14:28:13 | 3.0.2.1 | 李江霖 | 增加position_str的备注 |
| 2024-08-15 15:31:40 | V3.0.2.1005 | weill | 新增表结构 |

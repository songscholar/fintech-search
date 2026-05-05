# real_dsf_business - 实时代收代付确定交收表

**表对象ID**: 2838
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_time | 否 |  |  |
| 3 | order_id | 否 |  |  |
| 4 | clear_serial_no | 否 |  |  |
| 5 | clear_busi_type | 否 |  |  |
| 6 | net_balance | 否 |  |  |
| 7 | fare_sx_src | 否 |  |  |
| 8 | fare_sx_dest | 否 |  |  |
| 9 | szdc_send_date | 否 |  |  |
| 10 | deal_flag | 否 |  |  |
| 11 | init_date | 否 |  |  |
| 12 | curr_time | 否 |  |  |
| 13 | order_id | 否 |  |  |
| 14 | clear_serial_no | 否 |  |  |
| 15 | clear_busi_type | 否 |  |  |
| 16 | net_balance | 否 |  |  |
| 17 | fare_sx_src | 否 |  |  |
| 18 | fare_sx_dest | 否 |  |  |
| 19 | szdc_send_date | 否 |  |  |
| 20 | deal_flag | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_realdsfbusiness | 默认 | 是 | clear_serial_no, clear_serial_no |
| idx_rpt_realdsfbusiness | ART | 是 | init_date, clear_serial_no, init_date, clear_serial_no |
| idx_realdsfbusiness | 默认 | 是 | clear_serial_no, clear_serial_no |
| idx_rpt_realdsfbusiness | ART | 是 | init_date, clear_serial_no, init_date, clear_serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_realdsfbusiness | clear_serial_no, clear_serial_no |
| idx_realdsfbusiness | clear_serial_no, clear_serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-11-06 16:43:51 | V3.0.2.4 | 洪略 | 增加历史表 |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |
| 2025-11-06 16:43:51 | V3.0.2.4 | 洪略 | 增加历史表 |
| 2025-04-14 14:28:21 | V3.0.2.2002 | 蒋浩 |  |

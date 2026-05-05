# usps_seats - 席位参数表

**表对象ID**: 4
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 40 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 是 |  |  |
| 2 | default_mark | 是 |  |  |
| 3 | en_client_group | 是 |  |  |
| 4 | en_stock_type | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | trustee_seat_no | 是 |  |  |
| 7 | ics_etfvoucher_flag | 是 |  |  |
| 8 | seat_no | 是 |  |  |
| 9 | seat_prop | 是 |  |  |
| 10 | seatorgan_flag | 是 |  |  |
| 11 | transaction_no | 是 |  |  |
| 12 | cashreport_flag | 是 |  |  |
| 13 | optreport_flag | 是 |  |  |
| 14 | seats_ctrlstr | 是 |  |  |
| 15 | seatvip_flag | 是 |  |  |
| 16 | remark | 是 |  |  |
| 17 | update_date | 是 |  |  |
| 18 | update_time | 是 |  |  |
| 19 | position_str | 是 |  | exchange_type(4)+seat_no(8)+branch_no(6) |
| 20 | transaction_str | 是 |  |  |
| 21 | branch_no | 是 |  |  |
| 22 | default_mark | 是 |  |  |
| 23 | en_client_group | 是 |  |  |
| 24 | en_stock_type | 是 |  |  |
| 25 | exchange_type | 是 |  |  |
| 26 | trustee_seat_no | 是 |  |  |
| 27 | ics_etfvoucher_flag | 是 |  |  |
| 28 | seat_no | 是 |  |  |
| 29 | seat_prop | 是 |  |  |
| 30 | seatorgan_flag | 是 |  |  |
| 31 | transaction_no | 是 |  |  |
| 32 | cashreport_flag | 是 |  |  |
| 33 | optreport_flag | 是 |  |  |
| 34 | seats_ctrlstr | 是 |  |  |
| 35 | seatvip_flag | 是 |  |  |
| 36 | remark | 是 |  |  |
| 37 | update_date | 是 |  |  |
| 38 | update_time | 是 |  |  |
| 39 | position_str | 是 |  | exchange_type(4)+seat_no(8)+branch_no(6) |
| 40 | transaction_str | 是 |  |  |

## 索引（共 10 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_seats_prop | 默认 | 否 | branch_no, exchange_type, seat_prop, default_mark, branch_no, exchange_type, seat_prop, default_mark |
| idx_upbs_seats | ART | 是 | exchange_type, seat_no, branch_no, exchange_type, seat_no, branch_no |
| idx_upbs_seats_prop | ART | 是 | branch_no, exchange_type, seat_prop, default_mark, branch_no, exchange_type, seat_prop, default_mark |
| idx_upbs_seats_enclientgroup | ART | 是 | exchange_type, branch_no, seat_prop, seatvip_flag, en_stock_type, en_client_group, default_mark, exchange_type, branch_no, seat_prop, seatvip_flag, en_stock_type, en_client_group, default_mark |
| idx_upbs_seats_enstocktype | ART | 是 | exchange_type, branch_no, seat_prop, seatvip_flag, en_stock_type, default_mark, exchange_type, branch_no, seat_prop, seatvip_flag, en_stock_type, default_mark |
| idx_upbs_seats_prop | 默认 | 否 | branch_no, exchange_type, seat_prop, default_mark, branch_no, exchange_type, seat_prop, default_mark |
| idx_upbs_seats | ART | 是 | exchange_type, seat_no, branch_no, exchange_type, seat_no, branch_no |
| idx_upbs_seats_prop | ART | 是 | branch_no, exchange_type, seat_prop, default_mark, branch_no, exchange_type, seat_prop, default_mark |
| idx_upbs_seats_enclientgroup | ART | 是 | exchange_type, branch_no, seat_prop, seatvip_flag, en_stock_type, en_client_group, default_mark, exchange_type, branch_no, seat_prop, seatvip_flag, en_stock_type, en_client_group, default_mark |
| idx_upbs_seats_enstocktype | ART | 是 | exchange_type, branch_no, seat_prop, seatvip_flag, en_stock_type, default_mark, exchange_type, branch_no, seat_prop, seatvip_flag, en_stock_type, default_mark |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_seats | exchange_type, seat_no, branch_no, exchange_type, seat_no, branch_no |
| idx_upbs_seats | exchange_type, seat_no, branch_no, exchange_type, seat_no, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-06-13 14:40:06 | 3.0.6.1001 | 汪迎 | 物理表usps_seats，添加了表字段(transaction_str);
 |
| 2025-07-10 13:47:33 | 3.0.6.21 | 马天宇 | 物理表usps_seats，添加了表字段(seatvip_flag);
物理表usps_seats，添加了表字段(re... |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-05-19 20:05:24 | 3.0.6.139 |  | 物理表usps_seats，增加索引(idx_upbs_seats_prop:[branch_no,exchange_t... |
| 2025-02-19 13:53:50 | 3.0.6.86 | 李想 | 物理表usps_seats，添加了表字段(optreport_flag);
物理表usps_seats，添加了表字段(... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:12 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2025-06-13 14:40:06 | 3.0.6.1001 | 汪迎 | 物理表usps_seats，添加了表字段(transaction_str);
 |
| 2025-07-10 13:47:33 | 3.0.6.21 | 马天宇 | 物理表usps_seats，添加了表字段(seatvip_flag);
物理表usps_seats，添加了表字段(re... |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-05-19 20:05:24 | 3.0.6.139 |  | 物理表usps_seats，增加索引(idx_upbs_seats_prop:[branch_no,exchange_t... |
| 2025-02-19 13:53:50 | 3.0.6.86 | 李想 | 物理表usps_seats，添加了表字段(optreport_flag);
物理表usps_seats，添加了表字段(... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:12 | 0.0.0.9 | 吴威 | 新增transaction_no |

# stb_arg - 三板业务参数表

**表对象ID**: 2320
**所属模块**: cbptrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | en_trans_type | 否 |  |  |
| 4 | open_mode | 否 |  |  |
| 5 | seat_no | 否 |  |  |
| 6 | square_seat | 否 |  |  |
| 7 | start_contract | 否 |  |  |
| 8 | stop_contract | 否 |  |  |
| 9 | organ_id | 否 |  |  |
| 10 | start_time | 否 |  |  |
| 11 | stop_time | 否 |  |  |
| 12 | files | 否 |  |  |
| 13 | trans_opbranch | 否 |  |  |
| 14 | trans_op | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | branch_no | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | en_trans_type | 否 |  |  |
| 21 | open_mode | 否 |  |  |
| 22 | seat_no | 否 |  |  |
| 23 | square_seat | 否 |  |  |
| 24 | start_contract | 否 |  |  |
| 25 | stop_contract | 否 |  |  |
| 26 | organ_id | 否 |  |  |
| 27 | start_time | 否 |  |  |
| 28 | stop_time | 否 |  |  |
| 29 | files | 否 |  |  |
| 30 | trans_opbranch | 否 |  |  |
| 31 | trans_op | 否 |  |  |
| 32 | transaction_no | 否 |  |  |
| 33 | update_date | 否 |  |  |
| 34 | update_time | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stbarg | 默认 | 否 |  |
| idx_stbarg | ART | 是 | branch_no, exchange_type, en_trans_type, open_mode, branch_no, exchange_type, en_trans_type, open_mode |
| idx_stbarg | 默认 | 否 |  |
| idx_stbarg | ART | 是 | branch_no, exchange_type, en_trans_type, open_mode, branch_no, exchange_type, en_trans_type, open_mode |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stbarg | branch_no, exchange_type, en_trans_type, open_mode, branch_no, exchange_type, en_trans_type, open_mode |
| idx_stbarg | branch_no, exchange_type, en_trans_type, open_mode, branch_no, exchange_type, en_trans_type, open_mode |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:22:08 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-03-12 13:12:40 | V3.0.5.1026 | 李想 | 物理表stb_arg，添加了表字段(update_date);
物理表stb_arg，添加了表字段(update_ti... |
| 2024-09-09 11:22:40 | V3.0.2.15 | 杨森峰 | 表属性调整为不回库 |
| 2024-08-02 14:54:14 | V3.0.1.17 | 全春辉 | 新增 |
| 2026-03-04 15:22:08 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-03-12 13:12:40 | V3.0.5.1026 | 李想 | 物理表stb_arg，添加了表字段(update_date);
物理表stb_arg，添加了表字段(update_ti... |
| 2024-09-09 11:22:40 | V3.0.2.15 | 杨森峰 | 表属性调整为不回库 |
| 2024-08-02 14:54:14 | V3.0.1.17 | 全春辉 | 新增 |

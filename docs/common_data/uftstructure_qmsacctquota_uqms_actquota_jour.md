# uqms_actquota_jour - 额度流水表

**表对象ID**: 1602
**所属模块**: qmsacctquota
**数据空间**: HS_UFT_DATA

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_microtime | 否 |  |  |
| 5 | operator_no | 否 |  |  |
| 6 | op_branch_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | op_station | 否 |  |  |
| 9 | acode_account | 否 |  |  |
| 10 | exchange_type | 否 |  |  |
| 11 | stock_code | 否 |  |  |
| 12 | occur_amount | 否 |  |  |
| 13 | occur_balance | 否 |  |  |
| 14 | stock_account | 否 |  |  |
| 15 | join_serial_no | 否 |  |  |
| 16 | cancel_serial_no | 否 |  |  |
| 17 | remark | 否 |  |  |
| 18 | init_date | 否 |  |  |
| 19 | serial_no | 否 |  |  |
| 20 | curr_date | 否 |  |  |
| 21 | curr_microtime | 否 |  |  |
| 22 | operator_no | 否 |  |  |
| 23 | op_branch_no | 否 |  |  |
| 24 | op_entrust_way | 否 |  |  |
| 25 | op_station | 否 |  |  |
| 26 | acode_account | 否 |  |  |
| 27 | exchange_type | 否 |  |  |
| 28 | stock_code | 否 |  |  |
| 29 | occur_amount | 否 |  |  |
| 30 | occur_balance | 否 |  |  |
| 31 | stock_account | 否 |  |  |
| 32 | join_serial_no | 否 |  |  |
| 33 | cancel_serial_no | 否 |  |  |
| 34 | remark | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uqms_actquota_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_uqms_actquota_jour_cancel_join | ART | 是 | join_serial_no, cancel_serial_no, join_serial_no, cancel_serial_no |
| uk_uqms_actquota_jour | ART | 是 | init_date, serial_no, init_date, serial_no |
| idx_uqms_actquota_jour_cancel_join | ART | 是 | join_serial_no, cancel_serial_no, join_serial_no, cancel_serial_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uqms_actquota_jour | init_date, serial_no, init_date, serial_no |
| idx_uqms_actquota_jour | init_date, serial_no, init_date, serial_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 16:37:50 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-05 16:37:50 | V3.0.2.15 | taocong45644 | 勾选回库使用索引 |
| 2025-04-11 15:18:27 | 3.0.2.1 | 李江霖 | 修改物理表索引名 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

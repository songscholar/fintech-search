# pertrans_bind_param - 客户报盘绑定关系表1

**表对象ID**: 5737
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | report_account | 否 |  |  |
| 4 | seat_no | 否 |  |  |
| 5 | trans_name | 否 |  |  |
| 6 | transplat_type | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | report_account | 否 |  |  |
| 10 | seat_no | 否 |  |  |
| 11 | trans_name | 否 |  |  |
| 12 | transplat_type | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_pertrans_bind_param | ART | 是 | report_account, seat_no, transplat_type, report_account, seat_no, transplat_type |
| idx_pertrans_bind_param | ART | 是 | report_account, seat_no, transplat_type, report_account, seat_no, transplat_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_pertrans_bind_param | report_account, seat_no, transplat_type, report_account, seat_no, transplat_type |
| idx_pertrans_bind_param | report_account, seat_no, transplat_type, report_account, seat_no, transplat_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:40:17 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-03-09 14:40:17 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |

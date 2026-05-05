# settredo_arp_apply - 清算重做约定购回申请表

**表对象ID**: 12618
**所属模块**: cbpsrp
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | arp_apply_status | 否 |  |  |
| 4 | remark | 否 |  |  |
| 5 | date_clear | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | serial_no | 否 |  |  |
| 9 | arp_apply_status | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | date_clear | 否 |  |  |
| 12 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_arpapply | ART | 是 | sett_batch_no, serial_no, init_date, sett_batch_no, serial_no, init_date |
| idx_settredo_arpapply | ART | 是 | sett_batch_no, serial_no, init_date, sett_batch_no, serial_no, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_arpapply | sett_batch_no, serial_no, init_date, sett_batch_no, serial_no, init_date |
| idx_settredo_arpapply | sett_batch_no, serial_no, init_date, sett_batch_no, serial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 17:04:26 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-04 16:15:33 | V3.0.2.4 | taocong45644 | 新增表 |
| 2026-03-06 17:04:26 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-08-04 16:15:33 | V3.0.2.4 | taocong45644 | 新增表 |

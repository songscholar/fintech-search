# usps_ipo_seat_contrast - 申购席位对照表

**表对象ID**: 34
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | seat_no | 否 |  |  |
| 2 | seat_no_out | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | seat_no | 否 |  |  |
| 5 | seat_no_out | 否 |  |  |
| 6 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_ipo_seat_contrast | ART | 是 | seat_no, seat_no |
| idx_usps_ipo_seat_contrast | ART | 是 | seat_no, seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_ipo_seat_contrast | seat_no, seat_no |
| idx_usps_ipo_seat_contrast | seat_no, seat_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

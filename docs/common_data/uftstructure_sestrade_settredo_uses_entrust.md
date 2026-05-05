# settredo_uses_entrust - 清算重做证券实时订单表

**表对象ID**: 5994
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | entrust_status | 否 |  |  |
| 2 | error_no | 否 |  |  |
| 3 | position_str | 否 |  |  |
| 4 | sett_batch_no | 否 |  |  |
| 5 | entrust_status | 否 |  |  |
| 6 | error_no | 否 |  |  |
| 7 | position_str | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_entrust_pst | ART | 是 | position_str, position_str |
| idx_settredo_entrust_pst | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_entrust_pst | position_str, position_str |
| idx_settredo_entrust_pst | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:56:05 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:45:54 | 3.0.6.1007 | yangxz |  |
| 2026-03-09 14:56:05 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 09:45:54 | 3.0.6.1007 | yangxz |  |

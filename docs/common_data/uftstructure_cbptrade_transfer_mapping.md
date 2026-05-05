# transfer_mapping - 委托转发关联映射表

**表对象ID**: 2368
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 4 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | source_busin_str | 否 |  |  |
| 2 | dest_busin_str | 否 |  |  |
| 3 | source_busin_str | 否 |  |  |
| 4 | dest_busin_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_transfer_mapping | ART | 是 | source_busin_str, source_busin_str |
| idx_transfer_mapping | ART | 是 | source_busin_str, source_busin_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_transfer_mapping | source_busin_str, source_busin_str |
| idx_transfer_mapping | source_busin_str, source_busin_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:44:11 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-11-05 21:00:42 | V3.0.5.1003 | 赵良梓 | 新增表结构 |
| 2026-03-04 15:44:11 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-11-05 21:00:42 | V3.0.5.1003 | 赵良梓 | 新增表结构 |

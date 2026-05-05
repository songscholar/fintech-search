# upbs_error_msg - 错误信息表

**表对象ID**: 62
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | error_no | 否 |  |  |
| 2 | error_info | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | error_no | 否 |  |  |
| 5 | error_info | 否 |  |  |
| 6 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_error_msg | ART | 是 | error_no, error_no |
| idx_upbs_error_msg | ART | 是 | error_no, error_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_error_msg | error_no, error_no |
| idx_upbs_error_msg | error_no, error_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-05 13:59:41 | 8.26.2.100 | 汪杰 | 表空间修改为hs_uft_data |
| 2023-09-29 17:13:47 | V3.0.1.10 | 沈勋 | 物理表upbs_error_msg，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 13:41 | 0.0.0.4 | 程效 | 新增upbs_error_msg错误信息表 |
| 2026-01-05 13:59:41 | 8.26.2.100 | 汪杰 | 表空间修改为hs_uft_data |
| 2023-09-29 17:13:47 | V3.0.1.10 | 沈勋 | 物理表upbs_error_msg，添加了表字段(transaction_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 13:41 | 0.0.0.4 | 程效 | 新增upbs_error_msg错误信息表 |

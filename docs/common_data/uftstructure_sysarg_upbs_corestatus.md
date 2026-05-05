# upbs_corestatus - 核心在线状态表

**表对象ID**: 63
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | app_name | 否 |  |  |
| 2 | ldp_product_name | 否 |  |  |
| 3 | umt_core_status | 否 |  |  |
| 4 | app_name | 否 |  |  |
| 5 | ldp_product_name | 否 |  |  |
| 6 | umt_core_status | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_corestatus | ART | 是 | app_name, app_name |
| idx_upbs_corestatus | ART | 是 | app_name, app_name |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_corestatus | app_name, app_name |
| idx_upbs_corestatus | app_name, app_name |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 15:57 | 0.0.0.5 | 吴威 | 新增upbs_corestatus |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 15:57 | 0.0.0.5 | 吴威 | 新增upbs_corestatus |

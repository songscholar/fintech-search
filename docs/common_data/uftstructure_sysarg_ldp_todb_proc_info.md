# ldp_todb_proc_info - 平台持久化信息表

**表对象ID**: 94
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | concurrency_info | 否 |  |  |
| 2 | term_str | 否 |  |  |
| 3 | transaction_str | 否 |  |  |
| 4 | ldp_short_appname | 否 |  |  |
| 5 | concurrency_info | 否 |  |  |
| 6 | term_str | 否 |  |  |
| 7 | transaction_str | 否 |  |  |
| 8 | ldp_short_appname | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ldp_todb_info | ART | 是 | concurrency_info, concurrency_info |
| idx_ldp_todb_info | ART | 是 | concurrency_info, concurrency_info |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ldp_todb_info | concurrency_info, concurrency_info |
| idx_ldp_todb_info | concurrency_info, concurrency_info |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-12-12 19:44:33 | 3.0.6.6 | 袁文龙 | 新增表结构 |
| 2024-10-25 14:05:07 | 3.0.5.1002 | 杨森峰 | 新增表结构 |
| 2024-12-12 19:44:33 | 3.0.6.6 | 袁文龙 | 新增表结构 |
| 2024-10-25 14:05:07 | 3.0.5.1002 | 杨森峰 | 新增表结构 |

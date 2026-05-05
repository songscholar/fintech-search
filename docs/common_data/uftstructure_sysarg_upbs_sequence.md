# upbs_sequence - 序列信息表

**表对象ID**: 90
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sequence_value | 否 |  |  |
| 2 | sequence_span | 否 |  |  |
| 3 | sequence_syncinterval | 否 |  |  |
| 4 | ldp_short_appname | 否 |  |  |
| 5 | sequence_no_ldp | 否 |  |  |
| 6 | sequence_value | 否 |  |  |
| 7 | sequence_span | 否 |  |  |
| 8 | sequence_syncinterval | 否 |  |  |
| 9 | ldp_short_appname | 否 |  |  |
| 10 | sequence_no_ldp | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_sequence | ART | 是 | sequence_no_ldp, ldp_short_appname, sequence_no_ldp, ldp_short_appname |
| idx_upbs_sequence | ART | 是 | sequence_no_ldp, ldp_short_appname, sequence_no_ldp, ldp_short_appname |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_sequence | sequence_no_ldp, ldp_short_appname, sequence_no_ldp, ldp_short_appname |
| idx_upbs_sequence | sequence_no_ldp, ldp_short_appname, sequence_no_ldp, ldp_short_appname |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-12-06 18:05:44 | V3.0.1.21 | 李海洋 | 删除日志修复开发工具误报 |
| 2023-12-06 18:02:06 | V3.0.1.19 | 李海洋 | 新增 |
| 2023-12-06 18:05:44 | V3.0.1.21 | 李海洋 | 删除日志修复开发工具误报 |
| 2023-12-06 18:02:06 | V3.0.1.19 | 李海洋 | 新增 |

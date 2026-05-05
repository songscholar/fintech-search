# ststock_quota_control - 风险警示股允许买入控制表

**表对象ID**: 370
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_time | 否 |  |  |
| 3 | begin_time | 否 |  |  |
| 4 | end_time | 否 |  |  |
| 5 | ststock_quota_status | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | curr_time | 否 |  |  |
| 8 | begin_time | 否 |  |  |
| 9 | end_time | 否 |  |  |
| 10 | ststock_quota_status | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ststock_quota_control | 默认 | 否 |  |
| idx_ststock_quota_control | 默认 | 否 | init_date, init_date |
| idx_ststock_quota_control | ART | 是 | init_date, init_date |
| idx_ststock_quota_control | 默认 | 否 |  |
| idx_ststock_quota_control | 默认 | 否 | init_date, init_date |
| idx_ststock_quota_control | ART | 是 | init_date, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ststock_quota_control | init_date, init_date |
| idx_ststock_quota_control | init_date, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:13:13 | 3.0.2.103 | taocong45644 | 当前表ststock_quota_control，修改了索引idx_ststock_quota_control,索引字段... |
| 2025-07-29 15:56:52 | 3.0.6.12 | 汪杰 | 物理表ststock_quota_control，增加索引(idx_ststock_quota_control:[ini... |
| 2025-07-29 15:54:27 | 3.0.6.12 | 汪杰 | 物理表ststock_quota_control，添加了表字段(init_date);
物理表ststock_quot... |
| 2025-12-01 15:13:13 | 3.0.2.103 | taocong45644 | 当前表ststock_quota_control，修改了索引idx_ststock_quota_control,索引字段... |
| 2025-07-29 15:56:52 | 3.0.6.12 | 汪杰 | 物理表ststock_quota_control，增加索引(idx_ststock_quota_control:[ini... |
| 2025-07-29 15:54:27 | 3.0.6.12 | 汪杰 | 物理表ststock_quota_control，添加了表字段(init_date);
物理表ststock_quot... |

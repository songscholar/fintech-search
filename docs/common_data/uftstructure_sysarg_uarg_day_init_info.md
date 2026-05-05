# uarg_day_init_info - 参数日终信息表

**表对象ID**: 106
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | process_flag | 否 |  |  |
| 3 | remark | 否 |  |  |
| 4 | init_date | 否 |  |  |
| 5 | process_flag | 否 |  |  |
| 6 | remark | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uarg_day_init_info | 默认 | 否 |  |
| idx_uarg_day_init_info | ART | 是 | init_date, init_date |
| idx_uarg_day_init_info | 默认 | 否 |  |
| idx_uarg_day_init_info | ART | 是 | init_date, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uarg_day_init_info | init_date, init_date |
| idx_uarg_day_init_info | init_date, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:19:49 | 3.0.2.103 | taocong45644 | 当前表uarg_day_init_info，修改了索引idx_uarg_day_init_info,索引字段修改为：(i... |
| 2025-02-18 18:58:21 | 3.0.6.79 | 李想 | 新增表 |
| 2025-12-01 15:19:49 | 3.0.2.103 | taocong45644 | 当前表uarg_day_init_info，修改了索引idx_uarg_day_init_info,索引字段修改为：(i... |
| 2025-02-18 18:58:21 | 3.0.6.79 | 李想 | 新增表 |

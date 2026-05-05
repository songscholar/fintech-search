# fin_main_info - 融资主体基本信息表

**表对象ID**: 5013
**所属模块**: sesarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | full_name | 否 |  |  |
| 2 | acode_account | 否 |  |  |
| 3 | impawn_special_account | 否 |  |  |
| 4 | finrepurchmain_type | 否 |  |  |
| 5 | finrepurchmain_value | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | position_str | 否 |  | acode_account(20)+impawn_special_account(10) |
| 10 | full_name | 否 |  |  |
| 11 | acode_account | 否 |  |  |
| 12 | impawn_special_account | 否 |  |  |
| 13 | finrepurchmain_type | 否 |  |  |
| 14 | finrepurchmain_value | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | position_str | 否 |  | acode_account(20)+impawn_special_account(10) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fin_main_info | 默认 | 否 |  |
| idx_fin_main_info | ART | 是 | acode_account, impawn_special_account, acode_account, impawn_special_account |
| idx_fin_main_info | 默认 | 否 |  |
| idx_fin_main_info | ART | 是 | acode_account, impawn_special_account, acode_account, impawn_special_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_fin_main_info | acode_account, impawn_special_account, acode_account, impawn_special_account |
| idx_fin_main_info | acode_account, impawn_special_account, acode_account, impawn_special_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:22:41 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:15:04 | 3.0.2.84 | taocong45644 | 当前表fin_main_info，修改了索引idx_fin_main_info,索引字段修改为：(acode_accou... |
| 2025-02-20 14:13:58 | 3.0.6.40 | 李想 | 新增表 |
| 2026-03-05 17:22:41 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:15:04 | 3.0.2.84 | taocong45644 | 当前表fin_main_info，修改了索引idx_fin_main_info,索引字段修改为：(acode_accou... |
| 2025-02-20 14:13:58 | 3.0.6.40 | 李想 | 新增表 |

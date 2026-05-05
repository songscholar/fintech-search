# issue_main_level - 发行主体评级

**表对象ID**: 5554
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | issue_main | 否 |  |  |
| 2 | issue_main_grade | 否 |  |  |
| 3 | transaction_no | 否 |  |  |
| 4 | issue_main_full_name | 否 |  |  |
| 5 | issue_main_no | 否 |  |  |
| 6 | issue_main_phone | 否 |  |  |
| 7 | issue_main_relation | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | issue_main | 否 |  |  |
| 11 | issue_main_grade | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | issue_main_full_name | 否 |  |  |
| 14 | issue_main_no | 否 |  |  |
| 15 | issue_main_phone | 否 |  |  |
| 16 | issue_main_relation | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_issue_main_grade | ART | 是 | issue_main, issue_main |
| idx_uses_issue_main_grade | ART | 是 | issue_main, issue_main |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_issue_main_grade | issue_main, issue_main |
| idx_uses_issue_main_grade | issue_main, issue_main |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-20 13:30:00 | 3.0.6.19 | 李想 | 物理表issue_main_level，添加了表字段(issue_main_full_name);
物理表issue_... |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |
| 2025-02-20 13:30:00 | 3.0.6.19 | 李想 | 物理表issue_main_level，添加了表字段(issue_main_full_name);
物理表issue_... |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |

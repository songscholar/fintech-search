# issue_main_relinfo - 债券发行主体关联方信息表

**表对象ID**: 5552
**所属模块**: sestrade
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | issue_main | 否 |  |  |
| 2 | rel_issue_main | 否 |  |  |
| 3 | remark | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | update_date | 否 |  |  |
| 6 | update_time | 否 |  |  |
| 7 | issue_main | 否 |  |  |
| 8 | rel_issue_main | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_issue_main_relinfo | ART | 是 | issue_main, rel_issue_main, issue_main, rel_issue_main |
| idx_issue_main_relinfo | ART | 是 | issue_main, rel_issue_main, issue_main, rel_issue_main |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_issue_main_relinfo | issue_main, rel_issue_main, issue_main, rel_issue_main |
| idx_issue_main_relinfo | issue_main, rel_issue_main, issue_main, rel_issue_main |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:04:00 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 13:43:59 | 3.0.6.22 | 李想 | 物理表issue_main_relinfo，添加了表字段(update_date);
物理表issue_main_re... |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |
| 2026-03-09 14:04:00 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-02-20 13:43:59 | 3.0.6.22 | 李想 | 物理表issue_main_relinfo，添加了表字段(update_date);
物理表issue_main_re... |
| 2024-06-28 15:16:54 | 3.0.2.22 | 张云焘 | 新增 |

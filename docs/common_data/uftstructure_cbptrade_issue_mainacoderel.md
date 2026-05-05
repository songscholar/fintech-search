# issue_mainacoderel - 债券发行主体一码通对照表

**表对象ID**: 2332
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | issue_main | 否 |  |  |
| 2 | acode_account | 否 |  |  |
| 3 | remark | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | issue_main | 否 |  |  |
| 6 | acode_account | 否 |  |  |
| 7 | remark | 否 |  |  |
| 8 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_issuemainacoderel | 默认 | 否 |  |
| idx_issuemainacoderel | ART | 是 | acode_account, acode_account |
| idx_issuemainacoderel | 默认 | 否 |  |
| idx_issuemainacoderel | ART | 是 | acode_account, acode_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_issuemainacoderel | acode_account, acode_account |
| idx_issuemainacoderel | acode_account, acode_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 15:27:58 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-08-21 14:20:36 | V3.0.2.1006 | 杨涛 | issue_mainacoderel调整唯一索引字段为acode_account |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |
| 2026-03-04 15:27:58 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2024-08-21 14:20:36 | V3.0.2.1006 | 杨涛 | issue_mainacoderel调整唯一索引字段为acode_account |
| 2024-08-06 19:25:47 | V3.0.2.1004 | 骆鹏程 | 新增 |

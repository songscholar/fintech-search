# stock_code_match - 北交所股转代码对照表

**表对象ID**: 100
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | trans_code_tz | 否 |  |  |
| 3 | effect_date | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | trans_code_tz | 否 |  |  |
| 6 | effect_date | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stock_code_match | ART | 是 | stock_code, stock_code |
| idx_stock_code_match_tz | ART | 是 | trans_code_tz, trans_code_tz |
| idx_stock_code_match | ART | 是 | stock_code, stock_code |
| idx_stock_code_match_tz | ART | 是 | trans_code_tz, trans_code_tz |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stock_code_match | stock_code, stock_code |
| idx_stock_code_match | stock_code, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-17 20:32:30 | 3.0.2.83 | 全春辉 | 新增表stock_code_match |
| 2025-04-17 20:32:30 | 3.0.2.83 | 全春辉 | 新增表stock_code_match |

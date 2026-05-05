# upbs_elig_match_rel - 适当性匹配逻辑关系表

**表对象ID**: 86
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | eligmatch_kind | 否 |  |  |
| 2 | client_match_value | 否 |  |  |
| 3 | en_elig_match_value | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | eligmatch_kind | 否 |  |  |
| 6 | client_match_value | 否 |  |  |
| 7 | en_elig_match_value | 否 |  |  |
| 8 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_elig_match_rel | ART | 是 | eligmatch_kind, client_match_value, eligmatch_kind, client_match_value |
| idx_upbs_elig_match_rel | ART | 是 | eligmatch_kind, client_match_value, eligmatch_kind, client_match_value |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_elig_match_rel | eligmatch_kind, client_match_value, eligmatch_kind, client_match_value |
| idx_upbs_elig_match_rel | eligmatch_kind, client_match_value, eligmatch_kind, client_match_value |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-11-10 10:18:51 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |
| 2023-11-10 10:18:51 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |

# uref_ieopp_info - 信息交互平台关联对手方表

**表对象ID**: 6222
**所属模块**: refinex
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | create_date | 否 |  |  |
| 2 | entrust_no | 否 |  |  |
| 3 | opp_organ_code | 否 |  |  |
| 4 | opp_organ_name | 否 |  |  |
| 5 | opp_borrower_code | 否 |  |  |
| 6 | opp_borrower_name | 否 |  |  |
| 7 | withdraw_status | 否 |  |  |
| 8 | position_str | 否 |  |  |
| 9 | date_clear | 否 |  |  |
| 10 | create_date | 否 |  |  |
| 11 | entrust_no | 否 |  |  |
| 12 | opp_organ_code | 否 |  |  |
| 13 | opp_organ_name | 否 |  |  |
| 14 | opp_borrower_code | 否 |  |  |
| 15 | opp_borrower_name | 否 |  |  |
| 16 | withdraw_status | 否 |  |  |
| 17 | position_str | 否 |  |  |
| 18 | date_clear | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ieoppinfo | ART | 是 | position_str, position_str |
| idx_ieoppinfo_no | ART | 是 | entrust_no, create_date, entrust_no, create_date |
| idx_ieoppinfo | ART | 是 | position_str, position_str |
| idx_ieoppinfo_no | ART | 是 | entrust_no, create_date, entrust_no, create_date |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_ieoppinfo | position_str, position_str |
| idx_ieoppinfo_no | entrust_no, create_date, entrust_no, create_date |
| idx_ieoppinfo | position_str, position_str |
| idx_ieoppinfo_no | entrust_no, create_date, entrust_no, create_date |

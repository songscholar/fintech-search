# uref_settle_jour - 转融通清算流水表

**表对象ID**: 6153
**所属模块**: refsett
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | curr_date | 否 |  |  |
| 3 | curr_time | 否 |  |  |
| 4 | settle_no | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | init_date | 否 |  |  |
| 7 | curr_date | 否 |  |  |
| 8 | curr_time | 否 |  |  |
| 9 | settle_no | 否 |  |  |
| 10 | remark | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refsettlejour | ART | 是 | init_date, settle_no, init_date, settle_no |
| idx_refsettlejour | ART | 是 | init_date, settle_no, init_date, settle_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refsettlejour | init_date, settle_no, init_date, settle_no |
| idx_refsettlejour | init_date, settle_no, init_date, settle_no |

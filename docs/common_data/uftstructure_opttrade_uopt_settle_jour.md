# uopt_settle_jour - 股票期权清算流水表

**表对象ID**: 9630
**所属模块**: opttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | settle_no | 否 |  |  |
| 3 | curr_date | 否 |  |  |
| 4 | curr_time | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | settle_no | 否 |  |  |
| 9 | curr_date | 否 |  |  |
| 10 | curr_time | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | fund_account | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_settle_jour | 默认 | 是 | init_date, settle_no, init_date, settle_no |
| idx_uopt_settle_jour | 默认 | 是 | init_date, settle_no, init_date, settle_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_settle_jour | init_date, settle_no, init_date, settle_no |
| idx_uopt_settle_jour | init_date, settle_no, init_date, settle_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-30 22:52:17 | V3.0.2.2 | 吴笑东 | 新增 |
| 2025-07-30 22:52:17 | V3.0.2.2 | 吴笑东 | 新增 |

# setttouftcompfloatrate - 清算合约浮动利率

**表对象ID**: 3060
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | compact_id | 是 |  |  |
| 4 | begin_date | 是 |  |  |
| 5 | year_rate | 是 |  |  |
| 6 | float_ratio | 是 |  |  |
| 7 | date_clear | 是 |  |  |
| 8 | uft_data_change_status | 是 |  |  |
| 9 | init_date | 是 |  |  |
| 10 | fund_account | 是 |  |  |
| 11 | compact_id | 是 |  |  |
| 12 | begin_date | 是 |  |  |
| 13 | year_rate | 是 |  |  |
| 14 | float_ratio | 是 |  |  |
| 15 | date_clear | 是 |  |  |
| 16 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settcompfloatrate | 默认 | 是 | compact_id, begin_date, compact_id, begin_date |
| idx_settcompfloatrate_fund | 默认 | 是 | fund_account, fund_account |
| idx_settcompfloatrate | 默认 | 是 | compact_id, begin_date, compact_id, begin_date |
| idx_settcompfloatrate_fund | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_compfloatrate | compact_id, begin_date, compact_id, begin_date |
| idx_compfloatrate | compact_id, begin_date, compact_id, begin_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-08-21 19:40 | 8.26.1.32 | 徐斐 | 增加索引idx_settcompfloatrate_fund |
| 2018-08-21 19:40 | 8.26.1.32 | 徐斐 | 增加索引idx_settcompfloatrate_fund |

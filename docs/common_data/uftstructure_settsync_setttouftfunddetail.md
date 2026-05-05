# setttouftfunddetail - 清算入账资金明细表

**表对象ID**: 3090
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 是 |  |  |
| 2 | money_type | 是 |  |  |
| 3 | init_date | 是 |  |  |
| 4 | business_frozen_balance | 是 |  |  |
| 5 | business_unfrozen_balance | 是 |  |  |
| 6 | fund_enable_level | 是 |  | 0、5、25层级是增量，其它层级不会下发数据，需要交易系统清空除0，5，25层级外funddetail表上日数据。 |
| 7 | flow_count | 是 |  |  |
| 8 | fund_account | 是 |  |  |
| 9 | money_type | 是 |  |  |
| 10 | init_date | 是 |  |  |
| 11 | business_frozen_balance | 是 |  |  |
| 12 | business_unfrozen_balance | 是 |  |  |
| 13 | fund_enable_level | 是 |  | 0、5、25层级是增量，其它层级不会下发数据，需要交易系统清空除0，5，25层级外funddetail表上日数据。 |
| 14 | flow_count | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| sett_fund_detail_idx | 默认 | 是 | flow_count, fund_account, money_type, fund_enable_level, flow_count, fund_account, money_type, fund_enable_level |
| sett_fund_detail_idx | 默认 | 是 | flow_count, fund_account, money_type, fund_enable_level, flow_count, fund_account, money_type, fund_enable_level |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| sett_fund_detail_idx | flow_count, fund_account, money_type, fund_enable_level, flow_count, fund_account, money_type, fund_enable_level |
| sett_fund_detail_idx | flow_count, fund_account, money_type, fund_enable_level, flow_count, fund_account, money_type, fund_enable_level |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-07-11 10:38:05 | 1.0.0.1 | shikai | 支持清算入账 |
| 2024-07-11 10:38:05 | 1.0.0.1 | shikai | 支持清算入账 |

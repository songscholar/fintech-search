# setttouftsrpintegralinfo - 清算股票质押结息日期信息表

**表对象ID**: 3032
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | client_id | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | contract_id | 是 |  |  |
| 6 | funder_no | 是 |  |  |
| 7 | interest_date | 是 |  |  |
| 8 | agreed_interest | 是 |  |  |
| 9 | repaid_interest | 是 |  |  |
| 10 | auto_type | 是 |  |  |
| 11 | date_clear | 是 |  |  |
| 12 | position_str | 是 |  |  |
| 13 | uft_data_change_status | 是 |  |  |
| 14 | payinterest_deal_flag | 是 |  |  |
| 15 | init_date | 是 |  |  |
| 16 | fund_account | 是 |  |  |
| 17 | client_id | 是 |  |  |
| 18 | branch_no | 是 |  |  |
| 19 | contract_id | 是 |  |  |
| 20 | funder_no | 是 |  |  |
| 21 | interest_date | 是 |  |  |
| 22 | agreed_interest | 是 |  |  |
| 23 | repaid_interest | 是 |  |  |
| 24 | auto_type | 是 |  |  |
| 25 | date_clear | 是 |  |  |
| 26 | position_str | 是 |  |  |
| 27 | uft_data_change_status | 是 |  |  |
| 28 | payinterest_deal_flag | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_settsrpintegralinfo | 默认 | 是 | contract_id, interest_date, contract_id, interest_date |
| idx_settsrpintegralinfo_pos | 默认 | 是 | position_str, position_str |
| idx_settsrpintegralinfo_id | 默认 | 是 | contract_id, contract_id |
| uk_settsrpintegralinfo | 默认 | 是 | contract_id, interest_date, contract_id, interest_date |
| idx_settsrpintegralinfo_pos | 默认 | 是 | position_str, position_str |
| idx_settsrpintegralinfo_id | 默认 | 是 | contract_id, contract_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_settsrpintegralinfo | contract_id, interest_date, contract_id, interest_date |
| uk_settsrpintegralinfo | contract_id, interest_date, contract_id, interest_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-05-09 23:44 | 8.26.1.81 | 曾哲 | 删除stock_account,exchange_type字段 |
| 2018-04-16 16:22 | 8.26.1.8 | 王泽贵 | 新增表 |
| 2020-05-09 23:44 | 8.26.1.81 | 曾哲 | 删除stock_account,exchange_type字段 |
| 2018-04-16 16:22 | 8.26.1.8 | 王泽贵 | 新增表 |

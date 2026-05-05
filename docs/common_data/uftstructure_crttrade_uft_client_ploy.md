# uft_client_ploy - UFT客户平仓策略设置表

**表对象ID**: 7572
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | clientploy_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | payoffploy_no | 否 |  |  |
| 7 | poptarget_value | 否 |  |  |
| 8 | popdeal_flag | 否 |  |  |
| 9 | create_date | 否 |  |  |
| 10 | create_time | 否 |  |  |
| 11 | date_clear | 否 |  |  |
| 12 | remark | 否 |  |  |
| 13 | position_str | 否 |  |  |
| 14 | init_date | 否 |  |  |
| 15 | clientploy_id | 否 |  |  |
| 16 | branch_no | 否 |  |  |
| 17 | fund_account | 否 |  |  |
| 18 | client_id | 否 |  |  |
| 19 | payoffploy_no | 否 |  |  |
| 20 | poptarget_value | 否 |  |  |
| 21 | popdeal_flag | 否 |  |  |
| 22 | create_date | 否 |  |  |
| 23 | create_time | 否 |  |  |
| 24 | date_clear | 否 |  |  |
| 25 | remark | 否 |  |  |
| 26 | position_str | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_client_ploy | ART | 是 | clientploy_id, clientploy_id |
| idx_uft_client_ploy_pos | ART | 是 | position_str, position_str |
| idx_uft_client_ploy_acct | ART | 是 | fund_account, fund_account |
| idx_uft_client_ploy | ART | 是 | clientploy_id, clientploy_id |
| idx_uft_client_ploy_pos | ART | 是 | position_str, position_str |
| idx_uft_client_ploy_acct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_client_ploy | clientploy_id, clientploy_id |
| idx_uft_client_ploy | clientploy_id, clientploy_id |

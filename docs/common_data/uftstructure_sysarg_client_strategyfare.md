# client_strategyfare - 账户策略服务佣金表

**表对象ID**: 110
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | strategyfare_id | 否 |  |  |
| 5 | sign_date | 否 |  |  |
| 6 | sign_time | 否 |  |  |
| 7 | unsign_date | 否 |  |  |
| 8 | unsign_time | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | update_date | 否 |  |  |
| 11 | update_time | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | asset_prop | 否 |  |  |
| 14 | position_str | 否 |  | fund_account(18)+strategyfare_id(32) |
| 15 | client_id | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | branch_no | 否 |  |  |
| 18 | strategyfare_id | 否 |  |  |
| 19 | sign_date | 否 |  |  |
| 20 | sign_time | 否 |  |  |
| 21 | unsign_date | 否 |  |  |
| 22 | unsign_time | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | update_date | 否 |  |  |
| 25 | update_time | 否 |  |  |
| 26 | transaction_no | 否 |  |  |
| 27 | asset_prop | 否 |  |  |
| 28 | position_str | 否 |  | fund_account(18)+strategyfare_id(32) |

## 索引（共 12 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_client_strategyfare | 默认 | 否 |  |
| idx_client_strategyfare_f | 默认 | 否 |  |
| idx_client_strategyfare_c | 默认 | 否 |  |
| idx_client_strategyfare | ART | 是 | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_client_strategyfare_f | ART | 是 | fund_account, fund_account |
| idx_client_strategyfare_c | ART | 是 | client_id, client_id |
| idx_client_strategyfare | 默认 | 否 |  |
| idx_client_strategyfare_f | 默认 | 否 |  |
| idx_client_strategyfare_c | 默认 | 否 |  |
| idx_client_strategyfare | ART | 是 | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_client_strategyfare_f | ART | 是 | fund_account, fund_account |
| idx_client_strategyfare_c | ART | 是 | client_id, client_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_client_strategyfare | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_client_strategyfare | fund_account, strategyfare_id, fund_account, strategyfare_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:37:58 | 3.0.2.103 | taocong45644 | 当前表client_strategyfare，修改了索引idx_client_strategyfare,索引字段修改为：... |
| 2025-02-14 13:32:17 | 3.0.6.21 | 李想 | 新增表 |
| 2025-12-01 14:37:58 | 3.0.2.103 | taocong45644 | 当前表client_strategyfare，修改了索引idx_client_strategyfare,索引字段修改为：... |
| 2025-02-14 13:32:17 | 3.0.6.21 | 李想 | 新增表 |

# strategyfare_contract - 策略服务佣金签约信息表

**表对象ID**: 113
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
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
| 13 | position_str | 否 |  | fund_account(18)+strategyfare_id(32) |
| 14 | fund_account | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | branch_no | 否 |  |  |
| 17 | strategyfare_id | 否 |  |  |
| 18 | sign_date | 否 |  |  |
| 19 | sign_time | 否 |  |  |
| 20 | unsign_date | 否 |  |  |
| 21 | unsign_time | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | update_date | 否 |  |  |
| 24 | update_time | 否 |  |  |
| 25 | transaction_no | 否 |  |  |
| 26 | position_str | 否 |  | fund_account(18)+strategyfare_id(32) |

## 索引（共 14 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strategyfare_contract | 默认 | 否 |  |
| idx_strategyfare_contract_F | 默认 | 否 |  |
| idx_strategyfare_contract_C | 默认 | 否 |  |
| idx_strategyfare_contract_C | 默认 | 否 | client_id, client_id |
| idx_strategyfare_contract | ART | 是 | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_strategyfare_contract_F | ART | 是 | fund_account, fund_account |
| idx_strategyfare_contract_C | ART | 是 | client_id, client_id |
| idx_strategyfare_contract | 默认 | 否 |  |
| idx_strategyfare_contract_F | 默认 | 否 |  |
| idx_strategyfare_contract_C | 默认 | 否 |  |
| idx_strategyfare_contract_C | 默认 | 否 | client_id, client_id |
| idx_strategyfare_contract | ART | 是 | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_strategyfare_contract_F | ART | 是 | fund_account, fund_account |
| idx_strategyfare_contract_C | ART | 是 | client_id, client_id |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_strategyfare_contract | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_strategyfare_contract_C | client_id, client_id |
| idx_strategyfare_contract | fund_account, strategyfare_id, fund_account, strategyfare_id |
| idx_strategyfare_contract_C | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:55:28 | 3.0.2.103 | taocong45644 | 当前表strategyfare_contract，修改了索引idx_strategyfare_contract,索引字段... |
| 2025-07-17 14:13:45 | 3.0.6.1017 | 常行 | 物理表strategyfare_contract，增加索引(idx_strategyfare_contract_C:[c... |
| 2025-02-14 14:10:49 | 3.0.6.24 | 李想 | 新增表 |
| 2025-12-01 14:55:28 | 3.0.2.103 | taocong45644 | 当前表strategyfare_contract，修改了索引idx_strategyfare_contract,索引字段... |
| 2025-07-17 14:13:45 | 3.0.6.1017 | 常行 | 物理表strategyfare_contract，增加索引(idx_strategyfare_contract_C:[c... |
| 2025-02-14 14:10:49 | 3.0.6.24 | 李想 | 新增表 |

# uft_account_deploy - UFT资产账户部署表

**表对象ID**: 2808
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | uft_sysnode_id | 否 |  |  |
| 5 | enable_status | 否 |  |  |
| 6 | single_thread_flag | 否 |  |  |
| 7 | frozen_ratio | 否 |  |  |
| 8 | frozen_balance | 否 |  |  |
| 9 | orig_seat_no_str | 否 |  |  |
| 10 | new_uft_sysnode_id | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | ust_ctrlstr | 否 |  |  |
| 13 | sysnode_id | 否 |  |  |
| 14 | branch_no | 否 |  |  |
| 15 | client_id | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | uft_sysnode_id | 否 |  |  |
| 18 | enable_status | 否 |  |  |
| 19 | single_thread_flag | 否 |  |  |
| 20 | frozen_ratio | 否 |  |  |
| 21 | frozen_balance | 否 |  |  |
| 22 | orig_seat_no_str | 否 |  |  |
| 23 | new_uft_sysnode_id | 否 |  |  |
| 24 | transaction_no | 否 |  |  |
| 25 | ust_ctrlstr | 否 |  |  |
| 26 | sysnode_id | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uft_account_deploy | 默认 | 否 |  |
| uk_uft_account_deploy | ART | 是 | fund_account, fund_account |
| uk_uft_account_deploy | 默认 | 否 |  |
| uk_uft_account_deploy | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_uft_account_deploy | fund_account, fund_account |
| uk_uft_account_deploy | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:23:44 | 3.0.2.103 | taocong45644 | 当前表uft_account_deploy，修改了索引uk_uft_account_deploy,索引字段修改为：(fu... |
| 2025-09-09 11:19:56 | 8.26.2.92 | 冯元栋 | 所有表uft_account_deploy，添加了表字段(ust_ctrlstr);
所有表uft_account_d... |
| 2025-03-11 11:07:45 | 3.0.6.81 | 杨新照 | 新增表结构 |
| 2025-12-01 15:23:44 | 3.0.2.103 | taocong45644 | 当前表uft_account_deploy，修改了索引uk_uft_account_deploy,索引字段修改为：(fu... |
| 2025-09-09 11:19:56 | 8.26.2.92 | 冯元栋 | 所有表uft_account_deploy，添加了表字段(ust_ctrlstr);
所有表uft_account_d... |
| 2025-03-11 11:07:45 | 3.0.6.81 | 杨新照 | 新增表结构 |

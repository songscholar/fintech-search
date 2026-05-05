# uft_config - UFT配置表

**表对象ID**: 2810
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sysnode_id | 否 |  |  |
| 2 | sysnode_name | 否 |  |  |
| 3 | sys_status | 否 |  |  |
| 4 | en_exchange_type | 否 |  |  |
| 5 | en_stock_type | 否 |  |  |
| 6 | other_config | 否 |  |  |
| 7 | asset_prop | 否 |  |  |
| 8 | uft_sysnode_version | 否 |  |  |
| 9 | developer_id | 否 |  |  |
| 10 | other_config_str | 否 |  |  |
| 11 | uft_partition_id | 否 |  |  |
| 12 | onestep_trans_flag | 否 |  |  |
| 13 | en_acct_exch_type | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | counter_trade_flag | 否 |  |  |
| 16 | sysnode_id | 否 |  |  |
| 17 | sysnode_name | 否 |  |  |
| 18 | sys_status | 否 |  |  |
| 19 | en_exchange_type | 否 |  |  |
| 20 | en_stock_type | 否 |  |  |
| 21 | other_config | 否 |  |  |
| 22 | asset_prop | 否 |  |  |
| 23 | uft_sysnode_version | 否 |  |  |
| 24 | developer_id | 否 |  |  |
| 25 | other_config_str | 否 |  |  |
| 26 | uft_partition_id | 否 |  |  |
| 27 | onestep_trans_flag | 否 |  |  |
| 28 | en_acct_exch_type | 否 |  |  |
| 29 | transaction_no | 否 |  |  |
| 30 | counter_trade_flag | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uft_config | 默认 | 否 |  |
| uk_uft_config | ART | 是 | sysnode_id, sysnode_id |
| uk_uft_config | 默认 | 否 |  |
| uk_uft_config | ART | 是 | sysnode_id, sysnode_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_uft_config | sysnode_id, sysnode_id |
| uk_uft_config | sysnode_id, sysnode_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:24:47 | 3.0.2.103 | taocong45644 | 当前表uft_config，修改了索引uk_uft_config,索引字段修改为：(sysnode_id),索引唯一性修... |
| 2025-09-16 20:23:25 | 8.26.2.93 | tongck54118 | 所有表uft_config，添加了表字段(counter_trade_flag);
 |
| 2025-03-11 11:08:30 | 3.0.6.83 | 杨新照 | 新增表结构 |
| 2025-12-01 15:24:47 | 3.0.2.103 | taocong45644 | 当前表uft_config，修改了索引uk_uft_config,索引字段修改为：(sysnode_id),索引唯一性修... |
| 2025-09-16 20:23:25 | 8.26.2.93 | tongck54118 | 所有表uft_config，添加了表字段(counter_trade_flag);
 |
| 2025-03-11 11:08:30 | 3.0.6.83 | 杨新照 | 新增表结构 |

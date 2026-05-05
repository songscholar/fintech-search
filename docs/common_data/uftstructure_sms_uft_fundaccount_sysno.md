# uft_fundaccount_sysno - UFT资产账户节点信息表

**表对象ID**: 2809
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | system_no | 是 |  |  |
| 5 | trans_rate | 是 |  |  |
| 6 | uft_sysnode_id | 是 |  |  |
| 7 | enable_status | 是 |  |  |
| 8 | remark | 是 |  |  |
| 9 | transaction_no | 是 |  |  |
| 10 | client_id | 是 |  |  |
| 11 | fund_account | 是 |  |  |
| 12 | exchange_type | 是 |  |  |
| 13 | system_no | 是 |  |  |
| 14 | trans_rate | 是 |  |  |
| 15 | uft_sysnode_id | 是 |  |  |
| 16 | enable_status | 是 |  |  |
| 17 | remark | 是 |  |  |
| 18 | transaction_no | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_uft_fundaccount_sysno | 默认 | 是 | client_id, fund_account, exchange_type, system_no, client_id, fund_account, exchange_type, system_no |
| uk_uft_fundaccount_sysno | 默认 | 是 | client_id, fund_account, exchange_type, system_no, client_id, fund_account, exchange_type, system_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_uft_fundaccount_sysno | client_id, fund_account, exchange_type, system_no, client_id, fund_account, exchange_type, system_no |
| uk_uft_fundaccount_sysno | client_id, fund_account, exchange_type, system_no, client_id, fund_account, exchange_type, system_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-11 11:08:09 | 3.0.6.82 | 杨新照 | 新增表结构 |
| 2025-03-11 11:08:09 | 3.0.6.82 | 杨新照 | 新增表结构 |

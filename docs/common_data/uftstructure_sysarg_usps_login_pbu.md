# usps_login_pbu - PBU参数表

**表对象ID**: 2337
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | entrust_prop | 否 |  |  |
| 5 | login_pbu | 否 |  |  |
| 6 | seatvip_flag | 否 |  |  |
| 7 | uft_sysnode_id | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | transplat_type | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | company_no | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | entrust_prop | 否 |  |  |
| 15 | login_pbu | 否 |  |  |
| 16 | seatvip_flag | 否 |  |  |
| 17 | uft_sysnode_id | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | transplat_type | 否 |  |  |
| 20 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_loginpbu | ART | 是 | company_no, exchange_type, branch_no, entrust_prop, uft_sysnode_id, transplat_type, company_no, exchange_type, branch_no, entrust_prop, uft_sysnode_id, transplat_type |
| idx_loginpbu | ART | 是 | company_no, exchange_type, branch_no, entrust_prop, uft_sysnode_id, transplat_type, company_no, exchange_type, branch_no, entrust_prop, uft_sysnode_id, transplat_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_loginpbu | company_no, exchange_type, branch_no, entrust_prop, uft_sysnode_id, transplat_type, company_no, exchange_type, branch_no, entrust_prop, uft_sysnode_id, transplat_type |
| idx_loginpbu | company_no, exchange_type, branch_no, entrust_prop, uft_sysnode_id, transplat_type, company_no, exchange_type, branch_no, entrust_prop, uft_sysnode_id, transplat_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-12 16:25:28 | 8.26.2.93 | 冯元栋 | 调整表空间 |
| 2025-06-06 13:38:37 | 3.0.2.87 | 董乾坤 | 从cbp/cbptrade移动到pbs/sysarg目录 |
| 2024-08-06 19:25:47 | V3.0.2.2 | 骆鹏程 | 新增 |
| 2025-09-12 16:25:28 | 8.26.2.93 | 冯元栋 | 调整表空间 |
| 2025-06-06 13:38:37 | 3.0.2.87 | 董乾坤 | 从cbp/cbptrade移动到pbs/sysarg目录 |
| 2024-08-06 19:25:47 | V3.0.2.2 | 骆鹏程 | 新增 |

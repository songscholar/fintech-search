# uopt_black_acctctrl - 股票期权黑名单控制表

**表对象ID**: 9031
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | riskaccount_type | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | optblackacct_src | 否 |  |  |
| 6 | create_date | 否 |  |  |
| 7 | notice_status | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | opt_notice_text | 否 |  |  |
| 10 | partition_no | 否 |  |  |
| 11 | branch_no | 否 |  |  |
| 12 | riskaccount_type | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | optblackacct_src | 否 |  |  |
| 16 | create_date | 否 |  |  |
| 17 | notice_status | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | opt_notice_text | 否 |  |  |
| 20 | partition_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_black_acctctrl | 默认 | 是 | fund_account, fund_account |
| idx_uopt_black_acctctrl | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_black_acctctrl | fund_account, fund_account |
| idx_uopt_black_acctctrl | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-22 16:20:36 | V3.0.2.2 | 汪迎 | 所有表uopt_black_acctctrl，添加了表字段(partition_no);
 |
| 2025-01-06 20:01:24 | V3.0.3.12 |  | 新增 |
| 2025-08-22 16:20:36 | V3.0.2.2 | 汪迎 | 所有表uopt_black_acctctrl，添加了表字段(partition_no);
 |
| 2025-01-06 20:01:24 | V3.0.3.12 |  | 新增 |

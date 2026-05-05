# sett_idempotent_jour - 清算幂等信息流水表

**表对象ID**: 510
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | original_transaction_str | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | app_name | 否 |  |  |
| 4 | remark | 否 |  |  |
| 5 | original_transaction_str | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | app_name | 否 |  |  |
| 8 | remark | 否 |  |  |
| 9 | original_transaction_str | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | app_name | 否 |  |  |
| 12 | remark | 否 |  |  |
| 13 | original_transaction_str | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | app_name | 否 |  |  |
| 16 | remark | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sett_idempotent_jour | ART | 是 | original_transaction_str, original_transaction_str |
| idx_sett_idempotent_jour | ART | 是 | original_transaction_str, original_transaction_str |
| idx_sett_idempotent_jour | ART | 是 | original_transaction_str, original_transaction_str |
| idx_sett_idempotent_jour | ART | 是 | original_transaction_str, original_transaction_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_sett_idempotent_jour | original_transaction_str, original_transaction_str |
| idx_sett_idempotent_jour | original_transaction_str, original_transaction_str |
| idx_sett_idempotent_jour | original_transaction_str, original_transaction_str |
| idx_sett_idempotent_jour | original_transaction_str, original_transaction_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-17 14:31:58 | 3.0.2.1 |  | 添加表 |
| 2026-03-17 14:31:58 | 3.0.2.1 |  |  |
| 2026-03-17 14:31:58 | 3.0.2.1 |  | 添加表 |
| 2026-03-17 14:31:58 | 3.0.2.1 |  |  |

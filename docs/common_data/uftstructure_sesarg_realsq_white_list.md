# realsq_white_list - 实时交收白名单表

**表对象ID**: 5014
**所属模块**: sesarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 22 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | registe_date | 否 |  |  |
| 5 | en_realsq_busin_type | 否 |  |  |
| 6 | white_real_rtgs_type | 否 |  |  |
| 7 | remark | 否 |  |  |
| 8 | update_date | 否 |  |  |
| 9 | update_time | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | position_str | 否 |  | fund_account(18)+white_real_rtgs_type(1) |
| 12 | client_id | 否 |  |  |
| 13 | branch_no | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | registe_date | 否 |  |  |
| 16 | en_realsq_busin_type | 否 |  |  |
| 17 | white_real_rtgs_type | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | update_date | 否 |  |  |
| 20 | update_time | 否 |  |  |
| 21 | transaction_no | 否 |  |  |
| 22 | position_str | 否 |  | fund_account(18)+white_real_rtgs_type(1) |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_realsq_white_list | 默认 | 否 |  |
| idx_realsq_white_list | ART | 是 | fund_account, white_real_rtgs_type, fund_account, white_real_rtgs_type |
| idx_realsq_white_list | 默认 | 否 |  |
| idx_realsq_white_list | ART | 是 | fund_account, white_real_rtgs_type, fund_account, white_real_rtgs_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_realsq_white_list | fund_account, white_real_rtgs_type, fund_account, white_real_rtgs_type |
| idx_realsq_white_list | fund_account, white_real_rtgs_type, fund_account, white_real_rtgs_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:23:02 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:16:50 | 3.0.2.84 | taocong45644 | 当前表realsq_white_list，修改了索引idx_realsq_white_list,索引字段修改为：(fun... |
| 2025-02-20 14:17:41 | 3.0.6.41 | 李想 | 新增表 |
| 2026-03-05 17:23:02 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:16:50 | 3.0.2.84 | taocong45644 | 当前表realsq_white_list，修改了索引idx_realsq_white_list,索引字段修改为：(fun... |
| 2025-02-20 14:17:41 | 3.0.6.41 | 李想 | 新增表 |

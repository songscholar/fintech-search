# bond_breach_info - 正回购客户违约信息

**表对象ID**: 5012
**所属模块**: sesarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 30 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | entrust_no | 否 |  |  |
| 2 | init_date | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | fine_balance | 否 |  |  |
| 6 | fine_balance_rate | 否 |  |  |
| 7 | adv_balance | 否 |  |  |
| 8 | adv_balance_rate | 否 |  |  |
| 9 | draw_prohibit_flag | 否 |  |  |
| 10 | create_date | 否 |  |  |
| 11 | exchange_type | 否 |  |  |
| 12 | update_date | 否 |  |  |
| 13 | update_time | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | position_str | 否 |  | entrust_no(10)+init_date(8)+fund_account(18)+exchange_type(4 |
| 16 | entrust_no | 否 |  |  |
| 17 | init_date | 否 |  |  |
| 18 | branch_no | 否 |  |  |
| 19 | fund_account | 否 |  |  |
| 20 | fine_balance | 否 |  |  |
| 21 | fine_balance_rate | 否 |  |  |
| 22 | adv_balance | 否 |  |  |
| 23 | adv_balance_rate | 否 |  |  |
| 24 | draw_prohibit_flag | 否 |  |  |
| 25 | create_date | 否 |  |  |
| 26 | exchange_type | 否 |  |  |
| 27 | update_date | 否 |  |  |
| 28 | update_time | 否 |  |  |
| 29 | transaction_no | 否 |  |  |
| 30 | position_str | 否 |  | entrust_no(10)+init_date(8)+fund_account(18)+exchange_type(4 |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bond_breach_info | 默认 | 否 |  |
| idx_bond_breach_info | ART | 是 | entrust_no, init_date, fund_account, exchange_type, entrust_no, init_date, fund_account, exchange_type |
| idx_bond_breach_info | 默认 | 否 |  |
| idx_bond_breach_info | ART | 是 | entrust_no, init_date, fund_account, exchange_type, entrust_no, init_date, fund_account, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bond_breach_info | entrust_no, init_date, fund_account, exchange_type, entrust_no, init_date, fund_account, exchange_type |
| idx_bond_breach_info | entrust_no, init_date, fund_account, exchange_type, entrust_no, init_date, fund_account, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:22:18 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:11:38 | 3.0.2.84 | taocong45644 | 当前表bond_breach_info，修改了索引idx_bond_breach_info,索引字段修改为：(entru... |
| 2025-02-20 14:06:17 | 3.0.6.39 | 李想 | 新增表 |
| 2026-03-05 17:22:18 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 16:11:38 | 3.0.2.84 | taocong45644 | 当前表bond_breach_info，修改了索引idx_bond_breach_info,索引字段修改为：(entru... |
| 2025-02-20 14:06:17 | 3.0.6.39 | 李想 | 新增表 |

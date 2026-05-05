# finexe_clarg - 融资行权客户个性参数表

**表对象ID**: 2630
**所属模块**: cbpsrp
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | sopt_code | 否 |  |  |
| 5 | compact_term | 否 |  |  |
| 6 | compact_rate | 否 |  |  |
| 7 | margin_draw_ratio | 否 |  |  |
| 8 | margin_focus_ratio | 否 |  |  |
| 9 | margin_alert_ratio | 否 |  |  |
| 10 | margin_treat_ratio | 否 |  |  |
| 11 | spread_ratio | 否 |  |  |
| 12 | is_auto_impawn | 否 |  |  |
| 13 | transaction_no | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | branch_no(6)+fund_account(18)+exchange_type(4)+sopt_code(8) |
| 17 | branch_no | 否 |  |  |
| 18 | fund_account | 否 |  |  |
| 19 | exchange_type | 否 |  |  |
| 20 | sopt_code | 否 |  |  |
| 21 | compact_term | 否 |  |  |
| 22 | compact_rate | 否 |  |  |
| 23 | margin_draw_ratio | 否 |  |  |
| 24 | margin_focus_ratio | 否 |  |  |
| 25 | margin_alert_ratio | 否 |  |  |
| 26 | margin_treat_ratio | 否 |  |  |
| 27 | spread_ratio | 否 |  |  |
| 28 | is_auto_impawn | 否 |  |  |
| 29 | transaction_no | 否 |  |  |
| 30 | update_date | 否 |  |  |
| 31 | update_time | 否 |  |  |
| 32 | position_str | 否 |  | branch_no(6)+fund_account(18)+exchange_type(4)+sopt_code(8) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_finexeclarg | ART | 是 | branch_no, fund_account, exchange_type, sopt_code, branch_no, fund_account, exchange_type, sopt_code |
| idx_finexeclarg | ART | 是 | branch_no, fund_account, exchange_type, sopt_code, branch_no, fund_account, exchange_type, sopt_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_finexeclarg | branch_no, fund_account, exchange_type, sopt_code, branch_no, fund_account, exchange_type, sopt_code |
| idx_finexeclarg | branch_no, fund_account, exchange_type, sopt_code, branch_no, fund_account, exchange_type, sopt_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-06 16:56:47 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 22:06:56 | 3.0.3.9 | 李想 | 物理表finexe_clarg，添加了表字段(update_date);
物理表finexe_clarg，添加了表字段... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:23:44 | 3.0.3.1 | wuxd | 新增 |
| 2026-03-06 16:56:47 | V3.0.2.79 | taocong45644 | 勾选回库使用索引 |
| 2025-02-19 22:06:56 | 3.0.3.9 | 李想 | 物理表finexe_clarg，添加了表字段(update_date);
物理表finexe_clarg，添加了表字段... |
| 2024-11-29 17:43:37 | 3.0.2.2 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.1 | 范文浩 | 补充物理表索引 |
| 2024-10-22 18:23:44 | 3.0.3.1 | wuxd | 新增 |

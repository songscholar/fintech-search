# settredo_afof_entrust - 清算重做基金盘后业务委托表

**表对象ID**: 5800
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | entrust_status | 否 |  |  |
| 3 | return_info | 否 |  |  |
| 4 | position_str | 否 |  | curr_date(8)+partition_no(2)+curr_milltime(9)+branch_no(5)+s |
| 5 | sett_batch_no | 否 |  |  |
| 6 | fund_account | 否 |  |  |
| 7 | entrust_status | 否 |  |  |
| 8 | return_info | 否 |  |  |
| 9 | position_str | 否 |  | curr_date(8)+partition_no(2)+curr_milltime(9)+branch_no(5)+s |
| 10 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settredo_entrust_pos | ART | 是 | sett_batch_no, fund_account, position_str, sett_batch_no, fund_account, position_str |
| idx_settredo_entrust_pos | ART | 是 | sett_batch_no, fund_account, position_str, sett_batch_no, fund_account, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settredo_entrust_pos | sett_batch_no, fund_account, position_str, sett_batch_no, fund_account, position_str |
| idx_settredo_entrust_pos | sett_batch_no, fund_account, position_str, sett_batch_no, fund_account, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:43:38 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 10:02:26 | 3.0.6.1018 | yangxz |  |
| 2026-03-09 14:43:38 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-07-24 10:02:26 | 3.0.6.1018 | yangxz |  |

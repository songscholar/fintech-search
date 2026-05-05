# secu_busi_jour - 交易业务控制信息流水表

**表对象ID**: 2546
**所属模块**: cbptrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | serial_no | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_account | 否 |  |  |
| 7 | stkholder_ctrlstr | 否 |  |  |
| 8 | position_str | 否 |  |  |
| 9 | remark | 否 |  |  |
| 10 | init_date | 否 |  |  |
| 11 | serial_no | 否 |  |  |
| 12 | branch_no | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | exchange_type | 否 |  |  |
| 15 | stock_account | 否 |  |  |
| 16 | stkholder_ctrlstr | 否 |  |  |
| 17 | position_str | 否 |  |  |
| 18 | remark | 否 |  |  |

## 索引（共 8 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secubuctjour | 默认 | 否 |  |
| idx_secubuctjour_acc | 默认 | 否 |  |
| idx_secubuctjour | ART | 是 | position_str, position_str |
| idx_secubuctjour_acc | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |
| idx_secubuctjour | 默认 | 否 |  |
| idx_secubuctjour_acc | 默认 | 否 |  |
| idx_secubuctjour | ART | 是 | position_str, position_str |
| idx_secubuctjour_acc | ART | 是 | fund_account, exchange_type, stock_account, fund_account, exchange_type, stock_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_secubuctjour | position_str, position_str |
| idx_secubuctjour | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-04 16:27:42 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:49:51 | 3.0.2.75 | taocong45644 | 当前表secu_busi_jour，修改了索引idx_secubuctjour,索引字段修改为：(position_st... |
| 2025-04-12 17:11:29 | 3.0.2.2002 | 高志强 | 新增 |
| 2026-03-04 16:27:42 | V3.0.2.78 | taocong45644 | 勾选回库使用索引 |
| 2025-12-01 13:49:51 | 3.0.2.75 | taocong45644 | 当前表secu_busi_jour，修改了索引idx_secubuctjour,索引字段修改为：(position_st... |
| 2025-04-12 17:11:29 | 3.0.2.2002 | 高志强 | 新增 |

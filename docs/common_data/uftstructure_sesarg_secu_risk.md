# secu_risk - 风险业务控制信息表

**表对象ID**: 5001
**所属模块**: sesarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 28 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | entrust_prop | 否 |  |  |
| 7 | res_entrust_way | 否 |  |  |
| 8 | begin_date | 否 |  |  |
| 9 | end_date | 否 |  |  |
| 10 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_code(8)+stock_type(4 |
| 11 | transaction_no | 否 |  |  |
| 12 | branch_no | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |
| 15 | init_date | 否 |  |  |
| 16 | fund_account | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | stock_type | 否 |  |  |
| 20 | entrust_prop | 否 |  |  |
| 21 | res_entrust_way | 否 |  |  |
| 22 | begin_date | 否 |  |  |
| 23 | end_date | 否 |  |  |
| 24 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_code(8)+stock_type(4 |
| 25 | transaction_no | 否 |  |  |
| 26 | branch_no | 否 |  |  |
| 27 | update_date | 否 |  |  |
| 28 | update_time | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secu_risk_code | 默认 | 否 | exchange_type, stock_code, exchange_type, stock_code |
| idx_secu_risk_code | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_secu_risk_position_str | ART | 是 | position_str, position_str |
| idx_secu_risk_code | 默认 | 否 | exchange_type, stock_code, exchange_type, stock_code |
| idx_secu_risk_code | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_secu_risk_position_str | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_secu_risk | position_str, position_str |
| idx_secu_risk_code | exchange_type, stock_code, exchange_type, stock_code |
| idx_secu_risk | position_str, position_str |
| idx_secu_risk_code | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-05 17:20:45 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-04-02 14:48:01 | 3.0.2.81 | 张训华 | 不勾选[不落redo文件] |
| 2025-07-17 15:19:13 | 3.0.6.48 | 常行 | 物理表secu_risk，增加索引(idx_secu_risk_code:[exchange_type,stock_co... |
| 2025-02-19 15:15:34 | 3.0.6.37 | 李想 | 物理表secu_risk，添加了表字段(branch_no);
物理表secu_risk，添加了表字段(update_... |
| 2024-08-03 13:33:02 | 3.0.2.14 | 程猛 | 新增表结构 |
| 2026-03-05 17:20:45 | V3.0.2.85 | taocong45644 | 勾选回库使用索引 |
| 2025-04-02 14:48:01 | 3.0.2.81 | 张训华 | 不勾选[不落redo文件] |
| 2025-07-17 15:19:13 | 3.0.6.48 | 常行 | 物理表secu_risk，增加索引(idx_secu_risk_code:[exchange_type,stock_co... |
| 2025-02-19 15:15:34 | 3.0.6.37 | 李想 | 物理表secu_risk，添加了表字段(branch_no);
物理表secu_risk，添加了表字段(update_... |
| 2024-08-03 13:33:02 | 3.0.2.14 | 程猛 | 新增表结构 |

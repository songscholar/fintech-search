# upbs_online_cust - 客户上线标志表

**表对象ID**: 149
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | en_system_str | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | transaction_str | 否 |  |  |
| 5 | client_id | 否 |  |  |
| 6 | en_system_str | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | transaction_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_online_cust | 默认 | 否 |  |
| idx_upbs_online_cust | ART | 是 | client_id, fund_account, client_id, fund_account |
| idx_upbs_online_cust | 默认 | 否 |  |
| idx_upbs_online_cust | ART | 是 | client_id, fund_account, client_id, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_online_cust | client_id, fund_account, client_id, fund_account |
| idx_upbs_online_cust | client_id, fund_account, client_id, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:36:18 | 3.0.2.103 | taocong45644 | 当前表upbs_online_cust，修改了索引idx_upbs_online_cust,索引字段修改为：(clien... |
| 2024-11-11 15:59:13 | V3.0.3.10 | wuxd | 物理表upbs_online_cust，添加了表字段(transaction_str);
 |
| 2025-12-01 15:36:18 | 3.0.2.103 | taocong45644 | 当前表upbs_online_cust，修改了索引idx_upbs_online_cust,索引字段修改为：(clien... |
| 2024-11-11 15:59:13 | V3.0.3.10 | wuxd | 物理表upbs_online_cust，添加了表字段(transaction_str);
 |

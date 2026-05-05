# stb_resstock - 受限账户持仓控制表

**表对象ID**: 5711
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | stock_code | 否 |  |  |
| 2 | stock_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | sub_risk_status | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | exchange_type | 否 |  |  |
| 9 | sub_risk_status | 否 |  |  |
| 10 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_stb_resstock | ART | 是 | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |
| idx_stb_resstock | ART | 是 | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_stb_resstock | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |
| idx_stb_resstock | stock_account, stock_code, exchange_type, stock_account, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:36:04 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-08-14 10:03:15 | 3.0.2.76 | 高志强 | 增加DB模式,避免写表失败 |
| 2024-06-18 10:27:04 | 3.0.2.21 | 吴威 | 物理表stb_resstock，添加了表字段(transaction_no);支持不回库
 |
| 2024-06-14 10:38:18 | 3.0.2.19 | 乐闽庭 | 物理表stb_resstock，删除了表字段(sysnode_id);
物理表stb_resstock，删除索引字段(... |
| 2026-03-09 14:36:04 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-08-14 10:03:15 | 3.0.2.76 | 高志强 | 增加DB模式,避免写表失败 |
| 2024-06-18 10:27:04 | 3.0.2.21 | 吴威 | 物理表stb_resstock，添加了表字段(transaction_no);支持不回库
 |
| 2024-06-14 10:38:18 | 3.0.2.19 | 乐闽庭 | 物理表stb_resstock，删除了表字段(sysnode_id);
物理表stb_resstock，删除索引字段(... |

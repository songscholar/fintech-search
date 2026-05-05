# ofgradectrl - 分级基金控制表

**表对象ID**: 328
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | ofgrade_flag | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | ofgrade_flag | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ofgradectrl | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |
| idx_ofgradectrl | ART | 是 | exchange_type, stock_code, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ofgradectrl | exchange_type, stock_code, exchange_type, stock_code |
| idx_ofgradectrl | exchange_type, stock_code, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-26 19:40:33 | 3.0.3.14 | 张明月 | 物理表ofgradectrl，添加了表字段(transaction_no);
 |
| 2024-09-23 16:07:31 | 3.0.2.15 | 张明月 | 新增 |
| 2024-09-26 19:40:33 | 3.0.3.14 | 张明月 | 物理表ofgradectrl，添加了表字段(transaction_no);
 |
| 2024-09-23 16:07:31 | 3.0.2.15 | 张明月 | 新增 |

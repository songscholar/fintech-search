# exchange_rates - 汇率表

**表对象ID**: 108
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | money_type | 否 |  |  |
| 2 | dest_money_type | 否 |  |  |
| 3 | bill_rate | 否 |  |  |
| 4 | exchangerate_prec | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | money_type | 否 |  |  |
| 7 | dest_money_type | 否 |  |  |
| 8 | bill_rate | 否 |  |  |
| 9 | exchangerate_prec | 否 |  |  |
| 10 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_exchange_rate | ART | 是 | money_type, dest_money_type, money_type, dest_money_type |
| idx_exchange_rate | ART | 是 | money_type, dest_money_type, money_type, dest_money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_exchange_rate | money_type, dest_money_type, money_type, dest_money_type |
| idx_exchange_rate | money_type, dest_money_type, money_type, dest_money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-06-24 09:42:01 | 3.0.2.15 | 吴威 | 物理表exchange_rates，添加了表字段(transaction_no);
 |
| 2024-06-21 15:40:02 | 3.0.2.13 | 祝丁恺 | 物理表exchange_rates，添加了表字段(exchangerate_prec);
 |
| 2024-04-23 10:37:26 | 3.0.2.6 | 泮新国 | 增加汇率表 |
| 2024-06-24 09:42:01 | 3.0.2.15 | 吴威 | 物理表exchange_rates，添加了表字段(transaction_no);
 |
| 2024-06-21 15:40:02 | 3.0.2.13 | 祝丁恺 | 物理表exchange_rates，添加了表字段(exchangerate_prec);
 |
| 2024-04-23 10:37:26 | 3.0.2.6 | 泮新国 | 增加汇率表 |

# setttouftsrprate - 清算股票质押质押比例表

**表对象ID**: 3099
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | stock_code | 是 |  |  |
| 3 | impawn_rate | 是 |  |  |
| 4 | modify_date | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_code | 是 |  |  |
| 7 | impawn_rate | 是 |  |  |
| 8 | modify_date | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settsrprate | 默认 | 否 | exchange_type, stock_code, exchange_type, stock_code |
| idx_settsrprate | 默认 | 否 | exchange_type, stock_code, exchange_type, stock_code |

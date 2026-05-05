# uref_std_lender - 转融通合格出借人表

**表对象ID**: 6003
**所属模块**: refarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_account | 否 |  |  |
| 4 | seat_no | 否 |  |  |
| 5 | init_date | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | seat_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_refstdlender | ART | 是 | exchange_type, stock_account, seat_no, exchange_type, stock_account, seat_no |
| idx_refstdlender | ART | 是 | exchange_type, stock_account, seat_no, exchange_type, stock_account, seat_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_refstdlender | exchange_type, stock_account, seat_no, exchange_type, stock_account, seat_no |
| idx_refstdlender | exchange_type, stock_account, seat_no, exchange_type, stock_account, seat_no |

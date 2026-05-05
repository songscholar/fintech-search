# uses_deal_enable_total - 清算资金预冻结信息中间表

**表对象ID**: 3305
**所属模块**: settsync
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | money_type | 是 |  |  |
| 4 | clear_balance | 是 |  |  |
| 5 | flow_count | 是 |  |  |
| 6 | init_date | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | money_type | 是 |  |  |
| 9 | clear_balance | 是 |  |  |
| 10 | flow_count | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usesdealenabletotal | 默认 | 是 | init_date, fund_account, money_type, flow_count, init_date, fund_account, money_type, flow_count |
| idx_usesdealenabletotal | 默认 | 是 | init_date, fund_account, money_type, flow_count, init_date, fund_account, money_type, flow_count |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usesdealenabletotal | init_date, fund_account, money_type, flow_count, init_date, fund_account, money_type, flow_count |
| idx_usesdealenabletotal | init_date, fund_account, money_type, flow_count, init_date, fund_account, money_type, flow_count |

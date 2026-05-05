# setttoufthkvotestock - 清算港股投票份额表

**表对象ID**: 3004
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | stock_code | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | current_amount | 是 |  |  |
| 8 | date_clear | 是 |  |  |
| 9 | position_str | 是 |  |  |
| 10 | remark | 是 |  |  |
| 11 | init_date | 是 |  |  |
| 12 | branch_no | 是 |  |  |
| 13 | exchange_type | 是 |  |  |
| 14 | stock_code | 是 |  |  |
| 15 | fund_account | 是 |  |  |
| 16 | stock_account | 是 |  |  |
| 17 | current_amount | 是 |  |  |
| 18 | date_clear | 是 |  |  |
| 19 | position_str | 是 |  |  |
| 20 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_hkvotestock | 默认 | 是 | position_str, position_str |
| idx_hkvotestock | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_hkvotestock | position_str, position_str |
| idx_hkvotestock | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-06-28 14:53 | 8.26.1.14 | 曾哲 | 新增 |
| 2018-06-28 14:53 | 8.26.1.14 | 曾哲 | 新增 |

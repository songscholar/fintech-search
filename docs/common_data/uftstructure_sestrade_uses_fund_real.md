# uses_fund_real - 证券交易资金表

**表对象ID**: 5507
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 42 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | money_type | 是 |  |  |
| 4 | asset_prop | 是 |  |  |
| 5 | current_balance | 是 |  |  |
| 6 | enable_balance | 是 |  |  |
| 7 | cash_balance | 是 |  |  |
| 8 | check_balance | 是 |  |  |
| 9 | frozen_balance | 是 |  |  |
| 10 | unfrozen_balance | 是 |  |  |
| 11 | entrust_buy_balance | 是 |  |  |
| 12 | real_buy_balance | 是 |  |  |
| 13 | real_sell_balance | 是 |  |  |
| 14 | uncome_buy_balance | 是 |  |  |
| 15 | uncome_sell_balance | 是 |  |  |
| 16 | uncome_correct_balance | 是 |  |  |
| 17 | correct_balance | 是 |  |  |
| 18 | foregift_balance | 是 |  |  |
| 19 | mortgage_balance | 是 |  |  |
| 20 | partition_no | 是 |  |  |
| 21 | branch_no | 是 |  |  |
| 22 | client_id | 是 |  |  |
| 23 | fund_account | 是 |  |  |
| 24 | money_type | 是 |  |  |
| 25 | asset_prop | 是 |  |  |
| 26 | current_balance | 是 |  |  |
| 27 | enable_balance | 是 |  |  |
| 28 | cash_balance | 是 |  |  |
| 29 | check_balance | 是 |  |  |
| 30 | frozen_balance | 是 |  |  |
| 31 | unfrozen_balance | 是 |  |  |
| 32 | entrust_buy_balance | 是 |  |  |
| 33 | real_buy_balance | 是 |  |  |
| 34 | real_sell_balance | 是 |  |  |
| 35 | uncome_buy_balance | 是 |  |  |
| 36 | uncome_sell_balance | 是 |  |  |
| 37 | uncome_correct_balance | 是 |  |  |
| 38 | correct_balance | 是 |  |  |
| 39 | foregift_balance | 是 |  |  |
| 40 | mortgage_balance | 是 |  |  |
| 41 | partition_no | 是 |  |  |
| 42 | branch_no | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uft_secu_fund_real | ART | 是 | fund_account, money_type, fund_account, money_type |
| idx_uft_secu_fund_real | ART | 是 | fund_account, money_type, fund_account, money_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uft_secu_fund_real | fund_account, money_type, fund_account, money_type |
| idx_uft_secu_fund_real | fund_account, money_type, fund_account, money_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-05-14 10:44:08 | 3.0.2.67 | 於达 | 物理表uses_fund_real，添加了表字段(branch_no);
 |
| 2024-04-28 16:58:57 | 3.0.2.3 | 阮善宏 | 物理表uses_fund_real，添加了表字段(partition_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 14:23 | 0.0.0.7 | 程猛 | 删除表字段order_no |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2025-05-14 10:44:08 | 3.0.2.67 | 於达 | 物理表uses_fund_real，添加了表字段(branch_no);
 |
| 2024-04-28 16:58:57 | 3.0.2.3 | 阮善宏 | 物理表uses_fund_real，添加了表字段(partition_no);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 14:23 | 0.0.0.7 | 程猛 | 删除表字段order_no |

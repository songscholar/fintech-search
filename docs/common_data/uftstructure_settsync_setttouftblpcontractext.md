# setttouftblpcontractext - 清算债券借贷合约扩展表

**表对象ID**: 3011
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | branch_no | 是 |  |  |
| 3 | fund_account | 是 |  |  |
| 4 | stock_account | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_code | 是 |  |  |
| 7 | stock_type | 是 |  |  |
| 8 | cbpcontract_id | 是 |  |  |
| 9 | impawn_amount | 是 |  |  |
| 10 | exch_in_amount | 是 |  |  |
| 11 | exch_out_amount | 是 |  |  |
| 12 | fruits | 是 |  |  |
| 13 | exch_out_fruits | 是 |  |  |
| 14 | use_date | 是 |  |  |
| 15 | stock_property | 是 |  |  |
| 16 | uft_data_change_status | 是 |  |  |
| 17 | init_date | 是 |  |  |
| 18 | branch_no | 是 |  |  |
| 19 | fund_account | 是 |  |  |
| 20 | stock_account | 是 |  |  |
| 21 | exchange_type | 是 |  |  |
| 22 | stock_code | 是 |  |  |
| 23 | stock_type | 是 |  |  |
| 24 | cbpcontract_id | 是 |  |  |
| 25 | impawn_amount | 是 |  |  |
| 26 | exch_in_amount | 是 |  |  |
| 27 | exch_out_amount | 是 |  |  |
| 28 | fruits | 是 |  |  |
| 29 | exch_out_fruits | 是 |  |  |
| 30 | use_date | 是 |  |  |
| 31 | stock_property | 是 |  |  |
| 32 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settblpcontractext_cid | 默认 | 是 | cbpcontract_id, exchange_type, stock_code, stock_property, cbpcontract_id, exchange_type, stock_code, stock_property |
| idx_settblpcontractext_acct | 默认 | 是 | fund_account, fund_account |
| idx_settblpcontractext_cid | 默认 | 是 | cbpcontract_id, exchange_type, stock_code, stock_property, cbpcontract_id, exchange_type, stock_code, stock_property |
| idx_settblpcontractext_acct | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settblpcontractext_cid | cbpcontract_id, exchange_type, stock_property, cbpcontract_id, exchange_type, stock_property |
| idx_settblpcontractext_cid | cbpcontract_id, exchange_type, stock_property, cbpcontract_id, exchange_type, stock_property |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-11-09 09:39 | 8.26.2.11 | 杨念 | 增加表字段uft_data_change_status;调整分级索引idx_settblpcontractext_cid... |
| 2021-11-02 18:57 | 8.26.2.10 | 张军 | 新增 |
| 2021-11-09 09:39 | 8.26.2.11 | 杨念 | 增加表字段uft_data_change_status;调整分级索引idx_settblpcontractext_cid... |
| 2021-11-02 18:57 | 8.26.2.10 | 张军 | 新增 |

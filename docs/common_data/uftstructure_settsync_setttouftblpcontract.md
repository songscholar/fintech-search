# setttouftblpcontract - 清算债券借贷合约表

**表对象ID**: 3010
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 90 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 是 |  |  |
| 2 | cbpcontract_id | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | client_id | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | exchange_type | 是 |  |  |
| 8 | stock_code | 是 |  |  |
| 9 | stock_type | 是 |  |  |
| 10 | entrust_bs | 是 |  |  |
| 11 | entrust_date | 是 |  |  |
| 12 | entrust_balance | 是 |  |  |
| 13 | entrust_amount | 是 |  |  |
| 14 | real_back_balance | 是 |  |  |
| 15 | back_balance | 是 |  |  |
| 16 | real_back_amount | 是 |  |  |
| 17 | back_amount | 是 |  |  |
| 18 | real_date_back | 是 |  |  |
| 19 | date_back | 是 |  |  |
| 20 | real_year_rate | 是 |  |  |
| 21 | expire_year_rate | 是 |  |  |
| 22 | orig_report_id | 是 |  |  |
| 23 | blp_contract_status | 是 |  |  |
| 24 | date_clear | 是 |  |  |
| 25 | remark | 是 |  |  |
| 26 | oppo_agency | 是 |  |  |
| 27 | oppo_agency_name | 是 |  |  |
| 28 | oppo_trader_id | 是 |  |  |
| 29 | oppo_bond_investor_type | 是 |  |  |
| 30 | oppo_bond_investor_id | 是 |  |  |
| 31 | oppo_brp_investor_name | 是 |  |  |
| 32 | prop_seat_no | 是 |  |  |
| 33 | agency_no | 是 |  |  |
| 34 | trader_id | 是 |  |  |
| 35 | bond_investor_type | 是 |  |  |
| 36 | bond_investor_id | 是 |  |  |
| 37 | brp_investor_name | 是 |  |  |
| 38 | blp_contract_type | 是 |  |  |
| 39 | join_contract_id | 是 |  |  |
| 40 | blp_source_type | 是 |  |  |
| 41 | fruits | 是 |  |  |
| 42 | exch_out_fruits | 是 |  |  |
| 43 | fair_price | 是 |  |  |
| 44 | grace_days | 是 |  |  |
| 45 | uft_data_change_status | 是 |  |  |
| 46 | init_date | 是 |  |  |
| 47 | cbpcontract_id | 是 |  |  |
| 48 | branch_no | 是 |  |  |
| 49 | fund_account | 是 |  |  |
| 50 | client_id | 是 |  |  |
| 51 | stock_account | 是 |  |  |
| 52 | exchange_type | 是 |  |  |
| 53 | stock_code | 是 |  |  |
| 54 | stock_type | 是 |  |  |
| 55 | entrust_bs | 是 |  |  |
| 56 | entrust_date | 是 |  |  |
| 57 | entrust_balance | 是 |  |  |
| 58 | entrust_amount | 是 |  |  |
| 59 | real_back_balance | 是 |  |  |
| 60 | back_balance | 是 |  |  |
| 61 | real_back_amount | 是 |  |  |
| 62 | back_amount | 是 |  |  |
| 63 | real_date_back | 是 |  |  |
| 64 | date_back | 是 |  |  |
| 65 | real_year_rate | 是 |  |  |
| 66 | expire_year_rate | 是 |  |  |
| 67 | orig_report_id | 是 |  |  |
| 68 | blp_contract_status | 是 |  |  |
| 69 | date_clear | 是 |  |  |
| 70 | remark | 是 |  |  |
| 71 | oppo_agency | 是 |  |  |
| 72 | oppo_agency_name | 是 |  |  |
| 73 | oppo_trader_id | 是 |  |  |
| 74 | oppo_bond_investor_type | 是 |  |  |
| 75 | oppo_bond_investor_id | 是 |  |  |
| 76 | oppo_brp_investor_name | 是 |  |  |
| 77 | prop_seat_no | 是 |  |  |
| 78 | agency_no | 是 |  |  |
| 79 | trader_id | 是 |  |  |
| 80 | bond_investor_type | 是 |  |  |
| 81 | bond_investor_id | 是 |  |  |
| 82 | brp_investor_name | 是 |  |  |
| 83 | blp_contract_type | 是 |  |  |
| 84 | join_contract_id | 是 |  |  |
| 85 | blp_source_type | 是 |  |  |
| 86 | fruits | 是 |  |  |
| 87 | exch_out_fruits | 是 |  |  |
| 88 | fair_price | 是 |  |  |
| 89 | grace_days | 是 |  |  |
| 90 | uft_data_change_status | 是 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settblpcontract_cid | 默认 | 是 | cbpcontract_id, cbpcontract_id |
| idx_settblpcontract_acct | 默认 | 是 | fund_account, fund_account |
| idx_settblpcontract_report | 默认 | 是 | orig_report_id, orig_report_id |
| idx_settblpcontract_cid | 默认 | 是 | cbpcontract_id, cbpcontract_id |
| idx_settblpcontract_acct | 默认 | 是 | fund_account, fund_account |
| idx_settblpcontract_report | 默认 | 是 | orig_report_id, orig_report_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settblpcontract_cid | cbpcontract_id, cbpcontract_id |
| idx_settblpcontract_cid | cbpcontract_id, cbpcontract_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-11-09 15:22 | 8.26.2.11 | 杨念 | 增加表字段uft_data_change_status |
| 2021-11-02 18:57 | 8.26.2.10 | 张军 | 新增 |
| 2021-11-09 15:22 | 8.26.2.11 | 杨念 | 增加表字段uft_data_change_status |
| 2021-11-02 18:57 | 8.26.2.10 | 张军 | 新增 |

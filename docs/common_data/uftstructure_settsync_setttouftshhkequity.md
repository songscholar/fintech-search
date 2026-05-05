# setttouftshhkequity - 清算沪港通权益信息表

**表对象ID**: 3054
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_id | 是 |  |  |
| 2 | init_date | 是 |  |  |
| 3 | branch_no | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | exchange_type | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | stock_code | 是 |  |  |
| 8 | entrust_amount | 是 |  |  |
| 9 | hkdc_circulate_type | 是 |  |  |
| 10 | hkdc_authority_type | 是 |  |  |
| 11 | hkdc_authority_times | 是 |  |  |
| 12 | hkdc_market_year | 是 |  |  |
| 13 | seat_no | 是 |  |  |
| 14 | frozen_amount | 是 |  |  |
| 15 | position_str | 是 |  |  |
| 16 | uft_data_change_status | 是 |  |  |
| 17 | sett_id | 是 |  |  |
| 18 | init_date | 是 |  |  |
| 19 | branch_no | 是 |  |  |
| 20 | fund_account | 是 |  |  |
| 21 | exchange_type | 是 |  |  |
| 22 | stock_account | 是 |  |  |
| 23 | stock_code | 是 |  |  |
| 24 | entrust_amount | 是 |  |  |
| 25 | hkdc_circulate_type | 是 |  |  |
| 26 | hkdc_authority_type | 是 |  |  |
| 27 | hkdc_authority_times | 是 |  |  |
| 28 | hkdc_market_year | 是 |  |  |
| 29 | seat_no | 是 |  |  |
| 30 | frozen_amount | 是 |  |  |
| 31 | position_str | 是 |  |  |
| 32 | uft_data_change_status | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settshhkequity | 默认 | 是 | fund_account, stock_code, fund_account, stock_code |
| idx_settshhkequity_pos | 默认 | 是 | position_str, position_str |
| idx_settshhkequity | 默认 | 是 | fund_account, stock_code, fund_account, stock_code |
| idx_settshhkequity_pos | 默认 | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_shhkequity | fund_account, stock_code, fund_account, stock_code |
| idx_shhkequity | fund_account, stock_code, fund_account, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2022-11-03 10:04 | 8.26.2.40 | 徐世晗 | 新增 |
| 2022-11-03 10:04 | 8.26.2.40 | 徐世晗 | 新增 |

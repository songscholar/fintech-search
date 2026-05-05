# adviser_contract - 投顾产品签约信息

**表对象ID**: 322
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | adproduct_id | 否 |  |  |
| 3 | sign_date | 否 |  |  |
| 4 | unsign_date | 否 |  |  |
| 5 | position_str | 否 |  |  |
| 6 | follow_sell_rate | 否 |  |  |
| 7 | period_sell_rate | 否 |  |  |
| 8 | sign_time | 否 |  |  |
| 9 | unsign_time | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | en_stock_code | 否 |  |  |
| 12 | busiwhite_flag | 否 |  |  |
| 13 | busiwhite_transout_date | 否 |  |  |
| 14 | busiwhite_transout_time | 否 |  |  |
| 15 | busiwhite_transin_date | 否 |  |  |
| 16 | busiwhite_transin_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | remark | 否 |  |  |
| 19 | client_id | 否 |  |  |
| 20 | adproduct_id | 否 |  |  |
| 21 | sign_date | 否 |  |  |
| 22 | unsign_date | 否 |  |  |
| 23 | position_str | 否 |  |  |
| 24 | follow_sell_rate | 否 |  |  |
| 25 | period_sell_rate | 否 |  |  |
| 26 | sign_time | 否 |  |  |
| 27 | unsign_time | 否 |  |  |
| 28 | fund_account | 否 |  |  |
| 29 | en_stock_code | 否 |  |  |
| 30 | busiwhite_flag | 否 |  |  |
| 31 | busiwhite_transout_date | 否 |  |  |
| 32 | busiwhite_transout_time | 否 |  |  |
| 33 | busiwhite_transin_date | 否 |  |  |
| 34 | busiwhite_transin_time | 否 |  |  |
| 35 | transaction_no | 否 |  |  |
| 36 | remark | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_advcontract_id | ART | 是 | client_id, adproduct_id, fund_account, client_id, adproduct_id, fund_account |
| idx_advcontract_pos | ART | 是 | position_str, position_str |
| idx_advcontract_id | ART | 是 | client_id, adproduct_id, fund_account, client_id, adproduct_id, fund_account |
| idx_advcontract_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_advcontract_id | client_id, adproduct_id, fund_account, client_id, adproduct_id, fund_account |
| idx_advcontract_pos | position_str, position_str |
| idx_advcontract_id | client_id, adproduct_id, fund_account, client_id, adproduct_id, fund_account |
| idx_advcontract_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-10-06 09:41:11 | 3.0.2.31 | 李海洋 | 变长字段顺序调整，修复插入记录乱码问题 |
| 2024-09-24 13:27:40 | 3.0.2.29 | 范文浩 | 物理表adv_contract，添加了表字段(client_id);
物理表adv_contract，添加了表字段(a... |
| 2024-10-06 09:41:11 | 3.0.2.31 | 李海洋 | 变长字段顺序调整，修复插入记录乱码问题 |
| 2024-09-24 13:27:40 | 3.0.2.29 | 范文浩 | 物理表adv_contract，添加了表字段(client_id);
物理表adv_contract，添加了表字段(a... |

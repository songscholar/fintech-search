# setttouftriskcrdtlist - 清算客户信用记录表

**表对象ID**: 3070
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 46 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 是 |  |  |
| 2 | id_kind | 是 |  |  |
| 3 | id_no | 是 |  |  |
| 4 | seat_no | 是 |  |  |
| 5 | company_name | 是 |  |  |
| 6 | branch_no | 是 |  |  |
| 7 | fund_account | 是 |  |  |
| 8 | client_id | 是 |  |  |
| 9 | client_name | 是 |  |  |
| 10 | stock_account_sh | 是 |  |  |
| 11 | stock_account_sz | 是 |  |  |
| 12 | fine_balance | 是 |  |  |
| 13 | crdtfine_type | 是 |  |  |
| 14 | crdtlist_flag | 是 |  |  |
| 15 | crdtsrc_type | 是 |  |  |
| 16 | create_date | 是 |  |  |
| 17 | remark | 是 |  |  |
| 18 | compact_id_str | 是 |  |  |
| 19 | crdtfine_no | 是 |  |  |
| 20 | risk_begindate | 是 |  |  |
| 21 | sett_id | 是 |  |  |
| 22 | uft_data_change_status | 是 |  |  |
| 23 | stock_account_stb | 是 |  |  |
| 24 | company_no | 是 |  |  |
| 25 | id_kind | 是 |  |  |
| 26 | id_no | 是 |  |  |
| 27 | seat_no | 是 |  |  |
| 28 | company_name | 是 |  |  |
| 29 | branch_no | 是 |  |  |
| 30 | fund_account | 是 |  |  |
| 31 | client_id | 是 |  |  |
| 32 | client_name | 是 |  |  |
| 33 | stock_account_sh | 是 |  |  |
| 34 | stock_account_sz | 是 |  |  |
| 35 | fine_balance | 是 |  |  |
| 36 | crdtfine_type | 是 |  |  |
| 37 | crdtlist_flag | 是 |  |  |
| 38 | crdtsrc_type | 是 |  |  |
| 39 | create_date | 是 |  |  |
| 40 | remark | 是 |  |  |
| 41 | compact_id_str | 是 |  |  |
| 42 | crdtfine_no | 是 |  |  |
| 43 | risk_begindate | 是 |  |  |
| 44 | sett_id | 是 |  |  |
| 45 | uft_data_change_status | 是 |  |  |
| 46 | stock_account_stb | 是 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settriskcrdtlist | 默认 | 是 | id_no, id_kind, crdtfine_type, crdtfine_no, create_date, risk_begindate, fund_account, crdtlist_flag, id_no, id_kind, crdtfine_type, crdtfine_no, create_date, risk_begindate, fund_account, crdtlist_flag |
| idx_settriskcrdtlist_fund | 默认 | 是 | create_date, fund_account, create_date, fund_account |
| idx_settriskcrdtlist | 默认 | 是 | id_no, id_kind, crdtfine_type, crdtfine_no, create_date, risk_begindate, fund_account, crdtlist_flag, id_no, id_kind, crdtfine_type, crdtfine_no, create_date, risk_begindate, fund_account, crdtlist_flag |
| idx_settriskcrdtlist_fund | 默认 | 是 | create_date, fund_account, create_date, fund_account |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_riskcrdtlist | create_date, id_no, id_kind, crdtfine_type, crdtfine_no, risk_begindate, crdtlist_flag, create_date, id_no, id_kind, crdtfine_type, crdtfine_no, risk_begindate, crdtlist_flag |
| idx_riskcrdtlist_acct | fund_account, fund_account |
| idx_riskcrdtlist | create_date, id_no, id_kind, crdtfine_type, crdtfine_no, risk_begindate, crdtlist_flag, create_date, id_no, id_kind, crdtfine_type, crdtfine_no, risk_begindate, crdtlist_flag |
| idx_riskcrdtlist_acct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-10-15 16:16 | 8.26.2.11 | 张军 | 索引字段新增fund_account |
| 2021-05-17 11:22 | 8.26.1.95 | 何强 | 修改idx_settriskcrdtlist分级索引字段的顺序，增加idx_settriskcrdtlist_fund索... |
| 2020-10-29 15:58 | 8.26.1.78 | 宋瑞 | 添加stock_account_stb字段 |
| 2018-08-10 09:28 | 8.26.1.31 | 林忠芝 | 新增 |
| 2018-05-11 14:50 | 8.26.1.20 | 林忠芝 | 新增 |
| 2021-10-15 16:16 | 8.26.2.11 | 张军 | 索引字段新增fund_account |
| 2021-05-17 11:22 | 8.26.1.95 | 何强 | 修改idx_settriskcrdtlist分级索引字段的顺序，增加idx_settriskcrdtlist_fund索... |
| 2020-10-29 15:58 | 8.26.1.78 | 宋瑞 | 添加stock_account_stb字段 |
| 2018-08-10 09:28 | 8.26.1.31 | 林忠芝 | 新增 |
| 2018-05-11 14:50 | 8.26.1.20 | 林忠芝 | 新增 |

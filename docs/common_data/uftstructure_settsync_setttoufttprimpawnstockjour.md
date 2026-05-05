# setttoufttprimpawnstockjour - 清算三方回购质押券信息流水表

**表对象ID**: 3006
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sett_id | 是 |  |  |
| 2 | init_date | 是 |  |  |
| 3 | settserial_no | 是 |  |  |
| 4 | branch_no | 是 |  |  |
| 5 | client_id | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | exchange_type | 是 |  |  |
| 8 | stock_account | 是 |  |  |
| 9 | stock_code | 是 |  |  |
| 10 | basket_id | 是 |  |  |
| 11 | bond_end_date | 是 |  |  |
| 12 | store_amount | 是 |  |  |
| 13 | reg_impawn_amount | 是 |  |  |
| 14 | pre_out_amount | 是 |  |  |
| 15 | used_amount | 是 |  |  |
| 16 | fruits | 是 |  |  |
| 17 | remark | 是 |  |  |
| 18 | position_str | 是 |  |  |
| 19 | sett_id | 是 |  |  |
| 20 | init_date | 是 |  |  |
| 21 | settserial_no | 是 |  |  |
| 22 | branch_no | 是 |  |  |
| 23 | client_id | 是 |  |  |
| 24 | fund_account | 是 |  |  |
| 25 | exchange_type | 是 |  |  |
| 26 | stock_account | 是 |  |  |
| 27 | stock_code | 是 |  |  |
| 28 | basket_id | 是 |  |  |
| 29 | bond_end_date | 是 |  |  |
| 30 | store_amount | 是 |  |  |
| 31 | reg_impawn_amount | 是 |  |  |
| 32 | pre_out_amount | 是 |  |  |
| 33 | used_amount | 是 |  |  |
| 34 | fruits | 是 |  |  |
| 35 | remark | 是 |  |  |
| 36 | position_str | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_tprimpawnstockjour | 默认 | 是 | settserial_no, init_date, settserial_no, init_date |
| idx_tprimpawnstockjour | 默认 | 是 | settserial_no, init_date, settserial_no, init_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_tprimpawnstockjour | settserial_no, init_date, settserial_no, init_date |
| idx_tprimpawnstockjour | settserial_no, init_date, settserial_no, init_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-09-21 10:15 | 8.26.1.22 | 俞亚君 | 新增 |
| 2018-09-21 10:15 | 8.26.1.22 | 俞亚君 | 新增 |

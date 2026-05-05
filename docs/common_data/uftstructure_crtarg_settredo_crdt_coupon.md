# settredo_crdt_coupon - 日终清算融资融券优惠券表

**表对象ID**: 7127
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | end_date | 否 |  |  |
| 3 | begin_date | 否 |  |  |
| 4 | money_type | 否 |  |  |
| 5 | perfer_no | 否 |  |  |
| 6 | sett_batch_no | 否 |  |  |
| 7 | sett_dml_type | 否 |  |  |
| 8 | coupon_status | 否 |  |  |
| 9 | date_clear | 否 |  |  |
| 10 | prefer_balance | 否 |  |  |
| 11 | update_date | 否 |  |  |
| 12 | update_time | 否 |  |  |
| 13 | fund_account | 否 |  |  |
| 14 | end_date | 否 |  |  |
| 15 | begin_date | 否 |  |  |
| 16 | money_type | 否 |  |  |
| 17 | perfer_no | 否 |  |  |
| 18 | sett_batch_no | 否 |  |  |
| 19 | sett_dml_type | 否 |  |  |
| 20 | coupon_status | 否 |  |  |
| 21 | date_clear | 否 |  |  |
| 22 | prefer_balance | 否 |  |  |
| 23 | update_date | 否 |  |  |
| 24 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| strd_idx_crdtcoupon | ART | 是 | fund_account, end_date, begin_date, money_type, perfer_no, fund_account, end_date, begin_date, money_type, perfer_no |
| strd_idx_crdtcoupon | ART | 是 | fund_account, end_date, begin_date, money_type, perfer_no, fund_account, end_date, begin_date, money_type, perfer_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| strd_idx_crdtcoupon | fund_account, end_date, begin_date, money_type, perfer_no, fund_account, end_date, begin_date, money_type, perfer_no |
| strd_idx_crdtcoupon | fund_account, end_date, begin_date, money_type, perfer_no, fund_account, end_date, begin_date, money_type, perfer_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-16 19:02:30 | 3.0.6.1066 | 周兆军 | 表空间调整为HS_UFT_DATA |
| 2025-05-06 20:33:58 | 3.0.6.109 | 常行 | 新增表 |
| 2025-09-16 19:02:30 | 3.0.6.1066 | 周兆军 | 表空间调整为HS_UFT_DATA |
| 2025-05-06 20:33:58 | 3.0.6.109 | 常行 | 新增表 |

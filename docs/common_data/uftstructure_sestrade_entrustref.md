# entrustref - 委托引用表

**表对象ID**: 5732
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | sendercomp_id | 否 |  |  |
| 4 | ext_order_id | 否 |  |  |
| 5 | orig_ext_order_id | 否 |  |  |
| 6 | entrust_no | 否 |  |  |
| 7 | op_entrust_way | 否 |  |  |
| 8 | report_no | 否 |  |  |
| 9 | resp_error_no | 否 |  |  |
| 10 | fix_direct_no | 否 |  |  |
| 11 | init_date | 否 |  |  |
| 12 | fund_account | 否 |  |  |
| 13 | sendercomp_id | 否 |  |  |
| 14 | ext_order_id | 否 |  |  |
| 15 | orig_ext_order_id | 否 |  |  |
| 16 | entrust_no | 否 |  |  |
| 17 | op_entrust_way | 否 |  |  |
| 18 | report_no | 否 |  |  |
| 19 | resp_error_no | 否 |  |  |
| 20 | fix_direct_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_entrustref | ART | 是 | fund_account, sendercomp_id, ext_order_id, fund_account, sendercomp_id, ext_order_id |
| idx_entrustref_rept | ART | 是 | fund_account, entrust_no, report_no, fund_account, entrust_no, report_no |
| idx_entrustref_dir | ART | 是 | fund_account, fix_direct_no, fund_account, fix_direct_no |
| idx_entrustref | ART | 是 | fund_account, sendercomp_id, ext_order_id, fund_account, sendercomp_id, ext_order_id |
| idx_entrustref_rept | ART | 是 | fund_account, entrust_no, report_no, fund_account, entrust_no, report_no |
| idx_entrustref_dir | ART | 是 | fund_account, fix_direct_no, fund_account, fix_direct_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_entrustref | fund_account, sendercomp_id, ext_order_id, fund_account, sendercomp_id, ext_order_id |
| idx_entrustref | fund_account, sendercomp_id, ext_order_id, fund_account, sendercomp_id, ext_order_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:38:59 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2026-03-09 14:38:59 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |

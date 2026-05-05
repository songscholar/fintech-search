# uopt_nearfinalmarmodel - 期权临近到期保证金浮动比例模板

**表对象ID**: 9035
**所属模块**: optsms
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | near_final_ratio_kind | 否 |  |  |
| 2 | near_final_days1 | 否 |  |  |
| 3 | near_final_ratio1 | 否 |  |  |
| 4 | near_final_days2 | 否 |  |  |
| 5 | near_final_ratio2 | 否 |  |  |
| 6 | near_final_days3 | 否 |  |  |
| 7 | near_final_ratio3 | 否 |  |  |
| 8 | near_final_days4 | 否 |  |  |
| 9 | near_final_ratio4 | 否 |  |  |
| 10 | near_final_days5 | 否 |  |  |
| 11 | near_final_ratio5 | 否 |  |  |
| 12 | outmoney_ratio | 否 |  |  |
| 13 | deep_outmoney_ratio | 否 |  |  |
| 14 | inmoney_ratio | 否 |  |  |
| 15 | deep_inmoney_ratio | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | atmoney_ratio | 否 |  |  |
| 18 | call_degree | 否 |  |  |
| 19 | call_inmoney_ratio | 否 |  |  |
| 20 | call_outmoney_ratio | 否 |  |  |
| 21 | put_degree | 否 |  |  |
| 22 | put_outmoney_ratio | 否 |  |  |
| 23 | put_inmoney_ratio | 否 |  |  |
| 24 | put_margin_flag | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | near_final_ratio_kind | 否 |  |  |
| 29 | near_final_days1 | 否 |  |  |
| 30 | near_final_ratio1 | 否 |  |  |
| 31 | near_final_days2 | 否 |  |  |
| 32 | near_final_ratio2 | 否 |  |  |
| 33 | near_final_days3 | 否 |  |  |
| 34 | near_final_ratio3 | 否 |  |  |
| 35 | near_final_days4 | 否 |  |  |
| 36 | near_final_ratio4 | 否 |  |  |
| 37 | near_final_days5 | 否 |  |  |
| 38 | near_final_ratio5 | 否 |  |  |
| 39 | outmoney_ratio | 否 |  |  |
| 40 | deep_outmoney_ratio | 否 |  |  |
| 41 | inmoney_ratio | 否 |  |  |
| 42 | deep_inmoney_ratio | 否 |  |  |
| 43 | remark | 否 |  |  |
| 44 | atmoney_ratio | 否 |  |  |
| 45 | call_degree | 否 |  |  |
| 46 | call_inmoney_ratio | 否 |  |  |
| 47 | call_outmoney_ratio | 否 |  |  |
| 48 | put_degree | 否 |  |  |
| 49 | put_outmoney_ratio | 否 |  |  |
| 50 | put_inmoney_ratio | 否 |  |  |
| 51 | put_margin_flag | 否 |  |  |
| 52 | update_date | 否 |  |  |
| 53 | update_time | 否 |  |  |
| 54 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optnearfinalmarmodel | 默认 | 是 | near_final_ratio_kind, near_final_ratio_kind |
| idx_optnearfinalmarmodel | 默认 | 是 | near_final_ratio_kind, near_final_ratio_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optnearfinalmarmodel | near_final_ratio_kind, near_final_ratio_kind |
| idx_optnearfinalmarmodel | near_final_ratio_kind, near_final_ratio_kind |

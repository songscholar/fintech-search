# income_price_info_ext - 固收非公开行情三方回购扩展信息表

**表对象ID**: 2467
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | income_busi_type | 否 |  |  |
| 3 | entrust_prop | 否 |  |  |
| 4 | cbpconfer_id | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | impawn_amount | 否 |  |  |
| 8 | spot_full_price | 否 |  |  |
| 9 | current_assure_value | 否 |  |  |
| 10 | impawn_bs | 否 |  |  |
| 11 | remark | 否 |  |  |
| 12 | income_update_type | 否 |  |  |
| 13 | init_date | 否 |  |  |
| 14 | income_busi_type | 否 |  |  |
| 15 | entrust_prop | 否 |  |  |
| 16 | cbpconfer_id | 否 |  |  |
| 17 | exchange_type | 否 |  |  |
| 18 | stock_code | 否 |  |  |
| 19 | impawn_amount | 否 |  |  |
| 20 | spot_full_price | 否 |  |  |
| 21 | current_assure_value | 否 |  |  |
| 22 | impawn_bs | 否 |  |  |
| 23 | remark | 否 |  |  |
| 24 | income_update_type | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_incomepriinfoext | ART | 是 | init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs, init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs |
| idx_rpt_incomepriinfoext | ART | 是 | init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs, init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs |
| idx_incomepriinfoext | ART | 是 | init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs, init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs |
| idx_rpt_incomepriinfoext | ART | 是 | init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs, init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_incomepriinfoext | init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs, init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs |
| idx_incomepriinfoext | init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs, init_date, entrust_prop, cbpconfer_id, exchange_type, stock_code, impawn_bs |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-08 13:57:00 | 3.0.2.98 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-06 14:42:33 | 3.0.2.98 | 洪略 | 增加历史表 |
| 2025-04-09 09:57:05 | 3.0.2.82 | 钟兆星 | 新增固收非公开行情三方回购扩展信息表income_price_info_ext |
| 2025-12-08 13:57:00 | 3.0.2.98 | 洪略 | 历史表索引增加rpt前缀 |
| 2025-11-06 14:42:33 | 3.0.2.98 | 洪略 | 增加历史表 |
| 2025-04-09 09:57:05 | 3.0.2.82 | 钟兆星 | 新增固收非公开行情三方回购扩展信息表income_price_info_ext |

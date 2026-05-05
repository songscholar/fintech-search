# pre_assure_code - 预导入担保证券信息表

**表对象ID**: 7087
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 54 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | stock_code | 否 |  |  |
| 3 | assure_ratio | 否 |  |  |
| 4 | assure_std_ratio | 否 |  |  |
| 5 | circulate_amount | 否 |  |  |
| 6 | capital_amount | 否 |  |  |
| 7 | upper_assure_hold_amount | 否 |  |  |
| 8 | fair_price | 否 |  |  |
| 9 | fair_price_flag | 否 |  |  |
| 10 | fair_ratio | 否 |  |  |
| 11 | old_assure_ratio | 否 |  |  |
| 12 | old_assure_std_ratio | 否 |  |  |
| 13 | static_pe_ratio | 否 |  |  |
| 14 | com_assure_ratio | 否 |  |  |
| 15 | std_assure_ratio | 否 |  |  |
| 16 | slo_sellbuy_status | 否 |  |  |
| 17 | assure_status | 否 |  |  |
| 18 | std_assure_status | 否 |  |  |
| 19 | com_assure_status | 否 |  |  |
| 20 | crdtfile_kind_str | 否 |  |  |
| 21 | allow_blocktrade_flag | 否 |  |  |
| 22 | remark | 否 |  |  |
| 23 | collateral_ratio | 否 |  |  |
| 24 | collateral_pe_ratio | 否 |  |  |
| 25 | update_date | 否 |  |  |
| 26 | update_time | 否 |  |  |
| 27 | position_str | 否 |  | stock_code(8)+exchange_type(4) |
| 28 | exchange_type | 否 |  |  |
| 29 | stock_code | 否 |  |  |
| 30 | assure_ratio | 否 |  |  |
| 31 | assure_std_ratio | 否 |  |  |
| 32 | circulate_amount | 否 |  |  |
| 33 | capital_amount | 否 |  |  |
| 34 | upper_assure_hold_amount | 否 |  |  |
| 35 | fair_price | 否 |  |  |
| 36 | fair_price_flag | 否 |  |  |
| 37 | fair_ratio | 否 |  |  |
| 38 | old_assure_ratio | 否 |  |  |
| 39 | old_assure_std_ratio | 否 |  |  |
| 40 | static_pe_ratio | 否 |  |  |
| 41 | com_assure_ratio | 否 |  |  |
| 42 | std_assure_ratio | 否 |  |  |
| 43 | slo_sellbuy_status | 否 |  |  |
| 44 | assure_status | 否 |  |  |
| 45 | std_assure_status | 否 |  |  |
| 46 | com_assure_status | 否 |  |  |
| 47 | crdtfile_kind_str | 否 |  |  |
| 48 | allow_blocktrade_flag | 否 |  |  |
| 49 | remark | 否 |  |  |
| 50 | collateral_ratio | 否 |  |  |
| 51 | collateral_pe_ratio | 否 |  |  |
| 52 | update_date | 否 |  |  |
| 53 | update_time | 否 |  |  |
| 54 | position_str | 否 |  | stock_code(8)+exchange_type(4) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_pre_assure_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |
| idx_pre_assure_code | ART | 是 | stock_code, exchange_type, stock_code, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_pre_assure_code | stock_code, exchange_type, stock_code, exchange_type |
| idx_pre_assure_code | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-17 20:43:05 | 3.0.6.55 | 李想 | 新增表 |
| 2025-02-17 20:43:05 | 3.0.6.55 | 李想 | 新增表 |

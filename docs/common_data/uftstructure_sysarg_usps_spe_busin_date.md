# usps_spe_busin_date - 特殊业务日期表

**表对象ID**: 25
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | date_type | 否 |  |  |
| 3 | modify_date | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | position_str | 否 |  | date_type |
| 6 | init_date | 否 |  |  |
| 7 | date_type | 否 |  |  |
| 8 | modify_date | 否 |  |  |
| 9 | transaction_no | 否 |  |  |
| 10 | position_str | 否 |  | date_type |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_spe_busin_date | ART | 是 | date_type, date_type |
| idx_usps_spe_busin_date | ART | 是 | date_type, date_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_spe_busin_date | date_type, date_type |
| idx_usps_spe_busin_date | date_type, date_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-03 21:53:04 | 3.0.2.94 | 高志强 | 所有表usps_spe_busin_date，添加了表字段(position_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:07 | 0.0.0.9 | 吴威 | 新增transaction_no |
| 2025-09-03 21:53:04 | 3.0.2.94 | 高志强 | 所有表usps_spe_busin_date，添加了表字段(position_str);
 |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-19 17:07 | 0.0.0.9 | 吴威 | 新增transaction_no |

# ucrt_assure_prod_code - 担保产品信息表

**表对象ID**: 7025
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 34 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | prodta_no | 否 |  |  |
| 3 | prod_code | 否 |  |  |
| 4 | prodcode_type | 否 |  |  |
| 5 | prod_name | 否 |  |  |
| 6 | assure_ratio | 否 |  |  |
| 7 | assure_std_ratio | 否 |  |  |
| 8 | end_date | 否 |  |  |
| 9 | assure_status | 否 |  |  |
| 10 | net_value | 否 |  |  |
| 11 | slo_sellbuy_status | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | position_str | 否 |  | prod_code(32)+prodcode_type(1) |
| 17 | tohis_date | 否 | H |  |
| 18 | init_date | 否 |  |  |
| 19 | prodta_no | 否 |  |  |
| 20 | prod_code | 否 |  |  |
| 21 | prodcode_type | 否 |  |  |
| 22 | prod_name | 否 |  |  |
| 23 | assure_ratio | 否 |  |  |
| 24 | assure_std_ratio | 否 |  |  |
| 25 | end_date | 否 |  |  |
| 26 | assure_status | 否 |  |  |
| 27 | net_value | 否 |  |  |
| 28 | slo_sellbuy_status | 否 |  |  |
| 29 | transaction_no | 否 |  |  |
| 30 | remark | 否 |  |  |
| 31 | update_date | 否 |  |  |
| 32 | update_time | 否 |  |  |
| 33 | position_str | 否 |  | prod_code(32)+prodcode_type(1) |
| 34 | tohis_date | 否 | H |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_assure_prod_code | ART | 是 | prod_code, prodcode_type, prod_code, prodcode_type |
| uk_rpt_ucrtassureprodcode | ART | 是 | tohis_date, position_str, tohis_date, position_str |
| idx_ucrt_assure_prod_code | ART | 是 | prod_code, prodcode_type, prod_code, prodcode_type |
| uk_rpt_ucrtassureprodcode | ART | 是 | tohis_date, position_str, tohis_date, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_assure_prod_code | prod_code, prodcode_type, prod_code, prodcode_type |
| idx_ucrt_assure_prod_code | prod_code, prodcode_type, prod_code, prodcode_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-18 14:03:56 | 3.0.6.65 | 洪略 | 补齐分区 |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 21:44:02 | 3.0.6.65 | 李想 | 物理表ucrt_assure_prod_code，添加了表字段(remark);
物理表ucrt_assure_pro... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-12-18 14:03:56 | 3.0.6.65 | 洪略 | 补齐分区 |
| 2025-11-21 19:56:55 | V3.0.6.1069 | 周兆军 | 维护历史表 |
| 2025-02-17 21:44:02 | 3.0.6.65 | 李想 | 物理表ucrt_assure_prod_code，添加了表字段(remark);
物理表ucrt_assure_pro... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:20 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

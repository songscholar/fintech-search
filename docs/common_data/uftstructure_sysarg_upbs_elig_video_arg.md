# upbs_elig_video_arg - 双录参数设置表

**表对象ID**: 87
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | eligvideo_source | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | stock_code | 否 |  |  |
| 4 | en_branch_no | 否 |  |  |
| 5 | en_entrust_way | 否 |  |  |
| 6 | eligvideo_flag | 否 |  |  |
| 7 | en_organ_flag | 否 |  |  |
| 8 | en_prof_type | 否 |  |  |
| 9 | en_prodrisk_level | 否 |  |  |
| 10 | video_condition_str | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | finance_type | 否 |  |  |
| 13 | prodta_no | 否 |  |  |
| 14 | prod_code | 否 |  |  |
| 15 | eligvideo_mode | 否 |  |  |
| 16 | prod_type | 否 |  |  |
| 17 | eligvideo_source | 否 |  |  |
| 18 | exchange_type | 否 |  |  |
| 19 | stock_code | 否 |  |  |
| 20 | en_branch_no | 否 |  |  |
| 21 | en_entrust_way | 否 |  |  |
| 22 | eligvideo_flag | 否 |  |  |
| 23 | en_organ_flag | 否 |  |  |
| 24 | en_prof_type | 否 |  |  |
| 25 | en_prodrisk_level | 否 |  |  |
| 26 | video_condition_str | 否 |  |  |
| 27 | transaction_no | 否 |  |  |
| 28 | finance_type | 否 |  |  |
| 29 | prodta_no | 否 |  |  |
| 30 | prod_code | 否 |  |  |
| 31 | eligvideo_mode | 否 |  |  |
| 32 | prod_type | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_elig_video_arg | ART | 是 | eligvideo_source, exchange_type, stock_code, eligvideo_source, exchange_type, stock_code |
| idx_upbs_elig_video_arg | ART | 是 | eligvideo_source, exchange_type, stock_code, eligvideo_source, exchange_type, stock_code |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_elig_video_arg | eligvideo_source, exchange_type, stock_code, eligvideo_source, exchange_type, stock_code |
| idx_upbs_elig_video_arg | eligvideo_source, exchange_type, stock_code, eligvideo_source, exchange_type, stock_code |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-23 11:18:18 | 3.0.3.12 | 张明月 | 物理表upbs_elig_video_arg，添加了表字段(prod_type);
物理表upbs_elig_vide... |
| 2023-11-10 10:21:04 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |
| 2024-09-23 11:18:18 | 3.0.3.12 | 张明月 | 物理表upbs_elig_video_arg，添加了表字段(prod_type);
物理表upbs_elig_vide... |
| 2023-11-10 10:21:04 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |

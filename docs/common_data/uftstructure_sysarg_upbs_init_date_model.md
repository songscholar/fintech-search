# upbs_init_date_model - 交易日期表

**表对象ID**: 39
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | init_model | 否 |  |  |
| 3 | settle_flag | 否 |  |  |
| 4 | trade_flag | 否 |  |  |
| 5 | row_num | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | init_model | 否 |  |  |
| 9 | settle_flag | 否 |  |  |
| 10 | trade_flag | 否 |  |  |
| 11 | row_num | 否 |  |  |
| 12 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_init_date_model_model | 默认 | 否 |  |
| idx_upbs_init_date_model | ART | 是 | init_date, init_model, init_date, init_model |
| idx_upbs_init_date_model_model | 默认 | 否 |  |
| idx_upbs_init_date_model | ART | 是 | init_date, init_model, init_date, init_model |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_init_date_model | init_date, init_model, init_date, init_model |
| idx_upbs_init_date_model | init_date, init_model, init_date, init_model |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-05 14:01:16 | 8.26.2.102 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-10-10 09:53:43 | 3.0.2.97 | wuxd | 当前表upbs_init_date_model，删除了表索引（idx_upbs_init_date_model_mode... |
| 2025-09-20 16:27:51 | 3.0.2.96 | wuxd | 新增内存索引idx_upbs_init_date_model_model，调整索引字段顺序 |
| 2025-06-13 14:57:51 | 3.0.6.1007 | 汪迎 | 物理表upbs_init_date_model，添加了表字段(row_num);
 |
| 2023-08-17 11:25 | 0.3.3.138 | 李海洋 | 删除字段exchange_type、finance_type、treat_flag、special_trade_flag |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-06-10 16:51 | 0.0.0.6 | 李海洋 | 交易日期模板表字段更新 |
| 2026-01-05 14:01:16 | 8.26.2.102 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-10-10 09:53:43 | 3.0.2.97 | wuxd | 当前表upbs_init_date_model，删除了表索引（idx_upbs_init_date_model_mode... |
| 2025-09-20 16:27:51 | 3.0.2.96 | wuxd | 新增内存索引idx_upbs_init_date_model_model，调整索引字段顺序 |
| 2025-06-13 14:57:51 | 3.0.6.1007 | 汪迎 | 物理表upbs_init_date_model，添加了表字段(row_num);
 |
| 2023-08-17 11:25 | 0.3.3.138 | 李海洋 | 删除字段exchange_type、finance_type、treat_flag、special_trade_flag |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |

> 共 16 条修改记录，仅显示最近15条

# ucrt_primerate_str - 优惠利率策略表

**表对象ID**: 7041
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | primerate_strategy_type | 否 |  |  |
| 2 | strategy_param | 否 |  |  |
| 3 | remark | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | stp_strategy_info | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | primerate_strategy_type | 否 |  |  |
| 9 | strategy_param | 否 |  |  |
| 10 | remark | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | stp_strategy_info | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_primerate_str | ART | 是 | primerate_strategy_type, primerate_strategy_type |
| idx_ucrt_primerate_str | ART | 是 | primerate_strategy_type, primerate_strategy_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_primerate_str | primerate_strategy_type, primerate_strategy_type |
| idx_ucrt_primerate_str | primerate_strategy_type, primerate_strategy_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 16:37:44 | 3.0.6.35 | 李想 | 物理表ucrt_primerate_str，添加了表字段(stp_strategy_info);
物理表ucrt_pr... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-05-25 18:08 | 0.0.0.2 | 徐世晗 | 新增 |
| 2025-02-13 16:37:44 | 3.0.6.35 | 李想 | 物理表ucrt_primerate_str，添加了表字段(stp_strategy_info);
物理表ucrt_pr... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-07 14:59 | 0.3.3.128 | 徐志坚 | 新增transaction_no字段 |
| 2023-05-25 18:08 | 0.0.0.2 | 徐世晗 | 新增 |

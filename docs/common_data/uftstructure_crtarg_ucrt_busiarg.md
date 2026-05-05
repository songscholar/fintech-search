# ucrt_busiarg - 融资融券业务参数表

**表对象ID**: 7015
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | board_fin_quota | 否 |  |  |
| 3 | board_slo_quota | 否 |  |  |
| 4 | board_total_quota | 否 |  |  |
| 5 | fin_total_scale | 否 |  |  |
| 6 | slo_total_scale | 否 |  |  |
| 7 | credit_total_scale | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | company_no | 否 |  |  |
| 10 | board_fin_quota | 否 |  |  |
| 11 | board_slo_quota | 否 |  |  |
| 12 | board_total_quota | 否 |  |  |
| 13 | fin_total_scale | 否 |  |  |
| 14 | slo_total_scale | 否 |  |  |
| 15 | credit_total_scale | 否 |  |  |
| 16 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_busiarg | ART | 是 | company_no, company_no |
| idx_ucrt_busiarg | ART | 是 | company_no, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_busiarg | company_no, company_no |
| idx_ucrt_busiarg | company_no, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-22 13:33:32 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-22 13:33:32 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

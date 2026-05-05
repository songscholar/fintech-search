# ucrt_cpy_total_info - 融资融券公司总量信息

**表对象ID**: 7550
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | fin_total_balance | 否 |  |  |
| 3 | slo_sell_balance | 否 |  |  |
| 4 | stib_fin_balance | 否 |  |  |
| 5 | stib_slo_value | 否 |  |  |
| 6 | assure_market_value | 否 |  |  |
| 7 | gem_fin_balance | 否 |  |  |
| 8 | gem_slo_value | 否 |  |  |
| 9 | company_no | 否 |  |  |
| 10 | fin_total_balance | 否 |  |  |
| 11 | slo_sell_balance | 否 |  |  |
| 12 | stib_fin_balance | 否 |  |  |
| 13 | stib_slo_value | 否 |  |  |
| 14 | assure_market_value | 否 |  |  |
| 15 | gem_fin_balance | 否 |  |  |
| 16 | gem_slo_value | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_cpy_total_info | ART | 是 | company_no, company_no |
| idx_ucrt_cpy_total_info | ART | 是 | company_no, company_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_cpy_total_info | company_no, company_no |
| idx_ucrt_cpy_total_info | company_no, company_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-12 12:29 | 0.3.3.130 | 雷玄 | 新增表结构 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-12 12:29 | 0.3.3.130 | 雷玄 | 新增表结构 |

# ucrt_client_ploy - 客户平仓策略设置表

**表对象ID**: 7018
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | payoffploy_no | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | date_clear | 否 |  |  |
| 7 | init_date | 否 |  |  |
| 8 | client_id | 否 |  |  |
| 9 | fund_account | 否 |  |  |
| 10 | payoffploy_no | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | date_clear | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_client_ploy | ART | 是 | fund_account, payoffploy_no, fund_account, payoffploy_no |
| idx_ucrt_client_ploy | ART | 是 | fund_account, payoffploy_no, fund_account, payoffploy_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_client_ploy | fund_account, payoffploy_no, fund_account, payoffploy_no |
| idx_ucrt_client_ploy | fund_account, payoffploy_no, fund_account, payoffploy_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-04-04 10:45:50 | 3.0.2.2001 | 卢杰 | 物理表ucrt_client_ploy，添加了表字段(date_clear);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:24 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no；新增索引 |
| 2025-04-04 10:45:50 | 3.0.2.2001 | 卢杰 | 物理表ucrt_client_ploy，添加了表字段(date_clear);
 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-13 15:24 | 0.3.3.107 | 董瑞辉 | 新增表字段transaction_no；新增索引 |

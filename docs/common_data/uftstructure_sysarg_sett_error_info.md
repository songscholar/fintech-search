# sett_error_info - 清算错误信息表

**表对象ID**: 9037
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | app_name | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | risk_id | 否 |  | 初始化后业务处理(按业务并发)根据传入的risk_id进行并发 |
| 5 | error_info | 否 |  |  |
| 6 | curr_time | 否 |  |  |
| 7 | ordinal | 否 |  | 清算前端传入，用来控制初始化后业务处理接口的执行次数，每次+1 |
| 8 | init_date | 否 |  |  |
| 9 | app_name | 否 |  |  |
| 10 | fund_account | 否 |  |  |
| 11 | risk_id | 否 |  | 初始化后业务处理(按业务并发)根据传入的risk_id进行并发 |
| 12 | error_info | 否 |  |  |
| 13 | curr_time | 否 |  |  |
| 14 | ordinal | 否 |  | 清算前端传入，用来控制初始化后业务处理接口的执行次数，每次+1 |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sett_error_info | ART | 是 | init_date, app_name, fund_account, risk_id, curr_time, ordinal, init_date, app_name, fund_account, risk_id, curr_time, ordinal |
| idx_sett_error_info | ART | 是 | init_date, app_name, fund_account, risk_id, curr_time, ordinal, init_date, app_name, fund_account, risk_id, curr_time, ordinal |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sett_error_info | init_date, app_name, fund_account, risk_id, curr_time, ordinal, init_date, app_name, fund_account, risk_id, curr_time, ordinal |
| idx_sett_error_info | init_date, app_name, fund_account, risk_id, curr_time, ordinal, init_date, app_name, fund_account, risk_id, curr_time, ordinal |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-31 13:36:19 | 3.0.2.1011 | 马明智 |  |
| 2025-07-31 13:36:19 | 3.0.2.1011 | 马明智 |  |

# etf_dsf_quota_arg - ETF代收代付个人额度参数表

**表对象ID**: 2843
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 是 |  |  |
| 2 | group_no | 是 |  |  |
| 3 | total_quota | 是 |  |  |
| 4 | used_quota | 是 |  |  |
| 5 | enable_quota | 是 |  |  |
| 6 | fund_account | 是 |  |  |
| 7 | group_no | 是 |  |  |
| 8 | total_quota | 是 |  |  |
| 9 | used_quota | 是 |  |  |
| 10 | enable_quota | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etf_dsf_quota_arg | 默认 | 是 | fund_account, fund_account |
| idx_etf_dsf_quota_arg | 默认 | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etf_dsf_quota_arg | fund_account, fund_account |
| idx_etf_dsf_quota_arg | fund_account, fund_account |

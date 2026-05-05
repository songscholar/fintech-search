# etf_dsf_share_quota - ETF代收代付共享额度表

**表对象ID**: 2844
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | group_no | 是 |  |  |
| 2 | total_quota | 是 |  |  |
| 3 | used_quota | 是 |  |  |
| 4 | enable_quota | 是 |  |  |
| 5 | group_no | 是 |  |  |
| 6 | total_quota | 是 |  |  |
| 7 | used_quota | 是 |  |  |
| 8 | enable_quota | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_etf_dsf_share_quota | 默认 | 是 | group_no, group_no |
| idx_etf_dsf_share_quota | 默认 | 是 | group_no, group_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_etf_dsf_share_quota | group_no, group_no |
| idx_etf_dsf_share_quota | group_no, group_no |

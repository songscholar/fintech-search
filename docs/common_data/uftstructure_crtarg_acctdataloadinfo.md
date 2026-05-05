# acctdataloadinfo - 客户数据加载信息表

**表对象ID**: 7048
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | qrysync_times | 否 |  |  |
| 3 | start_time | 否 |  |  |
| 4 | end_time | 否 |  |  |
| 5 | deal_status | 否 |  |  |
| 6 | partition_no | 否 |  |  |
| 7 | fund_account | 否 |  |  |
| 8 | qrysync_times | 否 |  |  |
| 9 | start_time | 否 |  |  |
| 10 | end_time | 否 |  |  |
| 11 | deal_status | 否 |  |  |
| 12 | partition_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_acctdataloadinfo | ART | 是 | fund_account, fund_account |
| idx_acctdataloadinfo | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_acctdataloadinfo | fund_account, fund_account |
| idx_acctdataloadinfo | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-05 10:17:45 | 3.0.4.3 | 沈勋 | 物理表acctdataloadinfo，添加了表字段(partition_no);
 |
| 2024-07-30 10:26:50 | 3.0.3.7 | 董瑞辉 | 新增 |
| 2024-09-05 10:17:45 | 3.0.4.3 | 沈勋 | 物理表acctdataloadinfo，添加了表字段(partition_no);
 |
| 2024-07-30 10:26:50 | 3.0.3.7 | 董瑞辉 | 新增 |

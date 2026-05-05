# ucrt_client - 融资融券客户信息表

**表对象ID**: 7528
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 6 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | cust_id | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | cust_id | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_client | ART | 是 | client_id, client_id |
| idx_ucrt_client | ART | 是 | client_id, client_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_client | client_id, client_id |
| idx_ucrt_client | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-14 14:17 | 0.3.3.132 | 程猛 | client表取消与fund_account表的关联关系 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-08-14 14:17 | 0.3.3.132 | 程猛 | client表取消与fund_account表的关联关系 |

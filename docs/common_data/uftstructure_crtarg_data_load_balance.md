# data_load_balance - 数据加载负载均衡记录表

**表对象ID**: 7049
**所属模块**: crtarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 4 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | order_no | 否 |  |  |
| 2 | last_partition_no | 否 |  |  |
| 3 | order_no | 否 |  |  |
| 4 | last_partition_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_data_load_balance | ART | 是 | order_no, order_no |
| idx_data_load_balance | ART | 是 | order_no, order_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_data_load_balance | order_no, order_no |
| idx_data_load_balance | order_no, order_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-05 13:37:36 | 3.0.4.3 | 沈勋 | 新增data_load_balance-数据加载负载均衡记录表，支持试算系统加载客户数据负载均衡 |
| 2024-09-05 13:37:36 | 3.0.4.3 | 沈勋 | 新增data_load_balance-数据加载负载均衡记录表，支持试算系统加载客户数据负载均衡 |

# upbs_auth_vaskey - 认证共享密钥表

**表对象ID**: 150
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | vaskey_no | 否 |  |  |
| 2 | vas_key | 否 |  |  |
| 3 | create_date | 否 |  |  |
| 4 | create_time | 否 |  |  |
| 5 | transaction_str | 否 |  |  |
| 6 | vaskey_no | 否 |  |  |
| 7 | vas_key | 否 |  |  |
| 8 | create_date | 否 |  |  |
| 9 | create_time | 否 |  |  |
| 10 | transaction_str | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_auth_vaskey | 默认 | 否 |  |
| idx_upbs_auth_vaskey | ART | 是 | vaskey_no, vaskey_no |
| idx_upbs_auth_vaskey | 默认 | 否 |  |
| idx_upbs_auth_vaskey | ART | 是 | vaskey_no, vaskey_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_auth_vaskey | vaskey_no, vaskey_no |
| idx_upbs_auth_vaskey | vaskey_no, vaskey_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 15:32:10 | 3.0.2.103 | taocong45644 | 当前表upbs_auth_vaskey，修改了索引idx_upbs_auth_vaskey,索引字段修改为：(vaske... |
| 2024-11-20 15:39:42 | V3.0.3.12 | 韦子晗 | 新增字段transaction_str |
| 2024-11-15 14:35:44 | V3.0.3.11 | 周君杰 | 新增upbs_auth_vaskey表 |
| 2025-12-01 15:32:10 | 3.0.2.103 | taocong45644 | 当前表upbs_auth_vaskey，修改了索引idx_upbs_auth_vaskey,索引字段修改为：(vaske... |
| 2024-11-20 15:39:42 | V3.0.3.12 | 韦子晗 | 新增字段transaction_str |
| 2024-11-15 14:35:44 | V3.0.3.11 | 周君杰 | 新增upbs_auth_vaskey表 |

# pbs_sysnode_deploy - 系统节点部署表

**表对象ID**: 2807
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sysnode_id | 否 |  |  |
| 2 | subsys_id | 否 |  |  |
| 3 | subsys_name | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | sysnode_id | 否 |  |  |
| 6 | subsys_id | 否 |  |  |
| 7 | subsys_name | 否 |  |  |
| 8 | transaction_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| uk_sysnode_deploy | 默认 | 否 |  |
| uk_sysnode_deploy | ART | 是 | sysnode_id, subsys_id, sysnode_id, subsys_id |
| uk_sysnode_deploy | 默认 | 否 |  |
| uk_sysnode_deploy | ART | 是 | sysnode_id, subsys_id, sysnode_id, subsys_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| uk_sysnode_deploy | sysnode_id, subsys_id, sysnode_id, subsys_id |
| uk_sysnode_deploy | sysnode_id, subsys_id, sysnode_id, subsys_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-01 14:48:18 | 3.0.2.103 | taocong45644 | 当前表pbs_sysnode_deploy，修改了索引uk_sysnode_deploy,索引字段修改为：(sysnod... |
| 2025-12-01 14:48:18 | 3.0.2.103 | taocong45644 | 当前表pbs_sysnode_deploy，修改了索引uk_sysnode_deploy,索引字段修改为：(sysnod... |

# upbs_asset_prop_deploy - 资产属性部署配置表

**表对象ID**: 363
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | asset_prop | 否 |  |  |
| 3 | sysnode_id | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | branch_no | 否 |  |  |
| 6 | asset_prop | 否 |  |  |
| 7 | sysnode_id | 否 |  |  |
| 8 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_assetpropdeploy | ART | 是 | branch_no, asset_prop, branch_no, asset_prop |
| idx_assetpropdeploy | ART | 是 | branch_no, asset_prop, branch_no, asset_prop |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_assetpropdeploy | branch_no, asset_prop, branch_no, asset_prop |
| idx_assetpropdeploy | branch_no, asset_prop, branch_no, asset_prop |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-01-13 11:15:51 | 3.0.2.51 | 董乾坤 | 新增 |
| 2025-01-13 11:15:51 | 3.0.2.51 | 董乾坤 | 新增 |

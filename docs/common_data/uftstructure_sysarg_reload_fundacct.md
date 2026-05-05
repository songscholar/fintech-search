# reload_fundacct - 二次上场资产账户

**表对象ID**: 98
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 4 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | partition_no | 否 |  |  |
| 3 | fund_account | 否 |  |  |
| 4 | partition_no | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_reloadfundacct | 默认 | 否 | fund_account, fund_account |
| idx_reloadfundacct | ART | 是 | fund_account, fund_account |
| idx_reloadfundacct | 默认 | 否 | fund_account, fund_account |
| idx_reloadfundacct | ART | 是 | fund_account, fund_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_reloadfundacct | fund_account, fund_account |
| idx_reloadfundacct | fund_account, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-07 14:21:00 | 3.0.2.77 | 谢宗艺 | 物理表reload_fundacct，增加索引(idx_reloadfundacct:[fund_account]);... |
| 2025-03-07 14:21:00 | 3.0.2.77 | 谢宗艺 | 物理表reload_fundacct，增加索引(idx_reloadfundacct:[fund_account]);... |

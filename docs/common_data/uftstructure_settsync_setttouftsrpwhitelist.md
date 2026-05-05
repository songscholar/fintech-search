# setttouftsrpwhitelist - 清算股票质押白名单表

**表对象ID**: 3051
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 是 |  |  |
| 2 | client_id | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | registe_date | 是 |  |  |
| 5 | remark | 是 |  |  |
| 6 | branch_no | 是 |  |  |
| 7 | client_id | 是 |  |  |
| 8 | exchange_type | 是 |  |  |
| 9 | registe_date | 是 |  |  |
| 10 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settsrpwhitelist | 默认 | 是 | branch_no, client_id, exchange_type, branch_no, client_id, exchange_type |
| idx_settsrpwhitelist | 默认 | 是 | branch_no, client_id, exchange_type, branch_no, client_id, exchange_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settsrpwhitelist | branch_no, client_id, exchange_type, branch_no, client_id, exchange_type |
| idx_settsrpwhitelist | branch_no, client_id, exchange_type, branch_no, client_id, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2020-12-29 19:41 | 8.26.1.107 | 罗佳楠 | 新增 |
| 2020-12-29 19:41 | 8.26.1.107 | 罗佳楠 | 新增 |

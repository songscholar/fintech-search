# uopt_busiwhitelist - 期权业务白名单表

**表对象ID**: 9011
**所属模块**: optarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 是 |  |  |
| 2 | exchange_type | 是 |  |  |
| 3 | opt_whitebusi_kind | 是 |  |  |
| 4 | remark | 是 |  |  |
| 5 | fund_account | 是 |  |  |
| 6 | exchange_type | 是 |  |  |
| 7 | opt_whitebusi_kind | 是 |  |  |
| 8 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_busiwhitelist | 默认 | 是 | fund_account, exchange_type, opt_whitebusi_kind, fund_account, exchange_type, opt_whitebusi_kind |
| idx_uopt_busiwhitelist | 默认 | 是 | fund_account, exchange_type, opt_whitebusi_kind, fund_account, exchange_type, opt_whitebusi_kind |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_busiwhitelist | fund_account, exchange_type, opt_whitebusi_kind, fund_account, exchange_type, opt_whitebusi_kind |
| idx_uopt_busiwhitelist | fund_account, exchange_type, opt_whitebusi_kind, fund_account, exchange_type, opt_whitebusi_kind |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-12-16 17:28:58 | 3.0.0.0 | wuxd |  |
| 2023-12-16 17:28:58 | 3.0.0.0 | wuxd |  |

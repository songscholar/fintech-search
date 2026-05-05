# settredo_etf_cash_balanceinfo - 清算重做ETF预估现金冻结信息临时表

**表对象ID**: 2852
**所属模块**: sms
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | position_str | 否 |  |  |
| 2 | settle_mark | 否 |  |  |
| 3 | date_clear | 否 |  |  |
| 4 | sett_dml_type | 否 |  |  |
| 5 | sett_batch_no | 否 |  |  |
| 6 | position_str | 否 |  |  |
| 7 | settle_mark | 否 |  |  |
| 8 | date_clear | 否 |  |  |
| 9 | sett_dml_type | 否 |  |  |
| 10 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_strd_etfcashbalance_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_strd_etfcashbalance_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_strd_etfcashbalance_pos | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_strd_etfcashbalance_pos | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-08-04 15:54:54 | 8.26.2.91 | 马天宇 | 新建表结构 |
| 2025-08-04 15:54:54 | 8.26.2.91 | 马天宇 | 新建表结构 |

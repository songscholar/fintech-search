# settredo_adviser_contract - 清算重做投顾产品签约信息

**表对象ID**: 506
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB
**持久化**: true

## 字段列表（共 8 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | unsign_date | 否 |  |  |
| 2 | position_str | 否 |  |  |
| 3 | unsign_time | 否 |  |  |
| 4 | sett_batch_no | 否 |  |  |
| 5 | unsign_date | 否 |  |  |
| 6 | position_str | 否 |  |  |
| 7 | unsign_time | 否 |  |  |
| 8 | sett_batch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sett_advcontract_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_sett_advcontract_pos | ART | 是 | sett_batch_no, position_str, sett_batch_no, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sett_advcontract_pos | sett_batch_no, position_str, sett_batch_no, position_str |
| idx_sett_advcontract_pos | sett_batch_no, position_str, sett_batch_no, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-24 09:56:11 | 3.0.6.1011 | yangxz |  |
| 2025-07-24 09:56:11 | 3.0.6.1011 | yangxz |  |

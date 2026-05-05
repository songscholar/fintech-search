# szhk_equity - 深港通权益表

**表对象ID**: 5565
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA

## 字段列表（共 24 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_account | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | entrust_amount | 否 |  |  |
| 7 | market_prop | 否 |  |  |
| 8 | szhk_authority_prop | 否 |  |  |
| 9 | szhk_authority_id | 否 |  |  |
| 10 | position_str | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | frozen_amount | 否 |  |  |
| 13 | init_date | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_account | 否 |  |  |
| 17 | stock_code | 否 |  |  |
| 18 | entrust_amount | 否 |  |  |
| 19 | market_prop | 否 |  |  |
| 20 | szhk_authority_prop | 否 |  |  |
| 21 | szhk_authority_id | 否 |  |  |
| 22 | position_str | 否 |  |  |
| 23 | seat_no | 否 |  |  |
| 24 | frozen_amount | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_szhk_equity_pos | 默认 | 否 |  |
| idx_szhk_equity | ART | 是 | fund_account, stock_code, seat_no, fund_account, stock_code, seat_no |
| idx_szhk_equity_pos | ART | 是 | position_str, position_str |
| idx_szhk_equity_pos | 默认 | 否 |  |
| idx_szhk_equity | ART | 是 | fund_account, stock_code, seat_no, fund_account, stock_code, seat_no |
| idx_szhk_equity_pos | ART | 是 | position_str, position_str |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_szhk_equity_pos | position_str, position_str |
| idx_szhk_equity_pos | position_str, position_str |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 14:15:09 | V3.0.2.106 | taocong45644 | 当前表szhk_equity，修改了索引idx_szhk_equity_pos,索引字段修改为：(position_st... |
| 2025-04-23 17:35:24 | 3.0.2.67 | 张训华 | 调整idx_szhk_equity_pos为分级索引 |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，增加全局唯一索引idx_szhk_equity_pos |
| 2024-10-02 16:21:33 | 3.0.2.49 | 於达 | 内存索引从全部匹配改成部分匹配 |
| 2024-07-26 14:40:20 | 3.0.2.30 | 余世泽 | 新增 |
| 2026-03-09 14:15:09 | V3.0.2.106 | taocong45644 | 当前表szhk_equity，修改了索引idx_szhk_equity_pos,索引字段修改为：(position_st... |
| 2025-04-23 17:35:24 | 3.0.2.67 | 张训华 | 调整idx_szhk_equity_pos为分级索引 |
| 2025-03-21 13:46:56 | 3.0.2.63 | 张训华 | 支持二次上场，增加全局唯一索引idx_szhk_equity_pos |
| 2024-10-02 16:21:33 | 3.0.2.49 | 於达 | 内存索引从全部匹配改成部分匹配 |
| 2024-07-26 14:40:20 | 3.0.2.30 | 余世泽 | 新增 |

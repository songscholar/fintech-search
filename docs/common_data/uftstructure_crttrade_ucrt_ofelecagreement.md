# ucrt_ofelecagreement - 场内电子协议控制表

**表对象ID**: 7506
**所属模块**: crttrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 20 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | init_date | 否 |  |  |
| 2 | agreement_id | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | fund_account | 否 |  |  |
| 5 | exchange_type | 否 |  |  |
| 6 | stock_code | 否 |  |  |
| 7 | stock_account | 否 |  |  |
| 8 | sign_status | 否 |  |  |
| 9 | csfc_end_date | 否 |  |  |
| 10 | transaction_no | 否 |  |  |
| 11 | init_date | 否 |  |  |
| 12 | agreement_id | 否 |  |  |
| 13 | client_id | 否 |  |  |
| 14 | fund_account | 否 |  |  |
| 15 | exchange_type | 否 |  |  |
| 16 | stock_code | 否 |  |  |
| 17 | stock_account | 否 |  |  |
| 18 | sign_status | 否 |  |  |
| 19 | csfc_end_date | 否 |  |  |
| 20 | transaction_no | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_ofelecagreement | 默认 | 否 | fund_account, agreement_id, fund_account, agreement_id |
| idx_ucrt_ofelecagreement | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucrt_ofelecagreement_uk | ART | 是 | fund_account, agreement_id, fund_account, agreement_id |
| idx_ucrt_ofelecagreement | 默认 | 否 | fund_account, agreement_id, fund_account, agreement_id |
| idx_ucrt_ofelecagreement | ART | 是 | fund_account, stock_code, exchange_type, fund_account, stock_code, exchange_type |
| idx_ucrt_ofelecagreement_uk | ART | 是 | fund_account, agreement_id, fund_account, agreement_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_ofelecagreement | fund_account, agreement_id, fund_account, agreement_id |
| idx_ucrt_ofelecagreement | fund_account, agreement_id, fund_account, agreement_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-02 10:45:50 | 3.0.8.19 | 袁文龙 | 当前表ucrt_ofelecagreement，修改了索引idx_ucrt_ofelecagreement,索引字段修改... |
| 2023-08-22 13:33:32 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2026-03-02 10:45:50 | 3.0.8.19 | 袁文龙 | 当前表ucrt_ofelecagreement，修改了索引idx_ucrt_ofelecagreement,索引字段修改... |
| 2023-08-22 13:33:32 | 0.3.3.141 | 徐志坚 | 因参数同步需要增加transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

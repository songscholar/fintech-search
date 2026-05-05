# of_client_agreement - 证券场内电子协议控制表

**表对象ID**: 5535
**所属模块**: sestrade
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

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ofeleagrmtctrl_acct | ART | 是 | fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type |
| idx_ofeleagrmtctrl_id | ART | 是 | agreement_id, agreement_id |
| idx_ofeleagrmtctrl_acct | ART | 是 | fund_account, stock_account, stock_code, exchange_type, fund_account, stock_account, stock_code, exchange_type |
| idx_ofeleagrmtctrl_id | ART | 是 | agreement_id, agreement_id |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ofeleagrmtctrl_id | agreement_id, agreement_id |
| idx_ofeleagrmtctrl_id | agreement_id, agreement_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:51:29 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-05-29 21:21:28 | 3.0.2.12 | 祝丁恺 | 勾选不回库选项 |
| 2024-05-08 15:22:57 | 3.0.2.6 | 阮善宏 | 删除物理表索引idx_ofeleagrmtctrl_pos |
| 2024-05-08 15:21:04 | 3.0.2.6 | 阮善宏 | 物理表of_client_agreement，删除了表字段(branch_no);
物理表of_client_agre... |
| 2024-05-08 15:19:49 | 3.0.2.6 | 阮善宏 | 物理表of_client_agreement，添加了表字段(transaction_no);
 |
| 2026-03-09 13:51:29 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-05-29 21:21:28 | 3.0.2.12 | 祝丁恺 | 勾选不回库选项 |
| 2024-05-08 15:22:57 | 3.0.2.6 | 阮善宏 | 删除物理表索引idx_ofeleagrmtctrl_pos |
| 2024-05-08 15:21:04 | 3.0.2.6 | 阮善宏 | 物理表of_client_agreement，删除了表字段(branch_no);
物理表of_client_agre... |
| 2024-05-08 15:19:49 | 3.0.2.6 | 阮善宏 | 物理表of_client_agreement，添加了表字段(transaction_no);
 |

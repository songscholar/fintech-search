# fundacctcomm - 资产账户特殊佣金表

**表对象ID**: 329
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 36 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | client_id | 否 |  |  |
| 3 | branch_no | 否 |  |  |
| 4 | exchange_type | 否 |  |  |
| 5 | stock_type | 否 |  |  |
| 6 | money_type | 否 |  |  |
| 7 | entrust_bs | 否 |  |  |
| 8 | en_entrust_way | 否 |  |  |
| 9 | entrust_type | 否 |  |  |
| 10 | balance_ratio | 否 |  |  |
| 11 | min_fare2 | 否 |  |  |
| 12 | max_fare2 | 否 |  |  |
| 13 | netfare0_flag | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | asset_prop | 否 |  |  |
| 16 | update_date | 否 |  |  |
| 17 | update_time | 否 |  |  |
| 18 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_type(4)+money_type(3 |
| 19 | fund_account | 否 |  |  |
| 20 | client_id | 否 |  |  |
| 21 | branch_no | 否 |  |  |
| 22 | exchange_type | 否 |  |  |
| 23 | stock_type | 否 |  |  |
| 24 | money_type | 否 |  |  |
| 25 | entrust_bs | 否 |  |  |
| 26 | en_entrust_way | 否 |  |  |
| 27 | entrust_type | 否 |  |  |
| 28 | balance_ratio | 否 |  |  |
| 29 | min_fare2 | 否 |  |  |
| 30 | max_fare2 | 否 |  |  |
| 31 | netfare0_flag | 否 |  |  |
| 32 | transaction_no | 否 |  |  |
| 33 | asset_prop | 否 |  |  |
| 34 | update_date | 否 |  |  |
| 35 | update_time | 否 |  |  |
| 36 | position_str | 否 |  | fund_account(18)+exchange_type(4)+stock_type(4)+money_type(3 |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_fundacctcomm_bra | 默认 | 否 | branch_no, branch_no |
| idx_fundacctcomm | ART | 是 | fund_account, exchange_type, stock_type, money_type, entrust_bs, en_entrust_way, entrust_type, fund_account, exchange_type, stock_type, money_type, entrust_bs, en_entrust_way, entrust_type |
| idx_fundacctcomm_bra | ART | 是 | branch_no, branch_no |
| idx_fundacctcomm_bra | 默认 | 否 | branch_no, branch_no |
| idx_fundacctcomm | ART | 是 | fund_account, exchange_type, stock_type, money_type, entrust_bs, en_entrust_way, entrust_type, fund_account, exchange_type, stock_type, money_type, entrust_bs, en_entrust_way, entrust_type |
| idx_fundacctcomm_bra | ART | 是 | branch_no, branch_no |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_fundacctcomm | fund_account, exchange_type, stock_type, money_type, entrust_bs, en_entrust_way, entrust_type, fund_account, exchange_type, stock_type, money_type, entrust_bs, en_entrust_way, entrust_type |
| idx_fundacctcomm_bra | branch_no, branch_no |
| idx_fundacctcomm | fund_account, exchange_type, stock_type, money_type, entrust_bs, en_entrust_way, entrust_type, fund_account, exchange_type, stock_type, money_type, entrust_bs, en_entrust_way, entrust_type |
| idx_fundacctcomm_bra | branch_no, branch_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-17 14:27:16 | 3.0.6.1017 | 常行 | 物理表fundacctcomm，增加索引(idx_fundacctcomm_bra:[branch_no]);
 |
| 2025-02-14 15:51:48 | 3.0.6.34 | 李想 | 物理表fundacctcomm，添加了表字段(asset_prop);
物理表fundacctcomm，添加了表字段(... |
| 2024-09-26 19:41:27 | 3.0.3.14 | 张明月 | 物理表fundacctcomm，添加了表字段(transaction_no);
 |
| 2024-09-23 16:35:14 | 3.0.2.15 | 张明月 | 新增 |
| 2025-07-17 14:27:16 | 3.0.6.1017 | 常行 | 物理表fundacctcomm，增加索引(idx_fundacctcomm_bra:[branch_no]);
 |
| 2025-02-14 15:51:48 | 3.0.6.34 | 李想 | 物理表fundacctcomm，添加了表字段(asset_prop);
物理表fundacctcomm，添加了表字段(... |
| 2024-09-26 19:41:27 | 3.0.3.14 | 张明月 | 物理表fundacctcomm，添加了表字段(transaction_no);
 |
| 2024-09-23 16:35:14 | 3.0.2.15 | 张明月 | 新增 |

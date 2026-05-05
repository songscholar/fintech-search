# crdt_personalized_param - 融资融券个性化控制参数表

**表对象ID**: 7105
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 38 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | company_no | 否 |  |  |
| 2 | fund_account | 否 |  |  |
| 3 | client_id | 否 |  |  |
| 4 | branch_no | 否 |  |  |
| 5 | stock_code | 否 |  |  |
| 6 | exchange_type | 否 |  |  |
| 7 | stock_type | 否 |  |  |
| 8 | compact_id | 否 |  |  |
| 9 | create_date | 否 |  |  |
| 10 | crdt_business_type | 否 |  |  |
| 11 | crdt_limit_reason | 否 |  |  |
| 12 | end_date | 否 |  |  |
| 13 | res_entrust_way | 否 |  |  |
| 14 | stockgroup_no | 否 |  |  |
| 15 | en_crdt_busi_type | 否 |  |  |
| 16 | remark | 否 |  |  |
| 17 | update_date | 否 |  |  |
| 18 | update_time | 否 |  |  |
| 19 | position_str | 否 |  | fund_account(18)+crdt_business_type(1)+stock_code(8)+exchang |
| 20 | company_no | 否 |  |  |
| 21 | fund_account | 否 |  |  |
| 22 | client_id | 否 |  |  |
| 23 | branch_no | 否 |  |  |
| 24 | stock_code | 否 |  |  |
| 25 | exchange_type | 否 |  |  |
| 26 | stock_type | 否 |  |  |
| 27 | compact_id | 否 |  |  |
| 28 | create_date | 否 |  |  |
| 29 | crdt_business_type | 否 |  |  |
| 30 | crdt_limit_reason | 否 |  |  |
| 31 | end_date | 否 |  |  |
| 32 | res_entrust_way | 否 |  |  |
| 33 | stockgroup_no | 否 |  |  |
| 34 | en_crdt_busi_type | 否 |  |  |
| 35 | remark | 否 |  |  |
| 36 | update_date | 否 |  |  |
| 37 | update_time | 否 |  |  |
| 38 | position_str | 否 |  | fund_account(18)+crdt_business_type(1)+stock_code(8)+exchang |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_crdt_personalized_param_stk | 默认 | 否 | stock_code, exchange_type, stock_code, exchange_type |
| idx_crdt_personalized_param_stk | 默认 | 否 |  |
| idx_crdt_personalized_param | ART | 是 | fund_account, crdt_business_type, stock_code, exchange_type, company_no, compact_id, crdt_limit_reason, stockgroup_no, fund_account, crdt_business_type, stock_code, exchange_type, company_no, compact_id, crdt_limit_reason, stockgroup_no |
| idx_crdt_personalized_param_stk | 默认 | 否 | stock_code, exchange_type, stock_code, exchange_type |
| idx_crdt_personalized_param_stk | 默认 | 否 |  |
| idx_crdt_personalized_param | ART | 是 | fund_account, crdt_business_type, stock_code, exchange_type, company_no, compact_id, crdt_limit_reason, stockgroup_no, fund_account, crdt_business_type, stock_code, exchange_type, company_no, compact_id, crdt_limit_reason, stockgroup_no |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_crdt_personalized_param | fund_account, crdt_business_type, stock_code, exchange_type, company_no, compact_id, crdt_limit_reason, stockgroup_no, fund_account, crdt_business_type, stock_code, exchange_type, company_no, compact_id, crdt_limit_reason, stockgroup_no |
| idx_crdt_personalized_param_stk | stock_code, exchange_type, stock_code, exchange_type |
| idx_crdt_personalized_param | fund_account, crdt_business_type, stock_code, exchange_type, company_no, compact_id, crdt_limit_reason, stockgroup_no, fund_account, crdt_business_type, stock_code, exchange_type, company_no, compact_id, crdt_limit_reason, stockgroup_no |
| idx_crdt_personalized_param_stk | stock_code, exchange_type, stock_code, exchange_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-01 20:56:23 | 3.0.6.114 | 常行 | 物理表crdt_personalized_param，增加索引(idx_crdt_personalized_param_... |
| 2025-06-26 15:04:18 | 3.0.6.113 | 常行 | 物理表crdt_personalized_param，删除了表索引(idx_crdt_personalized_para... |
| 2025-05-29 09:53:51 | 3.0.6.110 | 常行 | 物理表crdt_personalized_param，添加了表字段(client_id);
物理表crdt_perso... |
| 2025-02-19 11:08:47 | 3.0.6.90 | 李想 | 新增表 |
| 2025-07-01 20:56:23 | 3.0.6.114 | 常行 | 物理表crdt_personalized_param，增加索引(idx_crdt_personalized_param_... |
| 2025-06-26 15:04:18 | 3.0.6.113 | 常行 | 物理表crdt_personalized_param，删除了表索引(idx_crdt_personalized_para... |
| 2025-05-29 09:53:51 | 3.0.6.110 | 常行 | 物理表crdt_personalized_param，添加了表字段(client_id);
物理表crdt_perso... |
| 2025-02-19 11:08:47 | 3.0.6.90 | 李想 | 新增表 |

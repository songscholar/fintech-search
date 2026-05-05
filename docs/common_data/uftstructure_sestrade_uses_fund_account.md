# uses_fund_account - 证券资产账号表

**表对象ID**: 5501
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 66 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | asset_prop | 否 |  |  |
| 2 | branch_no | 否 |  |  |
| 3 | client_group | 否 |  |  |
| 4 | client_id | 否 |  |  |
| 5 | discount_model | 否 |  |  |
| 6 | en_entrust_way | 否 |  |  |
| 7 | fare_kind_str | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | fundacct_status | 否 |  |  |
| 10 | main_flag | 否 |  |  |
| 11 | organ_flag | 否 |  |  |
| 12 | trade_password | 否 |  |  |
| 13 | profit_flag | 否 |  |  |
| 14 | room_code | 否 |  |  |
| 15 | partition_no | 否 |  |  |
| 16 | query_password | 否 |  |  |
| 17 | organ_prod_kind | 否 |  |  |
| 18 | product_flag | 否 |  |  |
| 19 | en_ext_rights | 否 |  |  |
| 20 | fund_account_type | 否 |  |  |
| 21 | en_ext_restriction | 否 |  |  |
| 22 | fund_card | 否 |  |  |
| 23 | risk_level | 否 |  |  |
| 24 | risk_enddate | 否 |  |  |
| 25 | inter_account | 否 |  |  |
| 26 | open_date | 否 |  |  |
| 27 | cancel_date | 否 |  |  |
| 28 | limit_flag | 否 |  |  |
| 29 | remark | 否 |  |  |
| 30 | position_str | 否 |  |  |
| 31 | sysnode_id | 否 |  |  |
| 32 | client_rights | 否 |  |  |
| 33 | restriction | 否 |  |  |
| 34 | asset_prop | 否 |  |  |
| 35 | branch_no | 否 |  |  |
| 36 | client_group | 否 |  |  |
| 37 | client_id | 否 |  |  |
| 38 | discount_model | 否 |  |  |
| 39 | en_entrust_way | 否 |  |  |
| 40 | fare_kind_str | 否 |  |  |
| 41 | fund_account | 否 |  |  |
| 42 | fundacct_status | 否 |  |  |
| 43 | main_flag | 否 |  |  |
| 44 | organ_flag | 否 |  |  |
| 45 | trade_password | 否 |  |  |
| 46 | profit_flag | 否 |  |  |
| 47 | room_code | 否 |  |  |
| 48 | partition_no | 否 |  |  |
| 49 | query_password | 否 |  |  |
| 50 | organ_prod_kind | 否 |  |  |
| 51 | product_flag | 否 |  |  |
| 52 | en_ext_rights | 否 |  |  |
| 53 | fund_account_type | 否 |  |  |
| 54 | en_ext_restriction | 否 |  |  |
| 55 | fund_card | 否 |  |  |
| 56 | risk_level | 否 |  |  |
| 57 | risk_enddate | 否 |  |  |
| 58 | inter_account | 否 |  |  |
| 59 | open_date | 否 |  |  |
| 60 | cancel_date | 否 |  |  |
| 61 | limit_flag | 否 |  |  |
| 62 | remark | 否 |  |  |
| 63 | position_str | 否 |  |  |
| 64 | sysnode_id | 否 |  |  |
| 65 | client_rights | 否 |  |  |
| 66 | restriction | 否 |  |  |

## 索引（共 6 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uses_fund_account_id | 默认 | 否 | client_id, client_id |
| idx_uses_fund_account | ART | 是 | fund_account, fund_account |
| idx_uses_fund_account_id | ART | 是 | client_id, client_id |
| idx_uses_fund_account_id | 默认 | 否 | client_id, client_id |
| idx_uses_fund_account | ART | 是 | fund_account, fund_account |
| idx_uses_fund_account_id | ART | 是 | client_id, client_id |

## 数据库索引（共 4 个）

| 索引名 | 字段 |
|--------|------|
| idx_uses_fund_account | fund_account, fund_account |
| idx_uses_fund_account_id | client_id, client_id |
| idx_uses_fund_account | fund_account, fund_account |
| idx_uses_fund_account_id | client_id, client_id |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 11:17:31 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2025-05-13 09:01:58 | 3.0.6.1000 | 刘洋 | uses_fund_account表新增sysnode_id字段 |
| 2025-04-25 17:23:28 | 3.0.2.67 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2024-12-17 21:21:09 | V3.0.6.5 | 李海洋 | LDP1.0-V202401-06-000平台开发工具升级,报错修复-变长字段必现在表结构末尾 |
| 2024-10-08 14:41:36 | 3.0.2.50 |  | 变长字段挪至最底部 |
| 2024-09-23 10:37:14 | 3.0.2.48 | 张明月 | 物理表uses_fund_account，添加了表字段(product_flag);
物理表uses_fund_acc... |
| 2024-08-14 14:08:14 | 3.0.2.37 | 张剑 | client_rights、restriction设置为变长字段 |
| 2024-06-18 18:41:52 | 3.0.2.20 | 乐闽庭 | 物理表uses_fund_account，添加了表字段(organ_prod_kind);
 |
| 2024-05-29 21:28:54 | 3.0.2.17 | 祝丁恺 | 勾选不回库选项 |
| 2024-05-21 15:17:22 | 3.0.2.9 | 吴威 | 支持uses_fund_account、uses_stock_holder账户同步 |
| 2024-05-13 20:52:28 | 3.0.2.7 | 泮新国 | 修改限制表的关联索引 |
| 2024-04-28 10:34:50 | 3.0.2.3 | 阮善宏 | 物理表uses_fund_account，添加了表字段(query_password);
 |
| 2023-11-27 16:27:55 | V3.0.1.6 | 沈勋 | 物理表uses_fund_account，增加索引(idx_uses_fund_account_id:[client_i... |
| 2023-08-25 16:35:27 | 0.3.3.143 | 徐志坚 | 调整事务控制方式，删除transaction_no字段 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

> 共 32 条修改记录，仅显示最近15条

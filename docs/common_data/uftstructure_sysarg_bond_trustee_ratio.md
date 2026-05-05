# bond_trustee_ratio - 债券回购托管比表

**表对象ID**: 306
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | acode_account | 否 |  |  |
| 2 | trustee_ratio | 否 |  |  |
| 3 | full_name | 否 |  |  |
| 4 | secubond_im_ratio | 否 |  |  |
| 5 | trustee_ratio_relax | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | update_date | 否 |  |  |
| 8 | update_time | 否 |  |  |
| 9 | acode_account | 否 |  |  |
| 10 | trustee_ratio | 否 |  |  |
| 11 | full_name | 否 |  |  |
| 12 | secubond_im_ratio | 否 |  |  |
| 13 | trustee_ratio_relax | 否 |  |  |
| 14 | transaction_no | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_bondtrusteeratio | ART | 是 | acode_account, acode_account |
| idx_bondtrusteeratio | ART | 是 | acode_account, acode_account |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_bondtrusteeratio | acode_account, acode_account |
| idx_bondtrusteeratio | acode_account, acode_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-20 13:23:51 | 3.0.6.114 | 李想 | 物理表bond_trustee_ratio，添加了表字段(update_date);
物理表bond_trustee_... |
| 2024-07-18 11:19:14 | 3.0.2.23 | 张云焘 | 物理表bond_trustee_ratio，添加了表字段(transaction_no);
 |
| 2025-02-20 13:23:51 | 3.0.6.114 | 李想 | 物理表bond_trustee_ratio，添加了表字段(update_date);
物理表bond_trustee_... |
| 2024-07-18 11:19:14 | 3.0.2.23 | 张云焘 | 物理表bond_trustee_ratio，添加了表字段(transaction_no);
 |

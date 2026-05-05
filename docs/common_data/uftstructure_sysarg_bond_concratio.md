# bond_concratio - 单一发行人信用类债券入库担保集中度信息表

**表对象ID**: 315
**所属模块**: sysarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | sebd_conc_ratio_no | 否 |  |  |
| 2 | adlm_undue_bal_beg | 否 |  |  |
| 3 | adlm_undue_bal_end | 否 |  |  |
| 4 | sebd_conc_ratio | 否 |  |  |
| 5 | transaction_no | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | sebd_conc_ratio_no | 否 |  |  |
| 9 | adlm_undue_bal_beg | 否 |  |  |
| 10 | adlm_undue_bal_end | 否 |  |  |
| 11 | sebd_conc_ratio | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |

## 索引（共 4 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_secubdccrtinfo | 默认 | 否 | sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end, sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end |
| idx_secubdccrtinfo | ART | 是 | sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end, sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end |
| idx_secubdccrtinfo | 默认 | 否 | sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end, sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end |
| idx_secubdccrtinfo | ART | 是 | sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end, sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_secubdccrtinfo | sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end, sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end |
| idx_secubdccrtinfo | sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end, sebd_conc_ratio_no, adlm_undue_bal_beg, adlm_undue_bal_end |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-03-17 16:03:02 | 3.0.6.126 | 李想 | 物理表bond_concratio，添加了表字段(update_date);
物理表bond_concratio，添加... |
| 2024-07-18 11:16:16 | 3.0.2.23 | 张云焘 | 物理表bond_concratio，添加了表字段(transaction_no);
 |
| 2023-12-17 20:30:07 | 3.0.0.260 | 全春辉 | 物理表增加索引 |
| 2025-03-17 16:03:02 | 3.0.6.126 | 李想 | 物理表bond_concratio，添加了表字段(update_date);
物理表bond_concratio，添加... |
| 2024-07-18 11:16:16 | 3.0.2.23 | 张云焘 | 物理表bond_concratio，添加了表字段(transaction_no);
 |
| 2023-12-17 20:30:07 | 3.0.0.260 | 全春辉 | 物理表增加索引 |

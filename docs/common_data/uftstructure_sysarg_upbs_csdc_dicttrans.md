# upbs_csdc_dicttrans - 中登字典转换表

**表对象ID**: 352
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 否 |  |  |
| 2 | dict_entry | 否 |  |  |
| 3 | access_level | 否 |  |  |
| 4 | trans_flag | 否 |  |  |
| 5 | subentry | 否 |  |  |
| 6 | subentry_out | 否 |  |  |
| 7 | remark | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | dict_entry | 否 |  |  |
| 11 | access_level | 否 |  |  |
| 12 | trans_flag | 否 |  |  |
| 13 | subentry | 否 |  |  |
| 14 | subentry_out | 否 |  |  |
| 15 | remark | 否 |  |  |
| 16 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_csdcdicttrans | ART | 是 | dict_entry, trans_flag, exchange_type, subentry, subentry_out, dict_entry, trans_flag, exchange_type, subentry, subentry_out |
| idx_csdcdicttrans | ART | 是 | dict_entry, trans_flag, exchange_type, subentry, subentry_out, dict_entry, trans_flag, exchange_type, subentry, subentry_out |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_csdcdicttrans | dict_entry, trans_flag, exchange_type, subentry, subentry_out, dict_entry, trans_flag, exchange_type, subentry, subentry_out |
| idx_csdcdicttrans | dict_entry, trans_flag, exchange_type, subentry, subentry_out, dict_entry, trans_flag, exchange_type, subentry, subentry_out |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-12-05 16:39:54 | 3.0.2.33 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.32 | 范文浩 | 补充物理表索引 |
| 2024-10-23 14:43:41 | 3.0.4.3 | wuxd | 新增 |
| 2024-12-05 16:39:54 | 3.0.2.33 | 范文浩 | 勾选不回库 |
| 2024-11-29 17:43:37 | 3.0.2.32 | 范文浩 | 补充物理表索引 |
| 2024-10-23 14:43:41 | 3.0.4.3 | wuxd | 新增 |

# client_agreement - 客户协议控制表

**表对象ID**: 5534
**所属模块**: sestrade
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 12 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | client_id | 否 |  |  |
| 2 | agree_type | 否 |  |  |
| 3 | begin_date | 否 |  |  |
| 4 | end_date | 否 |  |  |
| 5 | agree_sub_type | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | client_id | 否 |  |  |
| 8 | agree_type | 否 |  |  |
| 9 | begin_date | 否 |  |  |
| 10 | end_date | 否 |  |  |
| 11 | agree_sub_type | 否 |  |  |
| 12 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_agreementctrl | ART | 是 | client_id, agree_type, agree_sub_type, client_id, agree_type, agree_sub_type |
| idx_agreementctrl | ART | 是 | client_id, agree_type, agree_sub_type, client_id, agree_type, agree_sub_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_agreementctrl | client_id, agree_type, agree_sub_type, client_id, agree_type, agree_sub_type |
| idx_agreementctrl | client_id, agree_type, agree_sub_type, client_id, agree_type, agree_sub_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-09 13:51:01 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-05-29 21:25:43 | 3.0.2.15 | 祝丁恺 | 勾选不回库选项 |
| 2024-05-11 14:37:52 | 3.0.2.6 | 阮善宏 | 内存表删除idx_agreementctrl_pos索引 |
| 2024-05-11 14:36:15 | 3.0.2.6 | 阮善宏 | 物理表client_agreement，删除了表字段(position_str);
 |
| 2024-05-09 13:25:47 | 3.0.2.6 | 阮善宏 | 物理表client_agreement，添加了表字段(transaction_no);
 |
| 2026-03-09 13:51:01 | V3.0.2.106 | taocong45644 | 勾选回库使用索引 |
| 2024-05-29 21:25:43 | 3.0.2.15 | 祝丁恺 | 勾选不回库选项 |
| 2024-05-11 14:37:52 | 3.0.2.6 | 阮善宏 | 内存表删除idx_agreementctrl_pos索引 |
| 2024-05-11 14:36:15 | 3.0.2.6 | 阮善宏 | 物理表client_agreement，删除了表字段(position_str);
 |
| 2024-05-09 13:25:47 | 3.0.2.6 | 阮善宏 | 物理表client_agreement，添加了表字段(transaction_no);
 |

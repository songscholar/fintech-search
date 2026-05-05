# usps_pertrans_bindparam - 客户报盘绑定关系表

**表对象ID**: 89
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | fund_account | 否 |  |  |
| 2 | exchange_type | 否 |  |  |
| 3 | report_account | 否 |  |  |
| 4 | seat_no | 否 |  |  |
| 5 | trans_name | 否 |  |  |
| 6 | transplat_type | 否 |  |  |
| 7 | transaction_no | 否 |  |  |
| 8 | fund_account | 否 |  |  |
| 9 | exchange_type | 否 |  |  |
| 10 | report_account | 否 |  |  |
| 11 | seat_no | 否 |  |  |
| 12 | trans_name | 否 |  |  |
| 13 | transplat_type | 否 |  |  |
| 14 | transaction_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_usps_pertrans_bindparam | ART | 是 | report_account, seat_no, transplat_type, report_account, seat_no, transplat_type |
| idx_usps_pertrans_bindparam | ART | 是 | report_account, seat_no, transplat_type, report_account, seat_no, transplat_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_usps_pertrans_bindparam | report_account, seat_no, transplat_type, report_account, seat_no, transplat_type |
| idx_usps_pertrans_bindparam | report_account, seat_no, transplat_type, report_account, seat_no, transplat_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-05-29 21:29:31 | 3.0.2.12 | 祝丁恺 | 勾选不回库选项 |
| 2023-11-20 22:46:24 | V3.0.1.17 | 楼欣欣 | 新增客户报盘绑定关系表，供报盘拉取报盘绑定信息 |
| 2024-05-29 21:29:31 | 3.0.2.12 | 祝丁恺 | 勾选不回库选项 |
| 2023-11-20 22:46:24 | V3.0.1.17 | 楼欣欣 | 新增客户报盘绑定关系表，供报盘拉取报盘绑定信息 |

# upbs_sysconfig - 系统配置参数表

**表对象ID**: 6
**所属模块**: sysarg
**数据空间**: HS_UFT_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 否 |  |  |
| 2 | char_config | 否 |  |  |
| 3 | config_no | 否 |  |  |
| 4 | config_type | 否 |  |  |
| 5 | data_type | 否 |  |  |
| 6 | int_config | 否 |  |  |
| 7 | str_config | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | transaction_str | 否 |  |  |
| 10 | branch_no | 否 |  |  |
| 11 | char_config | 否 |  |  |
| 12 | config_no | 否 |  |  |
| 13 | config_type | 否 |  |  |
| 14 | data_type | 否 |  |  |
| 15 | int_config | 否 |  |  |
| 16 | str_config | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | transaction_str | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_sysconfig | ART | 是 | branch_no, config_no, branch_no, config_no |
| idx_sysconfig | ART | 是 | branch_no, config_no, branch_no, config_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_sysconfig | branch_no, config_no, branch_no, config_no |
| idx_sysconfig | branch_no, config_no, branch_no, config_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-01-05 14:02:09 | 8.26.2.103 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-06-13 14:51:57 | 3.0.6.1003 | 汪迎 | 物理表upbs_sysconfig，添加了表字段(transaction_str);
 |
| 2025-04-17 13:29:28 | 3.0.6.131 | 常行 | 修改表空间为hs_uarg |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-06 16:00 | 0.0.0.5 | 吴威 | 新增字段transaction_no |
| 2016-09-22 16:59 | 0.0.0.1 | 吴斌扬 | 索引顺序移动 |
| 2015-01-22 09:36 | 0.0.0.1 | 万修远 | 交换索引idx_sysconfig的两个索引字段的先后顺序 |
| 2014-12-27 18:43 | 0.0.0.1 | 叶玉林 | 新增double_config，删除str_config，remark |
| 2013-02-26 11:30 | 0.0.0.1 | 周平 | 增加order_no字段 |
| 2026-01-05 14:02:09 | 8.26.2.103 | 汪杰 | 表空间修改为hs_uft_data |
| 2025-06-13 14:51:57 | 3.0.6.1003 | 汪迎 | 物理表upbs_sysconfig，添加了表字段(transaction_str);
 |
| 2025-04-17 13:29:28 | 3.0.6.131 | 常行 | 修改表空间为hs_uarg |
| 2025-04-25 17:23:28 | 3.0.2.86 | 钟兆星 | 全局唯一索引调整为ART索引类型 |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |

> 共 20 条修改记录，仅显示最近15条

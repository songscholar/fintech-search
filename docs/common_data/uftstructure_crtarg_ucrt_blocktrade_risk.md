# ucrt_blocktrade_risk - 大宗交易检查参数表

**表对象ID**: 7017
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 14 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | crdtblocktraderisk_no | 否 |  |  |
| 2 | aim_value | 否 |  |  |
| 3 | enable_status | 否 |  |  |
| 4 | transaction_no | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | crdtblocktraderisk_no | 否 |  |  |
| 9 | aim_value | 否 |  |  |
| 10 | enable_status | 否 |  |  |
| 11 | transaction_no | 否 |  |  |
| 12 | remark | 否 |  |  |
| 13 | update_date | 否 |  |  |
| 14 | update_time | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_blocktrade_risk | ART | 是 | crdtblocktraderisk_no, crdtblocktraderisk_no |
| idx_ucrt_blocktrade_risk | ART | 是 | crdtblocktraderisk_no, crdtblocktraderisk_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_blocktrade_risk | crdtblocktraderisk_no, crdtblocktraderisk_no |
| idx_ucrt_blocktrade_risk | crdtblocktraderisk_no, crdtblocktraderisk_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-18 16:42:40 | 3.0.6.114 | 李奕轩 | 物理表ucrt_blocktrade_risk，添加了表字段(remark);
物理表ucrt_blocktrade_... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-07-18 16:42:40 | 3.0.6.114 | 李奕轩 | 物理表ucrt_blocktrade_risk，添加了表字段(remark);
物理表ucrt_blocktrade_... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

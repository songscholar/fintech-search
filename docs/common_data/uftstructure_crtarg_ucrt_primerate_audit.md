# ucrt_primerate_audit - 优惠利率审批参数表

**表对象ID**: 7014
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 32 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | primerate_param_type | 否 |  |  |
| 2 | primerate_audit_status | 否 |  |  |
| 3 | min_crdtaudit_value | 否 |  |  |
| 4 | max_crdtaudit_value | 否 |  |  |
| 5 | min_openmonths | 否 |  |  |
| 6 | max_openmonths | 否 |  |  |
| 7 | min_primerate | 否 |  |  |
| 8 | max_primerate | 否 |  |  |
| 9 | primerate_audit_type | 否 |  |  |
| 10 | crdt_param_type | 否 |  |  |
| 11 | compact_type | 否 |  |  |
| 12 | transaction_no | 否 |  |  |
| 13 | remark | 否 |  |  |
| 14 | update_date | 否 |  |  |
| 15 | update_time | 否 |  |  |
| 16 | en_branch_no | 否 |  |  |
| 17 | primerate_param_type | 否 |  |  |
| 18 | primerate_audit_status | 否 |  |  |
| 19 | min_crdtaudit_value | 否 |  |  |
| 20 | max_crdtaudit_value | 否 |  |  |
| 21 | min_openmonths | 否 |  |  |
| 22 | max_openmonths | 否 |  |  |
| 23 | min_primerate | 否 |  |  |
| 24 | max_primerate | 否 |  |  |
| 25 | primerate_audit_type | 否 |  |  |
| 26 | crdt_param_type | 否 |  |  |
| 27 | compact_type | 否 |  |  |
| 28 | transaction_no | 否 |  |  |
| 29 | remark | 否 |  |  |
| 30 | update_date | 否 |  |  |
| 31 | update_time | 否 |  |  |
| 32 | en_branch_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_ucrt_primerate_audit | ART | 是 | primerate_param_type, primerate_audit_type, compact_type, min_crdtaudit_value, max_crdtaudit_value, min_openmonths, max_openmonths, crdt_param_type, primerate_param_type, primerate_audit_type, compact_type, min_crdtaudit_value, max_crdtaudit_value, min_openmonths, max_openmonths, crdt_param_type |
| idx_ucrt_primerate_audit | ART | 是 | primerate_param_type, primerate_audit_type, compact_type, min_crdtaudit_value, max_crdtaudit_value, min_openmonths, max_openmonths, crdt_param_type, primerate_param_type, primerate_audit_type, compact_type, min_crdtaudit_value, max_crdtaudit_value, min_openmonths, max_openmonths, crdt_param_type |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_ucrt_primerate_audit | primerate_param_type, primerate_audit_type, compact_type, min_crdtaudit_value, max_crdtaudit_value, min_openmonths, max_openmonths, crdt_param_type, primerate_param_type, primerate_audit_type, compact_type, min_crdtaudit_value, max_crdtaudit_value, min_openmonths, max_openmonths, crdt_param_type |
| idx_ucrt_primerate_audit | primerate_param_type, primerate_audit_type, compact_type, min_crdtaudit_value, max_crdtaudit_value, min_openmonths, max_openmonths, crdt_param_type, primerate_param_type, primerate_audit_type, compact_type, min_crdtaudit_value, max_crdtaudit_value, min_openmonths, max_openmonths, crdt_param_type |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-14 15:10:04 | 3.0.2.2011 | huangzh | 物理表ucrt_primerate_audit，添加了表字段(en_branch_no);
 |
| 2025-02-13 17:15:13 | 3.0.6.36 |  | 物理表ucrt_primerate_audit，添加了表字段(remark);
物理表ucrt_primerate_a... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-07-13 13:49 | 0.3.3.125 | 程猛 | ucrt_primerate_audit表字段crdt_type调整为compact_type |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |
| 2025-07-14 15:10:04 | 3.0.2.2011 | huangzh | 物理表ucrt_primerate_audit，添加了表字段(en_branch_no);
 |
| 2025-02-13 17:15:13 | 3.0.6.36 |  | 物理表ucrt_primerate_audit，添加了表字段(remark);
物理表ucrt_primerate_a... |
| 2023-08-06 21:59 | 0.3.3.135 | 程猛 | 根据内存表索引增加物理表索引 |
| 2023-07-13 13:49 | 0.3.3.125 | 程猛 | ucrt_primerate_audit表字段crdt_type调整为compact_type |
| 2023-06-21 14:19 | 0.3.3.108 | 吴威 | 新增表字段transaction_no |

# coupon_stkgroup - 优惠券证券分组表

**表对象ID**: 7070
**所属模块**: crtarg
**数据空间**: HS_UARG_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | coupongrp_no | 否 |  |  |
| 2 | coupongrp_name | 否 |  |  |
| 3 | exchange_type | 否 |  |  |
| 4 | stock_code | 否 |  |  |
| 5 | remark | 否 |  |  |
| 6 | update_date | 否 |  |  |
| 7 | update_time | 否 |  |  |
| 8 | transaction_no | 否 |  |  |
| 9 | position_str | 否 |  | stock_code(8)+exchange_type(4)+coupongrp_no(10) |
| 10 | coupongrp_no | 否 |  |  |
| 11 | coupongrp_name | 否 |  |  |
| 12 | exchange_type | 否 |  |  |
| 13 | stock_code | 否 |  |  |
| 14 | remark | 否 |  |  |
| 15 | update_date | 否 |  |  |
| 16 | update_time | 否 |  |  |
| 17 | transaction_no | 否 |  |  |
| 18 | position_str | 否 |  | stock_code(8)+exchange_type(4)+coupongrp_no(10) |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_coupon_stkgroup | ART | 是 | stock_code, exchange_type, coupongrp_no, stock_code, exchange_type, coupongrp_no |
| idx_coupon_stkgroup | ART | 是 | stock_code, exchange_type, coupongrp_no, stock_code, exchange_type, coupongrp_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_coupon_stkgroup | stock_code, exchange_type, coupongrp_no, stock_code, exchange_type, coupongrp_no |
| idx_coupon_stkgroup | stock_code, exchange_type, coupongrp_no, stock_code, exchange_type, coupongrp_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-02-13 16:30:11 | 3.0.6.34 | 李想 | 新增表 |
| 2025-02-13 16:30:11 | 3.0.6.34 | 李想 | 新增表 |

# setttouftsoptwindow - 清算自主行权窗口表

**表对象ID**: 3001
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 10 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | exchange_type | 是 |  |  |
| 2 | sopt_code | 是 |  |  |
| 3 | begin_date | 是 |  |  |
| 4 | end_date | 是 |  |  |
| 5 | remark | 是 |  |  |
| 6 | exchange_type | 是 |  |  |
| 7 | sopt_code | 是 |  |  |
| 8 | begin_date | 是 |  |  |
| 9 | end_date | 是 |  |  |
| 10 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settsoptwindow | 默认 | 是 | sopt_code, exchange_type, begin_date, sopt_code, exchange_type, begin_date |
| idx_settsoptwindow | 默认 | 是 | sopt_code, exchange_type, begin_date, sopt_code, exchange_type, begin_date |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_soptwindow | sopt_code, exchange_type, begin_date, sopt_code, exchange_type, begin_date |
| idx_soptwindow | sopt_code, exchange_type, begin_date, sopt_code, exchange_type, begin_date |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2018-07-23 10:20 | 8.26.1.14 | 施凯 | 新增 |
| 2018-07-23 10:20 | 8.26.1.14 | 施凯 | 新增 |

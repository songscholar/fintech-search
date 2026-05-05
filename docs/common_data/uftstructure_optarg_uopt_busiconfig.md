# uopt_busiconfig - 期权业务参数表

**表对象ID**: 9010
**所属模块**: optarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 16 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | config_no | 是 |  | 为了同一业务便于区分，如果原先在系统配置中已有的配置参数，则延用系统配置编号； 若后续增加期权业务配置参数在系统配置参数 |
| 2 | config_name | 是 |  |  |
| 3 | data_type | 是 |  |  |
| 4 | abscondition_status | 是 |  |  |
| 5 | char_config | 是 |  |  |
| 6 | int_config | 是 |  |  |
| 7 | str_config | 是 |  |  |
| 8 | remark | 是 |  |  |
| 9 | config_no | 是 |  | 为了同一业务便于区分，如果原先在系统配置中已有的配置参数，则延用系统配置编号； 若后续增加期权业务配置参数在系统配置参数 |
| 10 | config_name | 是 |  |  |
| 11 | data_type | 是 |  |  |
| 12 | abscondition_status | 是 |  |  |
| 13 | char_config | 是 |  |  |
| 14 | int_config | 是 |  |  |
| 15 | str_config | 是 |  |  |
| 16 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_uopt_busiconfig | 默认 | 是 | config_no, config_no |
| idx_uopt_busiconfig | 默认 | 是 | config_no, config_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_uopt_busiconfig | config_no, config_no |
| idx_uopt_busiconfig | config_no, config_no |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-12-16 17:28:53 | 3.0.0.0 | wuxd |  |
| 2023-12-16 17:28:53 | 3.0.0.0 | wuxd |  |

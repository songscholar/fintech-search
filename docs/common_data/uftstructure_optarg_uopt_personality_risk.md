# uopt_personality_risk - 期权个性化风险参数表

**表对象ID**: 9009
**所属模块**: optarg
**数据空间**: HS_UFT_DATA

## 字段列表（共 26 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | optlabel_type | 是 |  |  |
| 2 | client_id | 是 |  |  |
| 3 | optrisk_no | 是 |  |  |
| 4 | fund_account | 是 |  |  |
| 5 | instant_risk_value | 是 |  |  |
| 6 | instant_risk_color | 是 |  |  |
| 7 | force_risk_value | 是 |  |  |
| 8 | force_risk_color | 是 |  |  |
| 9 | warn_risk_value | 是 |  |  |
| 10 | warn_risk_color | 是 |  |  |
| 11 | focus_risk_value | 是 |  |  |
| 12 | focus_risk_color | 是 |  |  |
| 13 | remark | 是 |  |  |
| 14 | optlabel_type | 是 |  |  |
| 15 | client_id | 是 |  |  |
| 16 | optrisk_no | 是 |  |  |
| 17 | fund_account | 是 |  |  |
| 18 | instant_risk_value | 是 |  |  |
| 19 | instant_risk_color | 是 |  |  |
| 20 | force_risk_value | 是 |  |  |
| 21 | force_risk_color | 是 |  |  |
| 22 | warn_risk_value | 是 |  |  |
| 23 | warn_risk_color | 是 |  |  |
| 24 | focus_risk_value | 是 |  |  |
| 25 | focus_risk_color | 是 |  |  |
| 26 | remark | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_optpersonalityrisk | 默认 | 是 | optlabel_type, fund_account, optrisk_no, optlabel_type, fund_account, optrisk_no |
| idx_optpersonalityrisk | 默认 | 是 | optlabel_type, fund_account, optrisk_no, optlabel_type, fund_account, optrisk_no |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_optpersonalityrisk | optlabel_type, optrisk_no, fund_account, optlabel_type, optrisk_no, fund_account |
| idx_optpersonalityrisk | optlabel_type, optrisk_no, fund_account, optlabel_type, optrisk_no, fund_account |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2023-12-16 17:28:48 | 3.0.0.0 | wuxd |  |
| 2023-12-16 17:28:48 | 3.0.0.0 | wuxd |  |

# upbs_elig_risk_match - 统一适当性风险等级匹配表

**表对象ID**: 85
**所属模块**: sysarg
**数据空间**: HS_USMS_DATA
**运行模式**: DB+MDB
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | organ_flag | 否 |  |  |
| 2 | corp_risk_level | 否 |  |  |
| 3 | en_prodrisk_level | 否 |  |  |
| 4 | force_risk_matchflag | 否 |  |  |
| 5 | busi_svr_kind_str | 否 |  |  |
| 6 | transaction_no | 否 |  |  |
| 7 | finance_type | 否 |  |  |
| 8 | prod_type | 否 |  |  |
| 9 | prodta_no | 否 |  |  |
| 10 | organ_flag | 否 |  |  |
| 11 | corp_risk_level | 否 |  |  |
| 12 | en_prodrisk_level | 否 |  |  |
| 13 | force_risk_matchflag | 否 |  |  |
| 14 | busi_svr_kind_str | 否 |  |  |
| 15 | transaction_no | 否 |  |  |
| 16 | finance_type | 否 |  |  |
| 17 | prod_type | 否 |  |  |
| 18 | prodta_no | 否 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_upbs_elig_risk_match | ART | 是 | organ_flag, corp_risk_level, organ_flag, corp_risk_level |
| idx_upbs_elig_risk_match | ART | 是 | organ_flag, corp_risk_level, organ_flag, corp_risk_level |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_upbs_elig_risk_match | organ_flag, corp_risk_level, organ_flag, corp_risk_level |
| idx_upbs_elig_risk_match | organ_flag, corp_risk_level, organ_flag, corp_risk_level |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-23 11:07:09 | 3.0.3.12 | 张明月 | 物理表upbs_elig_risk_match，添加了表字段(prodta_no);
物理表upbs_elig_ris... |
| 2023-11-10 10:18:42 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |
| 2024-09-23 11:07:09 | 3.0.3.12 | 张明月 | 物理表upbs_elig_risk_match，添加了表字段(prodta_no);
物理表upbs_elig_ris... |
| 2023-11-10 10:18:42 | V3.0.1.16 | 沈勋 | 新增表，支持适当性交易匹配 |

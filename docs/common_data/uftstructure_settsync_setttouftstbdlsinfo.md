# setttouftstbdlsinfo - 清算股转摘牌转让信息表

**表对象ID**: 3009
**所属模块**: settsync
**数据空间**: HS_UFT_DATA
**持久化**: true

## 字段列表（共 18 个）

| # | 字段名 | 允许为空 | 标记 | 备注 |
|---|--------|----------|------|------|
| 1 | branch_no | 是 |  |  |
| 2 | fund_account | 是 |  |  |
| 3 | exchange_type | 是 |  |  |
| 4 | entrust_bs | 是 |  |  |
| 5 | stock_code | 是 |  |  |
| 6 | stock_account | 是 |  |  |
| 7 | entrust_date | 是 |  |  |
| 8 | date_clear | 是 |  |  |
| 9 | uft_data_change_status | 是 |  |  |
| 10 | branch_no | 是 |  |  |
| 11 | fund_account | 是 |  |  |
| 12 | exchange_type | 是 |  |  |
| 13 | entrust_bs | 是 |  |  |
| 14 | stock_code | 是 |  |  |
| 15 | stock_account | 是 |  |  |
| 16 | entrust_date | 是 |  |  |
| 17 | date_clear | 是 |  |  |
| 18 | uft_data_change_status | 是 |  |  |

## 索引（共 2 个）

| 索引名 | 类型 | 全局 | 字段 |
|--------|------|------|------|
| idx_settstbdlsinfo | 默认 | 是 | fund_account, stock_account, exchange_type, stock_code, entrust_bs, fund_account, stock_account, exchange_type, stock_code, entrust_bs |
| idx_settstbdlsinfo | 默认 | 是 | fund_account, stock_account, exchange_type, stock_code, entrust_bs, fund_account, stock_account, exchange_type, stock_code, entrust_bs |

## 数据库索引（共 2 个）

| 索引名 | 字段 |
|--------|------|
| idx_settstbdlsinfo | fund_account, stock_account, exchange_type, stock_code, entrust_bs, fund_account, stock_account, exchange_type, stock_code, entrust_bs |
| idx_settstbdlsinfo | fund_account, stock_account, exchange_type, stock_code, entrust_bs, fund_account, stock_account, exchange_type, stock_code, entrust_bs |

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2021-06-29 16:17 | 8.26.2.1 | 罗佳楠 | 新增 |
| 2021-06-29 16:17 | 8.26.2.1 | 罗佳楠 | 新增 |

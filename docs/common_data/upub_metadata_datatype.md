# upub - 业务数据类型

业务数据类型定义，包含类型名称、中文名、标准类型、长度、精度等。

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-05-19 19:33:00 | V3.0.5.1005 | 张明月 | 新增数据类型HSApiBalance、HSApiVolume、HSApiPrice |
| 2024-11-04 21:28:05 | V3.0.5.1004 | 李海洋 | double类型标准字段统一更新 |
| 2024-10-31 19:30:16 | V3.0.5.1003 | 谢宗艺 | 新增数据类型HsChar1000 |
| 2024-10-30 20:07:25 | V3.0.5.1002 | 李海洋 | 新增数据类型HsProportion,double业务数据类型统一调整为与UF20一致 |
| 2024-10-29 17:24:00 | V3.0.5.1001 | 陆良铠 | HsStation数据类型长度由255调整为500 |
| 2024-12-18 18:16:27 | V3.0.1.3 | 刘景锋 | 新增数据类型HsProportion |
| 2023-12-14 15:16:45 | V3.0.1.2 | 楼欣欣 | 新增数据类型HsUnpackerV3 |
| 2023-09-04 14:32:17 | V3.0.1.1 | 沈勋 | 版本统一调整 |
| 2023-08-29 23:35:32 | 3.0.0.4 | 李海洋 | RPC无感调用支持pack出参用的unpack标准字段 |
| 2023-08-23 18:04:21 | 3.0.0.3 | 雷玄 | HsSerialNo、HsSerialID调整为Int32 |
| 2023-08-14 13:46 | 3.0.0.2 | nigang | 新增数据类型HsPackerV4 |
| 2023-03-21 15:36 | 3.0.0.1 | 陈盛志 | 初始版本号 |


## 类型列表（共 310 个）

| 名称 | 中文名 | 标准类型 | 长度 | 精度 | 默认值 |
|------|--------|----------|------|------|--------|
| HsStatus | 状态 | Char |  |  | SPACE_CHAR |
| HsType | 类别 | Char |  |  | SPACE_CHAR |
| HsFlag | 标志 | Char |  |  | SPACE_CHAR |
| HsClob | 字符对象类型 | Clob |  |  | NULL |
| HsDateTime | 日期时间 | String | 20 |  | EMPTY_STR |
| HsNum2 | 数字2 | Int32 |  |  | I_ZERO |
| HsNum3 | 数字3 | Int32 |  |  | I_ZERO |
| HsNum4 | 数字4 | Int32 |  |  | I_ZERO |
| HsFundPrice | 价格（基金） | Double | 9 | 4 | D_ZERO |
| HsRate | 费率 | Double | 9 | 8 | D_ZERO |
| HsBranchNo | 分支编号 | Int32 |  |  | I_ZERO |
| HsClientGroup | 客户类别 | Int32 |  |  | I_ZERO |
| HsRoomCode | 客户室号 | Int32 |  |  | I_ZERO |
| HsRoomID | 客户室号 | Int32 |  |  | I_ZERO |
| HsDate | 日期 | Int32 |  |  | TODAY |
| HsTime | 时间 | Int32 |  |  | NOW |
| HsStationNo | 站点编号 | Int32 |  |  | I_ZERO |
| HsStationID | 站点编号 | Int32 |  |  | I_ZERO |
| HsSerialNo | 流水号 | Int32 |  |  | I_ZERO |
| HsSerialID | 流水号 | Int32 |  |  | I_ZERO |
| HsFunctionNo | 功能号 | Int32 |  |  | I_ZERO |
| HsFunctionID | 功能号 | Int32 |  |  | I_ZERO |
| HsBusinessFlag | 业务标志 | Int32 |  |  | I_ZERO |
| HsNum | 整数 | Int32 |  |  | I_ZERO |
| HsNumID | 数字编号 | Int32 |  |  | I_ZERO |
| HsNum10 | 数字10  | Int32 |  |  | I_ZERO |
| HsPosInt | 定位串 | Int32 |  |  | I_ZERO |
| HsHighRate | 高精度费率 | Double | 14 | 13 | D_ZERO |
| HsHighPrice | 高精度价格 | Double | 15 | 8 | D_ZERO |
| HsPrice | 价格 | Double | 18 | 3 | D_ZERO |
| HsQuantity | 数量 | Double | 19 | 2 | D_ZERO |
| HsAmount | 金额 | Double | 19 | 2 | D_ZERO |
| HsBit | Bit位 | Double | 12 | 0 | D_ZERO |
| HsRisk | 风险 | Double | 16 | 4 | D_ZERO |
| HsAcctNo | 帐号 | Double | 19 | 1 | D_ZERO |
| HsFundQty | 基金份额 | Double | 19 | 2 | D_ZERO |
| HsFutuPrice | 价格（期货） | Double | 12 | 6 | D_ZERO |
| HsRecoupRate | 补偿比率 | Double | 15 | 8 | D_ZERO |
| HsChar2 | 字符2 | String | 2 |  | EMPTY_STR |
| HsChar3 | 字符3 | String | 3 |  | EMPTY_STR |
| HsChar4 | 字符4 | String | 4 |  | EMPTY_STR |
| HsChar6 | 字符6 | String | 6 |  | EMPTY_STR |
| HsChar8 | 字符8 | String | 8 |  | EMPTY_STR |
| HsChar10 | 字符10 | String | 10 |  | EMPTY_STR |
| HsChar16 | 字符16 | String | 16 |  | EMPTY_STR |
| HsChar18 | 字符18 | String | 18 |  | EMPTY_STR |
| HsChar19 | 字符19 | String | 19 |  | EMPTY_STR |
| HsChar20 | 字符20 | String | 20 |  | EMPTY_STR |
| HsChar24 | 字符24 | String | 24 |  | EMPTY_STR |
| HsChar32 | 字符32 | String | 32 |  | EMPTY_STR |
| HsChar64 | 字符64 | String | 64 |  | EMPTY_STR |
| HsChar100 | 字符100 | String | 100 |  | EMPTY_STR |
| HsChar120 | 字符120 | String | 120 |  | EMPTY_STR |
| HsChar128 | 字符128 | String | 128 |  | EMPTY_STR |
| HsChar255 | 字符255 | String | 255 |  | EMPTY_STR |
| HsChar500 | 字符500 | String | 500 |  | EMPTY_STR |
| HsChar2000 | 字符2000 | String | 2000 |  | EMPTY_STR |
| HsChar4000 | 字符4000 | String | 4000 |  | EMPTY_STR |
| HsChar8000 | 字符8000 | String | 8000 |  | EMPTY_STR |
| HsChar16000 | 字符16000 | String | 16000 |  | EMPTY_STR |
| HsAbstract | 备注 | String | 2000 |  | EMPTY_STR |
| HsAddress | 地址 | String | 120 |  | EMPTY_STR |
| HsMoneyType | 币种 | String | 3 |  | EMPTY_STR |
| HsStockType | 股票类别 | String | 4 |  | EMPTY_STR |
| HsExchangeType | 交易类别 | String | 4 |  | EMPTY_STR |
| HsBankID | 银行号 | String | 6 |  | EMPTY_STR |
| HsStockCode | 产品代码 | String | 8 |  | EMPTY_STR |
| HsZip | 邮编 | String | 6 |  | EMPTY_STR |
| HsSeatID | 席位号 | String | 8 |  | EMPTY_STR |
| HsFuturesAccount | 期货账号 | String | 12 |  | EMPTY_STR |
| HsBondCode | 债券代码 | String | 12 |  | EMPTY_STR |
| HsStockAccount | 交易账号 | String | 20 |  | EMPTY_STR |
| HsPassword | 密码 | String | 15 |  | EMPTY_STR |
| HsClientID | 客户编号 | String | 18 |  | EMPTY_STR |
| HsFundAccount | 资产账号 | String | 18 |  | EMPTY_STR |
| HsBankSerialID | 银行流水号 | String | 20 |  | EMPTY_STR |
| HsBankClientID | 客户账号（银行用） | String | 22 |  | EMPTY_STR |
| HsFuturesCode | 期货代码 | String | 30 |  | EMPTY_STR |
| HsPhone | 电话号码 | String | 32 |  | EMPTY_STR |
| HsBankAccount | 银行账号 | String | 32 |  | EMPTY_STR |
| HsPosStr | 字符型定位串 | String | 100 |  | EMPTY_STR |
| HsStockName | 产品名称 | String | 48 |  | EMPTY_STR |
| HsIDNo | 证件号码 | String | 40 |  | EMPTY_STR |
| HsIDENTITY | 证件号码 | String | 32 |  | EMPTY_STR |
| HsCardID | 资金卡号 | String | 32 |  | EMPTY_STR |
| HsFundstkAccount | 开放式基金交易账号 | String | 32 |  | EMPTY_STR |
| HsToken | 用户口令 | String | 512 |  | EMPTY_STR |
| HsName | 姓名 | String | 60 |  | EMPTY_STR |
| HsEnPassword | 增强型密码 | String | 64 |  | EMPTY_STR |
| HsStation | 站点地址 | String | 500 |  | EMPTY_STR |
| HsName2 | 名称 | String | 64 |  | EMPTY_STR |
| HsBondAccount | 债券账号 | String | 18 |  | EMPTY_STR |
| HsFutuCodeType | 合约代码类别 | String | 8 |  | EMPTY_STR |
| HsCursor | 游标 | Cursor |  |  | NULL |
| HsChar255List | 字符255数组 | Void |  |  | voidDefaultValue |
| HsQuantityList | 数量数组 | Void |  |  | voidDefaultValue |
| HsAmountList | 金额数组 | Void |  |  | voidDefaultValue |
| HsRateList | 利率数组 | Void |  |  | voidDefaultValue |
| HsPriceList | 价格数组 | Void |  |  | voidDefaultValue |
| HsNumList | 数据类型 | Void |  |  | voidDefaultValue |
| HsName3 | 字符120 | String | 120 |  | EMPTY_STR |
| HsOptCode | 期权合约编码 | String | 8 |  | EMPTY_STR |
| HsProdCode | 产品代码 | String | 32 |  | EMPTY_STR |
| HsOptName | 期权合约简称 | String | 128 |  | EMPTY_STR |
| HsSdcCode | 登记权益代码 | String | 32 |  | EMPTY_STR |
| HsSdcName | 登记权益名称 | String | 32 |  | EMPTY_STR |
| HsSdcAccount | 登记权益账号 | String | 32 |  | EMPTY_STR |
| HsSdcType | 登记权益类别 | String | 4 |  | EMPTY_STR |
| HsProdAccount | 产品账号 | String | 18 |  | EMPTY_STR |
| HsMchCode | 交易撮合代码 | String | 32 |  | EMPTY_STR |
| HsOtcType | 权益类别 | String | 4 |  | EMPTY_STR |
| HsOtcAccount | 权益账号 | String | 32 |  | EMPTY_STR |
| HsOtcCode | 权益代码 | String | 32 |  | EMPTY_STR |
| HsMchType | 交易撮合类别 | String | 4 |  | EMPTY_STR |
| HsMchAccount | 交易撮合账号 | String | 32 |  | EMPTY_STR |
| HsOtcName | 权益名称 | String | 32 |  | EMPTY_STR |
| HsPacker | 打包器 | CPacker |  |  | CPackerDefaultValue |
| HsUnpacker | 解包器 | CUnpacker |  |  | CUnpackerExDefaultValue |
| HsEntrustProp | 委托属性 | String | 4 |  | EMPTY_STR |
| HsEntrustReference | 委托引用 | String | 32 |  | EMPTY_STR |
| HsCompactId | 两融合约编号 | String | 32 |  | EMPTY_STR |
| HsSessionNo | 会话编号 | Int32 |  |  | I_ZERO |
| HsBusinessId | 成交编号 | String | 32 |  | EMPTY_STR |
| HsCancelInfo | 废单原因 | String | 255 |  | EMPTY_STR |
| HsEntrustId | 委托编号 | String | 16 |  | EMPTY_STR |
| HsErrorInfo | 错误提示 | String | 500 |  | EMPTY_STR |
| HsAcodeAccount | 一码通账户 | String | 20 |  | EMPTY_STR |
| HsPrice1 | 价格 | Double | 19 | 4 | D_ZERO |
| HsChar100000 | 字符100000 | String | 100000 |  | EMPTY_STR |
| HsHighPrice2 | 高精度价格 | Double | 23 | 8 | D_ZERO |
| HsChar502 | 字符502 | String | 502 |  | EMPTY_STR |
| HsSecuCode | 证券代码 | String | 32 |  | EMPTY_STR |
| HsChar300 | 字符300 | String | 300 |  | EMPTY_STR |
| HsMicroTime | 微秒级时间 | Int64 |  |  | I_ZERO |
| HsHighQuantity | 高精度数量 | Double | 23 | 6 | D_ZERO |
| HsChar36 | 字符36 | String | 36 |  | EMPTY_STR |
| HsName4 | 名称 | String | 180 |  | EMPTY_STR |
| HsAddress1 | 地址 | String | 180 |  | EMPTY_STR |
| HsChar30 | 字符30 | String | 30 |  | EMPTY_STR |
| HsName5 | 账户简称 | String | 90 |  | EMPTY_STR |
| HsChar32000 | 字符32000 | String | 32000 |  | EMPTY_STR |
| HsUnpackerV4 | PackV4解包器 | CUnpacker |  |  | CUnpackerExV4DefaultValue |
| HsPackerV4 | PackV4打包器 | CPacker |  |  | CpackerV4DefaultValue |
| HsUnpackerNull | 空Pack解包器 | CUnpacker |  |  | NULL |
| HsNum64 | 数字(int64) | Int64 |  |  | I_ZERO |
| HsUnpackerV3 | PackV3解包器 | CUnpacker |  |  | CUnpackerExV3DefaultValue |
| HsAddress2 | 地址 | String | 255 |  | EMPTY_STR |
| HsHighRisk | 高精度风险 | Double | 19 | 9 | D_ZERO |
| HsUNum64 | uint64 | UINT64 |  |  | I_ZERO |
| HsProportion | 比例 | Double | 21 | 4 | D_ZERO |
| HsChar1000 | 字符1000 | String | 1000 |  | EMPTY_STR |
| HsFutuPricePlus | 价格期货(扩展) | Double | 18 | 6 | D_ZERO |
| HSApiBalance | 金额 | Double | 19 | 2 | D_ZERO |
| HSApiVolume | 数量 | Double | 19 | 2 | D_ZERO |
| HSApiPrice | 价格 | Double | 12 | 6 | D_ZERO |
| HsStatus | 状态 | Char |  |  | SPACE_CHAR |
| HsType | 类别 | Char |  |  | SPACE_CHAR |
| HsFlag | 标志 | Char |  |  | SPACE_CHAR |
| HsClob | 字符对象类型 | Clob |  |  | NULL |
| HsDateTime | 日期时间 | String | 20 |  | EMPTY_STR |
| HsNum2 | 数字2 | Int32 |  |  | I_ZERO |
| HsNum3 | 数字3 | Int32 |  |  | I_ZERO |
| HsNum4 | 数字4 | Int32 |  |  | I_ZERO |
| HsFundPrice | 价格（基金） | Double | 9 | 4 | D_ZERO |
| HsRate | 费率 | Double | 9 | 8 | D_ZERO |
| HsBranchNo | 分支编号 | Int32 |  |  | I_ZERO |
| HsClientGroup | 客户类别 | Int32 |  |  | I_ZERO |
| HsRoomCode | 客户室号 | Int32 |  |  | I_ZERO |
| HsRoomID | 客户室号 | Int32 |  |  | I_ZERO |
| HsDate | 日期 | Int32 |  |  | TODAY |
| HsTime | 时间 | Int32 |  |  | NOW |
| HsStationNo | 站点编号 | Int32 |  |  | I_ZERO |
| HsStationID | 站点编号 | Int32 |  |  | I_ZERO |
| HsSerialNo | 流水号 | Int32 |  |  | I_ZERO |
| HsSerialID | 流水号 | Int32 |  |  | I_ZERO |
| HsFunctionNo | 功能号 | Int32 |  |  | I_ZERO |
| HsFunctionID | 功能号 | Int32 |  |  | I_ZERO |
| HsBusinessFlag | 业务标志 | Int32 |  |  | I_ZERO |
| HsNum | 整数 | Int32 |  |  | I_ZERO |
| HsNumID | 数字编号 | Int32 |  |  | I_ZERO |
| HsNum10 | 数字10  | Int32 |  |  | I_ZERO |
| HsPosInt | 定位串 | Int32 |  |  | I_ZERO |
| HsHighRate | 高精度费率 | Double | 14 | 13 | D_ZERO |
| HsHighPrice | 高精度价格 | Double | 15 | 8 | D_ZERO |
| HsPrice | 价格 | Double | 18 | 3 | D_ZERO |
| HsQuantity | 数量 | Double | 19 | 2 | D_ZERO |
| HsAmount | 金额 | Double | 19 | 2 | D_ZERO |
| HsBit | Bit位 | Double | 12 | 0 | D_ZERO |
| HsRisk | 风险 | Double | 16 | 4 | D_ZERO |
| HsAcctNo | 帐号 | Double | 19 | 1 | D_ZERO |
| HsFundQty | 基金份额 | Double | 19 | 2 | D_ZERO |
| HsFutuPrice | 价格（期货） | Double | 12 | 6 | D_ZERO |
| HsRecoupRate | 补偿比率 | Double | 15 | 8 | D_ZERO |
| HsChar2 | 字符2 | String | 2 |  | EMPTY_STR |
| HsChar3 | 字符3 | String | 3 |  | EMPTY_STR |
| HsChar4 | 字符4 | String | 4 |  | EMPTY_STR |
| HsChar6 | 字符6 | String | 6 |  | EMPTY_STR |
| HsChar8 | 字符8 | String | 8 |  | EMPTY_STR |
| HsChar10 | 字符10 | String | 10 |  | EMPTY_STR |
| HsChar16 | 字符16 | String | 16 |  | EMPTY_STR |
| HsChar18 | 字符18 | String | 18 |  | EMPTY_STR |
| HsChar19 | 字符19 | String | 19 |  | EMPTY_STR |
| HsChar20 | 字符20 | String | 20 |  | EMPTY_STR |
| HsChar24 | 字符24 | String | 24 |  | EMPTY_STR |
| HsChar32 | 字符32 | String | 32 |  | EMPTY_STR |
| HsChar64 | 字符64 | String | 64 |  | EMPTY_STR |
| HsChar100 | 字符100 | String | 100 |  | EMPTY_STR |
| HsChar120 | 字符120 | String | 120 |  | EMPTY_STR |
| HsChar128 | 字符128 | String | 128 |  | EMPTY_STR |
| HsChar255 | 字符255 | String | 255 |  | EMPTY_STR |
| HsChar500 | 字符500 | String | 500 |  | EMPTY_STR |
| HsChar2000 | 字符2000 | String | 2000 |  | EMPTY_STR |
| HsChar4000 | 字符4000 | String | 4000 |  | EMPTY_STR |
| HsChar8000 | 字符8000 | String | 8000 |  | EMPTY_STR |
| HsChar16000 | 字符16000 | String | 16000 |  | EMPTY_STR |
| HsAbstract | 备注 | String | 2000 |  | EMPTY_STR |
| HsAddress | 地址 | String | 120 |  | EMPTY_STR |
| HsMoneyType | 币种 | String | 3 |  | EMPTY_STR |
| HsStockType | 股票类别 | String | 4 |  | EMPTY_STR |
| HsExchangeType | 交易类别 | String | 4 |  | EMPTY_STR |
| HsBankID | 银行号 | String | 6 |  | EMPTY_STR |
| HsStockCode | 产品代码 | String | 8 |  | EMPTY_STR |
| HsZip | 邮编 | String | 6 |  | EMPTY_STR |
| HsSeatID | 席位号 | String | 8 |  | EMPTY_STR |
| HsFuturesAccount | 期货账号 | String | 12 |  | EMPTY_STR |
| HsBondCode | 债券代码 | String | 12 |  | EMPTY_STR |
| HsStockAccount | 交易账号 | String | 20 |  | EMPTY_STR |
| HsPassword | 密码 | String | 15 |  | EMPTY_STR |
| HsClientID | 客户编号 | String | 18 |  | EMPTY_STR |
| HsFundAccount | 资产账号 | String | 18 |  | EMPTY_STR |
| HsBankSerialID | 银行流水号 | String | 20 |  | EMPTY_STR |
| HsBankClientID | 客户账号（银行用） | String | 22 |  | EMPTY_STR |
| HsFuturesCode | 期货代码 | String | 30 |  | EMPTY_STR |
| HsPhone | 电话号码 | String | 32 |  | EMPTY_STR |
| HsBankAccount | 银行账号 | String | 32 |  | EMPTY_STR |
| HsPosStr | 字符型定位串 | String | 100 |  | EMPTY_STR |
| HsStockName | 产品名称 | String | 48 |  | EMPTY_STR |
| HsIDNo | 证件号码 | String | 40 |  | EMPTY_STR |
| HsIDENTITY | 证件号码 | String | 32 |  | EMPTY_STR |
| HsCardID | 资金卡号 | String | 32 |  | EMPTY_STR |
| HsFundstkAccount | 开放式基金交易账号 | String | 32 |  | EMPTY_STR |
| HsToken | 用户口令 | String | 512 |  | EMPTY_STR |
| HsName | 姓名 | String | 60 |  | EMPTY_STR |
| HsEnPassword | 增强型密码 | String | 64 |  | EMPTY_STR |
| HsStation | 站点地址 | String | 500 |  | EMPTY_STR |
| HsName2 | 名称 | String | 64 |  | EMPTY_STR |
| HsBondAccount | 债券账号 | String | 18 |  | EMPTY_STR |
| HsFutuCodeType | 合约代码类别 | String | 8 |  | EMPTY_STR |
| HsCursor | 游标 | Cursor |  |  | NULL |
| HsChar255List | 字符255数组 | Void |  |  | voidDefaultValue |
| HsQuantityList | 数量数组 | Void |  |  | voidDefaultValue |
| HsAmountList | 金额数组 | Void |  |  | voidDefaultValue |
| HsRateList | 利率数组 | Void |  |  | voidDefaultValue |
| HsPriceList | 价格数组 | Void |  |  | voidDefaultValue |
| HsNumList | 数据类型 | Void |  |  | voidDefaultValue |
| HsName3 | 字符120 | String | 120 |  | EMPTY_STR |
| HsOptCode | 期权合约编码 | String | 8 |  | EMPTY_STR |
| HsProdCode | 产品代码 | String | 32 |  | EMPTY_STR |
| HsOptName | 期权合约简称 | String | 128 |  | EMPTY_STR |
| HsSdcCode | 登记权益代码 | String | 32 |  | EMPTY_STR |
| HsSdcName | 登记权益名称 | String | 32 |  | EMPTY_STR |
| HsSdcAccount | 登记权益账号 | String | 32 |  | EMPTY_STR |
| HsSdcType | 登记权益类别 | String | 4 |  | EMPTY_STR |
| HsProdAccount | 产品账号 | String | 18 |  | EMPTY_STR |
| HsMchCode | 交易撮合代码 | String | 32 |  | EMPTY_STR |
| HsOtcType | 权益类别 | String | 4 |  | EMPTY_STR |
| HsOtcAccount | 权益账号 | String | 32 |  | EMPTY_STR |
| HsOtcCode | 权益代码 | String | 32 |  | EMPTY_STR |
| HsMchType | 交易撮合类别 | String | 4 |  | EMPTY_STR |
| HsMchAccount | 交易撮合账号 | String | 32 |  | EMPTY_STR |
| HsOtcName | 权益名称 | String | 32 |  | EMPTY_STR |
| HsPacker | 打包器 | CPacker |  |  | CPackerDefaultValue |
| HsUnpacker | 解包器 | CUnpacker |  |  | CUnpackerExDefaultValue |
| HsEntrustProp | 委托属性 | String | 4 |  | EMPTY_STR |
| HsEntrustReference | 委托引用 | String | 32 |  | EMPTY_STR |
| HsCompactId | 两融合约编号 | String | 32 |  | EMPTY_STR |
| HsSessionNo | 会话编号 | Int32 |  |  | I_ZERO |
| HsBusinessId | 成交编号 | String | 32 |  | EMPTY_STR |
| HsCancelInfo | 废单原因 | String | 255 |  | EMPTY_STR |
| HsEntrustId | 委托编号 | String | 16 |  | EMPTY_STR |
| HsErrorInfo | 错误提示 | String | 500 |  | EMPTY_STR |
| HsAcodeAccount | 一码通账户 | String | 20 |  | EMPTY_STR |
| HsPrice1 | 价格 | Double | 19 | 4 | D_ZERO |
| HsChar100000 | 字符100000 | String | 100000 |  | EMPTY_STR |
| HsHighPrice2 | 高精度价格 | Double | 23 | 8 | D_ZERO |
| HsChar502 | 字符502 | String | 502 |  | EMPTY_STR |
| HsSecuCode | 证券代码 | String | 32 |  | EMPTY_STR |
| HsChar300 | 字符300 | String | 300 |  | EMPTY_STR |
| HsMicroTime | 微秒级时间 | Int64 |  |  | I_ZERO |
| HsHighQuantity | 高精度数量 | Double | 23 | 6 | D_ZERO |
| HsChar36 | 字符36 | String | 36 |  | EMPTY_STR |
| HsName4 | 名称 | String | 180 |  | EMPTY_STR |
| HsAddress1 | 地址 | String | 180 |  | EMPTY_STR |
| HsChar30 | 字符30 | String | 30 |  | EMPTY_STR |
| HsName5 | 账户简称 | String | 90 |  | EMPTY_STR |
| HsChar32000 | 字符32000 | String | 32000 |  | EMPTY_STR |
| HsUnpackerV4 | PackV4解包器 | CUnpacker |  |  | CUnpackerExV4DefaultValue |
| HsPackerV4 | PackV4打包器 | CPacker |  |  | CpackerV4DefaultValue |
| HsUnpackerNull | 空Pack解包器 | CUnpacker |  |  | NULL |
| HsNum64 | 数字(int64) | Int64 |  |  | I_ZERO |
| HsUnpackerV3 | PackV3解包器 | CUnpacker |  |  | CUnpackerExV3DefaultValue |
| HsAddress2 | 地址 | String | 255 |  | EMPTY_STR |
| HsHighRisk | 高精度风险 | Double | 19 | 9 | D_ZERO |
| HsUNum64 | uint64 | UINT64 |  |  | I_ZERO |
| HsProportion | 比例 | Double | 21 | 4 | D_ZERO |
| HsChar1000 | 字符1000 | String | 1000 |  | EMPTY_STR |
| HsFutuPricePlus | 价格期货(扩展) | Double | 18 | 6 | D_ZERO |
| HSApiBalance | 金额 | Double | 19 | 2 | D_ZERO |
| HSApiVolume | 数量 | Double | 19 | 2 | D_ZERO |
| HSApiPrice | 价格 | Double | 12 | 6 | D_ZERO |
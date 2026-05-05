# upub - 标准字段

标准字段定义列表。

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2026-03-25 13:20:04 | V3.0.8.32 | 汪杰 | 新增标准字段char_config_31555 |
| 2026-03-17 14:39:34 | V3.0.8.31 | 袁文龙 | 新增标准字段breaker_name、char_config_31542 |
| 2026-03-23 14:04:12 | V3.0.2.120 | 张明月 | 新增标准字段optentrustinnercancel_clob,optentrustinnercancel_packer |
| 2026-03-27 10:29:11 | V3.0.2.119 | mamz50575 | 新增标准字段datetype_flag |
| 2026-03-26 10:52:36 | V3.0.2.118 | taocong45644 | 新增标准字段int_config_7906 |
| 2026-03-17 19:44:22 | V3.0.2.117 | 杨新照 | 新增标准字段original_transaction_str |
| 2026-03-09 19:44:22 | V3.0.2.116 | 陆良铠 | 新增标准字段cost_price_s |
| 2026-02-25 13:25:01 | V3.0.8.30 | 徐世晗 | 新增标准字段char_config_31805,int_config_87060 |
| 2026-02-26 10:31:54 | V3.0.8.29 | 冯元栋 | 新增标准字段csdc_market_status |
| 2026-03-02 16:48:12 | V3.0.2.115 | 舒来新 | 新增标准字段option_value_type、en_option_value_type |
| 2026-02-11 10:14:54 | V3.0.2.114 | 曾阳璞 | 新增标准字段allot_balance_src、allot_balance_dest |
| 2026-02-11 16:12:58 | V3.0.2.114 | 廖宏玮 | 新增标准字段ref_fused_quota |
| 2026-02-03 09:55:02 | V3.0.2.113 | 曾阳璞 | 新增标准字段allot_balance |
| 2026-02-06 10:41:30 | V3.0.8.27 | 陈征东 | 同步UF20标准字段mistake_amount，mistake_balance，新增标准字段refhfcc_type |
| 2026-02-02 16:59:01 | V3.0.2.112 | 舒来新 | 新增标准字段comb_side_close_flag |
| 2026-01-30 16:49:57 | V3.0.2.112 | yangxz | 新增char_config_3241标准字段 |
| 2026-01-26 16:49:57 | V3.0.2.111 | taocong45644 | 新增char_config_87059标准字段 |
| 2026-01-12 09:47:14 | V3.0.2.110 | 蒋浩 | bond_publisher_type扩位为HsChar30 |
| 2026-01-08 13:40:48 | V3.0.2.109 | 谢宗艺 | en_send_status字段类型更改为HsChar32 |
| 2026-01-04 14:39:35 | V3.0.2.108 | 洪略 | rej_reason字段更改为HsChar32 |

> 共 438 条修改记录，仅显示最近20条


## 字段列表（共 30526 个）

| 字段名 | 中文名 | 数据类型 | 长度 | 精度 |
|--------|--------|----------|------|------|
| abstract_account | 虚拟股东 | HsStockAccount |  |  |
| accept_name | 接收人 | HsChar8 |  |  |
| access_level | 存取级别 | HsType |  |  |
| account_config | 账号产生方式 | HsType |  |  |
| account_content | 输入内容 | HsChar255 |  |  |
| account_data | 开户规范信息 | HsName4 |  |  |
| account_flag | 账号标识 | HsFlag |  |  |
| account_len | 账号长度 | HsNum4 |  |  |
| account_prop | 股东性质(深) | HsChar2 |  |  |
| account_start | 起始账号 | HsAcctNo |  |  |
| account_status | 账户状态 | HsStatus |  |  |
| account_stop | 结束账号 | HsAcctNo |  |  |
| account_type | 账户类型 | HsType |  |  |
| accountnumber | 账号内部编号 | HsNum10 |  |  |
| acctconfig_type | 账号配置类型 | HsNumID |  |  |
| accum_flag | 是否累计 | HsType |  |  |
| accum_type | 累计方式 | HsType |  |  |
| action_in | 操作控制值 | HsNumID |  |  |
| action_in_temp | 操作控制值 | HsNumID |  |  |
| action_str | 输入字符串 | HsChar255 |  |  |
| action_type | 操作类型 | HsType |  |  |
| add_rowcount_flag | 行数标志 | HsFlag |  |  |
| active_flag | 当前使用标记 | HsFlag |  |  |
| address | 联系地址 | HsAddress1 |  |  |
| Address | 客户地址 | HsAddress |  |  |
| adjust_balance | 调账金额 | HsAmount |  |  |
| adjust_bk_serial_no | 调账银行流水号 | HsSerialNo |  |  |
| adjust_entrust_serial_no | 填banktransfer的流水号 | HsSerialNo |  |  |
| adjust_sc_serial_no | 调账证券流水号 | HsSerialNo |  |  |
| adjust_serial_no | 填fundjour的流水号 | HsSerialNo |  |  |
| adjust_status | 调账状态 | HsStatus |  |  |
| advance_month | 提前月份 | HsNum |  |  |
| agency_name | 销售商名称 | HsChar500 |  |  |
| agency_no | 销售商代码 | HsChar20 |  |  |
| agent | 代理信息 | HsName4 |  |  |
| agent_fare | 贡献利润 | HsAmount |  |  |
| agent_id | 法人名称 | HsIDNo |  |  |
| aim_value | 指标值 | HsAmount |  |  |
| all_lower_limit_in | 全部银行转进金额下限 | HsAmount |  |  |
| all_lower_limit_out | 全部银行转出金额下限 | HsAmount |  |  |
| all_upper_limit_in | 全部银行转进金额上限 | HsAmount |  |  |
| all_upper_limit_out | 全部银行转出金额上限 | HsAmount |  |  |
| allot_date | 交易日期 | HsDate |  |  |
| allot_limitshare | 个人追加认购金额 | HsAmount |  |  |
| allot_no | 申请编号 | HsChar24 |  |  |
| allot_share | 上日申购成功份额 | HsFundQty |  |  |
| allotno | 申请编号 | HsChar24 |  |  |
| allow_flag | 允许标志 | HsFlag |  |  |
| am_close | 上午结束时间 | HsTime |  |  |
| am_open | 上午开始时间 | HsTime |  |  |
| amount | 持仓量 | HsQuantity |  |  |
| amount_per_hand | 合约乘数 | HsNum |  |  |
| app_unit | 申购最小单位 | HsAmount |  |  |
| append_date | 追加数据日期 | HsDate |  |  |
| append_number | 前缀数值 | HsChar10 |  |  |
| append_pos | 附加串位置 | HsNum3 |  |  |
| append_string | 附加串 | HsChar32 |  |  |
| apply_begin_date | 行权开始日期 | HsDate |  |  |
| apply_code | 行权代码 | HsStockCode |  |  |
| apply_date | 申请日期 | HsDate |  |  |
| apply_end_date | 行权截至日期 | HsDate |  |  |
| apply_high_amount | 行权最大数量 | HsQuantity |  |  |
| apply_no | 交易申请编号 | HsChar24 |  |  |
| apply_price | 行权价格 | HsHighPrice |  |  |
| apply_rate | 行权比例 | HsHighPrice |  |  |
| apply_status | 行权允许标志 | HsType |  |  |
| apply_style | 行权方式 | HsType |  |  |
| apply_unit | 行权单位 | HsNum |  |  |
| ar_name | AR组名 | HsChar64 |  |  |
| arbit_type | 套利类型 | HsType |  |  |
| arbitrage_type | 组合类型 | HsType |  |  |
| as_name | AS名称 | HsChar255 |  |  |
| ask_balance | 申请金额 | HsAmount |  |  |
| ask_count | 委托笔数 | HsNum |  |  |
| ask_fare | 委托费用 | HsAmount |  |  |
| ask_share | 申请份额 | HsFundQty |  |  |
| ask_stamp_tax | 委托印花税 | HsAmount |  |  |
| asset | 资产 | HsAmount |  |  |
| asset_amount | 存管数量 | HsQuantity |  |  |
| asset_balance | 资产值 | HsAmount |  |  |
| asset_flag | 计算市值标志 | HsFlag |  |  |
| asset_price | 市值价 | HsRisk |  |  |
| asset_prop | 资产属性 | HsType |  |  |
| assign_mode | 复核任务分配模式 | HsFlag |  |  |
| assure_status | 担保状态 | HsStatus |  |  |
| audit_action | 复核类型 | HsType |  |  |
| audit_branch_no | 复核分支机构 | HsBranchNo |  |  |
| audit_date | 复核日期 | HsDate |  |  |
| audit_function_id | 功能号 | HsFunctionNo |  |  |
| audit_level | 复核级别 | HsNum |  |  |
| audit_mode | 复核模式 | HsType |  |  |
| audit_operator_name | 复核操作员姓名 | HsName |  |  |
| audit_operator_no | 复核操作员编号 | HsClientID |  |  |
| audit_remark | 复核说明 | HsChar255 |  |  |
| audit_serial_no | 复核流水号 | HsSerialNo |  |  |
| audit_status | 复核任务状态 | HsStatus |  |  |
| audit_time | 复核时间 | HsTime |  |  |
| auditop_branch_no | 复核操作分支机构 | HsBranchNo |  |  |
| auth_password | 应用系统密码 | HsEnPassword |  |  |
| auth_roles | 授权角色集 | HsChar2000 |  |  |
| auth_roles_b | 授权角色集 | HsChar2000 |  |  |
| authority_code | 权益代码 | HsStockCode |  |  |
| authority_str | 权益登记号 | HsPosStr |  |  |
| authorize_code | 授权码 | HsNum10 |  |  |
| auto_audit | 是否需要复核 | HsType |  |  |
| auto_bond | 自动抵押 | HsFlag |  |  |
| auto_buy | 分红方式 | HsFlag |  |  |
| auto_cancel | 超时是否自动撤单 | HsType |  |  |
| auto_flag | 自动开户 | HsFlag |  |  |
| auto_trans | 是否自动转账 | HsFlag |  |  |
| auto_type | 类型 | HsType |  |  |
| average_flag | 平均标志 | HsFlag |  |  |
| bAcctKind | 银行账号类型 | HsType |  |  |
| back_amount | 购回数量 | HsQuantity |  |  |
| back_balance | 购回金额 | HsAmount |  |  |
| back_date | 归还截至日期 | HsDate |  |  |
| back_margin | 返还履约金 | HsAmount |  |  |
| back_ratio | 返佣比例 | HsRate |  |  |
| back_share | 卖出数量 | HsFundQty |  |  |
| bail_balance | 客户保证金 | HsAmount |  |  |
| balance | 发生金额 | HsAmount |  |  |
| balance_change | 调整每手金额 | HsAmount |  |  |
| balance_fare | 固定返还 | HsAmount |  |  |
| balance_level | 金额阶段 | HsAmount |  |  |
| balance_local | 本地发生金额 | HsAmount |  |  |
| balance_ratio | 成交金额比例 | HsHighRate |  |  |
| balance_step | 金额阶段 | HsAmount |  |  |
| balance_ta | 确认金额 | HsAmount |  |  |
| balance_type | 收取方式 | HsType |  |  |
| bank_account | 银行账号 | HsBankAccount |  |  |
| bank_branch | 银行机构编号 | HsChar20 |  |  |
| bank_control | 特殊控制 | HsChar32 |  |  |
| bank_current_balance | 银行端余额 | HsAmount |  |  |
| bank_error_info | 银行错误信息 | HsAbstract |  |  |
| bank_error_no | 银行错误代码 | HsNumID |  |  |
| bank_flag | 转账标志 | HsType |  |  |
| bank_id | 银行清算编号 | HsChar8 |  |  |
| bank_name | 银行名称 | HsName4 |  |  |
| bank_no | 银行代码 | HsBankID |  |  |
| bank_no_str | 银行号字符串 | HsChar32 |  |  |
| bank_note | 银行说明 | HsAbstract |  |  |
| bank_occur | 银行发生 | HsAmount |  |  |
| bank_operator | 银行操作员 | HsClientID |  |  |
| bank_remark | 备注 | HsAbstract |  |  |
| bank_serial_no | 银行流水号 | HsBankSerialID |  |  |
| bank_serialno | 银行委托号 | HsBankSerialID |  |  |
| bank_status | 交易状态 | HsStatus |  |  |
| bank_trust_status | 银行端存管状态 | HsStatus |  |  |
| bank_type | 银行类型 | HsType |  |  |
| bankaccount_status | 状态 | HsStatus |  |  |
| bankarg_flag | 参数配置 | HsChar255 |  |  |
| bankentmode | 银行委托模式 | HsType |  |  |
| bar_group | 属于快捷工具栏的组号 | HsNumID |  |  |
| bar_index | 在快捷工具栏中的位置 | HsNumID |  |  |
| base_balance | 起始金额 | HsAmount |  |  |
| base_price | 基准价格 | HsHighPrice2 |  |  |
| base_rate | 限价公式中的比例 | HsNum |  |  |
| base_version | 基线包版本 | HsNum |  |  |
| baseprice_type | 基价类型 | HsType |  |  |
| basic_share | 红利基数 | HsAmount |  |  |
| batch_no | 委托批号 | HsSerialNo |  |  |
| bback_date | 系统后备份日 | HsDate |  |  |
| bBranchId | 银行分行号 | HsChar20 |  |  |
| bCustAcct | 银行账号 | HsBankAccount |  |  |
| bCustPwd | 银行密码 | HsPassword |  |  |
| bDeptId | 储蓄所号（银行网点号） | HsChar20 |  |  |
| beeppager | 传呼号码 | HsPhone |  |  |
| begin_account | 开始账号 | HsFundstkAccount |  |  |
| begin_amount | 期初数量 | HsQuantity |  |  |
| begin_amount_asset | 期初数量（存管） | HsQuantity |  |  |
| begin_asset | 起始资产 | HsAmount |  |  |
| begin_balance | 期初余额 | HsAmount |  |  |
| begin_current_amount | 现券额度 | HsQuantity |  |  |
| begin_date | 起始日期 | HsDate |  |  |
| begin_gap_amount | 初始轧差数量 | HsQuantity |  |  |
| begin_interest | 初始利息 | HsAmount |  |  |
| begin_position_str | 当日起始定位串 | HsPosStr |  |  |
| begin_rate | 期初保证金比例 | HsRisk |  |  |
| begin_share | 期初份额 | HsFundQty |  |  |
| begin_time | 开始时间 | HsTime |  |  |
| begin_value | 指标开始值 | HsAmount |  |  |
| BeginDate | 查询起始日期 | HsDate |  |  |
| bEnableBala | 银行可用金额 | HsAmount |  |  |
| benefit_account | 提成账号 | HsFundAccount |  |  |
| benefit_type | 分红方式或冻结原因 | HsType |  |  |
| bfare | 后台费用 | HsAmount |  |  |
| bfare_balance | 后台费用金额 | HsAmount |  |  |
| bfare_kind | 后台费用属性 | HsNumID |  |  |
| bfare_procedure | 后台费用存储过程 | HsChar32 |  |  |
| bfare1 | 后台费用 | HsAmount |  |  |
| bfare1_one | 后台费用 | HsAmount |  |  |
| bFetchBala | 银行可取金额 | HsAmount |  |  |
| bFrozenFlag | 冻结业务类型 | HsChar2 |  |  |
| bill_rate | 转汇比率 | HsRecoupRate |  |  |
| birthday | 出生日期 | HsDate |  |  |
| bk_bk_serial_no | 银行端银行流水号 | HsBankSerialID |  |  |
| bk_bktrans_status | 银行端委托状态 | HsStatus |  |  |
| bk_client_name | 银行端客户姓名 | HsName4 |  |  |
| bk_current_balance | 银行端余额 | HsAmount |  |  |
| bk_enable_balance | 银行可用金额 | HsAmount |  |  |

> 共 30526 个字段，仅显示前200个
# usms - 内存表定义

内存表（缓存表）定义，包含表名、同步表、索引等信息。

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-22 15:39:00 | 3.0.2.13 | 高志强 | 对物理表有position_str字段的，缓存表增加position_str非唯一索引，优化更新场景的性能表现 |
| 2025-12-19 09:09:42 | 3.0.2.10 | 冯元栋 | 增加非唯一索引 |
| 2025-12-15 19:03:00 | 3.0.2.9 | 高志强 | usms 的 缓存表 usps_stkcode 支持 position_str 索引 |
| 2025-10-13 15:21:00 | 3.0.2.8 | 高志强 | upbs_extern_error缓存表唯一索引变更为error_sort,error_source,error_no_original,去除error_no_... |
| 2025-11-25 15:46:00 | 3.0.2.8 | 蒋浩宇 | 新增 param_sync_ctrl |
| 2025-09-26 10:05:00 | 3.0.2.7 | 高志强 | 回退T202509167429的修改 |
| 2025-09-20 15:19:21 | 3.0.2.6 | 高志强 | upbs_arg改造为数据源是pbs库的缓存表 |
| 2025-09-19 16:23:05 | 3.0.2.5 | 蒋浩宇 | 删除usps_ofcode表，该表不上缓存 |
| 2025-09-05 16:23:05 | 3.0.2.4 | 高志强 | 资源改为和配置一致 |
| 2025-09-04 16:42:01 | 3.0.2.3 | 王云乾 | usms去掉了多余的物理表，这里同步去掉usms的本地缓存表，共计61个本地缓存表 |
| 2025-08-22 14:43:14 | 3.0.2.2 | 高志强 | 新增 upbs_license_info 从 hs_usms 库上缓存 |
| 2025-08-07 16:36:03 | 3.0.2.1 | 高志强 | 修复 idx_upbs_hs_function 显示有错误的问题 |


## 内存表列表（共 96 个）

### pbs_init_config

- **数据库表**: pbs_init_config
- **说明**: 初始化配置表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_init_config
- **索引**:
  - `uk_init_config` (唯一): service_name,table_name
  - `uk_init_config` (唯一): service_name,table_name

### pbs_sysdeploy

- **数据库表**: pbs_sysdeploy
- **说明**: 子系统部署表
- **用户**: pbssvr
- **字段**: subsys_id,subsys_name,subsys_status,micro_service,uf2_enable_flag,uf3_enable_flag,update_date,update_time,transaction_no,position_str
- **同步表**: pbs_sysdeploy
- **索引**:
  - `uk_pbs_sysdeploy` (唯一): subsys_id
  - `idx_pbs_sysdeploy_pos` (非唯一): position_str
  - `uk_pbs_sysdeploy` (唯一): subsys_id
  - `idx_pbs_sysdeploy_pos` (非唯一): position_str

### pbs_sysnode_deploy

- **数据库表**: pbs_sysnode_deploy
- **说明**: 系统节点部署表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_sysnode_deploy
- **索引**:
  - `uk_sysnode_deploy` (唯一): sysnode_id,subsys_id
  - `idx_sysnode_deploy_pos` (非唯一): position_str
  - `uk_sysnode_deploy` (唯一): sysnode_id,subsys_id
  - `idx_sysnode_deploy_pos` (非唯一): position_str

### upbs_all_company

- **数据库表**: upbs_all_company
- **说明**: 券商信息表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_all_company
- **索引**:
  - `idx_upbs_all_company` (唯一): company_no
  - `idx_upbs_all_company_pos` (非唯一): position_str
  - `idx_upbs_all_company` (唯一): company_no
  - `idx_upbs_all_company_pos` (非唯一): position_str

### upbs_hs_function

- **数据库表**: upbs_hs_function
- **说明**: 证券系统功能表
- **用户**: pbssvr
- **字段**: function_id,en_sys_status,func_flag_str,password_type,restend_time,reststart_time,transaction_no,func_busi_type,right_type
- **同步表**: pbs_hs_function
- **索引**:
  - `idx_upbs_hs_function` (唯一): function_id
  - `idx_upbs_hs_function_pos` (非唯一): position_str
  - `idx_upbs_hs_function` (唯一): function_id
  - `idx_upbs_hs_function_pos` (非唯一): position_str

### upbs_sysconfig

- **数据库表**: upbs_sysconfig
- **说明**: 系统配置参数表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_sysconfig
- **索引**:
  - `idx_sysconfig` (唯一): branch_no,config_no
  - `idx_sysconfig_pos` (非唯一): position_str
  - `idx_sysconfig` (唯一): branch_no,config_no
  - `idx_sysconfig_pos` (非唯一): position_str

### upbs_umtconfig

- **数据库表**: upbs_umtconfig
- **说明**: 内存交易参数表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_umtconfig
- **索引**:
  - `idx_upbs_umtconfig` (唯一): partition_no
  - `idx_upbs_umtconfig_pos` (非唯一): position_str
  - `idx_upbs_umtconfig` (唯一): partition_no
  - `idx_upbs_umtconfig_pos` (非唯一): position_str

### upbs_all_branch

- **数据库表**: upbs_all_branch
- **说明**: 券商机构表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_all_branch
- **索引**:
  - `idx_all_branch` (唯一): branch_no
  - `idx_all_branch_pos` (非唯一): position_str
  - `idx_all_branch` (唯一): branch_no
  - `idx_all_branch_pos` (非唯一): position_str

### upbs_acct_rule

- **数据库表**: upbs_acct_rule
- **说明**: 账户分片规则表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_acct_rule
- **索引**:
  - `idx_upbs_acct_rule_uk` (唯一): position_str
  - `idx_upbs_acct_rule` (非唯一): umt_begin_account,acct_rule_type,sysnode_id
  - `idx_upbs_acct_rule_uk` (唯一): position_str
  - `idx_upbs_acct_rule` (非唯一): umt_begin_account,acct_rule_type,sysnode_id

### upbs_init_date_model

- **数据库表**: upbs_init_date_model
- **说明**: 交易日期表
- **用户**: pbssvr
- **字段**: init_date,init_model,settle_flag,trade_flag,special_trade_flag,transaction_no,position_str
- **同步表**: pbs_init_date_model
- **索引**:
  - `idx_upbs_init_date_model` (唯一): init_date,init_model
  - `idx_upbs_init_date_model_pos` (非唯一): position_str
  - `idx_upbs_init_date_model` (唯一): init_date,init_model
  - `idx_upbs_init_date_model_pos` (非唯一): position_str

### upbs_account_deploy

- **数据库表**: upbs_account_deploy
- **说明**: 账户部署表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_account_deploy
- **索引**:
  - `idx_accountdeploy` (唯一): fund_account
  - `idx_accountdeploy_pos` (非唯一): position_str
  - `idx_accountdeploy` (唯一): fund_account
  - `idx_accountdeploy_pos` (非唯一): position_str

### upbs_asset_prop_deploy

- **数据库表**: upbs_asset_prop_deploy
- **说明**: 资产属性部署配置表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_asset_prop_deploy
- **索引**:
  - `idx_assetpropdeploy` (唯一): branch_no,asset_prop
  - `idx_assetpropdeploy_pos` (非唯一): position_str
  - `idx_assetpropdeploy` (唯一): branch_no,asset_prop
  - `idx_assetpropdeploy_pos` (非唯一): position_str

### upbs_extern_error

- **数据库表**: upbs_extern_error
- **说明**: 外部错误表
- **用户**: pbssvr
- **字段**: error_info,error_no_dest,error_sort,error_source,error_no_original,transaction_no,position_str
- **同步表**: pbs_extern_error
- **索引**:
  - `idx_upbs_extern_error` (唯一): error_sort,error_source,error_no_original
  - `idx_pbs_externerror` (非唯一): error_no_original
  - `idx_upbs_extern_error_pos` (非唯一): position_str
  - `idx_upbs_extern_error` (唯一): error_sort,error_source,error_no_original
  - `idx_pbs_externerror` (非唯一): error_no_original
  - `idx_upbs_extern_error_pos` (非唯一): position_str

### exchange_rates

- **数据库表**: exchange_rates
- **说明**: 汇率表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_exchange_rate
- **索引**:
  - `idx_exchange_rate` (唯一): money_type,dest_money_type
  - `idx_exchange_rate_pos` (非唯一): position_str
  - `idx_exchange_rate` (唯一): money_type,dest_money_type
  - `idx_exchange_rate_pos` (非唯一): position_str

### usps_branch_prefix

- **数据库表**: usps_branch_prefix
- **说明**: 机构前缀表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_branch_prefix
- **索引**:
  - `idx_branchprefix` (唯一): branch_no,exchange_type,finance_type
  - `idx_branchprefix_pos` (非唯一): position_str
  - `idx_branchprefix` (唯一): branch_no,exchange_type,finance_type
  - `idx_branchprefix_pos` (非唯一): position_str

### upbs_branch_acct_info

- **数据库表**: upbs_branch_acct_info
- **说明**: 机构对应账户信息
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_branch_acct_info
- **索引**:
  - `idx_branchacctinfo` (唯一): branch_no,branch_account_type
  - `idx_branchacctinfo_pos` (非唯一): position_str
  - `idx_branchacctinfo` (唯一): branch_no,branch_account_type
  - `idx_branchacctinfo_pos` (非唯一): position_str

### upbs_dictionary

- **数据库表**: upbs_dictionary
- **说明**: 数据字典表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_dictionary
- **索引**:
  - `idx_upbs_dictionary_uniq` (唯一): dict_entry,sub_entry
  - `idx_upbs_dictionary_pos` (非唯一): position_str
  - `idx_upbs_dictionary_uniq` (唯一): dict_entry,sub_entry
  - `idx_upbs_dictionary_pos` (非唯一): position_str

### upbs_error_msg

- **数据库表**: upbs_error_msg
- **说明**: 错误信息表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_error_msg
- **索引**:
  - `idx_upbs_error_msg` (唯一): error_no
  - `idx_upbs_error_msg_pos` (非唯一): position_str
  - `idx_upbs_error_msg` (唯一): error_no
  - `idx_upbs_error_msg_pos` (非唯一): position_str

### upbs_business_flag

- **数据库表**: upbs_business_flag
- **说明**: 业务标志
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_business_flag
- **索引**:
  - `idx_businflag` (唯一): business_flag
  - `idx_businflag_pos` (非唯一): position_str
  - `idx_businflag` (唯一): business_flag
  - `idx_businflag_pos` (非唯一): position_str

### pbs_sysnode

- **数据库表**: pbs_sysnode
- **说明**: 系统节点表
- **用户**: pbssvr
- **字段**: sysnode_id,sysnode_name,node_type,sysnode_version,update_date,update_time
- **同步表**: pbs_sysnode
- **索引**:
  - `idx_sysnode` (唯一): sysnode_id
  - `idx_sysnode_pos` (非唯一): position_str
  - `idx_sysnode` (唯一): sysnode_id
  - `idx_sysnode_pos` (非唯一): position_str

### upbs_dict_entry

- **数据库表**: upbs_dict_entry
- **说明**: 字典条目表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_dict_entry
- **索引**:
  - `idx_upbs_dict_entry` (唯一): dict_entry
  - `idx_upbs_dict_entry_pos` (非唯一): position_str
  - `idx_upbs_dict_entry` (唯一): dict_entry
  - `idx_upbs_dict_entry_pos` (非唯一): position_str

### usps_exch_arg

- **数据库表**: usps_exch_arg
- **说明**: 交易参数表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_exch_arg
- **索引**:
  - `idx_usps_exch_arg` (唯一): exchange_type
  - `idx_usps_exch_arg_pos` (非唯一): position_str
  - `idx_usps_exch_arg` (唯一): exchange_type
  - `idx_usps_exch_arg_pos` (非唯一): position_str

### usps_spe_busin_date

- **数据库表**: usps_spe_busin_date
- **说明**: 特殊业务日期表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_spe_busin_date
- **索引**:
  - `idx_usps_spe_busin_date` (唯一): date_type
  - `idx_usps_spe_busin_date_pos` (非唯一): position_str
  - `idx_usps_spe_busin_date` (唯一): date_type
  - `idx_usps_spe_busin_date_pos` (非唯一): position_str

### usps_seats

- **数据库表**: usps_seats
- **说明**: 席位参数表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_seats
- **索引**:
  - `idx_upbs_seats` (唯一): exchange_type,seat_no,branch_no
  - `idx_upbs_seats_prop` (非唯一): branch_no,exchange_type,seat_prop,default_mark
  - `idx_upbs_seats_enclientgroup` (非唯一): exchange_type,branch_no,seat_prop,seatvip_flag,en_stock_type,en_client_group,default_mark
  - `idx_upbs_seats_enstocktype` (非唯一): exchange_type,branch_no,seat_prop,seatvip_flag,en_stock_type,default_mark
  - `idx_upbs_seats_pos` (非唯一): position_str
  - `idx_upbs_seats` (唯一): exchange_type,seat_no,branch_no
  - `idx_upbs_seats_prop` (非唯一): branch_no,exchange_type,seat_prop,default_mark
  - `idx_upbs_seats_enclientgroup` (非唯一): exchange_type,branch_no,seat_prop,seatvip_flag,en_stock_type,en_client_group,default_mark
  - `idx_upbs_seats_enstocktype` (非唯一): exchange_type,branch_no,seat_prop,seatvip_flag,en_stock_type,default_mark
  - `idx_upbs_seats_pos` (非唯一): position_str

### usps_stkcode

- **数据库表**: usps_stkcode
- **说明**: 证券代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_stkcode
- **索引**:
  - `idx_uft_stkcode` (唯一): stock_code,exchange_type
  - `idx_uft_stkcode_pos` (非唯一): position_str
  - `idx_usps_stkcode_relative` (非唯一): exchange_type,relative_code,stock_type
  - `idx_usps_stkcode_stockcode` (非唯一): stock_code
  - `idx_uft_stkcode` (唯一): stock_code,exchange_type
  - `idx_uft_stkcode_pos` (非唯一): position_str
  - `idx_usps_stkcode_relative` (非唯一): exchange_type,relative_code,stock_type
  - `idx_usps_stkcode_stockcode` (非唯一): stock_code

### afof_agencyno

- **数据库表**: afof_agencyno
- **说明**: 基金盘后代销商表
- **用户**: uargsvr
- **字段**: *
- **同步表**: afof_agencyno
- **索引**:
  - `idx_afof_agencyno` (唯一): agency_no
  - `idx_afof_agencyno_pos` (非唯一): position_str
  - `idx_afof_agencyno` (唯一): agency_no
  - `idx_afof_agencyno_pos` (非唯一): position_str

### grade_impawn_rate

- **数据库表**: grade_impawn_rate
- **说明**: 分级质押比率表
- **用户**: uargsvr
- **字段**: *
- **同步表**: grade_impawn_rate
- **索引**:
  - `idx_grade_impawn_rate` (唯一): exchange_type,stock_code
  - `idx_grade_impawn_rate_pos` (非唯一): position_str
  - `idx_grade_impawn_rate` (唯一): exchange_type,stock_code
  - `idx_grade_impawn_rate_pos` (非唯一): position_str

### sett_process_info

- **数据库表**: sett_process_info
- **说明**: 清算流程信息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: sett_process_info
- **索引**:
  - `idx_sett_process_info` (唯一): init_date,exchange_type,sett_prop
  - `idx_sett_process_info_pos` (非唯一): position_str
  - `idx_sett_process_info` (唯一): init_date,exchange_type,sett_prop
  - `idx_sett_process_info_pos` (非唯一): position_str

### usps_authority

- **数据库表**: usps_authority
- **说明**: 权益登记表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_authority
- **索引**:
  - `idx_authority_pos` (唯一): position_str
  - `idx_usps_authority` (非唯一): exchange_type,business_type,authority_code,register_date,stock_code,placard_id,info_kind
  - `idx_usps_authority_type` (非唯一): exchange_type,business_type,authority_code,register_date
  - `idx_usps_authority_code` (非唯一): exchange_type,business_type,info_kind,placard_id,stock_code
  - `idx_authority_pos` (唯一): position_str
  - `idx_usps_authority` (非唯一): exchange_type,business_type,authority_code,register_date,stock_code,placard_id,info_kind
  - `idx_usps_authority_type` (非唯一): exchange_type,business_type,authority_code,register_date
  - `idx_usps_authority_code` (非唯一): exchange_type,business_type,info_kind,placard_id,stock_code

### usps_bond_rate

- **数据库表**: usps_bond_rate
- **说明**: 抵押比率表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_bond_rate
- **索引**:
  - `idx_usps_bond_rate` (唯一): exchange_type,stock_code
  - `idx_usps_bond_rate_pos` (非唯一): position_str
  - `idx_usps_bond_rate` (唯一): exchange_type,stock_code
  - `idx_usps_bond_rate_pos` (非唯一): position_str

### usps_debtinterest

- **数据库表**: usps_debtinterest
- **说明**: 国债利息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_debtinterest
- **索引**:
  - `idx_usps_debtinterest` (唯一): exchange_type,stock_code
  - `idx_usps_debtinterest_pos` (非唯一): position_str
  - `idx_usps_debtinterest` (唯一): exchange_type,stock_code
  - `idx_usps_debtinterest_pos` (非唯一): position_str

### usps_etf_code

- **数据库表**: usps_etf_code
- **说明**: ETF代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_etf_code
- **索引**:
  - `idx_usps_etf_code` (唯一): stock_code,channel_type,exchange_type,init_date
  - `idx_usps_etf_code_pos` (非唯一): position_str
  - `idx_usps_etf_code` (唯一): stock_code,channel_type,exchange_type,init_date
  - `idx_usps_etf_code_pos` (非唯一): position_str

### usps_exchange_time

- **数据库表**: usps_exchange_time
- **说明**: 交易时间表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_exchange_time
- **索引**:
  - `idx_usps_exchange_time` (唯一): time_kind,time_order,exchange_type
  - `idx_usps_exchange_time_kind` (非唯一): time_kind
  - `idx_usps_exchange_time_pos` (非唯一): position_str
  - `idx_usps_exchange_time` (唯一): time_kind,time_order,exchange_type
  - `idx_usps_exchange_time_kind` (非唯一): time_kind
  - `idx_usps_exchange_time_pos` (非唯一): position_str

### usps_ffare

- **数据库表**: usps_ffare
- **说明**: 前台费用表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_ffare
- **索引**:
  - `idx_usps_ffare` (唯一): fare_kind,fare_type,exchange_type,stock_type,entrust_way,money_type,sub_stock_type
  - `idx_usps_ffare_norm` (非唯一): fare_kind,fare_type,stock_type,exchange_type,sub_stock_type,entrust_way
  - `idx_usps_ffare_pos` (非唯一): position_str
  - `idx_usps_ffare` (唯一): fare_kind,fare_type,exchange_type,stock_type,entrust_way,money_type,sub_stock_type
  - `idx_usps_ffare_norm` (非唯一): fare_kind,fare_type,stock_type,exchange_type,sub_stock_type,entrust_way
  - `idx_usps_ffare_pos` (非唯一): position_str

### usps_fixed_price_params

- **数据库表**: usps_fixed_price_params
- **说明**: 盘后定价交易业务信息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_fixed_price_params
- **索引**:
  - `idx_usps_fixed_price_params` (唯一): exchange_type,stock_code
  - `idx_usps_fixed_price_params_pos` (非唯一): position_str
  - `idx_usps_fixed_price_params` (唯一): exchange_type,stock_code
  - `idx_usps_fixed_price_params_pos` (非唯一): position_str

### usps_promise_info

- **数据库表**: usps_promise_info
- **说明**: 要约信息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_promise_info
- **索引**:
  - `idx_usps_promise_info` (唯一): stock_code,exchange_type,purchase_id
  - `idx_usps_promise_info_exch` (非唯一): exchange_type
  - `idx_usps_promise_info_pos` (非唯一): position_str
  - `idx_usps_promise_info` (唯一): stock_code,exchange_type,purchase_id
  - `idx_usps_promise_info_exch` (非唯一): exchange_type
  - `idx_usps_promise_info_pos` (非唯一): position_str

### usps_qrp_code

- **数据库表**: usps_qrp_code
- **说明**: 报价回购代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_qrp_code
- **索引**:
  - `idx_qrpcode` (唯一): stock_code,exchange_type,company_no
  - `idx_qrpcode_pos` (非唯一): position_str
  - `idx_qrpcode` (唯一): stock_code,exchange_type,company_no
  - `idx_qrpcode_pos` (非唯一): position_str

### usps_srp_code

- **数据库表**: usps_srp_code
- **说明**: 股票质押代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_srp_code
- **索引**:
  - `idx_srpcode` (唯一): stock_code,exchange_type,srp_kind,company_no
  - `idx_srpcode_pos` (非唯一): position_str
  - `idx_srpcode` (唯一): stock_code,exchange_type,srp_kind,company_no
  - `idx_srpcode_pos` (非唯一): position_str

### usps_stb_stkcode

- **数据库表**: usps_stb_stkcode
- **说明**: 股转证券代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_stb_stkcode
- **索引**:
  - `idx_usps_stb_stkcode` (唯一): exchange_type,stock_code
  - `idx_usps_stb_stkcode_pos` (非唯一): position_str
  - `idx_usps_stb_stkcode` (唯一): exchange_type,stock_code
  - `idx_usps_stb_stkcode_pos` (非唯一): position_str

### usps_stkcode_ext

- **数据库表**: usps_stkcode_ext
- **说明**: 证券代码扩展表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_stkcode_ext
- **索引**:
  - `idx_usps_stkcodeext` (唯一): exchange_type,stock_code,bond_trade_type
  - `idx_usps_stkcodeext_stockcode` (非唯一): stock_code,exchange_type
  - `idx_usps_stkcodeext_pos` (非唯一): position_str
  - `idx_usps_stkcodeext` (唯一): exchange_type,stock_code,bond_trade_type
  - `idx_usps_stkcodeext_stockcode` (非唯一): stock_code,exchange_type
  - `idx_usps_stkcodeext_pos` (非唯一): position_str

### usps_stknotice_info

- **数据库表**: usps_stknotice_info
- **说明**: 证券提示信息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_stknotice_info
- **索引**:
  - `idx_usps_stknotice_info` (唯一): stock_code,exchange_type,stock_type,sub_stock_type,notice_type,start_date,end_date
  - `idx_usps_stknotice_info_pos` (非唯一): position_str
  - `idx_usps_stknotice_info` (唯一): stock_code,exchange_type,stock_type,sub_stock_type,notice_type,start_date,end_date
  - `idx_usps_stknotice_info_pos` (非唯一): position_str

### usps_warrant_code

- **数据库表**: usps_warrant_code
- **说明**: 权证代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_warrant_code
- **索引**:
  - `idx_warrant_code` (唯一): exchange_type,warrant_code
  - `idx_warrant_code_apply` (唯一): exchange_type,apply_code
  - `idx_warrant_code_pos` (非唯一): position_str
  - `idx_warrant_code` (唯一): exchange_type,warrant_code
  - `idx_warrant_code_apply` (唯一): exchange_type,apply_code
  - `idx_warrant_code_pos` (非唯一): position_str

### usps_witcode

- **数据库表**: usps_witcode
- **说明**: 国债预发行代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_witcode
- **索引**:
  - `idx_usps_witcode` (唯一): stock_code,exchange_type
  - `idx_usps_witcode_pos` (非唯一): position_str
  - `idx_usps_witcode` (唯一): stock_code,exchange_type
  - `idx_usps_witcode_pos` (非唯一): position_str

### etb_bond_code

- **数据库表**: etb_bond_code
- **说明**: 互联互通债券代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: etb_bond_code
- **索引**:
  - `idx_etb_bond_code` (唯一): stock_code_long,exchange_type
  - `idx_etb_bond_code_pos` (非唯一): position_str
  - `idx_etb_bond_code` (唯一): stock_code_long,exchange_type
  - `idx_etb_bond_code_pos` (非唯一): position_str

### secu_bond_info

- **数据库表**: secu_bond_info
- **说明**: 债券产品信息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: secu_bond_info
- **索引**:
  - `idx_secubondinfo` (唯一): stock_code
  - `idx_secubondinfo_pos` (非唯一): position_str
  - `idx_secubondinfo` (唯一): stock_code
  - `idx_secubondinfo_pos` (非唯一): position_str

### upbs_arg

- **数据库表**: upbs_arg
- **说明**: 系统参数表
- **用户**: uargsvr
- **字段**: *
- **同步表**: upbs_arg
- **索引**:
  - `idx_upbs_arg` (唯一): branch_no
  - `idx_upbs_arg_pos` (非唯一): position_str
  - `idx_upbs_arg` (唯一): branch_no
  - `idx_upbs_arg_pos` (非唯一): position_str

### upbs_license_info

- **数据库表**: upbs_license_info
- **说明**: 许可证信息表
- **用户**: usmssvr
- **字段**: *
- **同步表**: upbs_license_info
- **索引**:
  - `idx_upbs_licenseinfo` (唯一): license_id
  - `idx_upbs_licenseinfo` (唯一): license_id

### param_sync_ctrl

- **数据库表**: param_sync_ctrl
- **说明**: 内存交易参数回导控制表
- **用户**: uargsvr
- **字段**: *
- **同步表**: param_sync_ctrl
- **索引**:
  - `idx_param_sync_ctrl` (唯一): table_category
  - `idx_param_sync_ctrl_pos` (非唯一): position_str
  - `idx_param_sync_ctrl` (唯一): table_category
  - `idx_param_sync_ctrl_pos` (非唯一): position_str

### pbs_init_config

- **数据库表**: pbs_init_config
- **说明**: 初始化配置表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_init_config
- **索引**:
  - `uk_init_config` (唯一): service_name,table_name
  - `uk_init_config` (唯一): service_name,table_name

### pbs_sysdeploy

- **数据库表**: pbs_sysdeploy
- **说明**: 子系统部署表
- **用户**: pbssvr
- **字段**: subsys_id,subsys_name,subsys_status,micro_service,uf2_enable_flag,uf3_enable_flag,update_date,update_time,transaction_no,position_str
- **同步表**: pbs_sysdeploy
- **索引**:
  - `uk_pbs_sysdeploy` (唯一): subsys_id
  - `idx_pbs_sysdeploy_pos` (非唯一): position_str
  - `uk_pbs_sysdeploy` (唯一): subsys_id
  - `idx_pbs_sysdeploy_pos` (非唯一): position_str

### pbs_sysnode_deploy

- **数据库表**: pbs_sysnode_deploy
- **说明**: 系统节点部署表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_sysnode_deploy
- **索引**:
  - `uk_sysnode_deploy` (唯一): sysnode_id,subsys_id
  - `idx_sysnode_deploy_pos` (非唯一): position_str
  - `uk_sysnode_deploy` (唯一): sysnode_id,subsys_id
  - `idx_sysnode_deploy_pos` (非唯一): position_str

### upbs_all_company

- **数据库表**: upbs_all_company
- **说明**: 券商信息表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_all_company
- **索引**:
  - `idx_upbs_all_company` (唯一): company_no
  - `idx_upbs_all_company_pos` (非唯一): position_str
  - `idx_upbs_all_company` (唯一): company_no
  - `idx_upbs_all_company_pos` (非唯一): position_str

### upbs_hs_function

- **数据库表**: upbs_hs_function
- **说明**: 证券系统功能表
- **用户**: pbssvr
- **字段**: function_id,en_sys_status,func_flag_str,password_type,restend_time,reststart_time,transaction_no,func_busi_type,right_type
- **同步表**: pbs_hs_function
- **索引**:
  - `idx_upbs_hs_function` (唯一): function_id
  - `idx_upbs_hs_function_pos` (非唯一): position_str
  - `idx_upbs_hs_function` (唯一): function_id
  - `idx_upbs_hs_function_pos` (非唯一): position_str

### upbs_sysconfig

- **数据库表**: upbs_sysconfig
- **说明**: 系统配置参数表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_sysconfig
- **索引**:
  - `idx_sysconfig` (唯一): branch_no,config_no
  - `idx_sysconfig_pos` (非唯一): position_str
  - `idx_sysconfig` (唯一): branch_no,config_no
  - `idx_sysconfig_pos` (非唯一): position_str

### upbs_umtconfig

- **数据库表**: upbs_umtconfig
- **说明**: 内存交易参数表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_umtconfig
- **索引**:
  - `idx_upbs_umtconfig` (唯一): partition_no
  - `idx_upbs_umtconfig_pos` (非唯一): position_str
  - `idx_upbs_umtconfig` (唯一): partition_no
  - `idx_upbs_umtconfig_pos` (非唯一): position_str

### upbs_all_branch

- **数据库表**: upbs_all_branch
- **说明**: 券商机构表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_all_branch
- **索引**:
  - `idx_all_branch` (唯一): branch_no
  - `idx_all_branch_pos` (非唯一): position_str
  - `idx_all_branch` (唯一): branch_no
  - `idx_all_branch_pos` (非唯一): position_str

### upbs_acct_rule

- **数据库表**: upbs_acct_rule
- **说明**: 账户分片规则表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_acct_rule
- **索引**:
  - `idx_upbs_acct_rule_uk` (唯一): position_str
  - `idx_upbs_acct_rule` (非唯一): umt_begin_account,acct_rule_type,sysnode_id
  - `idx_upbs_acct_rule_uk` (唯一): position_str
  - `idx_upbs_acct_rule` (非唯一): umt_begin_account,acct_rule_type,sysnode_id

### upbs_init_date_model

- **数据库表**: upbs_init_date_model
- **说明**: 交易日期表
- **用户**: pbssvr
- **字段**: init_date,init_model,settle_flag,trade_flag,special_trade_flag,transaction_no,position_str
- **同步表**: pbs_init_date_model
- **索引**:
  - `idx_upbs_init_date_model` (唯一): init_date,init_model
  - `idx_upbs_init_date_model_pos` (非唯一): position_str
  - `idx_upbs_init_date_model` (唯一): init_date,init_model
  - `idx_upbs_init_date_model_pos` (非唯一): position_str

### upbs_account_deploy

- **数据库表**: upbs_account_deploy
- **说明**: 账户部署表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_account_deploy
- **索引**:
  - `idx_accountdeploy` (唯一): fund_account
  - `idx_accountdeploy_pos` (非唯一): position_str
  - `idx_accountdeploy` (唯一): fund_account
  - `idx_accountdeploy_pos` (非唯一): position_str

### upbs_asset_prop_deploy

- **数据库表**: upbs_asset_prop_deploy
- **说明**: 资产属性部署配置表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_asset_prop_deploy
- **索引**:
  - `idx_assetpropdeploy` (唯一): branch_no,asset_prop
  - `idx_assetpropdeploy_pos` (非唯一): position_str
  - `idx_assetpropdeploy` (唯一): branch_no,asset_prop
  - `idx_assetpropdeploy_pos` (非唯一): position_str

### upbs_extern_error

- **数据库表**: upbs_extern_error
- **说明**: 外部错误表
- **用户**: pbssvr
- **字段**: error_info,error_no_dest,error_sort,error_source,error_no_original,transaction_no,position_str
- **同步表**: pbs_extern_error
- **索引**:
  - `idx_upbs_extern_error` (唯一): error_sort,error_source,error_no_original
  - `idx_pbs_externerror` (非唯一): error_no_original
  - `idx_upbs_extern_error_pos` (非唯一): position_str
  - `idx_upbs_extern_error` (唯一): error_sort,error_source,error_no_original
  - `idx_pbs_externerror` (非唯一): error_no_original
  - `idx_upbs_extern_error_pos` (非唯一): position_str

### exchange_rates

- **数据库表**: exchange_rates
- **说明**: 汇率表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_exchange_rate
- **索引**:
  - `idx_exchange_rate` (唯一): money_type,dest_money_type
  - `idx_exchange_rate_pos` (非唯一): position_str
  - `idx_exchange_rate` (唯一): money_type,dest_money_type
  - `idx_exchange_rate_pos` (非唯一): position_str

### usps_branch_prefix

- **数据库表**: usps_branch_prefix
- **说明**: 机构前缀表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_branch_prefix
- **索引**:
  - `idx_branchprefix` (唯一): branch_no,exchange_type,finance_type
  - `idx_branchprefix_pos` (非唯一): position_str
  - `idx_branchprefix` (唯一): branch_no,exchange_type,finance_type
  - `idx_branchprefix_pos` (非唯一): position_str

### upbs_branch_acct_info

- **数据库表**: upbs_branch_acct_info
- **说明**: 机构对应账户信息
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_branch_acct_info
- **索引**:
  - `idx_branchacctinfo` (唯一): branch_no,branch_account_type
  - `idx_branchacctinfo_pos` (非唯一): position_str
  - `idx_branchacctinfo` (唯一): branch_no,branch_account_type
  - `idx_branchacctinfo_pos` (非唯一): position_str

### upbs_dictionary

- **数据库表**: upbs_dictionary
- **说明**: 数据字典表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_dictionary
- **索引**:
  - `idx_upbs_dictionary_uniq` (唯一): dict_entry,sub_entry
  - `idx_upbs_dictionary_pos` (非唯一): position_str
  - `idx_upbs_dictionary_uniq` (唯一): dict_entry,sub_entry
  - `idx_upbs_dictionary_pos` (非唯一): position_str

### upbs_error_msg

- **数据库表**: upbs_error_msg
- **说明**: 错误信息表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_error_msg
- **索引**:
  - `idx_upbs_error_msg` (唯一): error_no
  - `idx_upbs_error_msg_pos` (非唯一): position_str
  - `idx_upbs_error_msg` (唯一): error_no
  - `idx_upbs_error_msg_pos` (非唯一): position_str

### upbs_business_flag

- **数据库表**: upbs_business_flag
- **说明**: 业务标志
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_business_flag
- **索引**:
  - `idx_businflag` (唯一): business_flag
  - `idx_businflag_pos` (非唯一): position_str
  - `idx_businflag` (唯一): business_flag
  - `idx_businflag_pos` (非唯一): position_str

### pbs_sysnode

- **数据库表**: pbs_sysnode
- **说明**: 系统节点表
- **用户**: pbssvr
- **字段**: sysnode_id,sysnode_name,node_type,sysnode_version,update_date,update_time
- **同步表**: pbs_sysnode
- **索引**:
  - `idx_sysnode` (唯一): sysnode_id
  - `idx_sysnode_pos` (非唯一): position_str
  - `idx_sysnode` (唯一): sysnode_id
  - `idx_sysnode_pos` (非唯一): position_str

### upbs_dict_entry

- **数据库表**: upbs_dict_entry
- **说明**: 字典条目表
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_dict_entry
- **索引**:
  - `idx_upbs_dict_entry` (唯一): dict_entry
  - `idx_upbs_dict_entry_pos` (非唯一): position_str
  - `idx_upbs_dict_entry` (唯一): dict_entry
  - `idx_upbs_dict_entry_pos` (非唯一): position_str

### usps_exch_arg

- **数据库表**: usps_exch_arg
- **说明**: 交易参数表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_exch_arg
- **索引**:
  - `idx_usps_exch_arg` (唯一): exchange_type
  - `idx_usps_exch_arg_pos` (非唯一): position_str
  - `idx_usps_exch_arg` (唯一): exchange_type
  - `idx_usps_exch_arg_pos` (非唯一): position_str

### usps_spe_busin_date

- **数据库表**: usps_spe_busin_date
- **说明**: 特殊业务日期表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_spe_busin_date
- **索引**:
  - `idx_usps_spe_busin_date` (唯一): date_type
  - `idx_usps_spe_busin_date_pos` (非唯一): position_str
  - `idx_usps_spe_busin_date` (唯一): date_type
  - `idx_usps_spe_busin_date_pos` (非唯一): position_str

### usps_seats

- **数据库表**: usps_seats
- **说明**: 席位参数表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_seats
- **索引**:
  - `idx_upbs_seats` (唯一): exchange_type,seat_no,branch_no
  - `idx_upbs_seats_prop` (非唯一): branch_no,exchange_type,seat_prop,default_mark
  - `idx_upbs_seats_enclientgroup` (非唯一): exchange_type,branch_no,seat_prop,seatvip_flag,en_stock_type,en_client_group,default_mark
  - `idx_upbs_seats_enstocktype` (非唯一): exchange_type,branch_no,seat_prop,seatvip_flag,en_stock_type,default_mark
  - `idx_upbs_seats_pos` (非唯一): position_str
  - `idx_upbs_seats` (唯一): exchange_type,seat_no,branch_no
  - `idx_upbs_seats_prop` (非唯一): branch_no,exchange_type,seat_prop,default_mark
  - `idx_upbs_seats_enclientgroup` (非唯一): exchange_type,branch_no,seat_prop,seatvip_flag,en_stock_type,en_client_group,default_mark
  - `idx_upbs_seats_enstocktype` (非唯一): exchange_type,branch_no,seat_prop,seatvip_flag,en_stock_type,default_mark
  - `idx_upbs_seats_pos` (非唯一): position_str

### usps_stkcode

- **数据库表**: usps_stkcode
- **说明**: 证券代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_stkcode
- **索引**:
  - `idx_uft_stkcode` (唯一): stock_code,exchange_type
  - `idx_uft_stkcode_pos` (非唯一): position_str
  - `idx_usps_stkcode_relative` (非唯一): exchange_type,relative_code,stock_type
  - `idx_usps_stkcode_stockcode` (非唯一): stock_code
  - `idx_uft_stkcode` (唯一): stock_code,exchange_type
  - `idx_uft_stkcode_pos` (非唯一): position_str
  - `idx_usps_stkcode_relative` (非唯一): exchange_type,relative_code,stock_type
  - `idx_usps_stkcode_stockcode` (非唯一): stock_code

### afof_agencyno

- **数据库表**: afof_agencyno
- **说明**: 基金盘后代销商表
- **用户**: uargsvr
- **字段**: *
- **同步表**: afof_agencyno
- **索引**:
  - `idx_afof_agencyno` (唯一): agency_no
  - `idx_afof_agencyno_pos` (非唯一): position_str
  - `idx_afof_agencyno` (唯一): agency_no
  - `idx_afof_agencyno_pos` (非唯一): position_str

### grade_impawn_rate

- **数据库表**: grade_impawn_rate
- **说明**: 分级质押比率表
- **用户**: uargsvr
- **字段**: *
- **同步表**: grade_impawn_rate
- **索引**:
  - `idx_grade_impawn_rate` (唯一): exchange_type,stock_code
  - `idx_grade_impawn_rate_pos` (非唯一): position_str
  - `idx_grade_impawn_rate` (唯一): exchange_type,stock_code
  - `idx_grade_impawn_rate_pos` (非唯一): position_str

### sett_process_info

- **数据库表**: sett_process_info
- **说明**: 清算流程信息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: sett_process_info
- **索引**:
  - `idx_sett_process_info` (唯一): init_date,exchange_type,sett_prop
  - `idx_sett_process_info_pos` (非唯一): position_str
  - `idx_sett_process_info` (唯一): init_date,exchange_type,sett_prop
  - `idx_sett_process_info_pos` (非唯一): position_str

### usps_authority

- **数据库表**: usps_authority
- **说明**: 权益登记表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_authority
- **索引**:
  - `idx_authority_pos` (唯一): position_str
  - `idx_usps_authority` (非唯一): exchange_type,business_type,authority_code,register_date,stock_code,placard_id,info_kind
  - `idx_usps_authority_type` (非唯一): exchange_type,business_type,authority_code,register_date
  - `idx_usps_authority_code` (非唯一): exchange_type,business_type,info_kind,placard_id,stock_code
  - `idx_authority_pos` (唯一): position_str
  - `idx_usps_authority` (非唯一): exchange_type,business_type,authority_code,register_date,stock_code,placard_id,info_kind
  - `idx_usps_authority_type` (非唯一): exchange_type,business_type,authority_code,register_date
  - `idx_usps_authority_code` (非唯一): exchange_type,business_type,info_kind,placard_id,stock_code

### usps_bond_rate

- **数据库表**: usps_bond_rate
- **说明**: 抵押比率表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_bond_rate
- **索引**:
  - `idx_usps_bond_rate` (唯一): exchange_type,stock_code
  - `idx_usps_bond_rate_pos` (非唯一): position_str
  - `idx_usps_bond_rate` (唯一): exchange_type,stock_code
  - `idx_usps_bond_rate_pos` (非唯一): position_str

### usps_debtinterest

- **数据库表**: usps_debtinterest
- **说明**: 国债利息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_debtinterest
- **索引**:
  - `idx_usps_debtinterest` (唯一): exchange_type,stock_code
  - `idx_usps_debtinterest_pos` (非唯一): position_str
  - `idx_usps_debtinterest` (唯一): exchange_type,stock_code
  - `idx_usps_debtinterest_pos` (非唯一): position_str

### usps_etf_code

- **数据库表**: usps_etf_code
- **说明**: ETF代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_etf_code
- **索引**:
  - `idx_usps_etf_code` (唯一): stock_code,channel_type,exchange_type,init_date
  - `idx_usps_etf_code_pos` (非唯一): position_str
  - `idx_usps_etf_code` (唯一): stock_code,channel_type,exchange_type,init_date
  - `idx_usps_etf_code_pos` (非唯一): position_str

### usps_exchange_time

- **数据库表**: usps_exchange_time
- **说明**: 交易时间表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_exchange_time
- **索引**:
  - `idx_usps_exchange_time` (唯一): time_kind,time_order,exchange_type
  - `idx_usps_exchange_time_kind` (非唯一): time_kind
  - `idx_usps_exchange_time_pos` (非唯一): position_str
  - `idx_usps_exchange_time` (唯一): time_kind,time_order,exchange_type
  - `idx_usps_exchange_time_kind` (非唯一): time_kind
  - `idx_usps_exchange_time_pos` (非唯一): position_str

### usps_ffare

- **数据库表**: usps_ffare
- **说明**: 前台费用表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_ffare
- **索引**:
  - `idx_usps_ffare` (唯一): fare_kind,fare_type,exchange_type,stock_type,entrust_way,money_type,sub_stock_type
  - `idx_usps_ffare_norm` (非唯一): fare_kind,fare_type,stock_type,exchange_type,sub_stock_type,entrust_way
  - `idx_usps_ffare_pos` (非唯一): position_str
  - `idx_usps_ffare` (唯一): fare_kind,fare_type,exchange_type,stock_type,entrust_way,money_type,sub_stock_type
  - `idx_usps_ffare_norm` (非唯一): fare_kind,fare_type,stock_type,exchange_type,sub_stock_type,entrust_way
  - `idx_usps_ffare_pos` (非唯一): position_str

### usps_fixed_price_params

- **数据库表**: usps_fixed_price_params
- **说明**: 盘后定价交易业务信息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_fixed_price_params
- **索引**:
  - `idx_usps_fixed_price_params` (唯一): exchange_type,stock_code
  - `idx_usps_fixed_price_params_pos` (非唯一): position_str
  - `idx_usps_fixed_price_params` (唯一): exchange_type,stock_code
  - `idx_usps_fixed_price_params_pos` (非唯一): position_str

### usps_promise_info

- **数据库表**: usps_promise_info
- **说明**: 要约信息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_promise_info
- **索引**:
  - `idx_usps_promise_info` (唯一): stock_code,exchange_type,purchase_id
  - `idx_usps_promise_info_exch` (非唯一): exchange_type
  - `idx_usps_promise_info_pos` (非唯一): position_str
  - `idx_usps_promise_info` (唯一): stock_code,exchange_type,purchase_id
  - `idx_usps_promise_info_exch` (非唯一): exchange_type
  - `idx_usps_promise_info_pos` (非唯一): position_str

### usps_qrp_code

- **数据库表**: usps_qrp_code
- **说明**: 报价回购代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_qrp_code
- **索引**:
  - `idx_qrpcode` (唯一): stock_code,exchange_type,company_no
  - `idx_qrpcode_pos` (非唯一): position_str
  - `idx_qrpcode` (唯一): stock_code,exchange_type,company_no
  - `idx_qrpcode_pos` (非唯一): position_str

### usps_srp_code

- **数据库表**: usps_srp_code
- **说明**: 股票质押代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_srp_code
- **索引**:
  - `idx_srpcode` (唯一): stock_code,exchange_type,srp_kind,company_no
  - `idx_srpcode_pos` (非唯一): position_str
  - `idx_srpcode` (唯一): stock_code,exchange_type,srp_kind,company_no
  - `idx_srpcode_pos` (非唯一): position_str

### usps_stb_stkcode

- **数据库表**: usps_stb_stkcode
- **说明**: 股转证券代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_stb_stkcode
- **索引**:
  - `idx_usps_stb_stkcode` (唯一): exchange_type,stock_code
  - `idx_usps_stb_stkcode_pos` (非唯一): position_str
  - `idx_usps_stb_stkcode` (唯一): exchange_type,stock_code
  - `idx_usps_stb_stkcode_pos` (非唯一): position_str

### usps_stkcode_ext

- **数据库表**: usps_stkcode_ext
- **说明**: 证券代码扩展表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_stkcode_ext
- **索引**:
  - `idx_usps_stkcodeext` (唯一): exchange_type,stock_code,bond_trade_type
  - `idx_usps_stkcodeext_stockcode` (非唯一): stock_code,exchange_type
  - `idx_usps_stkcodeext_pos` (非唯一): position_str
  - `idx_usps_stkcodeext` (唯一): exchange_type,stock_code,bond_trade_type
  - `idx_usps_stkcodeext_stockcode` (非唯一): stock_code,exchange_type
  - `idx_usps_stkcodeext_pos` (非唯一): position_str

### usps_stknotice_info

- **数据库表**: usps_stknotice_info
- **说明**: 证券提示信息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_stknotice_info
- **索引**:
  - `idx_usps_stknotice_info` (唯一): stock_code,exchange_type,stock_type,sub_stock_type,notice_type,start_date,end_date
  - `idx_usps_stknotice_info_pos` (非唯一): position_str
  - `idx_usps_stknotice_info` (唯一): stock_code,exchange_type,stock_type,sub_stock_type,notice_type,start_date,end_date
  - `idx_usps_stknotice_info_pos` (非唯一): position_str

### usps_warrant_code

- **数据库表**: usps_warrant_code
- **说明**: 权证代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_warrant_code
- **索引**:
  - `idx_warrant_code` (唯一): exchange_type,warrant_code
  - `idx_warrant_code_apply` (唯一): exchange_type,apply_code
  - `idx_warrant_code_pos` (非唯一): position_str
  - `idx_warrant_code` (唯一): exchange_type,warrant_code
  - `idx_warrant_code_apply` (唯一): exchange_type,apply_code
  - `idx_warrant_code_pos` (非唯一): position_str

### usps_witcode

- **数据库表**: usps_witcode
- **说明**: 国债预发行代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: usps_witcode
- **索引**:
  - `idx_usps_witcode` (唯一): stock_code,exchange_type
  - `idx_usps_witcode_pos` (非唯一): position_str
  - `idx_usps_witcode` (唯一): stock_code,exchange_type
  - `idx_usps_witcode_pos` (非唯一): position_str

### etb_bond_code

- **数据库表**: etb_bond_code
- **说明**: 互联互通债券代码表
- **用户**: uargsvr
- **字段**: *
- **同步表**: etb_bond_code
- **索引**:
  - `idx_etb_bond_code` (唯一): stock_code_long,exchange_type
  - `idx_etb_bond_code_pos` (非唯一): position_str
  - `idx_etb_bond_code` (唯一): stock_code_long,exchange_type
  - `idx_etb_bond_code_pos` (非唯一): position_str

### secu_bond_info

- **数据库表**: secu_bond_info
- **说明**: 债券产品信息表
- **用户**: uargsvr
- **字段**: *
- **同步表**: secu_bond_info
- **索引**:
  - `idx_secubondinfo` (唯一): stock_code
  - `idx_secubondinfo_pos` (非唯一): position_str
  - `idx_secubondinfo` (唯一): stock_code
  - `idx_secubondinfo_pos` (非唯一): position_str

### upbs_arg

- **数据库表**: upbs_arg
- **说明**: 系统参数表
- **用户**: uargsvr
- **字段**: *
- **同步表**: upbs_arg
- **索引**:
  - `idx_upbs_arg` (唯一): branch_no
  - `idx_upbs_arg_pos` (非唯一): position_str
  - `idx_upbs_arg` (唯一): branch_no
  - `idx_upbs_arg_pos` (非唯一): position_str

### upbs_license_info

- **数据库表**: upbs_license_info
- **说明**: 许可证信息表
- **用户**: usmssvr
- **字段**: *
- **同步表**: upbs_license_info
- **索引**:
  - `idx_upbs_licenseinfo` (唯一): license_id
  - `idx_upbs_licenseinfo` (唯一): license_id

### param_sync_ctrl

- **数据库表**: param_sync_ctrl
- **说明**: 内存交易参数回导控制表
- **用户**: uargsvr
- **字段**: *
- **同步表**: param_sync_ctrl
- **索引**:
  - `idx_param_sync_ctrl` (唯一): table_category
  - `idx_param_sync_ctrl_pos` (非唯一): position_str
  - `idx_param_sync_ctrl` (唯一): table_category
  - `idx_param_sync_ctrl_pos` (非唯一): position_str

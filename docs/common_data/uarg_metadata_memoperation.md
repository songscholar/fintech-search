# uarg - 内存表定义

内存表（缓存表）定义，包含表名、同步表、索引等信息。

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-22 15:39:00 | 3.0.2.13 | 高志强 | 对物理表有position_str字段的，缓存表增加position_str非唯一索引，优化更新场景的性能表现 |
| 2025-12-19 09:09:42 | 3.0.2.12 | 冯元栋 | 增加非唯一索引 |
| 2025-11-19 15:46:00 | 3.0.2.11 | 蒋浩宇 | 新增 param_sync_ctrl |
| 2025-11-03 10:00:00 | 3.0.2.10 | 高志强 | uarg新增本地缓存upbs_arg,用于优化行情性能 |
| 2025-10-31 15:21:00 | 3.0.2.9 | 蒋浩 | 拼音表支持本地缓存表 |
| 2025-10-13 15:21:00 | 3.0.2.8 | 高志强 | upbs_extern_error缓存表唯一索引变更为error_sort,error_source,error_no_original,去除error_no_... |
| 2025-09-26 10:05:00 | 3.0.2.7 | 高志强 | 回退T202509167429的修改 |
| 2025-09-20 15:19:21 | 3.0.2.6 | 高志强 | upbs_arg改造为数据源是pbs库的缓存表 |
| 2025-09-18 15:19:21 | 3.0.2.5 | 蒋浩宇 | 删除多余的本地缓存表usps_witcode |
| 2025-09-05 15:53:58 | 3.0.2.4 | 高志强 | 资源改为和配置一致 |
| 2025-09-04 16:42:01 | 3.0.2.3 | 王云乾 | usms去掉了多余的物理表，这里同步去掉对应的uarg的本地缓存表，共计61个本地缓存表 |
| 2025-08-23 15:15:38 | 3.0.2.2 | 高志强 | 新增 pbs_tradeexport_tables |
| 2025-08-07 16:51:02 | 3.0.2.1 | 高志强 | 修复 idx_upbs_hs_function 显示有错误的问题 |


## 内存表列表（共 50 个）

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
  - `idx_upbs_acct_rule` (非唯一): umt_begin_account,acct_rule_type,sysnode_id
  - `idx_upbs_acct_rule_uk` (唯一): position_str
  - `idx_upbs_acct_rule` (非唯一): umt_begin_account,acct_rule_type,sysnode_id
  - `idx_upbs_acct_rule_uk` (唯一): position_str

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

### pbs_tradeexport_tables

- **数据库表**: pbs_tradeexport_tables
- **说明**: 清算导出表信息
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_tradeexport_tables
- **索引**:
  - `idx_pbs_tradeexport_tables` (唯一): subsys_id,table_name
  - `idx_pbs_tradeexport_tables` (唯一): subsys_id,table_name

### ccspell

- **数据库表**: ccspell
- **说明**: 拼音
- **用户**: uargsvr
- **字段**: *
- **同步表**: ccspell
- **索引**:
  - `idx_spell` (唯一): hz,py
  - `idx_spell` (唯一): hz,py

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

### assunderly_arg

- **数据库表**: assunderly_arg
- **说明**: 担保标的一站式参数表
- **用户**: uargsvr
- **字段**: *
- **同步表**: assunderly_arg
- **索引**:
  - `idx_assunderly_arg` (唯一): order_no
  - `idx_assunderly_arg_pos` (非唯一): position_str
  - `idx_assunderly_arg` (唯一): order_no
  - `idx_assunderly_arg_pos` (非唯一): position_str

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
  - `idx_upbs_acct_rule` (非唯一): umt_begin_account,acct_rule_type,sysnode_id
  - `idx_upbs_acct_rule_uk` (唯一): position_str
  - `idx_upbs_acct_rule` (非唯一): umt_begin_account,acct_rule_type,sysnode_id
  - `idx_upbs_acct_rule_uk` (唯一): position_str

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

### pbs_tradeexport_tables

- **数据库表**: pbs_tradeexport_tables
- **说明**: 清算导出表信息
- **用户**: pbssvr
- **字段**: *
- **同步表**: pbs_tradeexport_tables
- **索引**:
  - `idx_pbs_tradeexport_tables` (唯一): subsys_id,table_name
  - `idx_pbs_tradeexport_tables` (唯一): subsys_id,table_name

### ccspell

- **数据库表**: ccspell
- **说明**: 拼音
- **用户**: uargsvr
- **字段**: *
- **同步表**: ccspell
- **索引**:
  - `idx_spell` (唯一): hz,py
  - `idx_spell` (唯一): hz,py

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

### assunderly_arg

- **数据库表**: assunderly_arg
- **说明**: 担保标的一站式参数表
- **用户**: uargsvr
- **字段**: *
- **同步表**: assunderly_arg
- **索引**:
  - `idx_assunderly_arg` (唯一): order_no
  - `idx_assunderly_arg_pos` (非唯一): position_str
  - `idx_assunderly_arg` (唯一): order_no
  - `idx_assunderly_arg_pos` (非唯一): position_str

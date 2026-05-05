# usms - 用户自定义宏

用户自定义宏定义，包含宏名称、参数、内容和使用说明。

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-10-24 15:27:24 | 3.0.2.1 | 高志强 | 由于存在并发推送数据乱序的场景,因此回退掉T202510156708中除usms_fund_account以外的修改. |
| 2025-10-20 14:36:06 | 3.0.0.4 | 高志强 | 新增自定义宏"如果资产账户不存在"判断usms是否存在有n权限的资产账户 |
| 2025-09-29 14:42:57 | 3.0.0.3 | 冯元栋 | 新增获取参数管理分片号 |
| 2025-01-26 16:38:51 | 3.0.0.2 | 周鹏 | 新增用户自定义宏"核心DB通用参数同步" |
| 2023-03-21 15:37 | 3.0.0.1 | 陈盛志 | 初始版本号 |


## 宏列表（共 24 个）

### 核心DB通用参数同步

- **参数**: `[解包器名][对象名]{[全局唯一索引名]}{[不修改字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[手工解包开始\]\[$paramStr\]\[[解包器名]\] 
  \[事务处理开始\]
  <M>\[通用SQL执行\]\[$indexFieldsAssignStr\]\[count = @sql_row_count\]\[transaction_no = @transaction_no_t\]
  if (@sql_row_count > 0)
  {
    if (@transaction_no > @transaction_no_t)
    {
      if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
      {
        \[通用SQL执行\]\[$updateStr\]\[\]
      }
      else if (CNST_PARAMOPER_DELETE == @param_oper_type)
      {
        \[通用SQL执行\]\[$deleteStr\]\[\]
      }
    }
  }
  else if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
  {
    \[通用SQL执行\]\[$insertStr\]\[\]
  }
  \[事务处理结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[核心DB通用参数同步][@unpack_sett][upbs_extern_error][idx_upbs_extern_error]

### 核心DB特殊账户同步

- **参数**: `[解包器名][对象名][全局唯一索引名]{[修改字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@token_sync_flag = CNST_ALLSYNCFLAG_NO;
  \[事务处理开始\]
  <M>\[通用SQL执行\]\[select transaction_no from usms_sync_counter where table_category = @table_category and position_str = @position_str\]\[count = @sql_row_count\]\[transaction_no = @transaction_no_t\]
  \[EXCEPTION\]
  \[WHEN_NO_DATA_FOUND\]
  {
	@transaction_no_t = 0;
	<M>\[通用SQL执行\]\[insert into usms_sync_counter (table_category,position_str,transaction_no) values (@table_category,@position_str,@transaction_no)\]\[count = @sql_row_count\]
	\[EXCEPTION\]
	\[WHEN_DUP_VAL_ON_INDEX\]
	{
	  \[通用SQL执行\]\[update usms_sync_counter set transaction_no = @transaction_no_t where table_category = @table_category and position_str = @position_str\]\[count = @sql_row_count\]
	}
  }

  \[通用SQL执行\]\[$indexFieldsAssignStr\]\[count = @sql_row_count\]
  if (@sql_row_count > 0)
  {
    if (@transaction_no > @transaction_no_t)
    {
      if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
      {
        \[通用SQL执行\]\[$updateStr\]\[\]
      }
      else if (CNST_PARAMOPER_DELETE == @param_oper_type)
      {
        \[通用SQL执行\]\[$deleteStr\]\[\]
      }
	  \[通用SQL执行\]\[update usms_sync_counter set transaction_no = @transaction_no where table_category = @table_category and position_str = @position_str\]\[count = @sql_row_count\]
	  @token_sync_flag = CNST_ALLSYNCFLAG_YES;
    }
  }
  else if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
  {
    \[通用SQL执行\]\[$insertStr\]\[\]
    @token_sync_flag = CNST_ALLSYNCFLAG_YES;
  }
  \[事务处理结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[核心DB特殊账户同步][@unpack_sett][upbs_extern_error][idx_upbs_extern_error]

### 插入DB表记录

- **参数**: `[对象]{[参数列表]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
$macroFlag\[通用SQL执行\]\[$insertSql\]\[count = @sql_row_count\]
```

**说明**: 【参数说明】
·对象：具体插入的记录类型
·参数列表：field_name=@variable,...
【备注】
·只需要指定变量与对象字段不一致的字段，若全部一致，可省略。
.不支持在同一事务中，先删除后插入key值相同的记录
【标签】
 支持M标识，打上M标识报错后不返回。
【范例】
[插入DB表记录][Entrust][entrust_status=2, exchange_type=@exchange_type_t]

<M>[插入DB表记录][Entrust][entrust_status=2, exchange_type=@exchange_type_t]

### 通用账户参数同步

- **参数**: `[消息主题][对象名][表对象号]`
- **适用类型**: 函数,服务

```
\[手工打包头\]\[$FieldsStr\]
      \[手工打包体\]\[$FieldsParamStr\]
      \[手工打包结束\]
      
      @business_data = lpAnswer->GetPackBuf();
      pi_business_data = lpAnswer->GetPackLen();
      //4.将同步信息发表至MC
      \[消息发布\]\[topic_name = [消息主题]\]\[table_category = [表对象号],
                                                param_oper_type = @param_oper_type,
                                                transaction_no = @transaction_no,
                                                business_data = @business_data,
                                                position_str = @position_str,
                                                partition_no = @partition_no\]
```

### 参数同步结束

- **适用类型**: 函数,服务

```
\[手工解包结束\]
```

### 核心DB参数同步无解包

- **参数**: `[解包器名][对象名]{[全局唯一索引名]}{[不修改字段]}`
- **适用类型**: 函数,服务

```
@token_sync_flag = CNST_ALLSYNCFLAG_NO;
  \[事务处理开始\]
  <M>\[通用SQL执行\]\[$indexFieldsAssignStr\]\[count = @sql_row_count\]\[transaction_no = @transaction_no_t\]
  if (@sql_row_count > 0)
  {
    if (@transaction_no > @transaction_no_t)
    {
      if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
      {
        \[通用SQL执行\]\[$updateStr\]\[\]
        @token_sync_flag = CNST_ALLSYNCFLAG_YES;
      }
      else if (CNST_PARAMOPER_DELETE == @param_oper_type)
      {
        \[通用SQL执行\]\[$deleteStr\]\[\]
        @token_sync_flag = CNST_ALLSYNCFLAG_YES;
      }
    }
  }
  else if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
  {
    \[通用SQL执行\]\[$insertStr\]\[\]
    @token_sync_flag = CNST_ALLSYNCFLAG_YES;
  }
  \[事务处理结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[核心DB参数同步无解包][@unpack_sett][upbs_extern_error][idx_upbs_extern_error]

### 核心DB参数同步解包头

- **参数**: `[解包器名][对象名]{[全局唯一索引名]}{[不修改字段]}`
- **适用类型**: 函数,服务

```
\[手工解包开始\]\[$paramStr\]\[[解包器名]\]
```

### 核心DB业务报错返回

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,原子服务,原子函数

```
\[报错返回\]\[[错误号]\]\[{[参数列表]}\]
```

### 获取冲销流水号DB

- **参数**: `[标准字段]`
- **适用类型**: 函数,原子服务,原子函数

```
{
    \[查询缓存表\]\[select init_date,branch_no from upbs_arg\]\[\]
    \[SQL结果集解包开始\]\[init_date = @usermacro_temp_init_date,branch_no = @usermacro_temp_main_branch_no\]
    break;
    \[SQL结果集解包结束\]
    if (@usermacro_temp_init_date == 0)
    {
       \[核心DB业务报错返回\]\[ERR_USER_SYSARG_NOTEXISTS\]\[@usermacro_temp_init_date,@usermacro_temp_main_branch_no\]
    }
    \[通用SQL执行\]\[select serial_counter_value from usms_serial_counter where serial_counter_no = 99999 and branch_no = @usermacro_temp_main_branch_no for update\]\[count=@sql_row_count\]\[\]
    if (@sql_row_count == 0)
    {
      \[插入DB表记录\][usms_serial_counter][serial_counter_value = 1,serial_counter_no = 99999,branch_no = @usermacro_temp_main_branch_no]
    }
    else
    {
     \[通用SQL执行\]\[update usms_serial_counter set serial_counter_value = serial_counter_value +1 where serial_counter_no = 99999 and branch_no = @usermacro_temp_main_branch_no\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]
    }
    
    \[通用SQL执行\]\[select serial_counter_value from usms_serial_counter where serial_counter_no = 99999 and branch_no = @usermacro_temp_main_branch_no\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]

    if (@usermacro_temp_cancel_serial_no == 0)
    {
        <W>\[事务内报错返回\]\[ERR_ASSET_TABLERECORD_NOTEXISTS\]\[@init_date,@usermacro_temp_main_branch_no\]
    }
    \[事务处理结束\]
    hs_snprintf(@[标准字段], sizeof(@[标准字段]), "%08d%010d%s", @usermacro_temp_init_date,@usermacro_temp_cancel_serial_no, lpIUFTContext->GetLdpHost()->GetVariables()->GetString(VarID::ShortAppName));
}
```

### 获取带分片序列号8位DB

- **参数**: `\[序号\]\[序列号\]`
- **适用类型**: 函数,原子服务,原子函数

```
{
  \[通用SQL执行\]\[select init_date,branch_no from upbs_arg\]\[\]\[init_date = @usermacro_temp_init_date,branch_no = @usermacro_temp_main_branch_no\]
  if (@init_date == 0)
  {
    \[核心DB业务报错返回\]\[ERR_USER_SYSARG_NOTEXISTS\]\[@init_date,@usermacro_temp_main_branch_no\]
  }
  \[通用SQL执行\]\[select serial_counter_value from usms_serial_counter where serial_counter_no = [序号] and branch_no = @usermacro_temp_main_branch_no for update\]\[count=@sql_row_count\]\[\]
  if (@sql_row_count == 0)
  {
    \[插入DB表记录\][usms_serial_counter][serial_counter_value = 1,serial_counter_no = [序号],branch_no = @usermacro_temp_main_branch_no]
  }
  else
  {
    \[通用SQL执行\]\[update usms_serial_counter set serial_counter_value = serial_counter_value +1 where serial_counter_no = [序号] and branch_no = @usermacro_temp_main_branch_no\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]
  }

  \[通用SQL执行\]\[select serial_counter_value from usms_serial_counter where serial_counter_no = [序号] and branch_no = @usermacro_temp_main_branch_no\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]
  
  if (@usermacro_temp_cancel_serial_no == 0)
  {
    <W>\[事务内报错返回\]\[ERR_ASSET_TABLERECORD_NOTEXISTS\]\[@init_date,@usermacro_temp_main_branch_no\]
  }
  \[事务处理结束\]
  [序列号] += (lpIUFTContext->GetBizProc()->GetShardNo() * 1000000);
}
```

### 获取交易参数分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetUargPartitionNo();
```

### 获取经营管理库部署标识

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetRptDataSourceDeployFlag();
```

**说明**: 0:没有部署
1:已部署

### 核心DB通用参数同步

- **参数**: `[解包器名][对象名]{[全局唯一索引名]}{[不修改字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[手工解包开始\]\[$paramStr\]\[[解包器名]\] 
  \[事务处理开始\]
  <M>\[通用SQL执行\]\[$indexFieldsAssignStr\]\[count = @sql_row_count\]\[transaction_no = @transaction_no_t\]
  if (@sql_row_count > 0)
  {
    if (@transaction_no > @transaction_no_t)
    {
      if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
      {
        \[通用SQL执行\]\[$updateStr\]\[\]
      }
      else if (CNST_PARAMOPER_DELETE == @param_oper_type)
      {
        \[通用SQL执行\]\[$deleteStr\]\[\]
      }
    }
  }
  else if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
  {
    \[通用SQL执行\]\[$insertStr\]\[\]
  }
  \[事务处理结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[核心DB通用参数同步][@unpack_sett][upbs_extern_error][idx_upbs_extern_error]

### 核心DB特殊账户同步

- **参数**: `[解包器名][对象名][全局唯一索引名]{[修改字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@token_sync_flag = CNST_ALLSYNCFLAG_NO;
  \[事务处理开始\]
  <M>\[通用SQL执行\]\[select transaction_no from usms_sync_counter where table_category = @table_category and position_str = @position_str\]\[count = @sql_row_count\]\[transaction_no = @transaction_no_t\]
  \[EXCEPTION\]
  \[WHEN_NO_DATA_FOUND\]
  {
	@transaction_no_t = 0;
	<M>\[通用SQL执行\]\[insert into usms_sync_counter (table_category,position_str,transaction_no) values (@table_category,@position_str,@transaction_no)\]\[count = @sql_row_count\]
	\[EXCEPTION\]
	\[WHEN_DUP_VAL_ON_INDEX\]
	{
	  \[通用SQL执行\]\[update usms_sync_counter set transaction_no = @transaction_no_t where table_category = @table_category and position_str = @position_str\]\[count = @sql_row_count\]
	}
  }

  \[通用SQL执行\]\[$indexFieldsAssignStr\]\[count = @sql_row_count\]
  if (@sql_row_count > 0)
  {
    if (@transaction_no > @transaction_no_t)
    {
      if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
      {
        \[通用SQL执行\]\[$updateStr\]\[\]
      }
      else if (CNST_PARAMOPER_DELETE == @param_oper_type)
      {
        \[通用SQL执行\]\[$deleteStr\]\[\]
      }
	  \[通用SQL执行\]\[update usms_sync_counter set transaction_no = @transaction_no where table_category = @table_category and position_str = @position_str\]\[count = @sql_row_count\]
	  @token_sync_flag = CNST_ALLSYNCFLAG_YES;
    }
  }
  else if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
  {
    \[通用SQL执行\]\[$insertStr\]\[\]
    @token_sync_flag = CNST_ALLSYNCFLAG_YES;
  }
  \[事务处理结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[核心DB特殊账户同步][@unpack_sett][upbs_extern_error][idx_upbs_extern_error]

### 插入DB表记录

- **参数**: `[对象]{[参数列表]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
$macroFlag\[通用SQL执行\]\[$insertSql\]\[count = @sql_row_count\]
```

**说明**: 【参数说明】
·对象：具体插入的记录类型
·参数列表：field_name=@variable,...
【备注】
·只需要指定变量与对象字段不一致的字段，若全部一致，可省略。
.不支持在同一事务中，先删除后插入key值相同的记录
【标签】
 支持M标识，打上M标识报错后不返回。
【范例】
[插入DB表记录][Entrust][entrust_status=2, exchange_type=@exchange_type_t]

<M>[插入DB表记录][Entrust][entrust_status=2, exchange_type=@exchange_type_t]

### 通用账户参数同步

- **参数**: `[消息主题][对象名][表对象号]`
- **适用类型**: 函数,服务

```
\[手工打包头\]\[$FieldsStr\]
      \[手工打包体\]\[$FieldsParamStr\]
      \[手工打包结束\]
      
      @business_data = lpAnswer->GetPackBuf();
      pi_business_data = lpAnswer->GetPackLen();
      //4.将同步信息发表至MC
      \[消息发布\]\[topic_name = [消息主题]\]\[table_category = [表对象号],
                                                param_oper_type = @param_oper_type,
                                                transaction_no = @transaction_no,
                                                business_data = @business_data,
                                                position_str = @position_str,
                                                partition_no = @partition_no\]
```

### 参数同步结束

- **适用类型**: 函数,服务

```
\[手工解包结束\]
```

### 核心DB参数同步无解包

- **参数**: `[解包器名][对象名]{[全局唯一索引名]}{[不修改字段]}`
- **适用类型**: 函数,服务

```
@token_sync_flag = CNST_ALLSYNCFLAG_NO;
  \[事务处理开始\]
  <M>\[通用SQL执行\]\[$indexFieldsAssignStr\]\[count = @sql_row_count\]\[transaction_no = @transaction_no_t\]
  if (@sql_row_count > 0)
  {
    if (@transaction_no > @transaction_no_t)
    {
      if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
      {
        \[通用SQL执行\]\[$updateStr\]\[\]
        @token_sync_flag = CNST_ALLSYNCFLAG_YES;
      }
      else if (CNST_PARAMOPER_DELETE == @param_oper_type)
      {
        \[通用SQL执行\]\[$deleteStr\]\[\]
        @token_sync_flag = CNST_ALLSYNCFLAG_YES;
      }
    }
  }
  else if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
  {
    \[通用SQL执行\]\[$insertStr\]\[\]
    @token_sync_flag = CNST_ALLSYNCFLAG_YES;
  }
  \[事务处理结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[核心DB参数同步无解包][@unpack_sett][upbs_extern_error][idx_upbs_extern_error]

### 核心DB参数同步解包头

- **参数**: `[解包器名][对象名]{[全局唯一索引名]}{[不修改字段]}`
- **适用类型**: 函数,服务

```
\[手工解包开始\]\[$paramStr\]\[[解包器名]\]
```

### 核心DB业务报错返回

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,原子服务,原子函数

```
\[报错返回\]\[[错误号]\]\[{[参数列表]}\]
```

### 获取冲销流水号DB

- **参数**: `[标准字段]`
- **适用类型**: 函数,原子服务,原子函数

```
{
    \[查询缓存表\]\[select init_date,branch_no from upbs_arg\]\[\]
    \[SQL结果集解包开始\]\[init_date = @usermacro_temp_init_date,branch_no = @usermacro_temp_main_branch_no\]
    break;
    \[SQL结果集解包结束\]
    if (@usermacro_temp_init_date == 0)
    {
       \[核心DB业务报错返回\]\[ERR_USER_SYSARG_NOTEXISTS\]\[@usermacro_temp_init_date,@usermacro_temp_main_branch_no\]
    }
    \[通用SQL执行\]\[select serial_counter_value from usms_serial_counter where serial_counter_no = 99999 and branch_no = @usermacro_temp_main_branch_no for update\]\[count=@sql_row_count\]\[\]
    if (@sql_row_count == 0)
    {
      \[插入DB表记录\][usms_serial_counter][serial_counter_value = 1,serial_counter_no = 99999,branch_no = @usermacro_temp_main_branch_no]
    }
    else
    {
     \[通用SQL执行\]\[update usms_serial_counter set serial_counter_value = serial_counter_value +1 where serial_counter_no = 99999 and branch_no = @usermacro_temp_main_branch_no\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]
    }
    
    \[通用SQL执行\]\[select serial_counter_value from usms_serial_counter where serial_counter_no = 99999 and branch_no = @usermacro_temp_main_branch_no\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]

    if (@usermacro_temp_cancel_serial_no == 0)
    {
        <W>\[事务内报错返回\]\[ERR_ASSET_TABLERECORD_NOTEXISTS\]\[@init_date,@usermacro_temp_main_branch_no\]
    }
    \[事务处理结束\]
    hs_snprintf(@[标准字段], sizeof(@[标准字段]), "%08d%010d%s", @usermacro_temp_init_date,@usermacro_temp_cancel_serial_no, lpIUFTContext->GetLdpHost()->GetVariables()->GetString(VarID::ShortAppName));
}
```

### 获取带分片序列号8位DB

- **参数**: `\[序号\]\[序列号\]`
- **适用类型**: 函数,原子服务,原子函数

```
{
  \[通用SQL执行\]\[select init_date,branch_no from upbs_arg\]\[\]\[init_date = @usermacro_temp_init_date,branch_no = @usermacro_temp_main_branch_no\]
  if (@init_date == 0)
  {
    \[核心DB业务报错返回\]\[ERR_USER_SYSARG_NOTEXISTS\]\[@init_date,@usermacro_temp_main_branch_no\]
  }
  \[通用SQL执行\]\[select serial_counter_value from usms_serial_counter where serial_counter_no = [序号] and branch_no = @usermacro_temp_main_branch_no for update\]\[count=@sql_row_count\]\[\]
  if (@sql_row_count == 0)
  {
    \[插入DB表记录\][usms_serial_counter][serial_counter_value = 1,serial_counter_no = [序号],branch_no = @usermacro_temp_main_branch_no]
  }
  else
  {
    \[通用SQL执行\]\[update usms_serial_counter set serial_counter_value = serial_counter_value +1 where serial_counter_no = [序号] and branch_no = @usermacro_temp_main_branch_no\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]
  }

  \[通用SQL执行\]\[select serial_counter_value from usms_serial_counter where serial_counter_no = [序号] and branch_no = @usermacro_temp_main_branch_no\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]
  
  if (@usermacro_temp_cancel_serial_no == 0)
  {
    <W>\[事务内报错返回\]\[ERR_ASSET_TABLERECORD_NOTEXISTS\]\[@init_date,@usermacro_temp_main_branch_no\]
  }
  \[事务处理结束\]
  [序列号] += (lpIUFTContext->GetBizProc()->GetShardNo() * 1000000);
}
```

### 获取交易参数分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetUargPartitionNo();
```

### 获取经营管理库部署标识

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetRptDataSourceDeployFlag();
```

**说明**: 0:没有部署
1:已部署

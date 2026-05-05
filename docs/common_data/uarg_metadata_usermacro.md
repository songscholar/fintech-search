# uarg - 用户自定义宏

用户自定义宏定义，包含宏名称、参数、内容和使用说明。

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-09-25 20:44:48 | 3.0.0.6 | 高志强 | 修复clob参数名不一样时打的包无法解开的问题 |
| 2025-09-20 14:14:40 | 3.0.0.5 | 高志强 | 新增[业务核心缓存表同步调用] |
| 2025-09-13 11:08:41 | 3.0.0.4 | 高志强 | 新增[单行数据打包] |
| 2025-09-05 21:06:59 | 3.0.0.3 | 高志强 | 业务核心缓存表同步新增modify_flag判断是否需要落uarg物理库 |
| 2025-01-26 16:38:51 | 3.0.0.2 | 周鹏 | 新增用户自定义宏"核心DB通用参数同步" |
| 2023-03-21 15:37 | 3.0.0.1 | 陈盛志 | 初始版本号 |


## 宏列表（共 22 个）

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

### 获取交易管理分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetUsmsPartitionNo();
```

### 核心DB业务报错返回

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,原子服务,原子函数

```
\[报错返回\]\[[错误号]\]\[{[参数列表]}\]
```

### 获取冲销流水号DB

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
{
    \[通用SQL执行\]\[select a.serial_counter_value from uarg_serial_counter a inner join upbs_arg b on a.branch_no = b.branch_no where serial_counter_no = 99999 for update\]\[count=@sql_row_count\]\[\]
    if (@sql_row_count == 0)
    {
      \[通用SQL执行\][select branch_no from upbs_arg where rownum = 1][][branch_no = @usermacro_temp_main_branch_no]
      \[插入DB表记录\][uarg_serial_counter][serial_counter_value = 1,serial_counter_no = 99999,branch_no = @usermacro_temp_main_branch_no]
    }
    else
    {
        \[通用SQL执行\]\[update uarg_serial_counter a set serial_counter_value = serial_counter_value +1 where serial_counter_no = 99999 and exists (select 1 from upbs_arg where branch_no = a.branch_no)\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]
    }

    \[通用SQL执行\]\[select a.serial_counter_value from uarg_serial_counter a inner join upbs_arg b on a.branch_no = b.branch_no where serial_counter_no = 99999\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]
    if (@usermacro_temp_cancel_serial_no == 0)
    {
        <W>\[事务内报错返回\]\[ERR_ASSET_TABLERECORD_NOTEXISTS\]\[@init_date,@usermacro_temp_main_branch_no\]
    }
    \[事务处理结束\]
    hs_snprintf(@[标准字段], sizeof(@[标准字段]), "%08d%010d%s",@usermacro_temp_init_date,@usermacro_temp_cancel_serial_no, lpIUFTContext->GetLdpHost()->GetVariables()->GetString(VarID::ShortAppName));
}
```

### 业务核心缓存表同步

- **参数**: `[表对象号][对象名][消息主题][参数列表][不获取字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@table_category = [表对象号];

    //判断事务号大小并记录本次事务号.
    <M>\[通用SQL执行\]\[select transaction_no from uarg_syncinfo where table_name = @table_name and position_str = @position_str for update\]\[count = @sql_row_count\]\[transaction_no = @transaction_no_t\]
    //新增记录
    if (0 == @sql_row_count)
    {
      \[继续执行\]
      <M>\[插入DB表记录\]\[uarg_syncinfo\]\[\]
      \[处理失败\]
      {
        <W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type\]
      }
      \[事务处理结束\]
    }
    //更新记录
    else if (@transaction_no > @transaction_no_t)
    {
      <M>\[通用SQL执行\]\[update uarg_syncinfo
                             set transaction_no = @transaction_no
                           where table_name = @table_name
                             and position_str = @position_str\]\[count = @sql_row_count\]\[\]
      \[处理失败\]
      {
        <W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type,@transaction_no_t\]
      }
      else
      {
        \[事务处理结束\]
        if (0 == @sql_row_count)
	    {
	      \[直接返回\]
	    }
      }
    }
    //抛弃消息.
    else
    {
      \[事务处理结束\]
      \[直接返回\]
    }

    <I>\[LF_代码转换公用_系统公用_系统参数信息获取\]\[\]\[init_date = @init_date,main_branch_no = @main_branch_no\]
    @date_clear = @init_date;

    //20250901 gaozq mod 解包字段不包含transaction_no,避免覆盖入参传入的值,预期包体中的事务号和入参应该一致,多条场景下以入参为准.
    \[clob字段解包\]\[@unpacker_v4\]\[@busi_data\]\[pi_busi_data\]
    \[手工解包开始\]\[$paramStr\]\[@unpacker_v4\]
    {
      //20250905 gaozq27559 mod 新增一个标志区分是否落物理库,避免uarg无物理库的表报错.修改单:T202509056279
      //20250901 gaozq mod 临时落uarg物理库,待业务核心对接pbs数据上场后删除相关写物理表的逻辑.
      if (@modify_flag == '1')
      {
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
        else
        {
          \[继续执行\]
          \[通用SQL执行\]\[$insertStr\]\[\]
        }
        \[事务处理结束\]
      }

      //消息发布.
      \[手工打包头\]\[$FieldsStr\]\[@packer_arg\]
      \[手工打包体\]\[$FieldsParamStr\]\[@packer_arg\]
      \[手工打包结束\]\[@packer_arg\]

      @business_data = @packer_arg->GetPackBuf();
      vi_business_data = @packer_arg->GetPackLen();

      \[同步消息发布\]\[topic_name = [消息主题]\]\[table_category = @table_category,
                                                   position_str = @position_str,
                                                   param_oper_type = @param_oper_type,
                                                   transaction_no = @transaction_no,
                                                   business_data = @business_data,
                                                   partition_no = 0\]

      //记录日志.
      <M>\[插入DB表记录\]\[uarg_mc_publish_log\]\[\]
      \[处理失败\]
      {
        //<W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type\]
        \[继续执行\]
      }
      \[事务处理结束\]
    }
    \[手工解包结束\]
```

### 业务核心缓存表同步调用

- **参数**: `[表对象号][对象名][参数同步功能号][参数列表][不获取字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@table_category = [表对象号];

    //判断事务号大小并记录本次事务号.
    <M>\[通用SQL执行\]\[select transaction_no from uarg_syncinfo where table_name = @table_name and position_str = @position_str for update\]\[count = @sql_row_count\]\[transaction_no = @transaction_no_t\]
    //新增记录
    if (0 == @sql_row_count)
    {
      \[继续执行\]
      <M>\[插入DB表记录\]\[uarg_syncinfo\]\[\]
      \[处理失败\]
      {
        <W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type\]
      }
      \[事务处理结束\]
    }
    //更新记录
    else if (@transaction_no > @transaction_no_t)
    {
      <M>\[通用SQL执行\]\[update uarg_syncinfo
                             set transaction_no = @transaction_no
                           where table_name = @table_name
                             and position_str = @position_str\]\[count = @sql_row_count\]\[\]
      \[处理失败\]
      {
        <W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type,@transaction_no_t\]
      }
      else
      {
        \[事务处理结束\]
        if (0 == @sql_row_count)
	    {
	      \[直接返回\]
	    }
      }
    }
    //抛弃消息.
    else
    {
      \[事务处理结束\]
      \[直接返回\]
    }

    <I>\[LF_代码转换公用_系统公用_系统参数信息获取\]\[\]\[init_date = @init_date,main_branch_no = @main_branch_no\]
    @date_clear = @init_date;

    //20240918 gaozq mod 改为调用uconvert.修改单:T202509133255
    //20250901 gaozq mod 解包字段不包含transaction_no,避免覆盖入参传入的值,预期包体中的事务号和入参应该一致,多条场景下以入参为准.
    \[clob字段解包\]\[@unpacker_v4\]\[@business_data\]\[pi_business_data\]
    \[手工解包开始\]\[$paramStr\]\[@unpacker_v4\]
    {
      \[手工打包头\]\[$FieldsStr\]\[@packer_arg\]
      \[手工打包体\]\[$FieldsParamStr\]\[@packer_arg\]
      \[手工打包结束\]\[@packer_arg\]

      @busi_data = @packer_arg->GetPackBuf();
      vi_busi_data = @packer_arg->GetPackLen();

      //调用参数同步功能.
      if (989700 == [参数同步功能号])
      {
        <M>\[LF_代码转换公用_转换服务参数同步\]\[param_oper_type = @param_oper_type,table_category = @table_category,transaction_no = @transaction_no,busi_data = @busi_data,action_in = 0\]\[\]
        \[继续执行\]
      }

      //记录日志.
      <M>\[插入DB表记录\]\[uarg_mc_publish_log\]\[\]
      \[处理失败\]
      {
        //<W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type\]
        \[继续执行\]
      }
      \[事务处理结束\]
    }
    \[手工解包结束\]
```

### 单行数据打包

- **参数**: `[对象名][解包器][打包器][新包变量][新包长度][不获取字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
// 单行解包
  \[手工解包体\]\[$kvStr\]\[[解包器]\]
  
  // 重新打包
  \[手工打包头\]\[$keyStr\]\[[打包器]\]
  \[手工打包体\]\[$valStr\]\[[打包器]\]
  \[手工打包结束\]\[[打包器]\]
  
  // 赋值给新clob变量
  [新包变量] = [打包器]->GetPackBuf();
  [新包长度] = [打包器]->GetPackLen();
```

**说明**: 按照 [对象名] 获取表字段, 排除 js 中的 unModFieldArr 和 [不获取字段] 之后, 将 [解包器] 中当前指针指向的这一行的数据通过 [打包器] 转换给 [新包变量] 和 [新包长度].

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

### 通用账户参数同步

- **参数**: `[消息主题][对象名][表对象号]`
- **适用类型**: 函数,服务

```
\[手工打包头\]\[$FieldsStr\][@packer_arg]
      \[手工打包体\]\[$FieldsParamStr\][@packer_arg]
      \[手工打包结束\][@packer_arg]
      
      @business_data =@packer_arg ->GetPackBuf();
      pi_business_data = @packer_arg ->GetPackLen();
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

### 获取交易管理分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetUsmsPartitionNo();
```

### 核心DB业务报错返回

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,原子服务,原子函数

```
\[报错返回\]\[[错误号]\]\[{[参数列表]}\]
```

### 获取冲销流水号DB

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
{
    \[通用SQL执行\]\[select a.serial_counter_value from uarg_serial_counter a inner join upbs_arg b on a.branch_no = b.branch_no where serial_counter_no = 99999 for update\]\[count=@sql_row_count\]\[\]
    if (@sql_row_count == 0)
    {
      \[通用SQL执行\][select branch_no from upbs_arg where rownum = 1][][branch_no = @usermacro_temp_main_branch_no]
      \[插入DB表记录\][uarg_serial_counter][serial_counter_value = 1,serial_counter_no = 99999,branch_no = @usermacro_temp_main_branch_no]
    }
    else
    {
        \[通用SQL执行\]\[update uarg_serial_counter a set serial_counter_value = serial_counter_value +1 where serial_counter_no = 99999 and exists (select 1 from upbs_arg where branch_no = a.branch_no)\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]
    }

    \[通用SQL执行\]\[select a.serial_counter_value from uarg_serial_counter a inner join upbs_arg b on a.branch_no = b.branch_no where serial_counter_no = 99999\]\[\]\[serial_counter_value = @usermacro_temp_cancel_serial_no\]
    if (@usermacro_temp_cancel_serial_no == 0)
    {
        <W>\[事务内报错返回\]\[ERR_ASSET_TABLERECORD_NOTEXISTS\]\[@init_date,@usermacro_temp_main_branch_no\]
    }
    \[事务处理结束\]
    hs_snprintf(@[标准字段], sizeof(@[标准字段]), "%08d%010d%s",@usermacro_temp_init_date,@usermacro_temp_cancel_serial_no, lpIUFTContext->GetLdpHost()->GetVariables()->GetString(VarID::ShortAppName));
}
```

### 业务核心缓存表同步

- **参数**: `[表对象号][对象名][消息主题][参数列表][不获取字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@table_category = [表对象号];

    //判断事务号大小并记录本次事务号.
    <M>\[通用SQL执行\]\[select transaction_no from uarg_syncinfo where table_name = @table_name and position_str = @position_str for update\]\[count = @sql_row_count\]\[transaction_no = @transaction_no_t\]
    //新增记录
    if (0 == @sql_row_count)
    {
      \[继续执行\]
      <M>\[插入DB表记录\]\[uarg_syncinfo\]\[\]
      \[处理失败\]
      {
        <W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type\]
      }
      \[事务处理结束\]
    }
    //更新记录
    else if (@transaction_no > @transaction_no_t)
    {
      <M>\[通用SQL执行\]\[update uarg_syncinfo
                             set transaction_no = @transaction_no
                           where table_name = @table_name
                             and position_str = @position_str\]\[count = @sql_row_count\]\[\]
      \[处理失败\]
      {
        <W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type,@transaction_no_t\]
      }
      else
      {
        \[事务处理结束\]
        if (0 == @sql_row_count)
	    {
	      \[直接返回\]
	    }
      }
    }
    //抛弃消息.
    else
    {
      \[事务处理结束\]
      \[直接返回\]
    }

    <I>\[LF_代码转换公用_系统公用_系统参数信息获取\]\[\]\[init_date = @init_date,main_branch_no = @main_branch_no\]
    @date_clear = @init_date;

    //20250901 gaozq mod 解包字段不包含transaction_no,避免覆盖入参传入的值,预期包体中的事务号和入参应该一致,多条场景下以入参为准.
    \[clob字段解包\]\[@unpacker_v4\]\[@busi_data\]\[pi_busi_data\]
    \[手工解包开始\]\[$paramStr\]\[@unpacker_v4\]
    {
      //20250905 gaozq27559 mod 新增一个标志区分是否落物理库,避免uarg无物理库的表报错.修改单:T202509056279
      //20250901 gaozq mod 临时落uarg物理库,待业务核心对接pbs数据上场后删除相关写物理表的逻辑.
      if (@modify_flag == '1')
      {
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
        else
        {
          \[继续执行\]
          \[通用SQL执行\]\[$insertStr\]\[\]
        }
        \[事务处理结束\]
      }

      //消息发布.
      \[手工打包头\]\[$FieldsStr\]\[@packer_arg\]
      \[手工打包体\]\[$FieldsParamStr\]\[@packer_arg\]
      \[手工打包结束\]\[@packer_arg\]

      @business_data = @packer_arg->GetPackBuf();
      vi_business_data = @packer_arg->GetPackLen();

      \[同步消息发布\]\[topic_name = [消息主题]\]\[table_category = @table_category,
                                                   position_str = @position_str,
                                                   param_oper_type = @param_oper_type,
                                                   transaction_no = @transaction_no,
                                                   business_data = @business_data,
                                                   partition_no = 0\]

      //记录日志.
      <M>\[插入DB表记录\]\[uarg_mc_publish_log\]\[\]
      \[处理失败\]
      {
        //<W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type\]
        \[继续执行\]
      }
      \[事务处理结束\]
    }
    \[手工解包结束\]
```

### 业务核心缓存表同步调用

- **参数**: `[表对象号][对象名][参数同步功能号][参数列表][不获取字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@table_category = [表对象号];

    //判断事务号大小并记录本次事务号.
    <M>\[通用SQL执行\]\[select transaction_no from uarg_syncinfo where table_name = @table_name and position_str = @position_str for update\]\[count = @sql_row_count\]\[transaction_no = @transaction_no_t\]
    //新增记录
    if (0 == @sql_row_count)
    {
      \[继续执行\]
      <M>\[插入DB表记录\]\[uarg_syncinfo\]\[\]
      \[处理失败\]
      {
        <W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type\]
      }
      \[事务处理结束\]
    }
    //更新记录
    else if (@transaction_no > @transaction_no_t)
    {
      <M>\[通用SQL执行\]\[update uarg_syncinfo
                             set transaction_no = @transaction_no
                           where table_name = @table_name
                             and position_str = @position_str\]\[count = @sql_row_count\]\[\]
      \[处理失败\]
      {
        <W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type,@transaction_no_t\]
      }
      else
      {
        \[事务处理结束\]
        if (0 == @sql_row_count)
	    {
	      \[直接返回\]
	    }
      }
    }
    //抛弃消息.
    else
    {
      \[事务处理结束\]
      \[直接返回\]
    }

    <I>\[LF_代码转换公用_系统公用_系统参数信息获取\]\[\]\[init_date = @init_date,main_branch_no = @main_branch_no\]
    @date_clear = @init_date;

    //20240918 gaozq mod 改为调用uconvert.修改单:T202509133255
    //20250901 gaozq mod 解包字段不包含transaction_no,避免覆盖入参传入的值,预期包体中的事务号和入参应该一致,多条场景下以入参为准.
    \[clob字段解包\]\[@unpacker_v4\]\[@business_data\]\[pi_business_data\]
    \[手工解包开始\]\[$paramStr\]\[@unpacker_v4\]
    {
      \[手工打包头\]\[$FieldsStr\]\[@packer_arg\]
      \[手工打包体\]\[$FieldsParamStr\]\[@packer_arg\]
      \[手工打包结束\]\[@packer_arg\]

      @busi_data = @packer_arg->GetPackBuf();
      vi_busi_data = @packer_arg->GetPackLen();

      //调用参数同步功能.
      if (989700 == [参数同步功能号])
      {
        <M>\[LF_代码转换公用_转换服务参数同步\]\[param_oper_type = @param_oper_type,table_category = @table_category,transaction_no = @transaction_no,busi_data = @busi_data,action_in = 0\]\[\]
        \[继续执行\]
      }

      //记录日志.
      <M>\[插入DB表记录\]\[uarg_mc_publish_log\]\[\]
      \[处理失败\]
      {
        //<W>\[事务内报错返回\]\[ERR_EXEC_SQL_FAIL\]\[@table_name,@position_str,@transaction_no,@param_oper_type\]
        \[继续执行\]
      }
      \[事务处理结束\]
    }
    \[手工解包结束\]
```

### 单行数据打包

- **参数**: `[对象名][解包器][打包器][新包变量][新包长度][不获取字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
// 单行解包
  \[手工解包体\]\[$kvStr\]\[[解包器]\]
  
  // 重新打包
  \[手工打包头\]\[$keyStr\]\[[打包器]\]
  \[手工打包体\]\[$valStr\]\[[打包器]\]
  \[手工打包结束\]\[[打包器]\]
  
  // 赋值给新clob变量
  [新包变量] = [打包器]->GetPackBuf();
  [新包长度] = [打包器]->GetPackLen();
```

**说明**: 按照 [对象名] 获取表字段, 排除 js 中的 unModFieldArr 和 [不获取字段] 之后, 将 [解包器] 中当前指针指向的这一行的数据通过 [打包器] 转换给 [新包变量] 和 [新包长度].

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

### 通用账户参数同步

- **参数**: `[消息主题][对象名][表对象号]`
- **适用类型**: 函数,服务

```
\[手工打包头\]\[$FieldsStr\][@packer_arg]
      \[手工打包体\]\[$FieldsParamStr\][@packer_arg]
      \[手工打包结束\][@packer_arg]
      
      @business_data =@packer_arg ->GetPackBuf();
      pi_business_data = @packer_arg ->GetPackLen();
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

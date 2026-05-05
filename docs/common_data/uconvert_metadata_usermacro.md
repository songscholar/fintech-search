# uconvert - 用户自定义宏

用户自定义宏定义，包含宏名称、参数、内容和使用说明。

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-07-01 14:27:05 | 3.0.5.1003 | 牟家乐 | 新增[新高可用通用参数同步结束]宏 |
| 2025-03-06 21:07:01 | 3.0.5.1002 | 许琮擎 | 新增[高可用通用参数同步结束]宏 |
| 2024-09-30 13:30:01 | 3.0.5.1001 | 余丰亮 | 内存交易错误号信息以及错误号二次重置代码优化 |
| 2024-09-02 13:51:03 | 3.0.4.1 | 袁文龙 | 统一版本号为V3.0.4.1 |
| 2024-08-07 13:32:58 | 3.0.3.2 | 李海洋 | 支持用户自定义宏【通用参数同步开始】、【通用参数同步结束】 |
| 2024-06-28 13:51:03 | 3.0.3.1 | 楼欣欣 | 统一版本号为V3.0.3.1 |
| 2024-05-14 14:45:11 | 3.0.2.2 | 徐志坚 | 修正[clob字段解包]的错误返回方式 |
| 2024-04-16 13:44:16 | 3.0.2.1 | 徐志坚 | 将[获取冲销流水号]宏中用到的hs_snprintf改为snprintf |
| 2024-04-03 16:52:29 | V3.0.1.9 | 徐志坚 | 增加[轮询错误处理]宏 |
| 2024-01-06 11:14:21 | V3.0.1.8 | 楼欣欣 | go to end使用方式优化  |
| 2023-12-23 15:12:33 | V3.0.1.7 | 黄积冲 | 获取请求分片号、获取RPC超时时间、获取回库RPC超时时间、获取转换服务分片号允许因子服务,因子函数执行 |
| 2023-12-19 14:22:28 | V3.0.1.6 | 李海洋 | 修复业务自定义上下文二进制兼容问题  |
| 2023-11-20 10:29:03 | V3.0.1.5 | 程猛 | 调整宏[节点定位插件分片状态更新]的报错信息 |
| 2023-10-31 09:41:17 | V3.0.1.4 | 程猛 | 支持uconvert分片号从json配置获取 |
| 2023-09-25 19:19:24 | V3.0.1.3 | 华曌 | 新增获取RPC、回库RPC超时时间自定义宏 |
| 2023-09-19 11:04:17 | V3.0.1.2 | 徐志坚 | 新增[获取仲裁状态] |
| 2023-09-04 14:40:43 | V3.0.1.1 | 沈勋 | 版本统一调整 |
| 2023-08-30 13:54:17 | 3.0.0.10 | 黄佳平 | deploy_type字典变更改造 |
| 2023-08-23 19:46:05 | 3.0.0.9 | 余世泽 | 新增[业务复核标志] |
| 2023-08-21 12:28 | 3.0.0.8 | 周贺 | 新增[获取请求分片号] |

> 共 28 条修改记录，仅显示最近20条


## 宏列表（共 8 个）

### 通用参数同步开始

- **参数**: `[解包器名][对象名][全局唯一索引名][主题名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
/*1、根据表对象号和操作标志解包
    2、进行数据转换：UF2.0至UFT3.0(表结构)
    3、数据持久化：主动落库，持久化相应参数账户记录
    4、在线核心获取：UFTMDB中获取核心在线信息
    5、参数账户同步流水记录：根据核心在线信息分别插入upbs_syncinfo
    6、消息发布：调用MC接口进行消息发布（根据不同参数账户类型指定主题）
    */
    
  //目前系统内置宏手工解包开始，入参不允许空，暂时随便取一个字段，后续升级后该字段可删除
  \[手工解包开始\]\[partition_no= @partition_no\]\[[解包器名]\]
  
    //2.根据操作类型，按需解包
    if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
    {
      //field_expression,当前表所有字段（除了transaction_no）
      \[手工解包体\]\[$field_expression\]\[[解包器名]\]
    }
    else if (CNST_PARAMOPER_DELETE == @param_oper_type)
    {
      //索引赋值字符串index_expression
      \[手工解包体\]\[$index_expression\]\[[解包器名]\]
    }
```

**说明**: 仅用于uconvert核心的参数同步，用于实现转换服务的通用的参数同步逻辑
适用场景：通用的参数同步场景： UF20柜台参数同步请求的pack包中，包含了内存表同步需要的所有字段。
不适用场景：
带关联关系场景、表同步时有时序逻辑、字段需要字典转换、特殊的处理逻辑等。
[通用参数同步开始]需要与[通用参数同步结束]配合使用，
中间需自行根据业务场景，拼接参数同步流水定位串，用于实现幂等控制。

使用范例：
  [clob字段解包][@unpack_sett][@busi_data][pi_busi_data] 
  
  //填写表名和索引及发布的主题
  [通用参数同步开始][@unpack_sett][usps_vote_code][idx_usps_vote_code][CNST_MC_UFT_PUBSYNC]
 
  //拼接唯一定位串,范例
  hs_strncpy(@meeting_seq_t, @meeting_seq, sizeof(@meeting_seq_t) - 1);
  hs_strncpy(@exchange_type_t, @exchange_type, sizeof(@exchange_type_t) - 1);
  hs_strncpy(@stock_code_t, @stock_code, sizeof(@stock_code_t) - 1); 
  hs_snprintf(@position_str, sizeof(@position_str), "%s%s%s", lpad(@meeting_seq_t, 8, '0'), lpad(@exchange_type_t, 4, '0'), lpad(@stock_code_t, 8, '0'));
  [AF_转换服务公用_参数同步幂等校验][table_category = @table_category, position_str = @position_str, transaction_no = @transaction_no][row_count = @row_count]
  
  [通用参数同步结束][@unpack_sett][usps_vote_code][idx_usps_vote_code][CNST_MC_UFT_PUBSYNC]

### 通用参数同步结束

- **参数**: `[解包器名][对象名][全局唯一索引名][主题名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[事务处理开始\]
      
      //3.存在，本次操作不调整物理库，只记录同步流水；不存在，本次操作按param_oper_type调整物理库，并记录流水
      \[获取时间\]\[@curr_time\]
      if (@row_count == 0)
      {
         \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$index_expression\]\[transaction_no = @transaction_no_t\]
        \[记录不为空\]\[[对象名]\]
        {
          if (@transaction_no > @transaction_no_t)
          {
            if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
            {
              \[修改记录\]\[[对象名]\]\[$update_expression\]
              $modIndexExpression

              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$update_sql"\]\[\]\[\]
            }
            else if (CNST_PARAMOPER_DELETE == @param_oper_type)
            {
              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$delete_sql"\]\[\]\[\]

              \[删除记录\]\[[对象名]\]
            }
          }

        }
        else
        {
          if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
          {
            \[插入记录\]\[[对象名]\]\[$insert_expression\]

            \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$insert_sql"\]\[\]\[\]
          }
        }
      }
     //根据已维护的核心在线状态信息插入upbs_syncinfo,
    [AF_转换服务公用_记录参数账户同步流水][][token_sync_flag = @token_sync_flag]
    \[事务处理结束\]
    
    if ((@row_count == 0) && (@token_sync_flag == CNST_ALLSYNCFLAG_YES))
    {
      \[手工打包头\]\[$pack_header\]
      \[手工打包体\]\[$pack_body\]
      \[手工打包结束\]
      
      
      @business_data = lpAnswer->GetPackBuf();
      vi_business_data = lpAnswer->GetPackLen();
      //4.将同步信息发表至MC
      \[消息发布\]\[topic_name = [主题名]\]\[$mc_pubMsg\]
    }  
  \[手工解包结束\]
```

**说明**: 需与[通用参数同步开始]配合使用。

宏标记说明:
1、I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式

    示例如下：
    I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式
    示例如下：
      [clob字段解包][@unpack_sett][@busi_data][pi_busi_data] 
      [通用参数同步开始][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC]
      //拼接唯一定位串,范例
      hs_snprintf(@position_str, sizeof(@position_str), "%010d%010d", @segment_kind, @seg_order);
      [AF_转换服务公用_参数同步幂等校验][table_category = @table_category, position_str = @position_str, transaction_no = @transaction_no][row_count = @row_count]
      
      <I>[通用参数同步结束][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC][aim_value = @aim_value] 

2、P:支持消息中心发布时，自动传入字段partition_no
    使用场景：消息中心发布时，主题需要填写过滤字段partition_no

### 高可用通用参数同步结束

- **参数**: `[解包器名][对象名][全局唯一索引名][主题名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[事务处理开始\]
      
      //3.存在，本次操作不调整物理库，只记录同步流水；不存在，本次操作按param_oper_type调整物理库，并记录流水
      \[获取时间\]\[@curr_time\]
      if (@row_count == 0)
      {
         \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$index_expression\]\[transaction_no = @transaction_no_t\]
        \[记录不为空\]\[[对象名]\]
        {
          if (@transaction_no > @transaction_no_t)
          {
            if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
            {
              \[修改记录\]\[[对象名]\]\[$update_expression\]
              $modIndexExpression

              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$update_sql"\]\[\]\[\]
            }
            else if (CNST_PARAMOPER_DELETE == @param_oper_type)
            {
              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$delete_sql"\]\[\]\[\]

              \[删除记录\]\[[对象名]\]
            }
          }

        }
        else
        {
          if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
          {
            \[插入记录\]\[[对象名]\]\[$insert_expression\]

            \<UO\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$db_index"\]\[\]\[\]
          }
        }
      }
     //根据已维护的核心在线状态信息插入upbs_syncinfo,
    [AF_转换服务公用_记录参数账户同步流水][][token_sync_flag = @token_sync_flag]
    \[事务处理结束\]
    
    if ((@row_count == 0 || @transaction_no == @transaction_no_t) && (@token_sync_flag == CNST_ALLSYNCFLAG_YES))
    {
      \[手工打包头\]\[$pack_header\]
      \[手工打包体\]\[$pack_body\]
      \[手工打包结束\]
      
      
      @business_data = lpAnswer->GetPackBuf();
      vi_business_data = lpAnswer->GetPackLen();
      //4.将同步信息发表至MC
      \[同步消息发布\]\[topic_name = [主题名]\]\[$mc_pubMsg\]
    }  
  \[手工解包结束\]
```

**说明**: 需与[通用参数同步开始]配合使用。

宏标记说明:
1、I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式

    示例如下：
    I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式
    示例如下：
      [clob字段解包][@unpack_sett][@busi_data][pi_busi_data] 
      [通用参数同步开始][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC]
      //拼接唯一定位串,范例
      hs_snprintf(@position_str, sizeof(@position_str), "%010d%010d", @segment_kind, @seg_order);
      [AF_转换服务公用_参数同步幂等校验][table_category = @table_category, position_str = @position_str, transaction_no = @transaction_no][row_count = @row_count]
      
      <I>[通用参数同步结束][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC][aim_value = @aim_value] 

2、P:支持消息中心发布时，自动传入字段partition_no
    使用场景：消息中心发布时，主题需要填写过滤字段partition_no

### 高可用并发参数同步结束

- **参数**: `[解包器名][对象名][全局唯一索引名][主题名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[事务处理开始\]
      
      //3.存在，本次操作不调整物理库，只记录同步流水；不存在，本次操作按param_oper_type调整物理库，并记录流水
      \[获取时间\]\[@curr_time\]
      if (@row_count == 0)
      {
         \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$index_expression\]\[transaction_no = @transaction_no_t\]
        \[记录不为空\]\[[对象名]\]
        {
          if (@transaction_no > @transaction_no_t)
          {
            if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
            {
              \[修改记录\]\[[对象名]\]\[$update_expression\]
              $modIndexExpression

              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$update_sql"\]\[\]\[\]
            }
            else if (CNST_PARAMOPER_DELETE == @param_oper_type)
            {
              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$delete_sql"\]\[\]\[\]

              \[删除记录\]\[[对象名]\]
            }
          }

        }
        else
        {
          if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
          {
            \<C\>\[插入记录\]\[[对象名]\]\[$insert_expression\]
            
            \[索引冲突\]
            {
              \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$index_expression\]\[transaction_no = @transaction_no_t\]

              if (@transaction_no > @transaction_no_t)
              {
                \[修改记录\]\[[对象名]\]\[$update_expression\]
                $modIndexExpression

                \<UO\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$db_index"\]\[\]\[\]
              }
            }
            else
            {
              \<UO\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$db_index"\]\[\]\[\]
            }
          }
        }
      }
     //根据已维护的核心在线状态信息插入upbs_syncinfo,
    [AF_转换服务公用_记录参数账户同步流水][][token_sync_flag = @token_sync_flag]
    \[事务处理结束\]
    
    if ((@row_count == 0 || @transaction_no == @transaction_no_t) && (@token_sync_flag == CNST_ALLSYNCFLAG_YES))
    {
      \[手工打包头\]\[$pack_header\]
      \[手工打包体\]\[$pack_body\]
      \[手工打包结束\]
      
      
      @business_data = lpAnswer->GetPackBuf();
      vi_business_data = lpAnswer->GetPackLen();
      //4.将同步信息发表至MC
      \[同步消息发布\]\[topic_name = [主题名]\]\[$mc_pubMsg\]
    }  
  \[手工解包结束\]
```

**说明**: 需与[通用参数同步开始]配合使用，支持并发时的表记录插入操作。

宏标记说明:
1、I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式

    示例如下：
    I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式
    示例如下：
      [clob字段解包][@unpack_sett][@busi_data][pi_busi_data] 
      [通用参数同步开始][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC]
      //拼接唯一定位串,范例
      hs_snprintf(@position_str, sizeof(@position_str), "%010d%010d", @segment_kind, @seg_order);
      [AF_转换服务公用_参数同步幂等校验][table_category = @table_category, position_str = @position_str, transaction_no = @transaction_no][row_count = @row_count]
      
      <I>[通用参数同步结束][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC][aim_value = @aim_value] 

2、P:支持消息中心发布时，自动传入字段partition_no
    使用场景：消息中心发布时，主题需要填写过滤字段partition_no

### 通用参数同步开始

- **参数**: `[解包器名][对象名][全局唯一索引名][主题名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
/*1、根据表对象号和操作标志解包
    2、进行数据转换：UF2.0至UFT3.0(表结构)
    3、数据持久化：主动落库，持久化相应参数账户记录
    4、在线核心获取：UFTMDB中获取核心在线信息
    5、参数账户同步流水记录：根据核心在线信息分别插入upbs_syncinfo
    6、消息发布：调用MC接口进行消息发布（根据不同参数账户类型指定主题）
    */
    
  //目前系统内置宏手工解包开始，入参不允许空，暂时随便取一个字段，后续升级后该字段可删除
  \[手工解包开始\]\[partition_no= @partition_no\]\[[解包器名]\]
  
    //2.根据操作类型，按需解包
    if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
    {
      //field_expression,当前表所有字段（除了transaction_no）
      \[手工解包体\]\[$field_expression\]\[[解包器名]\]
    }
    else if (CNST_PARAMOPER_DELETE == @param_oper_type)
    {
      //索引赋值字符串index_expression
      \[手工解包体\]\[$index_expression\]\[[解包器名]\]
    }
```

**说明**: 仅用于uconvert核心的参数同步，用于实现转换服务的通用的参数同步逻辑
适用场景：通用的参数同步场景： UF20柜台参数同步请求的pack包中，包含了内存表同步需要的所有字段。
不适用场景：
带关联关系场景、表同步时有时序逻辑、字段需要字典转换、特殊的处理逻辑等。
[通用参数同步开始]需要与[通用参数同步结束]配合使用，
中间需自行根据业务场景，拼接参数同步流水定位串，用于实现幂等控制。

使用范例：
  [clob字段解包][@unpack_sett][@busi_data][pi_busi_data] 
  
  //填写表名和索引及发布的主题
  [通用参数同步开始][@unpack_sett][usps_vote_code][idx_usps_vote_code][CNST_MC_UFT_PUBSYNC]
 
  //拼接唯一定位串,范例
  hs_strncpy(@meeting_seq_t, @meeting_seq, sizeof(@meeting_seq_t) - 1);
  hs_strncpy(@exchange_type_t, @exchange_type, sizeof(@exchange_type_t) - 1);
  hs_strncpy(@stock_code_t, @stock_code, sizeof(@stock_code_t) - 1); 
  hs_snprintf(@position_str, sizeof(@position_str), "%s%s%s", lpad(@meeting_seq_t, 8, '0'), lpad(@exchange_type_t, 4, '0'), lpad(@stock_code_t, 8, '0'));
  [AF_转换服务公用_参数同步幂等校验][table_category = @table_category, position_str = @position_str, transaction_no = @transaction_no][row_count = @row_count]
  
  [通用参数同步结束][@unpack_sett][usps_vote_code][idx_usps_vote_code][CNST_MC_UFT_PUBSYNC]

### 通用参数同步结束

- **参数**: `[解包器名][对象名][全局唯一索引名][主题名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[事务处理开始\]
      
      //3.存在，本次操作不调整物理库，只记录同步流水；不存在，本次操作按param_oper_type调整物理库，并记录流水
      \[获取时间\]\[@curr_time\]
      if (@row_count == 0)
      {
         \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$index_expression\]\[transaction_no = @transaction_no_t\]
        \[记录不为空\]\[[对象名]\]
        {
          if (@transaction_no > @transaction_no_t)
          {
            if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
            {
              \[修改记录\]\[[对象名]\]\[$update_expression\]
              $modIndexExpression

              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$update_sql"\]\[\]\[\]
            }
            else if (CNST_PARAMOPER_DELETE == @param_oper_type)
            {
              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$delete_sql"\]\[\]\[\]

              \[删除记录\]\[[对象名]\]
            }
          }

        }
        else
        {
          if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
          {
            \[插入记录\]\[[对象名]\]\[$insert_expression\]

            \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$insert_sql"\]\[\]\[\]
          }
        }
      }
     //根据已维护的核心在线状态信息插入upbs_syncinfo,
    [AF_转换服务公用_记录参数账户同步流水][][token_sync_flag = @token_sync_flag]
    \[事务处理结束\]
    
    if ((@row_count == 0) && (@token_sync_flag == CNST_ALLSYNCFLAG_YES))
    {
      \[手工打包头\]\[$pack_header\]
      \[手工打包体\]\[$pack_body\]
      \[手工打包结束\]
      
      
      @business_data = lpAnswer->GetPackBuf();
      vi_business_data = lpAnswer->GetPackLen();
      //4.将同步信息发表至MC
      \[消息发布\]\[topic_name = [主题名]\]\[$mc_pubMsg\]
    }  
  \[手工解包结束\]
```

**说明**: 需与[通用参数同步开始]配合使用。

宏标记说明:
1、I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式

    示例如下：
    I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式
    示例如下：
      [clob字段解包][@unpack_sett][@busi_data][pi_busi_data] 
      [通用参数同步开始][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC]
      //拼接唯一定位串,范例
      hs_snprintf(@position_str, sizeof(@position_str), "%010d%010d", @segment_kind, @seg_order);
      [AF_转换服务公用_参数同步幂等校验][table_category = @table_category, position_str = @position_str, transaction_no = @transaction_no][row_count = @row_count]
      
      <I>[通用参数同步结束][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC][aim_value = @aim_value] 

2、P:支持消息中心发布时，自动传入字段partition_no
    使用场景：消息中心发布时，主题需要填写过滤字段partition_no

### 高可用通用参数同步结束

- **参数**: `[解包器名][对象名][全局唯一索引名][主题名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[事务处理开始\]
      
      //3.存在，本次操作不调整物理库，只记录同步流水；不存在，本次操作按param_oper_type调整物理库，并记录流水
      \[获取时间\]\[@curr_time\]
      if (@row_count == 0)
      {
         \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$index_expression\]\[transaction_no = @transaction_no_t\]
        \[记录不为空\]\[[对象名]\]
        {
          if (@transaction_no > @transaction_no_t)
          {
            if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
            {
              \[修改记录\]\[[对象名]\]\[$update_expression\]
              $modIndexExpression

              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$update_sql"\]\[\]\[\]
            }
            else if (CNST_PARAMOPER_DELETE == @param_oper_type)
            {
              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$delete_sql"\]\[\]\[\]

              \[删除记录\]\[[对象名]\]
            }
          }

        }
        else
        {
          if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
          {
            \[插入记录\]\[[对象名]\]\[$insert_expression\]

            \<UO\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$db_index"\]\[\]\[\]
          }
        }
      }
     //根据已维护的核心在线状态信息插入upbs_syncinfo,
    [AF_转换服务公用_记录参数账户同步流水][][token_sync_flag = @token_sync_flag]
    \[事务处理结束\]
    
    if ((@row_count == 0 || @transaction_no == @transaction_no_t) && (@token_sync_flag == CNST_ALLSYNCFLAG_YES))
    {
      \[手工打包头\]\[$pack_header\]
      \[手工打包体\]\[$pack_body\]
      \[手工打包结束\]
      
      
      @business_data = lpAnswer->GetPackBuf();
      vi_business_data = lpAnswer->GetPackLen();
      //4.将同步信息发表至MC
      \[同步消息发布\]\[topic_name = [主题名]\]\[$mc_pubMsg\]
    }  
  \[手工解包结束\]
```

**说明**: 需与[通用参数同步开始]配合使用。

宏标记说明:
1、I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式

    示例如下：
    I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式
    示例如下：
      [clob字段解包][@unpack_sett][@busi_data][pi_busi_data] 
      [通用参数同步开始][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC]
      //拼接唯一定位串,范例
      hs_snprintf(@position_str, sizeof(@position_str), "%010d%010d", @segment_kind, @seg_order);
      [AF_转换服务公用_参数同步幂等校验][table_category = @table_category, position_str = @position_str, transaction_no = @transaction_no][row_count = @row_count]
      
      <I>[通用参数同步结束][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC][aim_value = @aim_value] 

2、P:支持消息中心发布时，自动传入字段partition_no
    使用场景：消息中心发布时，主题需要填写过滤字段partition_no

### 高可用并发参数同步结束

- **参数**: `[解包器名][对象名][全局唯一索引名][主题名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[事务处理开始\]
      
      //3.存在，本次操作不调整物理库，只记录同步流水；不存在，本次操作按param_oper_type调整物理库，并记录流水
      \[获取时间\]\[@curr_time\]
      if (@row_count == 0)
      {
         \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$index_expression\]\[transaction_no = @transaction_no_t\]
        \[记录不为空\]\[[对象名]\]
        {
          if (@transaction_no > @transaction_no_t)
          {
            if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
            {
              \[修改记录\]\[[对象名]\]\[$update_expression\]
              $modIndexExpression

              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$update_sql"\]\[\]\[\]
            }
            else if (CNST_PARAMOPER_DELETE == @param_oper_type)
            {
              \<O\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$delete_sql"\]\[\]\[\]

              \[删除记录\]\[[对象名]\]
            }
          }

        }
        else
        {
          if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
          {
            \<C\>\[插入记录\]\[[对象名]\]\[$insert_expression\]
            
            \[索引冲突\]
            {
              \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$index_expression\]\[transaction_no = @transaction_no_t\]

              if (@transaction_no > @transaction_no_t)
              {
                \[修改记录\]\[[对象名]\]\[$update_expression\]
                $modIndexExpression

                \<UO\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$db_index"\]\[\]\[\]
              }
            }
            else
            {
              \<UO\>\[数据回库\]\[[对象名]\]\["usessvr"\]\["$db_index"\]\[\]\[\]
            }
          }
        }
      }
     //根据已维护的核心在线状态信息插入upbs_syncinfo,
    [AF_转换服务公用_记录参数账户同步流水][][token_sync_flag = @token_sync_flag]
    \[事务处理结束\]
    
    if ((@row_count == 0 || @transaction_no == @transaction_no_t) && (@token_sync_flag == CNST_ALLSYNCFLAG_YES))
    {
      \[手工打包头\]\[$pack_header\]
      \[手工打包体\]\[$pack_body\]
      \[手工打包结束\]
      
      
      @business_data = lpAnswer->GetPackBuf();
      vi_business_data = lpAnswer->GetPackLen();
      //4.将同步信息发表至MC
      \[同步消息发布\]\[topic_name = [主题名]\]\[$mc_pubMsg\]
    }  
  \[手工解包结束\]
```

**说明**: 需与[通用参数同步开始]配合使用，支持并发时的表记录插入操作。

宏标记说明:
1、I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式

    示例如下：
    I:支持索引字段修改
    注意：使用I标记时，必须传入索引字段修改表达式
    示例如下：
      [clob字段解包][@unpack_sett][@busi_data][pi_busi_data] 
      [通用参数同步开始][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC]
      //拼接唯一定位串,范例
      hs_snprintf(@position_str, sizeof(@position_str), "%010d%010d", @segment_kind, @seg_order);
      [AF_转换服务公用_参数同步幂等校验][table_category = @table_category, position_str = @position_str, transaction_no = @transaction_no][row_count = @row_count]
      
      <I>[通用参数同步结束][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][CNST_MC_UFT_PUBSYNC][aim_value = @aim_value] 

2、P:支持消息中心发布时，自动传入字段partition_no
    使用场景：消息中心发布时，主题需要填写过滤字段partition_no

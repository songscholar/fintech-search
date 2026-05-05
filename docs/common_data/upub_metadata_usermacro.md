# upub - 用户自定义宏

用户自定义宏定义，包含宏名称、参数、内容和使用说明。

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2025-12-16 16:01:35 | 3.0.2.28 | 蒋浩 | 获取机房类型增加DB模式 |
| 2025-11-20 15:22:56 | 3.0.2.27 | 蒋浩 | 新增获取微秒时间戳 |
| 2025-10-16 15:03:34 | 3.0.2.26 | 韦子晗 | 期权报盘重发回报判断逻辑修改 |
| 2025-08-25 19:25:43 | 3.0.5.1056 | 张剑 | 新增宏 获取机房类型 |
| 2025-07-31 15:45:41 | 3.0.6.1 | dongh | 增加自定义宏[SvrEnd出参打包] |
| 2025-09-20 13:32:30 | 3.0.2.25 | 高志强 | 新增用户自定义宏查询缓存表数据单行,封装查询缓存表的select...into语法 |
| 2025-09-18 09:45:53 | 3.0.2.24 | 张明月 | 新增[期权报盘重发回报判断] |
| 2025-08-25 15:11:32 | 3.0.2.23 | 马明智 | [PRO*C语句]宏定义中在[通用SQL执行]后增加 @sql_error_no = lpIUFTContext->nErrorNo; |
| 2025-08-09 14:58:22 | 3.0.2.22 | 余世泽 | 新增[底座参数同步字段转换] |
| 2025-07-29 16:09:06 | 3.0.2.21 | 沈勋 | 增加[重置所有序列号] |
| 2025-05-19 19:37:15 | 3.0.2.20 | 张明月 | 增加获取时间(毫秒)、获取重发标志、获取TraceID |
| 2025-10-10 13:32:33 | 3.0.6.1002 | 汪杰 | 修改重置参数错误信息宏 |
| 2025-05-14 19:41:50 | 3.0.6.1001 | 杨森峰 | 新增宏，支持回库到多中心 |
| 2025-05-20 19:41:31 | 3.0.2.22 | 赵良梓 | 新增自定义宏[SQL结果集返回] |
| 2025-03-27 16:25:00 | 3.0.2.2001 | 董瑞辉 | 新增标准可选查询条件整数 |
| 2025-04-29 13:56:30 | 3.0.2.21 | taocong45644 | 自定义错误信息报错返回宏支持M标签 |
| 2025-04-22 19:42:48 | 3.0.2.20 | taocong45644 | 新增自定义错误信息报错返回宏 |
| 2025-04-18 14:33:31 | 3.0.2.20 | taocong45644 | 新增宏[内存申请]、[内存释放] |
| 2025-04-22 15:51:18 | 3.0.2.20 | 程猛 | 调整序列号相关宏 |
| 2025-04-11 14:39:40 | 3.0.2.19 | 乐闽庭 | [EXCEPTION] 和 [PRO*C语句] 宏重置上下文错误号时，将 iRaiseError 置为 0 |

> 共 66 条修改记录，仅显示最近20条


## 宏列表（共 292 个）

### 正常返回

- **适用类型**: 函数,服务,原子服务,原子函数

```
iRaiseError = 0;
lpIUFTContext->nErrorNo = OK_SUCCESS;
goto svr_end;
```

**说明**: 跳转到函数结束

### 继续执行

- **适用类型**: 函数,原子函数

```
iRaiseError = 0;	//避免后续业务报错时，错误路径被截断
lpIUFTContext->nErrorNo = OK_SUCCESS;
```

### 处理成功

- **适用类型**: 函数,原子函数

```
if (lpIUFTContext->nErrorNo == OK_SUCCESS)
```

### 处理失败

- **适用类型**: 函数,原子函数

```
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
```

### 记录为空

- **参数**: `[对象]`
- **适用类型**: 函数,原子函数

```
//[对象]为空
if (@[对象] == InvalidRecordHandle)
```

**说明**: 判断指针为空

### 记录不为空

- **参数**: `[对象]`
- **适用类型**: 函数,原子函数,原子服务

```
//[对象]不为空
if (@[对象] != InvalidRecordHandle)
```

**说明**: 判断指针不为空

### 记录赋值

- **参数**: `[目标记录][源记录]`
- **适用类型**: 函数

```
@[目标记录] = @[源记录];
lp[目标记录] = lp[源记录];
```

**说明**: 建议使用系统宏【对象赋值】

### 索引冲突

- **适用类型**: 函数,原子函数

```
if(lpIUFTContext->nErrorNo == UFTCORE_ERR_DUP_KEY)
```

### 记录条数

- **参数**: `[标准字段][对象]`
- **适用类型**: 函数,原子函数

```
@[标准字段] = lpIUFTContext->GetTableFactory()->GetTable(Category[对象])->GetRecordCount();
```

**说明**: 获取记录条数

### 获取记录为空

- **参数**: `[对象]`
- **适用类型**: 函数

```
if(lpIUFTContext->nErrorNo == UFTCORE_ERR_INVALID_CATEGORY)
{
   lpIUFTContext->GetErrorFormat()->Format20(lpIUFTContext->nErrorNo, "[对象]");
   lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
   goto svr_end;
}
else if (@[对象] == InvalidRecordHandle)
```

**说明**: 获取记录为空，且错误号是无效的数据种类，返回报错。并且判断记录指针为空。
示例代码：
<M>[获取记录][branch(idx_branch)][branch_no=@branch_no]
[获取记录为空][branch]
{
    // [老版报错返回][ERR_751001][@branch_no]
    或者
    //[继续执行]
    //[插入记录][branch][]
}

### 业务报错返回

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,原子服务,原子函数

```
//业务报错返回
memset(@usermacro_errorinfo,0,sizeof(@usermacro_errorinfo));
\<Z\>\[获取记录\]\[upbs_error_msg(idx_upbs_error_msg)\]\[error_no = [错误号]\]\[error_info=@usermacro_errorinfo\]
\[记录为空\]\[upbs_error_msg\]
{
\[报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
else
{
\[自定义错误信息返回\]\[[错误号]\]\[@usermacro_errorinfo\]\[{[参数列表]}\]
}
```

### 获取序列号

- **参数**: `[序号][序列号]`
- **适用类型**: 函数,原子函数

```
[序列号] = lpITransCtrl->GetNextSequence([序号], &lpIUFTContext->nErrorNo);
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   \[报错返回\]\[ERR_SEQUENCEERR\]\[[序号]\]
}
```

**说明**: 示例代码：
[获取序列号][CNST_USESSERIALTYPE_USES_FUND_DETAIL_JOUR][@serial_no]

### 清理内存数据库

- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->ResetMDB();
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   goto svr_end;
}
```

### 建立全量关联关系

- **适用类型**: 函数,服务,原子函数,原子服务

```
lpIUFTContext->BuildRelation();
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   goto svr_end;
}
```

### 字符串为空

- **参数**: `[字段]`
- **适用类型**: 函数,服务

```
(isnull([字段]) == 0 || [字段][0] == ' ')
```

**说明**: if ([字符串为空][@fund_account])
{
  xxxx;
}

### 如果字符串为空

- **参数**: `[字段]`
- **适用类型**: 函数,服务

```
if (isnull([字段]) == 0 || [字段][0] == ' ')
```

### 如果字符串不为空

- **参数**: `[字段]`
- **适用类型**: 函数,服务

```
if (isnull([字段]) != 0 && [字段][0] != ' ')
```

### 字符串不为空

- **参数**: `[字段]`
- **适用类型**: 函数,服务

```
(isnull([字段]) != 0 && [字段][0] != ' ')
```

### 获取日期

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子函数

```
@[标准字段] = lpIUFTContext->nDate;
```

**说明**: 日期格式 YYYYMMDD

### 获取时间

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子函数

```
@[标准字段] = lpIUFTContext->nTime;
```

**说明**: 时间格式HHMMSS

### 获取微秒时间

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] = (HsMicroTime)lpIUFTContext->GetMicroSecs();
```

### clob字段解包

- **参数**: `[解包器][clob字段][clob长度]`
- **适用类型**: 函数

```
if (![解包器])
{
   iRaiseError = 1;
   lpIUFTContext->nErrorNo = ERR_EXEC_BUSIPACK_ISNULL;
   lpIUFTContext->GetErrorFormat()->Format(ERR_EXEC_BUSIPACK_ISNULL, wrap("解包错误（无法获取解包器）"));
   lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
   goto svr_end;
}
lpIUFTContext->nErrorNo = [解包器]->Open([clob字段],[clob长度]);
if ( lpIUFTContext->nErrorNo != 0)
{  
   iRaiseError = 1;
   lpIUFTContext->nErrorNo = ERR_EXEC_BUSIPACK_ISNULL;
   lpIUFTContext->GetErrorFormat()->Format(ERR_EXEC_BUSIPACK_ISNULL, wrap("解包错误（无法获取解包器）"));
   lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
   goto svr_end;
}
else if (  [解包器]->GetColCount() < 0)
{   
   iRaiseError = 1;
   lpIUFTContext->nErrorNo = ERR_PACKRESULE_ISNULL;
   lpIUFTContext->GetErrorFormat()->Format(ERR_PACKRESULE_ISNULL, wrap("解包错误（行列不匹配）"));
   lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
   goto svr_end;
}
```

### 获取部署类型

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetDeployType();
```

### 获取冲销流水号

- **参数**: `[标准字段]`
- **适用类型**: 函数,原子函数

```
{
    HsSerialNo v_usermacro_temp_serial_no;
    \[获取序列号\]\[CNST_SERIALTYPE_CANCEL_SERIAL_NO\]\[v_usermacro_temp_serial_no\]
    hs_snprintf(@[标准字段], sizeof(@[标准字段]), "%010d%s", v_usermacro_temp_serial_no, lpIUFTContext->GetLdpHost()->GetVariables()->GetString(VarID::ShortAppName));
}
```

**说明**: 获取冲销流水号
拼接方式：流水号（10位）+集群名
如证券竞价交易核心（分片号62）获取冲销流水号，流水号为1：
结果为：0000000001usesbid62

使用参考：
[获取冲销流水号][@cancel_serial_no]

### 获取轮询配置

- **参数**: `[轮询提前时间][轮询延迟时间][轮询间隔时间][轮询一次发送最大笔数]`
- **适用类型**: 函数,服务

```
@[轮询提前时间] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetPollingAheadTime();
@[轮询延迟时间] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetPollingDelayTime();
@[轮询间隔时间] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetPollingTimerInterval();
@[轮询一次发送最大笔数] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetPollingSendMaxCount();
```

### 业务远程调用

- **参数**: `[标准参数列表][{[发送数据列表]}][输出列表] `
- **适用类型**: 原子函数

```
IF2UnPacker* lpUnPacker;
\[同步调用\]\[[标准参数列表]\]\[{[发送数据列表]}\]\[out_packer = lpUnPacker\]  
\[手工解包体\]\[@error_no,@error_info,@error_pathinfo]\[lpUnPacker\] 
if (@error_no != OK_SUCCESS)
{
    char szErrorPath[256] = "";
    iRaiseError = 1;
    lpIUFTContext->nErrorNo = @error_no;
    lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap(@error_info));
    snprintf(szErrorPath, sizeof(szErrorPath), "%s->%s",__FUNCTION__,@error_pathinfo);
    lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, szErrorPath);
    if (lpPackerV3)
    {
        lpPackerV3->FreeMem(lpPackerV3->GetPackBuf());
        lpPackerV3->Release();
    }
    lpIUFTContext->EndProcess(szErrorPath, iRaiseError);
    return lpIUFTContext->nErrorNo;
}
\[手工解包体\]\[[输出列表]]\[lpUnPacker\]
```

**说明**: 基于系统内置宏[同步调用]封装，支持[同步调用]失败时，自动解析错误信息报错
用法示例：
[业务远程调用][ function_id = XXXXXX, timeout = 10000][@fund_account][entrust_no = @entrust_no]

### 获取分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] =lpIUFTContext->GetBizProc()->GetShardNo();
```

### 表记录不存在

- **适用类型**: 函数

```
if (lpIUFTContext->nErrorNo == LDP_MDB_RECORD_NOTEXISTS)
```

**说明**: 根据上下文中的错误号判断表记录是否存在，一般用于综合模块进行判断，竞价模块可使用用户自定义宏记录为空/记录不为空进行判断

### 节点定位插件分片状态更新

- **参数**: `[分片规则名变量][打包变量]`
- **适用类型**: 函数

```
if (lpIUFTContext->GetLocateImpl() == NULL)
{
  iRaiseError = 1;
  lpIUFTContext->nErrorNo = LDP_PLUGIN_GET_FAILED;
  lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap("ldp_locate"));
  goto svr_end;
}
else
{
  lpIUFTContext->nErrorNo = lpIUFTContext->GetLocateImpl()->ReloadByRuleName([分片规则名变量], (char*)[打包变量]->GetPackBuf());
  
  if (unlikely(lpIUFTContext->nErrorNo != OK_SUCCESS))
  {
    iRaiseError = 1;
    lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, [分片规则名变量]);
    goto svr_end;
  }
}
```

**说明**: 用于调用Locate插件的ReloadByRuleName接口上传json字符串

### 节点定位Rules打包头

- **参数**: `[打包变量][内存分片号字段][内存分片状态字段]`
- **适用类型**: 函数

```
//节点定位Rules手工打包头
[打包变量]->BeginPack();
[打包变量]->AddField("[内存分片号字段]", 'S');
[打包变量]->AddField("[内存分片状态字段]", 'I');
```

**说明**: Rules打包头，Rules打包体，Rules打包结束用来打包Rules标签下的结果集内容

### 节点定位Rules打包体

- **参数**: `[打包变量][内存分片号变量][内存分片状态变量]`
- **适用类型**: 函数

```
//节点定位Rules手工打包体
[打包变量]->AddStr([内存分片号变量]);
[打包变量]->AddInt([内存分片状态变量]);
```

**说明**: Rules打包头，Rules打包体，Rules打包结束用来打包Rules标签下的结果集内容

### 节点定位Rules打包结束

- **参数**: `[打包变量][Rules]`
- **适用类型**: 函数

```
//节点定位Rules手工打包结束
[打包变量]->EndPack();
[Rules] = [打包变量]->GetPackBuf();
vi_Rules = [打包变量]->GetPackLen();
```

**说明**: Rules打包头，Rules打包体，Rules打包结束用来打包Rules标签下的结果集内容

### 节点定位更新打包头

- **参数**: `[打包变量][规则名称][内存分片号字段][内存分片状态字段]`
- **适用类型**: 函数

```
//节点定位更新打包头
[打包变量]->BeginPack();
[打包变量]->AddField([规则名称], 'S');
[打包变量]->AddField([内存分片号字段], 'S');
[打包变量]->AddField([内存分片状态字段], 'S');
[打包变量]->AddField("Rules", 'R', vi_Rules);
```

### 节点定位更新打包体

- **参数**: `[打包变量][规则名称][内存分片号变量][内存分片状态变量]`
- **适用类型**: 函数

```
//节点定位更新打包体
[打包变量]->AddStr([规则名称]);
[打包变量]->AddStr([内存分片号变量]);
[打包变量]->AddStr([内存分片状态变量]);
[打包变量]->AddRawEx(v_Rules, vi_Rules);
```

### 节点定位更新打包结束

- **参数**: `[打包变量]`
- **适用类型**: 函数

```
//节点定位更新打包结束
[打包变量]->EndPack();
```

### 获取额度管理分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子函数,因子服务

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetUqmsPartitionNo();
```

### 获取请求分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =lpIUFTContext->GetLdpMsgReader()->GetHead()->NodeNo;
```

### 业务复核标志

- **适用类型**: 函数,服务

```
if ( @audit_action == CNST_AUDIT_BUSI_CHK )
{
  goto svr_end;
}
```

### 获取功能号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] =lpIUFTContext->GetLdpMsgReader()->GetHead()->FunctionID;
```

**说明**: 说明：该宏以后作废，待两融修改完删除该宏

### 获取仲裁状态

- **参数**: `[仲裁状态]`
- **适用类型**: 函数,服务

```
@[仲裁状态] = (int32_t)lpIUFTContext->GetBizProc()->GetArbStatus();
```

### 获取RPC超时时间

- **参数**: `[标准字段] `
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetRpcTimeout();
```

**说明**: 单位:毫秒

### 获取回库RPC超时时间

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetTogwRpcTimeout();
```

**说明**: 单位:毫秒

### 获取转换服务分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetUconvertPartitionNo();
```

### 设置序列号

- **参数**: `[序号][序列号]`
- **适用类型**: 函数,原子函数

```
lpITransCtrl->ResetSequence([序号], [序列号] );
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   \[报错返回\]\[ERR_SEQUENCEERR\]\[[序号]\]
}
```

**说明**: 示例代码：
[设置序列号][CNST_USESSERIALTYPE_USES_FUND_DETAIL_JOUR][@serial_no]

### 获取应用集群名

- **参数**: `[集群名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
hs_strncpy(@[集群名] , lpIUFTContext->GetLdpHost()->GetVariables()->GetString(VarID::ShortAppName),sizeof(@[集群名] )-1);
```

### 业务报错自定义返回

- **参数**: `[错误号1][错误号2][错误信息]`
- **适用类型**: 函数,原子函数

```
//业务报错返回
iRaiseError = 1;
lpIUFTContext->nErrorNo = [错误号1];
lpIUFTContext->GetErrorFormat()->Format([错误号2], wrap([错误信息]));
lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
goto svr_end;
```

### 直接返回

- **适用类型**: 函数,原子函数

```
goto svr_end;
```

### 获取调用功能号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] = lpIUFTContext->GetLdpMsgReader()->GetOptionalHead()->GetInt(TagOrgFunctionId);
//请求进来调用SetRequest会清空可选头，所以这里可以根据可选头中的功能号是否为0 来区分本次请求是否经过RPC调用
if (@[标准字段] == 0)
{
   @[标准字段] = lpIUFTContext->GetLdpMsgReader()->GetHead()->FunctionID;
}
```

### 轮询错误处理

- **适用类型**: 服务

```
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
    {
        //内部引用标准字段变量初始化
        HsChar500 v_error_message = "";
        if (iRaiseError == 0)
        {
            (void)snprintf(szErrorPath, sizeof(szErrorPath), "%s->%s", __FUNCTION__, lpIUFTContext->GetErrorPath());
        }
        else
        {
            (void)snprintf(szErrorPath, sizeof(szErrorPath), "%s", __FUNCTION__);
        }
        snprintf(v_error_message, sizeof(v_error_message), "轮询处理错误:function(%s),error_no(%d),error_info(%s),error_pathinfo(%s)",
        __FUNCTION__, lpIUFTContext->nErrorNo, lpIUFTContext->GetErrorFormat()->GetUTF8Message(), szErrorPath);
        
        //记录分布式日志
        LDPBIZLOG_ERROR(lpIUFTContext->GetLdpContext(),lpIUFTContext->nErrorNo,NULL,wrap(v_error_message));
    }
```

**说明**: 该宏用于轮询处理结束前判断是否有返回错误，若有就记录相应错误日志
注：需要轮询处理函数前加<M>标志

### 获取带分片序列号

- **参数**: `[序号][序列号]`
- **适用类型**: 函数,原子函数

```
[序列号] = lpITransCtrl->GetNextSequence([序号], &lpIUFTContext->nErrorNo);
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   \[报错返回\]\[ERR_SEQUENCEERR\]\[[序号]\]
}
[序列号] += (lpIUFTContext->GetBizProc()->GetShardNo() * 10000000);
```

**说明**: 获取序列号后，拼接分片号
示例代码：[获取带分片序列号][CNST_USES_SEQUENCE_ENTRUST_REPORT_NO][@serial_no]

### 重置周边获取记录行数

- **参数**: `[请求行数]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([请求行数] <= 0)
{
  [请求行数] = CNST_EXT_DEFAULT_ROWCOUNT;
}
else if ([请求行数] > CNST_EXT_MAX_ROWCOUNT)
{ 
  [请求行数] = CNST_EXT_MAX_ROWCOUNT;
}
```

### 核心通用参数同步

- **参数**: `[解包器名][对象名][全局唯一索引名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[手工解包开始\]\[$paramStr\]\[[解包器名]\] 
  \[事务处理开始\]
  \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$indexFieldsAssignStr\]\[transaction_no = @transaction_no_t\]
  \[记录不为空\]\[[对象名]\]
  {
        if (@transaction_no > @transaction_no_t)
        {
          if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
          {
            \[修改记录\]\[[对象名]\]\[$structureFieldsWithOutIndexFieldAssignStr\]

            $modIndexExpression
          }
          else if (CNST_PARAMOPER_DELETE == @param_oper_type)
          {
            \[删除记录\]\[[对象名]\]
          }
        }
  }
  else
  {
    if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
    {
      \[插入记录\]\[[对象名]\]\[$structureFieldsAssignStr\]
    }
  }
  \[事务处理结束\]
\[手工解包结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[核心通用参数同步][@unpack_sett][upbs_extern_error][idx_upbs_extern_error] 

宏标记说明:
I:支持索引字段修改
注意：使用I标记时，必须传入索引字段修改表达式
示例如下：
<I>[核心通用参数同步][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][aim_value = @aim_value]

### 获取表名称

- **参数**: `[表号][表名称]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
{
    ITableFactory * const lpTempITableFactory = lpIUFTContext->GetTableFactory();
    ITable * const lpTempTable = lpTempITableFactory->GetTable(@[表号]);

    if (unlikely(nullptr == lpTempTable))
    {
      iRaiseError = 1;
      lpIUFTContext->nErrorNo = LDP_MDB_QRY_FAIL;
      lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap("table_category:"), wrap(@[表号]));
      lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
      goto svr_end;
    }

    hs_strncpy(@[表名称], lpTempTable->GetRecordName(), sizeof(@[表名称]) - 1);
}
```

**说明**: 根据UFT对象表号获取UFT对象的表名称(英文名称)
范例：
[获取表名称][@table_category][@table_name]

注意:表号必须是变量

### 客户数据同步

- **参数**: `[解包器名][对象名][全局唯一索引名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[手工解包开始\]\[$paramStr\]\[[解包器名]\] 
  \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$indexFieldsAssignStr\]
  \[记录为空\]\[[对象名]\]
  {
    \<C\>\[插入记录\]\[[对象名]\]\[$structureFieldsAssignStr\]
  }
\[手工解包结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[客户数据同步][@unpack_sett][upbs_extern_error][idx_upbs_extern_error] 

宏标记说明:
I:支持索引字段修改
注意：
1.使用I标记时，必须传入索引字段修改表达式
示例如下：
<I>[核心通用参数同步][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][aim_value = @aim_value]

### 客户数据关联同步

- **参数**: `[解包器名][对象名][非全局唯一索引名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[手工解包开始\]\[$paramStr\]\[[解包器名]\] 
    \<Z\>\[获取记录\]\[ucrt_fund_account.[对象名]([非全局唯一索引名])\]\[$indexFieldsAssignStr\]
  \[记录为空\]\[[对象名]\]
  {
    \<C\>\[插入记录\]\[[对象名]\]\[$structureFieldsAssignStr\]
  }
\[手工解包结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[客户数据关联同步][@busi_data][ucrt_unity_video][idx_ucrt_unity_video] 

宏标记说明:
I:支持索引字段修改
注意：
1.使用I标记时，必须传入索引字段修改表达式
示例如下：
<I>[客户数据关联同步][@busi_data][ucrt_unity_video][idx_ucrt_unity_video][value = @value]

### 获取结构体

- **参数**: `[组件名][输出列表]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
//业务自定义宏:获取结构体
$codestr
```

**说明**: 用户获取结构体组件的字段信息
注:仅适用于勾选了“是否结构体”的标准组件

使用范例：
注：
[comp_crtexchinfo]手工勾选了“是否结构体”
[获取结构体][comp_crtexchinfo][real_balance = @real_balance,
 entrust_type = @entrust_type]

### 修改结构体

- **参数**: `[组件名][{参数列表}]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
//业务自定义宏:修改结构体
$codestr
```

**说明**: 用户修改结构体组件的字段信息
注:仅适用于勾选了“是否结构体”的标准组件

使用范例：
注：comp_crtexchinfo手工勾选了“是否结构体”
  [修改结构体][comp_crtexchinfo][init_date = @usps_exch_arg.init_date]

### EXCEPTION

- **适用类型**: 函数,服务,原子服务,原子函数

```
@sql_error_no = lpIUFTContext->nErrorNo;
lpIUFTContext->nErrorNo = OK_SUCCESS;
iRaiseError = 0;
if (unlikely(OK_SUCCESS == @sql_error_no)) 
{
}
```

### WHEN_TOO_MANY_ROWS

- **适用类型**: 函数,服务,原子服务,原子函数

```
else if (LDP_ARES_SQL_QRY_FAIL ==  @sql_error_no && @sql_row_count > 1)
```

### WHEN_NO_DATA_FOUND

- **适用类型**: 函数,服务,原子服务,原子函数

```
else if (LDP_ARES_SQL_QRY_FAIL == @sql_error_no && @sql_row_count == 0)
```

### WHEN_OTHERS

- **适用类型**: 函数,服务,原子服务,原子函数

```
else
```

### WHEN_DUP_VAL_ON_INDEX

- **适用类型**: 函数,服务,原子服务,原子函数

```
else if( UFTCORE_ERR_DUP_KEY == @sql_error_no)
```

### 动态SQL执行

- **参数**: `[SQL语句][{标准参数列表}]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[通用SQL执行\]\[[SQL语句]\]\[{[标准参数列表]}\]
```

### 标准可选查询条件字符串

- **参数**: `[变量][字段][运算符][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
   hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and [表别名][字段] [运算符]'", [变量],"' ");
}
```

### 标准可选查询条件字符串instr

- **参数**: `[变量][字段][运算符][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
    hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and instr(',' || '",[变量],"' || ',', ',' ||  to_char([表别名][字段]) || ',') [运算符] 0 ");
}
```

### 标准可选查询条件字符

- **参数**: `[变量][字段][运算符][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_c([变量]) != 0)
{
   hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%c%s",    @sSql,"    and [表别名][字段] [运算符]'", [变量],"' ");
}
```

### 通用SELECT

- **参数**: `[SQL语句][结果集变量或者打包变量]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[通用SQL执行\]\[[SQL语句]\]\[count = @sql_row_count, packer = @packer\]
\[结果集转换\]\[@packer\]\[[结果集变量或者打包变量]\]
```

### 重置结束日期函数

- **参数**: `[开始日期][结束日期][时间间隔]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([开始日期] > 0 && [时间间隔] > 0)
{
  int li_date = hs_dateadd([开始日期],[时间间隔]);
  
  if (li_date < [结束日期])
    [结束日期] = li_date;
}
```

### 获取带分片序列号8位

- **参数**: `[序号][序列号]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
[序列号] = lpITransCtrl->GetNextSequence([序号], &lpIUFTContext->nErrorNo);
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   \[报错返回\]\[ERR_SEQUENCEERR\]\[[序号]\]
}
[序列号] += (lpIUFTContext->GetBizProc()->GetShardNo() * 1000000);
```

### PRO*C结果集为空

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (LDP_ARES_SQL_QRY_FAIL == @sql_error_no && @sql_row_count  == 0)
```

### PRO*C语句

- **参数**: `[SQL语句]{[表名]}{[变量]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\<M\>\[通用SQL执行\]\[[SQL语句]\]\[count = @sql_row_count\]
@sql_error_no = lpIUFTContext->nErrorNo;
if (LDP_ARES_SQL_QRY_FAIL == lpIUFTContext->nErrorNo && @sql_row_count == 0)
{
   @sql_error_no = lpIUFTContext->nErrorNo;
   lpIUFTContext->nErrorNo = OK_SUCCESS ;
  iRaiseError = 0;
}
if (@sql_error_no == OK_SUCCESS ||  (LDP_ARES_SQL_QRY_FAIL == @sql_error_no && @sql_row_count == 0))
```

### PRO*C结果集不为空

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (@sql_error_no == OK_SUCCESS)
```

### 通用SQL捕获

- **参数**: `[sql参数]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
hs_strncpy(@sSql, [sql参数], sizeof(@sSql)-1); 
  hs_strncpy(@execute_sql, " ", sizeof(@sSql)-1); 
  for (int v_i = 1; @i <= (int)lpSqlArgsIn->GetCount(); @i ++ )
  {
    int pos = instr(@sSql, '?');
    
    if (lpSqlArgsIn->Get(@i)->eType == 1)
    {
      if (pos > 0)
      {
        hs_strncpy(@sql_str, "", sizeof(@sql_str) - 1);
        hs_strncpy(@sql_str1, "", sizeof(@sql_str1) - 1);
        substr(@sSql, 1, pos - 1, @sql_str);
        substr(@sSql, pos + 1, 0 , @sql_str1);
        snprintf(@sSql, sizeof(@sSql), "%s%ld%s", @sql_str, lpSqlArgsIn->Get(@i)->iVal ,@sql_str1);
      }
      DEBUG_LOG_TRACE("@%d=%ld--\n", @i, lpSqlArgsIn->Get(@i)->iVal);	  
    }
    else if (lpSqlArgsIn->Get(@i)->eType == 2)
    {
      if (pos > 0)
      {
        hs_strncpy(@sql_str, "", sizeof(@sql_str) - 1);
        hs_strncpy(@sql_str1, "", sizeof(@sql_str1) - 1);
        substr(@sSql, 1, pos - 1, @sql_str);
        substr(@sSql, pos + 1, 0 , @sql_str1);
        snprintf(@sSql, sizeof(@sSql), "%s%f%s", @sql_str, lpSqlArgsIn->Get(@i)->dVal ,@sql_str1);
      }
	  DEBUG_LOG_TRACE("@%d=%f--\n", @i, lpSqlArgsIn->Get(@i)->dVal);
    }
    else if (lpSqlArgsIn->Get(@i)->eType == 3)
    {
      if (pos > 0)
      {
        hs_strncpy(@sql_str, "", sizeof(@sql_str) - 1);
        hs_strncpy(@sql_str1, "", sizeof(@sql_str1) - 1);
        substr(@sSql, 1, pos - 1, @sql_str);
        substr(@sSql, pos + 1, 0 , @sql_str1);
        snprintf(@sSql, sizeof(@sSql), "%s'%s'%s", @sql_str, lpSqlArgsIn->Get(@i)->lpszVal ,@sql_str1);
      }
	  DEBUG_LOG_TRACE("@%d='%s'--\n", @i, lpSqlArgsIn->Get(@i)->lpszVal);
    }
  }
  DEBUG_LOG_TRACE("sql = %s\n", @sSql);
```

**说明**: 跟[通用SQL执行]配套使用，用于捕获sql语句，仅可用于调试。
<M>[通用SQL执行][select stock_account
                     into @stock_account_inparam
                     from uses_stock_holder
                     where fund_account = @fund_account_inparam
                     and exchange_type = @exchange_type_inparam
                     and main_flag = '1'][count = @count]
需要传入原始sql，配套使用，未报错时无法捕获sql
[通用SQL捕获][lpSqlResultSet1943923_1->GetLastErrorSql()]

### 函数结果集字段获取

- **参数**: `{[标准字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[手工解包体\]\[{[标准字段]}\]\[lpResultSet\]
```

### 如果结果集不为空

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (!lpResultSet->IsEmpty())
```

### PRO*C结果集返回

- **适用类型**: 函数,服务,原子服务,原子函数

```
\[结果集转换\]\[lpResultSet\]\[lpOutPacker\]
\[直接返回\]
```

### 如果结果集为空

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (lpResultSet->IsEmpty())
```

### LS结果集返回

- **适用类型**: 服务

```
\[结果集转换\]\[lpResultSet\]\[lpAnswer\]
```

### LF结果集返回

- **适用类型**: 函数,服务,原子服务,原子函数

```
\[结果集转换\]\[lpResultSet\]\[lpOutPacker\]
```

### 取系统节点号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[获取分片号\]\[标准字段\]
```

### PRO*C结果集语句

- **参数**: `[SQL语句]{[表名]}{[变量]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\<M\>\[通用SQL执行\]\[[SQL语句]\]\[count = @sql_row_count\]
```

### 结果集返回

- **适用类型**: 函数,服务,原子服务,原子函数

```
\[结果集转换\]\[lpResultSet\]\[lpOutPacker\]
```

### PRO*C函数多记录校验

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (@sql_row_count > 1)
```

### 错误描述重置

- **参数**: `[重置错误信息]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->GetErrorFormat()->Format(ERR_SECUUFT_USER_DEFINE_ERROR, [重置错误信息]);
```

### 重置错误信息

- **参数**: `[错误号][错误信息]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->nErrorNo = [错误号];
lpIUFTContext->GetErrorFormat()->SetMultiByteFormattedMessage(0, IMsgFormat::$encode_type, @[错误信息]);
```

### 自定义参数报错返回

- **参数**: `[错误号][参数信息]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
memset(@usermacro_errorinfo,0,sizeof(@usermacro_errorinfo));
\<Z\>\[获取记录\]\[upbs_error_msg(idx_upbs_error_msg)\]\[error_no = [错误号]\]\[error_info=@usermacro_errorinfo\]
\[记录为空\]\[upbs_error_msg\]
{
  iRaiseError = 1;
  lpIUFTContext->nErrorNo = [错误号];
  lpIUFTContext->GetErrorFormat()->Format([错误号], [参数信息]);
  lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
  goto svr_end;
}
else
{
  iRaiseError = 1;
  lpIUFTContext->nErrorNo = [错误号];
  lpIUFTContext->GetErrorFormat()->MultiByteFormat([错误号], IMsgFormat::LdpEncodingType::Utf8, @usermacro_errorinfo, [参数信息]);
  lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
  goto svr_end;  
}
```

### 重置参数错误信息

- **参数**: `[错误号][错误信息1][错误信息2]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->nErrorNo = [错误号];
lpIUFTContext->GetErrorFormat()->SetMultiByteFormattedMessage(0, IMsgFormat::$encode_type, @[错误信息1],@[错误信息2]);
```

### 获取额度管理流水号切换增量

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetUqmsMaxSerialInCrement();
```

**说明**: 用于获取json业务配置中的额度管理流水号切换增量
备机房额度管理核心切换至主机时，
额度管理流水号增加值 = 额度管理流水号切换增量 * serial_assign_counts

### 标准可选查询条件字符串存在instr

- **参数**: `[变量][字段][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (instr([变量], ',') > 0)
  {
    hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and instr(',' || '",[变量],"' || ',', ',' ||  [表别名][字段] || ',') > 0 ");
  }
  else
  {  
    hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and [表别名][字段] = '",[变量],"' ");
  }
}
```

### 标准可选查询条件实数exact

- **参数**: `[变量][字段][运算符][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (fabs([变量]) > 0.000001)
{
  hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%f%s",    @sSql,"    and [表别名][字段] [运算符]", [变量]," ");
}
```

### 客户数据删除

- **参数**: `[对象名][全局唯一索引名][条件列表]`
- **适用类型**: 函数

```
\<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[[条件列表]\]
  \[记录不为空\]\[[对象名]\]
  {
    \[删除记录\]\[[对象名]\]
  }
```

**说明**: 实现通用的删除逻辑
示例：
[客户数据删除][ucrt_fund_account][idx_ucrt_fund_account][fund_account = @fund_account]

### 客户批量数据删除

- **参数**: `[上级][对象名][索引][条件列表][批量大小]`
- **适用类型**: 函数

```
\<E\>\[遍历记录开始\]\[[上级].[对象名]([索引])\]\[[条件列表]\]\[[批量大小]\]
{
   \[删除记录\]\[[对象名]\]
}
\[遍历记录结束\]
```

### 客户二层批量数据删除

- **参数**: `[上上级][上级][对象名][上级索引][索引][上级条件列表][条件列表][批量大小]`
- **适用类型**: 函数

```
\<E\>\[遍历记录开始\]\[[上上级].[上级]([上级索引])\]\[[上级条件列表]\]\[[批量大小]\]
   \<E\>\[遍历记录开始\]\[[上级].[对象名]([索引])\]\[[条件列表]\]\[[批量大小]\]
  {
     \[删除记录\]\[[对象名]\]
  }
  \[遍历记录结束\]
\[遍历记录结束\]
```

### 客户三层批量数据删除

- **参数**: `[上上上级][上上级][上级][对象名][上上级索引][上级索引][索引][上上级条件列表][上级条件列表][条件列表][批量大小]`
- **适用类型**: 函数

```
\<E\>\[遍历记录开始\]\[[上上上级].[上上级]([上上级索引])\]\[[上上级条件列表]\]\[[批量大小]\]  
   \<E\>\[遍历记录开始\]\[[上上级].[上级]([上级索引])\]\[[上级条件列表]\]\[[批量大小]\]
     \<E\>\[遍历记录开始\]\[[上级].[对象名]([索引])\]\[[条件列表]\]\[[批量大小]\]
    {
       \[删除记录\]\[[对象名]\]
    }
    \[遍历记录结束\]
  \[遍历记录结束\] 
\[遍历记录结束\]
```

### 等待客户回切事务处理

- **参数**: `[等待超时秒数][事务号]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
/// 等待客户回切事务处理
if (lpIUFTContext == NULL || lpIUFTContext->GetBizProc() == NULL)
{
  iRaiseError = 1;
  lpIUFTContext->nErrorNo = UFTCORE_ERR_NULL_OBJECT;
  lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap("等待客户回切事务处理异常"));
  goto svr_end;
}
else
{
  /// 同步等待调用本接口之前的工作线程内的所有任务执行完成
  if (lpIUFTContext->GetBizProc()->WaitForAllPreTasks([等待超时秒数]) == true)
  {
    /// 获取下一个事务号
    @[事务号] = lpIUFTContext->GetBizProc()->GetNextTranscationNo();
  }
  else
  {
    iRaiseError = 1;
    lpIUFTContext->nErrorNo = LDP_ARES_SYNC_CALL_FAIL;
    lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap("等待客户回切事务处理失败"));
    goto svr_end;
  }
}
```

**说明**: 等待客户回切事务处理，封装以下函数。
bool WaitForAllPreTasks(uint_32_t uTimeout = -1);
@uTimeout：等待超时秒数，-1表示一直等待；
@return：之前所有任务都执行完成返回true，超时或调用失败返回false；
@details：同步等待调用本接口之前的工作线程内的所有任务执行完成，线程安全。

获取客户回切事务号，封装的函数说明如下：
uint64_t GetNextTranscationNo();
@return：下一个事务号；
@details：接口调用时期：IBizData::Init 以后，IBizData::Exit 以前；多线程调用安全。

### 检查PRO*C结果集为空

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (@sql_row_count == 0)
```

### 报盘重发回报判断

- **适用类型**: 服务

```
<svr_end>:
	// 如果有新增的需要报盘重发处理的错误号，都在这里补充判断
	if ((lpIUFTContext->nErrorNo == 270030) || (lpIUFTContext->nErrorNo == 151533) || (lpIUFTContext->nErrorNo == 151422))
	{
		@is_resend = 1;
	}
```

**说明**: 每个回报LS的最后都调用这个自定义宏，判断是否重置is_resend

### PRO*C语句块更新记录不存在

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,原子服务,原子函数

```
if (@sql_row_count == 0)
{
  \[报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
```

### 更新记录不存在 

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (@sql_row_count == 0)
{
  \[报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
```

### 存在序列号V2记录

- **参数**: `[序号类型in][序号索引字段in][结果out]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (((ITransCtrl * const)lpIUFTContext->GetTransCtrl())->IsExistSeq([序号类型in], 
                                 SeqKeyBuilder {
                                     [序号索引字段in]
                                 },
                                 &lpIUFTContext->nErrorNo))
        {
          [结果out] = 1;
        }
        else
        {
          if (likely(lpIUFTContext->nErrorNo == OK_SUCCESS))
          {
            [结果out] = 0;
          }
          else
          {
             //序列号获取错误
             iRaiseError = 1;
             lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap([序号类型in]));
             lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
             goto svr_end;
          }
        }
```

**说明**: 用于判断是否存在序列号V2记录。
示例：
[存在序列号V2记录][@sequence_type_dest][CNST_UCBPSERIALTYPE_ENTRUST][@count]

if (@count == 1)

{

}

### PRO*C函数无记录事务内报错返回

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (@sql_row_count == 0)
{
  \[报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
```

### 重置序列号V2简式

- **参数**: `[序号类型in][序号索引字段in][序号参数列表out]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
{
        SequenceSetParam seqSetParam([序号参数列表out]);
        lpIUFTContext->nErrorNo = ((ITransCtrl * const)lpIUFTContext->GetTransCtrl())->ResetSeqEx([序号类型in], 
                                 SeqKeyBuilder {
                                     [序号索引字段in]
                                 },
                                 &seqSetParam
                               );
        if (unlikely(lpIUFTContext->nErrorNo != OK_SUCCESS))
        {
            //序列号重置错误
            iRaiseError = 1;
            lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap([序号类型in]));
            lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
            goto svr_end;
        }
      }
```

**说明**: 支持序列号相关参数的重置，建议日初数据加载阶段使用，盘中使用时需要同时调用MDB的相关函数清理低层序列空间的缓存。
示例：

[重置序列号V2简式][@sequence_type_dest][@serial_counter_no][@sequence_min, @sequence_max, @sequence_next, @sequence_syncinterval, @sequence_increment]

### 重置获取记录行数

- **参数**: `[请求行数]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([请求行数] <= 0)
{
  [请求行数] = CNST_EXT_DEFAULT_ROWCOUNT;
}
else if ([请求行数] > CNST_EXT_MAX_ROWCOUNT)
{ 
  [请求行数] = CNST_EXT_MAX_ROWCOUNT;
}
```

### 序号类型映射V2

- **参数**: `[序号类型in][映射关系in][映射类型out]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
[映射类型out] = lpIUFTContext->GetSeqTypeByOpera([序号类型in],[映射关系in], &lpIUFTContext->nErrorNo);
        if ([映射类型out] < 0)
        {
            //序号类型in映射获取错误
            iRaiseError = 1;
            lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap([序号类型in]), wrap([映射关系in]));
            lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
            goto svr_end;
        }
```

**说明**: 根据序列类型获取映射类型；映射关系：0:进程->远程 1:线程->进程 2:线程->远程。
宏使用了上下文，不可在因子模块使用。
示例：
[序号类型映射V2][CNST_UPUB_SEQUENCE_V2SET_LPC_BRANCHNO][CNST_UPUB_SEQUENCE_V2MAP_THREAD_PROCESS][@sequence_type_dest]

### 记录不存在

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (LDP_ARES_SQL_QRY_FAIL == @sql_error_no && @sql_row_count == 0)
{
  \[业务报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
```

### 序号类型映射V2不报错返回

- **参数**: `[序号类型in][映射关系in][映射类型out]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
[映射类型out] = lpIUFTContext->GetSeqTypeByOpera([序号类型in],[映射关系in], &lpIUFTContext->nErrorNo);
```

**说明**: 根据序列类型获取映射类型；映射关系：0:进程->远程 1:线程->进程 2:线程->远程。
注意该宏不能保证出参[映射类型_out]是合法的值，需要调用方另外再判断返回值是否合法；需要使用[继续执行宏]将上下文的lpIUFTContext->nErrorNo重置成零。
示例：
[序号类型映射V2][CNST_UPUB_SEQUENCE_V2SET_LPC_BRANCHNO][CNST_UPUB_SEQUENCE_V2MAP_THREAD_PROCESS][@sequence_type_dest]

### 通用SELECT报错不返回

- **参数**: `[SQL语句][结果集变量或者打包变量]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
<M>\[通用SQL执行\]\[[SQL语句]\]\[count = @sql_row_count, packer = @packer\]
\[结果集转换\]\[@packer\]\[[结果集变量或者打包变量]\]
```

### 获取序列号区间V2

- **参数**: `[序号索引字段in][序号类型in][最小序列号out][最大序列号out]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->nErrorNo = ((ITransCtrl * const)lpIUFTContext->GetTransCtrl())->GetNextSeqEx([序号类型in],
                                                             SeqKeyBuilder {
                                                                [序号索引字段in]
                                                             },
                                                             &[最小序列号out],
                                                             &[最大序列号out]
                                                            );
```

**说明**: 没有报错返回，需要调用方解决处理失败的情况。
示例：
[获取序列号区间V2][@serial_counter_no, @branch_no][@sequence_type_dest][@sequence_min][@sequence_max]

### 标准结果集返回

- **适用类型**: 函数,服务,原子服务,原子函数

### 获取柜面RPC超时时间

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetExternalRpcTimeout();
```

**说明**: 单位:毫秒

### 通用可选查询条件字符串

- **参数**: `[变量][字段][运算符][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
   hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and [字段] [运算符]'", [变量],"' ");
}
```

### 自定义错误信息报错返回

- **参数**: `[错误号][错误信息]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
iRaiseError = 1;
lpIUFTContext->nErrorNo = [错误号];
lpIUFTContext->GetErrorFormat()->SetMultiByteFormattedMessage([错误号], IMsgFormat::$encode_type, @[错误信息]);
lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
$is_svr_end
```

**说明**: 自定义错误信息报错返回宏支持自定义错误信息的修改,支持带M标签，适合场景如下：
1.@error_info:[][][] | [][][] | XXX
2.@error_info:[][][]
3.@error_info:XXXX
示例：
[自定义错误信息返回][@error_no][@error_info]
<M>[自定义错误信息返回][@error_no][@error_info]

### 内存申请

- **参数**: `[clob包][V4打包器]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[clob包] = lpIUFTContext->NewMem(@[V4打包器]->GetPackLen());
if (@[clob包] == nullptr)
{
   \[报错返回\]\[UFTCORE_ERR_MALLOC\]
}
else
{
  memcpy(@[clob包], @[V4打包器]->GetPackBuf(), @[V4打包器]->GetPackLen());
}
```

**说明**: [内存申请] 和 [内存释放] 需要配对使用，并且需要增加<svr_end>标签
注意：只支持packerV4打包器
示例:
[内存申请][@entrust_clob][@packerV4]
....
<svr_end>:
[内存释放][@entrust_clob]

### 事务开始

- **适用类型**: 函数,服务,原子服务,原子函数

```
\[事务处理开始\]
```

### 内存释放

- **参数**: `[clob地址]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
{
  if (@[clob地址] == 0)
  {
    void *clob_addr_temp = (void*)(uintptr_t)@[clob地址];
    if (clob_addr_temp != nullptr)
    {
       lpIUFTContext->RecycleMem(clob_addr_temp);
    }
  }
}
```

**说明**: [内存申请] 和 [内存释放] 需要配对使用，并且需要增加<svr_end>标签
示例:
[内存申请][@entrust_clob][@packerV4]
....
<svr_end>:
[内存释放][@entrust_clob]

### 通用可选查询条件整数

- **参数**: `[变量][字段][运算符][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([变量] != 0)
{
   hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%d%s",    [目标字符串],"    and [字段] [运算符]", [变量]," ");
}
```

### 日终回库多中心数据打包

- **参数**: `[表名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[结果集记录池开始\]\[[表名]\]\[*, position_int = @position_int, request_num = @request_num\]
    {
      \<Z\>\[获取记录\]\[uses_fund_account(idx_uses_fund_account)\]\[fund_account = @fund_account\]\[sysnode_id = @sysnode_id_t\]
      \[记录为空\]\[uses_fund_account\]
      {
          continue;
      }
      if (@sysnode_id_t != @sysnode_id)
      {
        continue;
      }
    }
    \[结果集记录池结束\]
```

**说明**: 【参数说明】
·对象：具体获取的记录类型
·输出列表：field_name=@variable,...
【备注】
·只有在回库的UF2.0系统是多交易中心场景下，回库数据需要校验sysnode_id时才使用。
·需要指定position_int和request_num字段的值，否则无法遍历到数据。其中，position_int指定起始记录号，request_num指定遍历的记录条数
·遍历记录的同时打包输出列表字段
·输出列表为*，表示对象全字段。

### 通用可选查询条件字符存在instr

- **参数**: `[变量][字段][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (length([变量]) == 1)
  {
     hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and [字段] = '",[变量],"' ");
  }
  else
  {
     hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and instr('",[变量],"' , [字段]) > 0 ");
  }
}
```

### SQL结果集返回

- **适用类型**: 函数,服务,原子服务,原子函数

```
\[结果集转换\]\[lpResultSet\]\[lpAnswer\]
```

**说明**: [PROC结果集语句]查询到的结果直接作为应答出去。要求：[PROC结果集语句]返回的结果必须与当前LS接口要求的应答字段一致,且无需对返回的结果进行业务处理。

范例1:
[PRO*C结果集语句][select a.name,a.age from demo a]
[处理成功]
{
  [SQL结果集返回]
}

范例2:
[通用SQL执行][select a.name,a.age from demo a]
[处理成功]
{
  [SQL结果集返回]
}

### 通用可选查询条件实数

- **参数**: `[变量][字段][运算符][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (fabs([变量]) > 0.000001)
{
   hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%f%s",    [目标字符串],"    and [字段] [运算符]", [变量]," ");
}
```

### 上海交易类别判断

- **适用类型**: 函数,服务,原子服务,原子函数

```
if ((hs_strcmp(@exchange_type,CNST_EXCHANGETYPE_SHA) == 0) || (hs_strcmp(@exchange_type,CNST_EXCHANGETYPE_SHB) == 0)|| (hs_strcmp(@exchange_type,CNST_EXCHANGETYPE_GDSY) == 0))
```

### 中断跳转

- **适用类型**: 函数,服务,原子服务,原子函数

```
goto svr_end;
```

### 通用可选查询条件字符

- **参数**: `[变量][字段][运算符][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([变量] != CNST_CHAR_DEFAULTVALUE)
{
   hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%c%s",    [目标字符串],"    and [字段] [运算符]'", [变量],"' ");
}
```

### 通用可选查询条件整数存在instr

- **参数**: `[变量][字段][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (instr([变量], ',') > 0)
  {
     if ([变量][0] == ',')
        [变量][0] = ' ';
     
     if ([变量][length([变量])-1] == ',')
        [变量][length([变量])-1] = ' ';
     
     if (hs_isnull_s([变量]) > 0)
        hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and [字段]  in (", [变量], ") ");
  }
  else
  {
     hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s",      [目标字符串],"    and [字段] = ",[变量]);
  }
}
```

### 通用可选查询条件字符串存在instr

- **参数**: `[变量][字段][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (instr([变量], ',') > 0)
  {
    hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and instr(',' || '",[变量],"' || ',', ',' ||  [字段] || ',') > 0 ");
  }
  else
  {  
    hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and [字段] = '",[变量],"' ");
  }
}
```

### 信用业务函数判断

- **参数**: `[资产属性]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([资产属性] == CNST_ASSETPROP_CREDIT)
```

**说明**: 判断是否为信用业务

### 标准可选查询条件整数

- **参数**: `[变量][字段][运算符][表别名]`
- **适用类型**: 函数,服务,原子函数,原子服务

```
if ([变量] != 0)
{
   hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%d%s",    @sSql,"    and [表别名][字段] [运算符]", [变量]," ");
}
```

### 事务内自定义异常返回

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,服务,原子函数,原子服务

```
\[WHEN_OTHERS\]
{
  \[事务回滚\]
  \[业务报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
```

### 同步等待

- **参数**: `[参数]`
- **适用类型**: 函数,服务,原子服务,原子函数

### 并发数据回库

- **参数**: `[表名][sql语句]`
- **适用类型**: 函数,服务,原子函数,原子服务,,因子服务,因子函数

### 初始化同步等待

- **适用类型**: 函数,服务,原子服务,原子函数

```
int32_t nLdpErrorNo = 0;
    uint32_t nCount = 0;    
    ILdpMsgReader **lppLdpMsgRpcReader = NULL;
    IF2UnPacker * lppUnPacker[256] =
    {
        NULL
    };
```

### 文件并发数据加载

- **参数**: `[对象名]{[数据库连接名]}{[加载sql语句]}`
- **适用类型**: 函数,服务,原子函数,原子服务,,因子服务,因子函数

### 获取时间(毫秒)

- **参数**: `[标准字段]`
- **适用类型**: 函数

```
@[标准字段] = (HsMicroTime)lpIUFTContext->GetMicroSecs() / 1000;
```

### 获取重发标志

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子函数,原子服务,,因子服务,因子函数

```
ILdpMsgReader * lpMsgReaderEx = lpIUFTContext->GetLdpMsgReader();
auto lpOptHeadEx = lpMsgReaderEx->GetOptionalHead();
//int TagMsgRetransmmited = 8;
if( lpOptHeadEx)
{
	@[标准字段] = lpOptHeadEx->Contains(42);
}
else
{
	@[标准字段] = 0;
}
```

**说明**: 获取委托包头中是否重发标志

### 获取TraceID

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子函数,原子服务,,因子服务,因子函数

```
ILdpMsgReader * lpMsgReader = lpIUFTContext->GetLdpMsgReader();
auto lpOptHead = lpMsgReader->GetOptionalHead();
//int TagMessageTraceID = 8;
const char * lpTraceID = lpOptHead->GetStr(8);
if( !lpTraceID )
{
	//traceid无效
	memset(@[标准字段],0,64);
}
else
{
	hs_strcpy(@[标准字段],lpTraceID);
}
```

### 重置所有序列号

- **适用类型**: 函数,服务,原子服务,原子函数

```
//重置序列号
$strSerialReset
```

**说明**: 遍历序列号资源，重置所有序列号，设置成初始值

### 标准可选查询条件字符存在instr

- **参数**: `[变量][字段][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (length([变量]) == 1)
  {
     hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and [表别名][字段] = '",[变量],"' ");
  }
  else
  {
     hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and instr('",[变量],"' , [表别名][字段]) > 0 ");
  }
}
```

### 标准可选查询条件整数存在instr

- **参数**: `[变量][字段][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (instr([变量], ',') > 0)
  {
     if ([变量][0] == ',')
        [变量][0] = ' ';
     
     if ([变量][length([变量])-1] == ',')
        [变量][length([变量])-1] = ' ';
     
     if (hs_isnull_s([变量]) > 0)
        hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and [表别名][字段]  in (", [变量], ") ");
  }
  else
  {
     hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s",      @sSql,"    and [表别名][字段] = ",[变量]);
  }
}
```

### 底座参数同步字段转换

- **参数**: `[内存变量名][UF3变量名][UF2变量名][解包器名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ('0' == @char_config_87028)
{
  \[手工解包体\]\[[UF2变量名] = @[内存变量名] \]\[@[解包器名]\]
}
else
{
  \[手工解包体\]\[[UF3变量名] = @[内存变量名] \]\[@[解包器名]\]
}
```

**说明**: 内存对接UF2和UF3参数同步时，当两个系统使用标准字段不一致场景，使用该自定义宏。标准字段一致时，无需对使用该自定义宏

范例：
[底座参数同步字段转换][day_buy_balance_uplimit][day_buy_balance_uplimit][total_quota][unpack_sett]

### 获取清算RPC超时时间

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetSettRpcTimeout();
```

### 获取LDP上场RPC超时时间

- **参数**: `[标准字段] `
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetLdpRpcTimeout();
```

**说明**: 单位:毫秒

### 期权报盘重发回报判断

- **适用类型**: 服务

```
<svr_end>:
	// 如果有新增的需要报盘重发处理的错误号，都在这里补充判断
	if ((lpIUFTContext->nErrorNo == 270030) || (lpIUFTContext->nErrorNo == 302) || (lpIUFTContext->nErrorNo == 10043))
	{
		@is_resend = 1;
	}
	else if (lpIUFTContext->nErrorNo == 21901)
	{
		@is_resend = 1;
	}
         else if (lpIUFTContext->nErrorNo == 21902)
	{
		@is_resend = 1;
	}
```

**说明**: 每个回报LS的最后都调用这个自定义宏，判断是否重置is_resend

### SvrEnd出参打包

- **适用类型**: 服务

```
<svr_end>:
if(lpIUFTContext->nErrorNo == ERR_SYSWARNING)
  {
  	  	$code
	nErrorNoTemp = 0; 
}
```

### 获取机房类型

- **参数**: `[机房类型]`
- **适用类型**: 函数,服务

```
hs_strncpy(@[机房类型], lpIUFTContext->GetZoneType(), sizeof(@[机房类型]) - 1);
```

### 查询缓存表数据单行

- **参数**: `[SQL语句][标准参数列表][输出参数列表]`
- **适用类型**: 服务,函数,原子服务,原子函数

```
\<$macroFlag\>\[查询缓存表\]\[[SQL语句]\]\[[标准参数列表]\]

//20250920 gaozq27559 mod 参考通用SQL执行时对行数的判断,解析输出参数.
if (unlikely(lpIUFTContext->nErrorNo != OK_SUCCESS))
{
  //避免重置失败场景的错误信息.
}
else
{
  //等同于获取v_sql_row_count之后的那次查询结果的行数判断.
  if (@sql_row_count != 1)
  {
    //select..into语句查询失败，查询条数wrap("select_count", v_sql_row_count)
    iRaiseError = 1;
    lpIUFTContext->nErrorNo = LDP_ARES_SQL_QRY_FAIL;
    lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap("select_count", v_sql_row_count));
    lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
    
    //复刻使用通用SQL执行时M标签生成代码的逻辑.
    if ('M' != '$macroFlag')
    {
      goto svr_end;
    }
  }
  else
  {
    \[SQL结果集解包开始\]\[[输出参数列表]\]
    break;
    \[SQL结果集解包结束\]
  }
}
```

**说明**: M:生成函数代码，函数报错时不生成返回语句。
标准参数列表必须包含“count = @sql_row_count”，否则判断行数时会有问题。

### 获取微秒时间戳

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] = std::chrono::duration_cast<std::chrono::microseconds>(
                  std::chrono::system_clock::now().time_since_epoch()
              ).count();
```

**说明**: 获取当前服务器时间和1970年初始时间戳之间的微秒级别的差值

### 正常返回

- **适用类型**: 函数,服务,原子服务,原子函数

```
iRaiseError = 0;
lpIUFTContext->nErrorNo = OK_SUCCESS;
goto svr_end;
```

**说明**: 跳转到函数结束

### 继续执行

- **适用类型**: 函数,原子函数

```
iRaiseError = 0;	//避免后续业务报错时，错误路径被截断
lpIUFTContext->nErrorNo = OK_SUCCESS;
```

### 处理成功

- **适用类型**: 函数,原子函数

```
if (lpIUFTContext->nErrorNo == OK_SUCCESS)
```

### 处理失败

- **适用类型**: 函数,原子函数

```
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
```

### 记录为空

- **参数**: `[对象]`
- **适用类型**: 函数,原子函数

```
//[对象]为空
if (@[对象] == InvalidRecordHandle)
```

**说明**: 判断指针为空

### 记录不为空

- **参数**: `[对象]`
- **适用类型**: 函数,原子函数,原子服务

```
//[对象]不为空
if (@[对象] != InvalidRecordHandle)
```

**说明**: 判断指针不为空

### 记录赋值

- **参数**: `[目标记录][源记录]`
- **适用类型**: 函数

```
@[目标记录] = @[源记录];
lp[目标记录] = lp[源记录];
```

**说明**: 建议使用系统宏【对象赋值】

### 索引冲突

- **适用类型**: 函数,原子函数

```
if(lpIUFTContext->nErrorNo == UFTCORE_ERR_DUP_KEY)
```

### 记录条数

- **参数**: `[标准字段][对象]`
- **适用类型**: 函数,原子函数

```
@[标准字段] = lpIUFTContext->GetTableFactory()->GetTable(Category[对象])->GetRecordCount();
```

**说明**: 获取记录条数

### 获取记录为空

- **参数**: `[对象]`
- **适用类型**: 函数

```
if(lpIUFTContext->nErrorNo == UFTCORE_ERR_INVALID_CATEGORY)
{
   lpIUFTContext->GetErrorFormat()->Format20(lpIUFTContext->nErrorNo, "[对象]");
   lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
   goto svr_end;
}
else if (@[对象] == InvalidRecordHandle)
```

**说明**: 获取记录为空，且错误号是无效的数据种类，返回报错。并且判断记录指针为空。
示例代码：
<M>[获取记录][branch(idx_branch)][branch_no=@branch_no]
[获取记录为空][branch]
{
    // [老版报错返回][ERR_751001][@branch_no]
    或者
    //[继续执行]
    //[插入记录][branch][]
}

### 业务报错返回

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,原子服务,原子函数

```
//业务报错返回
memset(@usermacro_errorinfo,0,sizeof(@usermacro_errorinfo));
\<Z\>\[获取记录\]\[upbs_error_msg(idx_upbs_error_msg)\]\[error_no = [错误号]\]\[error_info=@usermacro_errorinfo\]
\[记录为空\]\[upbs_error_msg\]
{
\[报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
else
{
\[自定义错误信息返回\]\[[错误号]\]\[@usermacro_errorinfo\]\[{[参数列表]}\]
}
```

### 获取序列号

- **参数**: `[序号][序列号]`
- **适用类型**: 函数,原子函数

```
[序列号] = lpITransCtrl->GetNextSequence([序号], &lpIUFTContext->nErrorNo);
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   \[报错返回\]\[ERR_SEQUENCEERR\]\[[序号]\]
}
```

**说明**: 示例代码：
[获取序列号][CNST_USESSERIALTYPE_USES_FUND_DETAIL_JOUR][@serial_no]

### 清理内存数据库

- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->ResetMDB();
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   goto svr_end;
}
```

### 建立全量关联关系

- **适用类型**: 函数,服务,原子函数,原子服务

```
lpIUFTContext->BuildRelation();
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   goto svr_end;
}
```

### 字符串为空

- **参数**: `[字段]`
- **适用类型**: 函数,服务

```
(isnull([字段]) == 0 || [字段][0] == ' ')
```

**说明**: if ([字符串为空][@fund_account])
{
  xxxx;
}

### 如果字符串为空

- **参数**: `[字段]`
- **适用类型**: 函数,服务

```
if (isnull([字段]) == 0 || [字段][0] == ' ')
```

### 如果字符串不为空

- **参数**: `[字段]`
- **适用类型**: 函数,服务

```
if (isnull([字段]) != 0 && [字段][0] != ' ')
```

### 字符串不为空

- **参数**: `[字段]`
- **适用类型**: 函数,服务

```
(isnull([字段]) != 0 && [字段][0] != ' ')
```

### 获取日期

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子函数

```
@[标准字段] = lpIUFTContext->nDate;
```

**说明**: 日期格式 YYYYMMDD

### 获取时间

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子函数

```
@[标准字段] = lpIUFTContext->nTime;
```

**说明**: 时间格式HHMMSS

### 获取微秒时间

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] = (HsMicroTime)lpIUFTContext->GetMicroSecs();
```

### clob字段解包

- **参数**: `[解包器][clob字段][clob长度]`
- **适用类型**: 函数

```
if (![解包器])
{
   iRaiseError = 1;
   lpIUFTContext->nErrorNo = ERR_EXEC_BUSIPACK_ISNULL;
   lpIUFTContext->GetErrorFormat()->Format(ERR_EXEC_BUSIPACK_ISNULL, wrap("解包错误（无法获取解包器）"));
   lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
   goto svr_end;
}
lpIUFTContext->nErrorNo = [解包器]->Open([clob字段],[clob长度]);
if ( lpIUFTContext->nErrorNo != 0)
{  
   iRaiseError = 1;
   lpIUFTContext->nErrorNo = ERR_EXEC_BUSIPACK_ISNULL;
   lpIUFTContext->GetErrorFormat()->Format(ERR_EXEC_BUSIPACK_ISNULL, wrap("解包错误（无法获取解包器）"));
   lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
   goto svr_end;
}
else if (  [解包器]->GetColCount() < 0)
{   
   iRaiseError = 1;
   lpIUFTContext->nErrorNo = ERR_PACKRESULE_ISNULL;
   lpIUFTContext->GetErrorFormat()->Format(ERR_PACKRESULE_ISNULL, wrap("解包错误（行列不匹配）"));
   lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
   goto svr_end;
}
```

### 获取部署类型

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetDeployType();
```

### 获取冲销流水号

- **参数**: `[标准字段]`
- **适用类型**: 函数,原子函数

```
{
    HsSerialNo v_usermacro_temp_serial_no;
    \[获取序列号\]\[CNST_SERIALTYPE_CANCEL_SERIAL_NO\]\[v_usermacro_temp_serial_no\]
    hs_snprintf(@[标准字段], sizeof(@[标准字段]), "%010d%s", v_usermacro_temp_serial_no, lpIUFTContext->GetLdpHost()->GetVariables()->GetString(VarID::ShortAppName));
}
```

**说明**: 获取冲销流水号
拼接方式：流水号（10位）+集群名
如证券竞价交易核心（分片号62）获取冲销流水号，流水号为1：
结果为：0000000001usesbid62

使用参考：
[获取冲销流水号][@cancel_serial_no]

### 获取轮询配置

- **参数**: `[轮询提前时间][轮询延迟时间][轮询间隔时间][轮询一次发送最大笔数]`
- **适用类型**: 函数,服务

```
@[轮询提前时间] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetPollingAheadTime();
@[轮询延迟时间] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetPollingDelayTime();
@[轮询间隔时间] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetPollingTimerInterval();
@[轮询一次发送最大笔数] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetPollingSendMaxCount();
```

### 业务远程调用

- **参数**: `[标准参数列表][{[发送数据列表]}][输出列表] `
- **适用类型**: 原子函数

```
IF2UnPacker* lpUnPacker;
\[同步调用\]\[[标准参数列表]\]\[{[发送数据列表]}\]\[out_packer = lpUnPacker\]  
\[手工解包体\]\[@error_no,@error_info,@error_pathinfo]\[lpUnPacker\] 
if (@error_no != OK_SUCCESS)
{
    char szErrorPath[256] = "";
    iRaiseError = 1;
    lpIUFTContext->nErrorNo = @error_no;
    lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap(@error_info));
    snprintf(szErrorPath, sizeof(szErrorPath), "%s->%s",__FUNCTION__,@error_pathinfo);
    lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, szErrorPath);
    if (lpPackerV3)
    {
        lpPackerV3->FreeMem(lpPackerV3->GetPackBuf());
        lpPackerV3->Release();
    }
    lpIUFTContext->EndProcess(szErrorPath, iRaiseError);
    return lpIUFTContext->nErrorNo;
}
\[手工解包体\]\[[输出列表]]\[lpUnPacker\]
```

**说明**: 基于系统内置宏[同步调用]封装，支持[同步调用]失败时，自动解析错误信息报错
用法示例：
[业务远程调用][ function_id = XXXXXX, timeout = 10000][@fund_account][entrust_no = @entrust_no]

### 获取分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] =lpIUFTContext->GetBizProc()->GetShardNo();
```

### 表记录不存在

- **适用类型**: 函数

```
if (lpIUFTContext->nErrorNo == LDP_MDB_RECORD_NOTEXISTS)
```

**说明**: 根据上下文中的错误号判断表记录是否存在，一般用于综合模块进行判断，竞价模块可使用用户自定义宏记录为空/记录不为空进行判断

### 节点定位插件分片状态更新

- **参数**: `[分片规则名变量][打包变量]`
- **适用类型**: 函数

```
if (lpIUFTContext->GetLocateImpl() == NULL)
{
  iRaiseError = 1;
  lpIUFTContext->nErrorNo = LDP_PLUGIN_GET_FAILED;
  lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap("ldp_locate"));
  goto svr_end;
}
else
{
  lpIUFTContext->nErrorNo = lpIUFTContext->GetLocateImpl()->ReloadByRuleName([分片规则名变量], (char*)[打包变量]->GetPackBuf());
  
  if (unlikely(lpIUFTContext->nErrorNo != OK_SUCCESS))
  {
    iRaiseError = 1;
    lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, [分片规则名变量]);
    goto svr_end;
  }
}
```

**说明**: 用于调用Locate插件的ReloadByRuleName接口上传json字符串

### 节点定位Rules打包头

- **参数**: `[打包变量][内存分片号字段][内存分片状态字段]`
- **适用类型**: 函数

```
//节点定位Rules手工打包头
[打包变量]->BeginPack();
[打包变量]->AddField("[内存分片号字段]", 'S');
[打包变量]->AddField("[内存分片状态字段]", 'I');
```

**说明**: Rules打包头，Rules打包体，Rules打包结束用来打包Rules标签下的结果集内容

### 节点定位Rules打包体

- **参数**: `[打包变量][内存分片号变量][内存分片状态变量]`
- **适用类型**: 函数

```
//节点定位Rules手工打包体
[打包变量]->AddStr([内存分片号变量]);
[打包变量]->AddInt([内存分片状态变量]);
```

**说明**: Rules打包头，Rules打包体，Rules打包结束用来打包Rules标签下的结果集内容

### 节点定位Rules打包结束

- **参数**: `[打包变量][Rules]`
- **适用类型**: 函数

```
//节点定位Rules手工打包结束
[打包变量]->EndPack();
[Rules] = [打包变量]->GetPackBuf();
vi_Rules = [打包变量]->GetPackLen();
```

**说明**: Rules打包头，Rules打包体，Rules打包结束用来打包Rules标签下的结果集内容

### 节点定位更新打包头

- **参数**: `[打包变量][规则名称][内存分片号字段][内存分片状态字段]`
- **适用类型**: 函数

```
//节点定位更新打包头
[打包变量]->BeginPack();
[打包变量]->AddField([规则名称], 'S');
[打包变量]->AddField([内存分片号字段], 'S');
[打包变量]->AddField([内存分片状态字段], 'S');
[打包变量]->AddField("Rules", 'R', vi_Rules);
```

### 节点定位更新打包体

- **参数**: `[打包变量][规则名称][内存分片号变量][内存分片状态变量]`
- **适用类型**: 函数

```
//节点定位更新打包体
[打包变量]->AddStr([规则名称]);
[打包变量]->AddStr([内存分片号变量]);
[打包变量]->AddStr([内存分片状态变量]);
[打包变量]->AddRawEx(v_Rules, vi_Rules);
```

### 节点定位更新打包结束

- **参数**: `[打包变量]`
- **适用类型**: 函数

```
//节点定位更新打包结束
[打包变量]->EndPack();
```

### 获取额度管理分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子函数,因子服务

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetUqmsPartitionNo();
```

### 获取请求分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =lpIUFTContext->GetLdpMsgReader()->GetHead()->NodeNo;
```

### 业务复核标志

- **适用类型**: 函数,服务

```
if ( @audit_action == CNST_AUDIT_BUSI_CHK )
{
  goto svr_end;
}
```

### 获取功能号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] =lpIUFTContext->GetLdpMsgReader()->GetHead()->FunctionID;
```

**说明**: 说明：该宏以后作废，待两融修改完删除该宏

### 获取仲裁状态

- **参数**: `[仲裁状态]`
- **适用类型**: 函数,服务

```
@[仲裁状态] = (int32_t)lpIUFTContext->GetBizProc()->GetArbStatus();
```

### 获取RPC超时时间

- **参数**: `[标准字段] `
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetRpcTimeout();
```

**说明**: 单位:毫秒

### 获取回库RPC超时时间

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetTogwRpcTimeout();
```

**说明**: 单位:毫秒

### 获取转换服务分片号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetUconvertPartitionNo();
```

### 设置序列号

- **参数**: `[序号][序列号]`
- **适用类型**: 函数,原子函数

```
lpITransCtrl->ResetSequence([序号], [序列号] );
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   \[报错返回\]\[ERR_SEQUENCEERR\]\[[序号]\]
}
```

**说明**: 示例代码：
[设置序列号][CNST_USESSERIALTYPE_USES_FUND_DETAIL_JOUR][@serial_no]

### 获取应用集群名

- **参数**: `[集群名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
hs_strncpy(@[集群名] , lpIUFTContext->GetLdpHost()->GetVariables()->GetString(VarID::ShortAppName),sizeof(@[集群名] )-1);
```

### 业务报错自定义返回

- **参数**: `[错误号1][错误号2][错误信息]`
- **适用类型**: 函数,原子函数

```
//业务报错返回
iRaiseError = 1;
lpIUFTContext->nErrorNo = [错误号1];
lpIUFTContext->GetErrorFormat()->Format([错误号2], wrap([错误信息]));
lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
goto svr_end;
```

### 直接返回

- **适用类型**: 函数,原子函数

```
goto svr_end;
```

### 获取调用功能号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] = lpIUFTContext->GetLdpMsgReader()->GetOptionalHead()->GetInt(TagOrgFunctionId);
//请求进来调用SetRequest会清空可选头，所以这里可以根据可选头中的功能号是否为0 来区分本次请求是否经过RPC调用
if (@[标准字段] == 0)
{
   @[标准字段] = lpIUFTContext->GetLdpMsgReader()->GetHead()->FunctionID;
}
```

### 轮询错误处理

- **适用类型**: 服务

```
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
    {
        //内部引用标准字段变量初始化
        HsChar500 v_error_message = "";
        if (iRaiseError == 0)
        {
            (void)snprintf(szErrorPath, sizeof(szErrorPath), "%s->%s", __FUNCTION__, lpIUFTContext->GetErrorPath());
        }
        else
        {
            (void)snprintf(szErrorPath, sizeof(szErrorPath), "%s", __FUNCTION__);
        }
        snprintf(v_error_message, sizeof(v_error_message), "轮询处理错误:function(%s),error_no(%d),error_info(%s),error_pathinfo(%s)",
        __FUNCTION__, lpIUFTContext->nErrorNo, lpIUFTContext->GetErrorFormat()->GetUTF8Message(), szErrorPath);
        
        //记录分布式日志
        LDPBIZLOG_ERROR(lpIUFTContext->GetLdpContext(),lpIUFTContext->nErrorNo,NULL,wrap(v_error_message));
    }
```

**说明**: 该宏用于轮询处理结束前判断是否有返回错误，若有就记录相应错误日志
注：需要轮询处理函数前加<M>标志

### 获取带分片序列号

- **参数**: `[序号][序列号]`
- **适用类型**: 函数,原子函数

```
[序列号] = lpITransCtrl->GetNextSequence([序号], &lpIUFTContext->nErrorNo);
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   \[报错返回\]\[ERR_SEQUENCEERR\]\[[序号]\]
}
[序列号] += (lpIUFTContext->GetBizProc()->GetShardNo() * 10000000);
```

**说明**: 获取序列号后，拼接分片号
示例代码：[获取带分片序列号][CNST_USES_SEQUENCE_ENTRUST_REPORT_NO][@serial_no]

### 重置周边获取记录行数

- **参数**: `[请求行数]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([请求行数] <= 0)
{
  [请求行数] = CNST_EXT_DEFAULT_ROWCOUNT;
}
else if ([请求行数] > CNST_EXT_MAX_ROWCOUNT)
{ 
  [请求行数] = CNST_EXT_MAX_ROWCOUNT;
}
```

### 核心通用参数同步

- **参数**: `[解包器名][对象名][全局唯一索引名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[手工解包开始\]\[$paramStr\]\[[解包器名]\] 
  \[事务处理开始\]
  \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$indexFieldsAssignStr\]\[transaction_no = @transaction_no_t\]
  \[记录不为空\]\[[对象名]\]
  {
        if (@transaction_no > @transaction_no_t)
        {
          if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
          {
            \[修改记录\]\[[对象名]\]\[$structureFieldsWithOutIndexFieldAssignStr\]

            $modIndexExpression
          }
          else if (CNST_PARAMOPER_DELETE == @param_oper_type)
          {
            \[删除记录\]\[[对象名]\]
          }
        }
  }
  else
  {
    if (CNST_PARAMOPER_INSERT == @param_oper_type || CNST_PARAMOPER_UPDATE == @param_oper_type)
    {
      \[插入记录\]\[[对象名]\]\[$structureFieldsAssignStr\]
    }
  }
  \[事务处理结束\]
\[手工解包结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[核心通用参数同步][@unpack_sett][upbs_extern_error][idx_upbs_extern_error] 

宏标记说明:
I:支持索引字段修改
注意：使用I标记时，必须传入索引字段修改表达式
示例如下：
<I>[核心通用参数同步][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][aim_value = @aim_value]

### 获取表名称

- **参数**: `[表号][表名称]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
{
    ITableFactory * const lpTempITableFactory = lpIUFTContext->GetTableFactory();
    ITable * const lpTempTable = lpTempITableFactory->GetTable(@[表号]);

    if (unlikely(nullptr == lpTempTable))
    {
      iRaiseError = 1;
      lpIUFTContext->nErrorNo = LDP_MDB_QRY_FAIL;
      lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap("table_category:"), wrap(@[表号]));
      lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
      goto svr_end;
    }

    hs_strncpy(@[表名称], lpTempTable->GetRecordName(), sizeof(@[表名称]) - 1);
}
```

**说明**: 根据UFT对象表号获取UFT对象的表名称(英文名称)
范例：
[获取表名称][@table_category][@table_name]

注意:表号必须是变量

### 客户数据同步

- **参数**: `[解包器名][对象名][全局唯一索引名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[手工解包开始\]\[$paramStr\]\[[解包器名]\] 
  \<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[$indexFieldsAssignStr\]
  \[记录为空\]\[[对象名]\]
  {
    \<C\>\[插入记录\]\[[对象名]\]\[$structureFieldsAssignStr\]
  }
\[手工解包结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[客户数据同步][@unpack_sett][upbs_extern_error][idx_upbs_extern_error] 

宏标记说明:
I:支持索引字段修改
注意：
1.使用I标记时，必须传入索引字段修改表达式
示例如下：
<I>[核心通用参数同步][@unpack_sett][usps_dfare2seg][idx_usps_dfare2seg][aim_value = @aim_value]

### 客户数据关联同步

- **参数**: `[解包器名][对象名][非全局唯一索引名]{[修改索引字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[手工解包开始\]\[$paramStr\]\[[解包器名]\] 
    \<Z\>\[获取记录\]\[ucrt_fund_account.[对象名]([非全局唯一索引名])\]\[$indexFieldsAssignStr\]
  \[记录为空\]\[[对象名]\]
  {
    \<C\>\[插入记录\]\[[对象名]\]\[$structureFieldsAssignStr\]
  }
\[手工解包结束\]
```

**说明**: 实现通用的参数同步逻辑
示例：
[客户数据关联同步][@busi_data][ucrt_unity_video][idx_ucrt_unity_video] 

宏标记说明:
I:支持索引字段修改
注意：
1.使用I标记时，必须传入索引字段修改表达式
示例如下：
<I>[客户数据关联同步][@busi_data][ucrt_unity_video][idx_ucrt_unity_video][value = @value]

### 获取结构体

- **参数**: `[组件名][输出列表]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
//业务自定义宏:获取结构体
$codestr
```

**说明**: 用户获取结构体组件的字段信息
注:仅适用于勾选了“是否结构体”的标准组件

使用范例：
注：
[comp_crtexchinfo]手工勾选了“是否结构体”
[获取结构体][comp_crtexchinfo][real_balance = @real_balance,
 entrust_type = @entrust_type]

### 修改结构体

- **参数**: `[组件名][{参数列表}]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
//业务自定义宏:修改结构体
$codestr
```

**说明**: 用户修改结构体组件的字段信息
注:仅适用于勾选了“是否结构体”的标准组件

使用范例：
注：comp_crtexchinfo手工勾选了“是否结构体”
  [修改结构体][comp_crtexchinfo][init_date = @usps_exch_arg.init_date]

### EXCEPTION

- **适用类型**: 函数,服务,原子服务,原子函数

```
@sql_error_no = lpIUFTContext->nErrorNo;
lpIUFTContext->nErrorNo = OK_SUCCESS;
iRaiseError = 0;
if (unlikely(OK_SUCCESS == @sql_error_no)) 
{
}
```

### WHEN_TOO_MANY_ROWS

- **适用类型**: 函数,服务,原子服务,原子函数

```
else if (LDP_ARES_SQL_QRY_FAIL ==  @sql_error_no && @sql_row_count > 1)
```

### WHEN_NO_DATA_FOUND

- **适用类型**: 函数,服务,原子服务,原子函数

```
else if (LDP_ARES_SQL_QRY_FAIL == @sql_error_no && @sql_row_count == 0)
```

### WHEN_OTHERS

- **适用类型**: 函数,服务,原子服务,原子函数

```
else
```

### WHEN_DUP_VAL_ON_INDEX

- **适用类型**: 函数,服务,原子服务,原子函数

```
else if( UFTCORE_ERR_DUP_KEY == @sql_error_no)
```

### 动态SQL执行

- **参数**: `[SQL语句][{标准参数列表}]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[通用SQL执行\]\[[SQL语句]\]\[{[标准参数列表]}\]
```

### 标准可选查询条件字符串

- **参数**: `[变量][字段][运算符][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
   hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and [表别名][字段] [运算符]'", [变量],"' ");
}
```

### 标准可选查询条件字符串instr

- **参数**: `[变量][字段][运算符][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
    hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and instr(',' || '",[变量],"' || ',', ',' ||  to_char([表别名][字段]) || ',') [运算符] 0 ");
}
```

### 标准可选查询条件字符

- **参数**: `[变量][字段][运算符][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_c([变量]) != 0)
{
   hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%c%s",    @sSql,"    and [表别名][字段] [运算符]'", [变量],"' ");
}
```

### 通用SELECT

- **参数**: `[SQL语句][结果集变量或者打包变量]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[通用SQL执行\]\[[SQL语句]\]\[count = @sql_row_count, packer = @packer\]
\[结果集转换\]\[@packer\]\[[结果集变量或者打包变量]\]
```

### 重置结束日期函数

- **参数**: `[开始日期][结束日期][时间间隔]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([开始日期] > 0 && [时间间隔] > 0)
{
  int li_date = hs_dateadd([开始日期],[时间间隔]);
  
  if (li_date < [结束日期])
    [结束日期] = li_date;
}
```

### 获取带分片序列号8位

- **参数**: `[序号][序列号]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
[序列号] = lpITransCtrl->GetNextSequence([序号], &lpIUFTContext->nErrorNo);
if (lpIUFTContext->nErrorNo != OK_SUCCESS)
{
   \[报错返回\]\[ERR_SEQUENCEERR\]\[[序号]\]
}
[序列号] += (lpIUFTContext->GetBizProc()->GetShardNo() * 1000000);
```

### PRO*C结果集为空

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (LDP_ARES_SQL_QRY_FAIL == @sql_error_no && @sql_row_count  == 0)
```

### PRO*C语句

- **参数**: `[SQL语句]{[表名]}{[变量]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\<M\>\[通用SQL执行\]\[[SQL语句]\]\[count = @sql_row_count\]
@sql_error_no = lpIUFTContext->nErrorNo;
if (LDP_ARES_SQL_QRY_FAIL == lpIUFTContext->nErrorNo && @sql_row_count == 0)
{
   @sql_error_no = lpIUFTContext->nErrorNo;
   lpIUFTContext->nErrorNo = OK_SUCCESS ;
  iRaiseError = 0;
}
if (@sql_error_no == OK_SUCCESS ||  (LDP_ARES_SQL_QRY_FAIL == @sql_error_no && @sql_row_count == 0))
```

### PRO*C结果集不为空

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (@sql_error_no == OK_SUCCESS)
```

### 通用SQL捕获

- **参数**: `[sql参数]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
hs_strncpy(@sSql, [sql参数], sizeof(@sSql)-1); 
  hs_strncpy(@execute_sql, " ", sizeof(@sSql)-1); 
  for (int v_i = 1; @i <= (int)lpSqlArgsIn->GetCount(); @i ++ )
  {
    int pos = instr(@sSql, '?');
    
    if (lpSqlArgsIn->Get(@i)->eType == 1)
    {
      if (pos > 0)
      {
        hs_strncpy(@sql_str, "", sizeof(@sql_str) - 1);
        hs_strncpy(@sql_str1, "", sizeof(@sql_str1) - 1);
        substr(@sSql, 1, pos - 1, @sql_str);
        substr(@sSql, pos + 1, 0 , @sql_str1);
        snprintf(@sSql, sizeof(@sSql), "%s%ld%s", @sql_str, lpSqlArgsIn->Get(@i)->iVal ,@sql_str1);
      }
      DEBUG_LOG_TRACE("@%d=%ld--\n", @i, lpSqlArgsIn->Get(@i)->iVal);	  
    }
    else if (lpSqlArgsIn->Get(@i)->eType == 2)
    {
      if (pos > 0)
      {
        hs_strncpy(@sql_str, "", sizeof(@sql_str) - 1);
        hs_strncpy(@sql_str1, "", sizeof(@sql_str1) - 1);
        substr(@sSql, 1, pos - 1, @sql_str);
        substr(@sSql, pos + 1, 0 , @sql_str1);
        snprintf(@sSql, sizeof(@sSql), "%s%f%s", @sql_str, lpSqlArgsIn->Get(@i)->dVal ,@sql_str1);
      }
	  DEBUG_LOG_TRACE("@%d=%f--\n", @i, lpSqlArgsIn->Get(@i)->dVal);
    }
    else if (lpSqlArgsIn->Get(@i)->eType == 3)
    {
      if (pos > 0)
      {
        hs_strncpy(@sql_str, "", sizeof(@sql_str) - 1);
        hs_strncpy(@sql_str1, "", sizeof(@sql_str1) - 1);
        substr(@sSql, 1, pos - 1, @sql_str);
        substr(@sSql, pos + 1, 0 , @sql_str1);
        snprintf(@sSql, sizeof(@sSql), "%s'%s'%s", @sql_str, lpSqlArgsIn->Get(@i)->lpszVal ,@sql_str1);
      }
	  DEBUG_LOG_TRACE("@%d='%s'--\n", @i, lpSqlArgsIn->Get(@i)->lpszVal);
    }
  }
  DEBUG_LOG_TRACE("sql = %s\n", @sSql);
```

**说明**: 跟[通用SQL执行]配套使用，用于捕获sql语句，仅可用于调试。
<M>[通用SQL执行][select stock_account
                     into @stock_account_inparam
                     from uses_stock_holder
                     where fund_account = @fund_account_inparam
                     and exchange_type = @exchange_type_inparam
                     and main_flag = '1'][count = @count]
需要传入原始sql，配套使用，未报错时无法捕获sql
[通用SQL捕获][lpSqlResultSet1943923_1->GetLastErrorSql()]

### 函数结果集字段获取

- **参数**: `{[标准字段]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[手工解包体\]\[{[标准字段]}\]\[lpResultSet\]
```

### 如果结果集不为空

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (!lpResultSet->IsEmpty())
```

### PRO*C结果集返回

- **适用类型**: 函数,服务,原子服务,原子函数

```
\[结果集转换\]\[lpResultSet\]\[lpOutPacker\]
\[直接返回\]
```

### 如果结果集为空

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (lpResultSet->IsEmpty())
```

### LS结果集返回

- **适用类型**: 服务

```
\[结果集转换\]\[lpResultSet\]\[lpAnswer\]
```

### LF结果集返回

- **适用类型**: 函数,服务,原子服务,原子函数

```
\[结果集转换\]\[lpResultSet\]\[lpOutPacker\]
```

### 取系统节点号

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[获取分片号\]\[标准字段\]
```

### PRO*C结果集语句

- **参数**: `[SQL语句]{[表名]}{[变量]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\<M\>\[通用SQL执行\]\[[SQL语句]\]\[count = @sql_row_count\]
```

### 结果集返回

- **适用类型**: 函数,服务,原子服务,原子函数

```
\[结果集转换\]\[lpResultSet\]\[lpOutPacker\]
```

### PRO*C函数多记录校验

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (@sql_row_count > 1)
```

### 错误描述重置

- **参数**: `[重置错误信息]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->GetErrorFormat()->Format(ERR_SECUUFT_USER_DEFINE_ERROR, [重置错误信息]);
```

### 重置错误信息

- **参数**: `[错误号][错误信息]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->nErrorNo = [错误号];
lpIUFTContext->GetErrorFormat()->SetMultiByteFormattedMessage(0, IMsgFormat::$encode_type, @[错误信息]);
```

### 自定义参数报错返回

- **参数**: `[错误号][参数信息]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
memset(@usermacro_errorinfo,0,sizeof(@usermacro_errorinfo));
\<Z\>\[获取记录\]\[upbs_error_msg(idx_upbs_error_msg)\]\[error_no = [错误号]\]\[error_info=@usermacro_errorinfo\]
\[记录为空\]\[upbs_error_msg\]
{
  iRaiseError = 1;
  lpIUFTContext->nErrorNo = [错误号];
  lpIUFTContext->GetErrorFormat()->Format([错误号], [参数信息]);
  lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
  goto svr_end;
}
else
{
  iRaiseError = 1;
  lpIUFTContext->nErrorNo = [错误号];
  lpIUFTContext->GetErrorFormat()->MultiByteFormat([错误号], IMsgFormat::LdpEncodingType::Utf8, @usermacro_errorinfo, [参数信息]);
  lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
  goto svr_end;  
}
```

### 重置参数错误信息

- **参数**: `[错误号][错误信息1][错误信息2]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->nErrorNo = [错误号];
lpIUFTContext->GetErrorFormat()->SetMultiByteFormattedMessage(0, IMsgFormat::$encode_type, @[错误信息1],@[错误信息2]);
```

### 获取额度管理流水号切换增量

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetUqmsMaxSerialInCrement();
```

**说明**: 用于获取json业务配置中的额度管理流水号切换增量
备机房额度管理核心切换至主机时，
额度管理流水号增加值 = 额度管理流水号切换增量 * serial_assign_counts

### 标准可选查询条件字符串存在instr

- **参数**: `[变量][字段][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (instr([变量], ',') > 0)
  {
    hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and instr(',' || '",[变量],"' || ',', ',' ||  [表别名][字段] || ',') > 0 ");
  }
  else
  {  
    hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and [表别名][字段] = '",[变量],"' ");
  }
}
```

### 标准可选查询条件实数exact

- **参数**: `[变量][字段][运算符][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (fabs([变量]) > 0.000001)
{
  hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%f%s",    @sSql,"    and [表别名][字段] [运算符]", [变量]," ");
}
```

### 客户数据删除

- **参数**: `[对象名][全局唯一索引名][条件列表]`
- **适用类型**: 函数

```
\<Z\>\[获取记录\]\[[对象名]([全局唯一索引名])\]\[[条件列表]\]
  \[记录不为空\]\[[对象名]\]
  {
    \[删除记录\]\[[对象名]\]
  }
```

**说明**: 实现通用的删除逻辑
示例：
[客户数据删除][ucrt_fund_account][idx_ucrt_fund_account][fund_account = @fund_account]

### 客户批量数据删除

- **参数**: `[上级][对象名][索引][条件列表][批量大小]`
- **适用类型**: 函数

```
\<E\>\[遍历记录开始\]\[[上级].[对象名]([索引])\]\[[条件列表]\]\[[批量大小]\]
{
   \[删除记录\]\[[对象名]\]
}
\[遍历记录结束\]
```

### 客户二层批量数据删除

- **参数**: `[上上级][上级][对象名][上级索引][索引][上级条件列表][条件列表][批量大小]`
- **适用类型**: 函数

```
\<E\>\[遍历记录开始\]\[[上上级].[上级]([上级索引])\]\[[上级条件列表]\]\[[批量大小]\]
   \<E\>\[遍历记录开始\]\[[上级].[对象名]([索引])\]\[[条件列表]\]\[[批量大小]\]
  {
     \[删除记录\]\[[对象名]\]
  }
  \[遍历记录结束\]
\[遍历记录结束\]
```

### 客户三层批量数据删除

- **参数**: `[上上上级][上上级][上级][对象名][上上级索引][上级索引][索引][上上级条件列表][上级条件列表][条件列表][批量大小]`
- **适用类型**: 函数

```
\<E\>\[遍历记录开始\]\[[上上上级].[上上级]([上上级索引])\]\[[上上级条件列表]\]\[[批量大小]\]  
   \<E\>\[遍历记录开始\]\[[上上级].[上级]([上级索引])\]\[[上级条件列表]\]\[[批量大小]\]
     \<E\>\[遍历记录开始\]\[[上级].[对象名]([索引])\]\[[条件列表]\]\[[批量大小]\]
    {
       \[删除记录\]\[[对象名]\]
    }
    \[遍历记录结束\]
  \[遍历记录结束\] 
\[遍历记录结束\]
```

### 等待客户回切事务处理

- **参数**: `[等待超时秒数][事务号]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
/// 等待客户回切事务处理
if (lpIUFTContext == NULL || lpIUFTContext->GetBizProc() == NULL)
{
  iRaiseError = 1;
  lpIUFTContext->nErrorNo = UFTCORE_ERR_NULL_OBJECT;
  lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap("等待客户回切事务处理异常"));
  goto svr_end;
}
else
{
  /// 同步等待调用本接口之前的工作线程内的所有任务执行完成
  if (lpIUFTContext->GetBizProc()->WaitForAllPreTasks([等待超时秒数]) == true)
  {
    /// 获取下一个事务号
    @[事务号] = lpIUFTContext->GetBizProc()->GetNextTranscationNo();
  }
  else
  {
    iRaiseError = 1;
    lpIUFTContext->nErrorNo = LDP_ARES_SYNC_CALL_FAIL;
    lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap("等待客户回切事务处理失败"));
    goto svr_end;
  }
}
```

**说明**: 等待客户回切事务处理，封装以下函数。
bool WaitForAllPreTasks(uint_32_t uTimeout = -1);
@uTimeout：等待超时秒数，-1表示一直等待；
@return：之前所有任务都执行完成返回true，超时或调用失败返回false；
@details：同步等待调用本接口之前的工作线程内的所有任务执行完成，线程安全。

获取客户回切事务号，封装的函数说明如下：
uint64_t GetNextTranscationNo();
@return：下一个事务号；
@details：接口调用时期：IBizData::Init 以后，IBizData::Exit 以前；多线程调用安全。

### 检查PRO*C结果集为空

- **适用类型**: 函数,服务,原子服务,原子函数

```
if (@sql_row_count == 0)
```

### 报盘重发回报判断

- **适用类型**: 服务

```
<svr_end>:
	// 如果有新增的需要报盘重发处理的错误号，都在这里补充判断
	if ((lpIUFTContext->nErrorNo == 270030) || (lpIUFTContext->nErrorNo == 151533) || (lpIUFTContext->nErrorNo == 151422))
	{
		@is_resend = 1;
	}
```

**说明**: 每个回报LS的最后都调用这个自定义宏，判断是否重置is_resend

### PRO*C语句块更新记录不存在

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,原子服务,原子函数

```
if (@sql_row_count == 0)
{
  \[报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
```

### 更新记录不存在 

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (@sql_row_count == 0)
{
  \[报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
```

### 存在序列号V2记录

- **参数**: `[序号类型in][序号索引字段in][结果out]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (((ITransCtrl * const)lpIUFTContext->GetTransCtrl())->IsExistSeq([序号类型in], 
                                 SeqKeyBuilder {
                                     [序号索引字段in]
                                 },
                                 &lpIUFTContext->nErrorNo))
        {
          [结果out] = 1;
        }
        else
        {
          if (likely(lpIUFTContext->nErrorNo == OK_SUCCESS))
          {
            [结果out] = 0;
          }
          else
          {
             //序列号获取错误
             iRaiseError = 1;
             lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap([序号类型in]));
             lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
             goto svr_end;
          }
        }
```

**说明**: 用于判断是否存在序列号V2记录。
示例：
[存在序列号V2记录][@sequence_type_dest][CNST_UCBPSERIALTYPE_ENTRUST][@count]

if (@count == 1)

{

}

### PRO*C函数无记录事务内报错返回

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (@sql_row_count == 0)
{
  \[报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
```

### 重置序列号V2简式

- **参数**: `[序号类型in][序号索引字段in][序号参数列表out]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
{
        SequenceSetParam seqSetParam([序号参数列表out]);
        lpIUFTContext->nErrorNo = ((ITransCtrl * const)lpIUFTContext->GetTransCtrl())->ResetSeqEx([序号类型in], 
                                 SeqKeyBuilder {
                                     [序号索引字段in]
                                 },
                                 &seqSetParam
                               );
        if (unlikely(lpIUFTContext->nErrorNo != OK_SUCCESS))
        {
            //序列号重置错误
            iRaiseError = 1;
            lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap([序号类型in]));
            lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
            goto svr_end;
        }
      }
```

**说明**: 支持序列号相关参数的重置，建议日初数据加载阶段使用，盘中使用时需要同时调用MDB的相关函数清理低层序列空间的缓存。
示例：

[重置序列号V2简式][@sequence_type_dest][@serial_counter_no][@sequence_min, @sequence_max, @sequence_next, @sequence_syncinterval, @sequence_increment]

### 重置获取记录行数

- **参数**: `[请求行数]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([请求行数] <= 0)
{
  [请求行数] = CNST_EXT_DEFAULT_ROWCOUNT;
}
else if ([请求行数] > CNST_EXT_MAX_ROWCOUNT)
{ 
  [请求行数] = CNST_EXT_MAX_ROWCOUNT;
}
```

### 序号类型映射V2

- **参数**: `[序号类型in][映射关系in][映射类型out]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
[映射类型out] = lpIUFTContext->GetSeqTypeByOpera([序号类型in],[映射关系in], &lpIUFTContext->nErrorNo);
        if ([映射类型out] < 0)
        {
            //序号类型in映射获取错误
            iRaiseError = 1;
            lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap([序号类型in]), wrap([映射关系in]));
            lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
            goto svr_end;
        }
```

**说明**: 根据序列类型获取映射类型；映射关系：0:进程->远程 1:线程->进程 2:线程->远程。
宏使用了上下文，不可在因子模块使用。
示例：
[序号类型映射V2][CNST_UPUB_SEQUENCE_V2SET_LPC_BRANCHNO][CNST_UPUB_SEQUENCE_V2MAP_THREAD_PROCESS][@sequence_type_dest]

### 记录不存在

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (LDP_ARES_SQL_QRY_FAIL == @sql_error_no && @sql_row_count == 0)
{
  \[业务报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
```

### 序号类型映射V2不报错返回

- **参数**: `[序号类型in][映射关系in][映射类型out]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
[映射类型out] = lpIUFTContext->GetSeqTypeByOpera([序号类型in],[映射关系in], &lpIUFTContext->nErrorNo);
```

**说明**: 根据序列类型获取映射类型；映射关系：0:进程->远程 1:线程->进程 2:线程->远程。
注意该宏不能保证出参[映射类型_out]是合法的值，需要调用方另外再判断返回值是否合法；需要使用[继续执行宏]将上下文的lpIUFTContext->nErrorNo重置成零。
示例：
[序号类型映射V2][CNST_UPUB_SEQUENCE_V2SET_LPC_BRANCHNO][CNST_UPUB_SEQUENCE_V2MAP_THREAD_PROCESS][@sequence_type_dest]

### 通用SELECT报错不返回

- **参数**: `[SQL语句][结果集变量或者打包变量]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
<M>\[通用SQL执行\]\[[SQL语句]\]\[count = @sql_row_count, packer = @packer\]
\[结果集转换\]\[@packer\]\[[结果集变量或者打包变量]\]
```

### 获取序列号区间V2

- **参数**: `[序号索引字段in][序号类型in][最小序列号out][最大序列号out]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->nErrorNo = ((ITransCtrl * const)lpIUFTContext->GetTransCtrl())->GetNextSeqEx([序号类型in],
                                                             SeqKeyBuilder {
                                                                [序号索引字段in]
                                                             },
                                                             &[最小序列号out],
                                                             &[最大序列号out]
                                                            );
```

**说明**: 没有报错返回，需要调用方解决处理失败的情况。
示例：
[获取序列号区间V2][@serial_counter_no, @branch_no][@sequence_type_dest][@sequence_min][@sequence_max]

### 标准结果集返回

- **适用类型**: 函数,服务,原子服务,原子函数

### 获取柜面RPC超时时间

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetExternalRpcTimeout();
```

**说明**: 单位:毫秒

### 通用可选查询条件字符串

- **参数**: `[变量][字段][运算符][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
   hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and [字段] [运算符]'", [变量],"' ");
}
```

### 自定义错误信息报错返回

- **参数**: `[错误号][错误信息]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
iRaiseError = 1;
lpIUFTContext->nErrorNo = [错误号];
lpIUFTContext->GetErrorFormat()->SetMultiByteFormattedMessage([错误号], IMsgFormat::$encode_type, @[错误信息]);
lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
$is_svr_end
```

**说明**: 自定义错误信息报错返回宏支持自定义错误信息的修改,支持带M标签，适合场景如下：
1.@error_info:[][][] | [][][] | XXX
2.@error_info:[][][]
3.@error_info:XXXX
示例：
[自定义错误信息返回][@error_no][@error_info]
<M>[自定义错误信息返回][@error_no][@error_info]

### 内存申请

- **参数**: `[clob包][V4打包器]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[clob包] = lpIUFTContext->NewMem(@[V4打包器]->GetPackLen());
if (@[clob包] == nullptr)
{
   \[报错返回\]\[UFTCORE_ERR_MALLOC\]
}
else
{
  memcpy(@[clob包], @[V4打包器]->GetPackBuf(), @[V4打包器]->GetPackLen());
}
```

**说明**: [内存申请] 和 [内存释放] 需要配对使用，并且需要增加<svr_end>标签
注意：只支持packerV4打包器
示例:
[内存申请][@entrust_clob][@packerV4]
....
<svr_end>:
[内存释放][@entrust_clob]

### 事务开始

- **适用类型**: 函数,服务,原子服务,原子函数

```
\[事务处理开始\]
```

### 内存释放

- **参数**: `[clob地址]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
{
  if (@[clob地址] == 0)
  {
    void *clob_addr_temp = (void*)(uintptr_t)@[clob地址];
    if (clob_addr_temp != nullptr)
    {
       lpIUFTContext->RecycleMem(clob_addr_temp);
    }
  }
}
```

**说明**: [内存申请] 和 [内存释放] 需要配对使用，并且需要增加<svr_end>标签
示例:
[内存申请][@entrust_clob][@packerV4]
....
<svr_end>:
[内存释放][@entrust_clob]

### 通用可选查询条件整数

- **参数**: `[变量][字段][运算符][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([变量] != 0)
{
   hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%d%s",    [目标字符串],"    and [字段] [运算符]", [变量]," ");
}
```

### 日终回库多中心数据打包

- **参数**: `[表名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
\[结果集记录池开始\]\[[表名]\]\[*, position_int = @position_int, request_num = @request_num\]
    {
      \<Z\>\[获取记录\]\[uses_fund_account(idx_uses_fund_account)\]\[fund_account = @fund_account\]\[sysnode_id = @sysnode_id_t\]
      \[记录为空\]\[uses_fund_account\]
      {
          continue;
      }
      if (@sysnode_id_t != @sysnode_id)
      {
        continue;
      }
    }
    \[结果集记录池结束\]
```

**说明**: 【参数说明】
·对象：具体获取的记录类型
·输出列表：field_name=@variable,...
【备注】
·只有在回库的UF2.0系统是多交易中心场景下，回库数据需要校验sysnode_id时才使用。
·需要指定position_int和request_num字段的值，否则无法遍历到数据。其中，position_int指定起始记录号，request_num指定遍历的记录条数
·遍历记录的同时打包输出列表字段
·输出列表为*，表示对象全字段。

### 通用可选查询条件字符存在instr

- **参数**: `[变量][字段][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (length([变量]) == 1)
  {
     hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and [字段] = '",[变量],"' ");
  }
  else
  {
     hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and instr('",[变量],"' , [字段]) > 0 ");
  }
}
```

### SQL结果集返回

- **适用类型**: 函数,服务,原子服务,原子函数

```
\[结果集转换\]\[lpResultSet\]\[lpAnswer\]
```

**说明**: [PROC结果集语句]查询到的结果直接作为应答出去。要求：[PROC结果集语句]返回的结果必须与当前LS接口要求的应答字段一致,且无需对返回的结果进行业务处理。

范例1:
[PRO*C结果集语句][select a.name,a.age from demo a]
[处理成功]
{
  [SQL结果集返回]
}

范例2:
[通用SQL执行][select a.name,a.age from demo a]
[处理成功]
{
  [SQL结果集返回]
}

### 通用可选查询条件实数

- **参数**: `[变量][字段][运算符][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (fabs([变量]) > 0.000001)
{
   hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%f%s",    [目标字符串],"    and [字段] [运算符]", [变量]," ");
}
```

### 上海交易类别判断

- **适用类型**: 函数,服务,原子服务,原子函数

```
if ((hs_strcmp(@exchange_type,CNST_EXCHANGETYPE_SHA) == 0) || (hs_strcmp(@exchange_type,CNST_EXCHANGETYPE_SHB) == 0)|| (hs_strcmp(@exchange_type,CNST_EXCHANGETYPE_GDSY) == 0))
```

### 中断跳转

- **适用类型**: 函数,服务,原子服务,原子函数

```
goto svr_end;
```

### 通用可选查询条件字符

- **参数**: `[变量][字段][运算符][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([变量] != CNST_CHAR_DEFAULTVALUE)
{
   hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%c%s",    [目标字符串],"    and [字段] [运算符]'", [变量],"' ");
}
```

### 通用可选查询条件整数存在instr

- **参数**: `[变量][字段][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (instr([变量], ',') > 0)
  {
     if ([变量][0] == ',')
        [变量][0] = ' ';
     
     if ([变量][length([变量])-1] == ',')
        [变量][length([变量])-1] = ' ';
     
     if (hs_isnull_s([变量]) > 0)
        hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and [字段]  in (", [变量], ") ");
  }
  else
  {
     hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s",      [目标字符串],"    and [字段] = ",[变量]);
  }
}
```

### 通用可选查询条件字符串存在instr

- **参数**: `[变量][字段][目标字符串]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (instr([变量], ',') > 0)
  {
    hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and instr(',' || '",[变量],"' || ',', ',' ||  [字段] || ',') > 0 ");
  }
  else
  {  
    hs_snprintf([目标字符串], sizeof([目标字符串]),"%s \n %s%s%s",    [目标字符串],"    and [字段] = '",[变量],"' ");
  }
}
```

### 信用业务函数判断

- **参数**: `[资产属性]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ([资产属性] == CNST_ASSETPROP_CREDIT)
```

**说明**: 判断是否为信用业务

### 标准可选查询条件整数

- **参数**: `[变量][字段][运算符][表别名]`
- **适用类型**: 函数,服务,原子函数,原子服务

```
if ([变量] != 0)
{
   hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%d%s",    @sSql,"    and [表别名][字段] [运算符]", [变量]," ");
}
```

### 事务内自定义异常返回

- **参数**: `[错误号][错误说明]{[参数列表]}`
- **适用类型**: 函数,服务,原子函数,原子服务

```
\[WHEN_OTHERS\]
{
  \[事务回滚\]
  \[业务报错返回\]\[[错误号]\]\[{[参数列表]}\]
}
```

### 同步等待

- **参数**: `[参数]`
- **适用类型**: 函数,服务,原子服务,原子函数

### 并发数据回库

- **参数**: `[表名][sql语句]`
- **适用类型**: 函数,服务,原子函数,原子服务,,因子服务,因子函数

### 初始化同步等待

- **适用类型**: 函数,服务,原子服务,原子函数

```
int32_t nLdpErrorNo = 0;
    uint32_t nCount = 0;    
    ILdpMsgReader **lppLdpMsgRpcReader = NULL;
    IF2UnPacker * lppUnPacker[256] =
    {
        NULL
    };
```

### 文件并发数据加载

- **参数**: `[对象名]{[数据库连接名]}{[加载sql语句]}`
- **适用类型**: 函数,服务,原子函数,原子服务,,因子服务,因子函数

### 获取时间(毫秒)

- **参数**: `[标准字段]`
- **适用类型**: 函数

```
@[标准字段] = (HsMicroTime)lpIUFTContext->GetMicroSecs() / 1000;
```

### 获取重发标志

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子函数,原子服务,,因子服务,因子函数

```
ILdpMsgReader * lpMsgReaderEx = lpIUFTContext->GetLdpMsgReader();
auto lpOptHeadEx = lpMsgReaderEx->GetOptionalHead();
//int TagMsgRetransmmited = 8;
if( lpOptHeadEx)
{
	@[标准字段] = lpOptHeadEx->Contains(42);
}
else
{
	@[标准字段] = 0;
}
```

**说明**: 获取委托包头中是否重发标志

### 获取TraceID

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子函数,原子服务,,因子服务,因子函数

```
ILdpMsgReader * lpMsgReader = lpIUFTContext->GetLdpMsgReader();
auto lpOptHead = lpMsgReader->GetOptionalHead();
//int TagMessageTraceID = 8;
const char * lpTraceID = lpOptHead->GetStr(8);
if( !lpTraceID )
{
	//traceid无效
	memset(@[标准字段],0,64);
}
else
{
	hs_strcpy(@[标准字段],lpTraceID);
}
```

### 重置所有序列号

- **适用类型**: 函数,服务,原子服务,原子函数

```
//重置序列号
$strSerialReset
```

**说明**: 遍历序列号资源，重置所有序列号，设置成初始值

### 标准可选查询条件字符存在instr

- **参数**: `[变量][字段][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (length([变量]) == 1)
  {
     hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and [表别名][字段] = '",[变量],"' ");
  }
  else
  {
     hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and instr('",[变量],"' , [表别名][字段]) > 0 ");
  }
}
```

### 标准可选查询条件整数存在instr

- **参数**: `[变量][字段][表别名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if (hs_isnull_s([变量]) != 0)
{
  if (instr([变量], ',') > 0)
  {
     if ([变量][0] == ',')
        [变量][0] = ' ';
     
     if ([变量][length([变量])-1] == ',')
        [变量][length([变量])-1] = ' ';
     
     if (hs_isnull_s([变量]) > 0)
        hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s%s",    @sSql,"    and [表别名][字段]  in (", [变量], ") ");
  }
  else
  {
     hs_snprintf(@sSql,CNST_SQLSTR_LEN,"%s \n %s%s",      @sSql,"    and [表别名][字段] = ",[变量]);
  }
}
```

### 底座参数同步字段转换

- **参数**: `[内存变量名][UF3变量名][UF2变量名][解包器名]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
if ('0' == @char_config_87028)
{
  \[手工解包体\]\[[UF2变量名] = @[内存变量名] \]\[@[解包器名]\]
}
else
{
  \[手工解包体\]\[[UF3变量名] = @[内存变量名] \]\[@[解包器名]\]
}
```

**说明**: 内存对接UF2和UF3参数同步时，当两个系统使用标准字段不一致场景，使用该自定义宏。标准字段一致时，无需对使用该自定义宏

范例：
[底座参数同步字段转换][day_buy_balance_uplimit][day_buy_balance_uplimit][total_quota][unpack_sett]

### 获取清算RPC超时时间

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetSettRpcTimeout();
```

### 获取LDP上场RPC超时时间

- **参数**: `[标准字段] `
- **适用类型**: 函数,服务,原子服务,原子函数,因子服务,因子函数

```
@[标准字段] =((CCustomContext *)(lpIUFTContext->GetBizContext()))->GetLdpRpcTimeout();
```

**说明**: 单位:毫秒

### 期权报盘重发回报判断

- **适用类型**: 服务

```
<svr_end>:
	// 如果有新增的需要报盘重发处理的错误号，都在这里补充判断
	if ((lpIUFTContext->nErrorNo == 270030) || (lpIUFTContext->nErrorNo == 302) || (lpIUFTContext->nErrorNo == 10043))
	{
		@is_resend = 1;
	}
	else if (lpIUFTContext->nErrorNo == 21901)
	{
		@is_resend = 1;
	}
         else if (lpIUFTContext->nErrorNo == 21902)
	{
		@is_resend = 1;
	}
```

**说明**: 每个回报LS的最后都调用这个自定义宏，判断是否重置is_resend

### SvrEnd出参打包

- **适用类型**: 服务

```
<svr_end>:
if(lpIUFTContext->nErrorNo == ERR_SYSWARNING)
  {
  	  	$code
	nErrorNoTemp = 0; 
}
```

### 获取机房类型

- **参数**: `[机房类型]`
- **适用类型**: 函数,服务

```
hs_strncpy(@[机房类型], lpIUFTContext->GetZoneType(), sizeof(@[机房类型]) - 1);
```

### 查询缓存表数据单行

- **参数**: `[SQL语句][标准参数列表][输出参数列表]`
- **适用类型**: 服务,函数,原子服务,原子函数

```
\<$macroFlag\>\[查询缓存表\]\[[SQL语句]\]\[[标准参数列表]\]

//20250920 gaozq27559 mod 参考通用SQL执行时对行数的判断,解析输出参数.
if (unlikely(lpIUFTContext->nErrorNo != OK_SUCCESS))
{
  //避免重置失败场景的错误信息.
}
else
{
  //等同于获取v_sql_row_count之后的那次查询结果的行数判断.
  if (@sql_row_count != 1)
  {
    //select..into语句查询失败，查询条数wrap("select_count", v_sql_row_count)
    iRaiseError = 1;
    lpIUFTContext->nErrorNo = LDP_ARES_SQL_QRY_FAIL;
    lpIUFTContext->GetErrorFormat()->Format(lpIUFTContext->nErrorNo, wrap("select_count", v_sql_row_count));
    lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
    
    //复刻使用通用SQL执行时M标签生成代码的逻辑.
    if ('M' != '$macroFlag')
    {
      goto svr_end;
    }
  }
  else
  {
    \[SQL结果集解包开始\]\[[输出参数列表]\]
    break;
    \[SQL结果集解包结束\]
  }
}
```

**说明**: M:生成函数代码，函数报错时不生成返回语句。
标准参数列表必须包含“count = @sql_row_count”，否则判断行数时会有问题。

### 获取微秒时间戳

- **参数**: `[标准字段]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
@[标准字段] = std::chrono::duration_cast<std::chrono::microseconds>(
                  std::chrono::system_clock::now().time_since_epoch()
              ).count();
```

**说明**: 获取当前服务器时间和1970年初始时间戳之间的微秒级别的差值

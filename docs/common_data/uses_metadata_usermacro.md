# uses - 用户自定义宏

用户自定义宏定义，包含宏名称、参数、内容和使用说明。

## 修改历史

| 日期 | 版本 | 作者 | 说明 |
|------|------|------|------|
| 2024-09-30 13:30:01 | V3.0.5.1001 | 余丰亮 | 内存交易错误号信息以及错误号二次重置代码优化 |
| 2024-08-12 10:06:18 | V3.0.1.10 | 范文浩 | 新增[错误信息重置]宏 |
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
| 2023-08-08 14:38 | 3.0.0.7 | 杨森峰 | 临时修改[业务远程调用]宏 |
| 2023-07-27 15:18 | 3.0.0.6 | 吴威 | 调整自定义宏[clob字段解包]，去除[解包器]->Release(); |
| 2023-07-25 21:19 | 3.0.0.5 | 李海洋 | 不合理依赖问题修复 |
| 2023-07-17 17:34 | 3.0.0.4 | 吴威 | 调整自定义宏[clob字段解包] |
| 2023-06-28 20:52 | 3.0.0.4 | 汪林 | 新增自定义宏[表记录不存在] |
| 2023-06-26 23:57 | 3.0.0.3 | 汪林 | 调整自定义宏获取冲销流水号的宏定义，调整自定义宏获取时间的使用范围 |

> 共 22 条修改记录，仅显示最近20条


## 宏列表（共 108 个）

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
- **适用类型**: 函数,原子函数

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
- **适用类型**: 函数,原子函数

```
\[报错返回\]\[[错误号]\]\[{[参数列表]}\]
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
   @error_no   = ERR_EXEC_BUSIPACK_ISNULL;
   hs_snprintf(@error_info,CNST_ERRORINFO_LEN,  "%s","解包错误（无法获取解包器）");
   goto svr_end;
}
lpIUFTContext->nErrorNo = [解包器]->Open([clob字段],[clob长度]);
if ( lpIUFTContext->nErrorNo != 0)
{  
   @error_no   = ERR_EXEC_BUSIPACK_ISNULL;
   hs_snprintf(@error_info,CNST_ERRORINFO_LEN,  "%s","解包错误（无法获取解包器）");
   goto svr_end;
}
else if (  [解包器]->GetColCount() < 0)
{   
   @error_no   =  ERR_PACKRESULE_ISNULL;
   hs_snprintf(@error_info,CNST_ERRORINFO_LEN,  "%s","解包错误（行列不匹配）");
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
\[获取序列号\]\[CNST_SERIALTYPE_CANCEL_SERIAL_NO\]\[@serial_no_x\]
hs_snprintf(@[标准字段], 11, "%02d%08d", @partition_no, @serial_no_x);
```

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
- **适用类型**: 函数,服务,原子函数

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
- **适用类型**: 函数,服务,原子服务,原子函数

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

### 错误信息重置

- **参数**: `[原始错误号][原始错误信息][错误类型][重置错误信息][冲销流水号]`
- **适用类型**: 函数,原子函数

```
// 用于远程调用错误回冲时处理错误信息
hs_snprintf(@error_info, sizeof(@error_info), "%s | %s：%d-%s %s\r\n", @[原始错误信息], [错误类型],
lpIUFTContext->nErrorNo, [重置错误信息], @[冲销流水号]);
lpIUFTContext->nErrorNo = @[原始错误号];
lpIUFTContext->GetErrorFormat()->Format(ERR_SECUUFT_USER_DEFINE_ERROR, @error_info);
hs_strncpy(@[原始错误信息], lpIUFTContext->GetErrorFormat()->GetUTF8Message(), sizeof(@[原始错误信息])-1);
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

### 错误信息重置

- **参数**: `[原始错误号][原始错误信息][错误类型][重置错误信息][冲销流水号]`
- **适用类型**: 函数,原子函数

```
// 用于远程调用错误回冲时处理错误信息
hs_snprintf(@error_info, sizeof(@error_info), "%s | %s：%d-%s %s\r\n", @[原始错误信息], [错误类型],
lpIUFTContext->nErrorNo, [重置错误信息], @[冲销流水号]);
lpIUFTContext->nErrorNo = @[原始错误号];
lpIUFTContext->GetErrorFormat()->Format(ERR_SECUUFT_USER_DEFINE_ERROR, @error_info);
hs_strncpy(@[原始错误信息], lpIUFTContext->GetErrorFormat()->GetUTF8Message(), sizeof(@[原始错误信息])-1);
```

### 直接返回

- **适用类型**: 函数,原子函数

```
goto svr_end;
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
iRaiseError = 1;
lpIUFTContext->nErrorNo =  [错误号];
lpIUFTContext->GetErrorFormat()->Format([错误号], [参数信息]);
lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
goto svr_end;
```

### 重置参数错误信息

- **参数**: `[错误号][错误信息1][错误信息2]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->nErrorNo = [错误号];
lpIUFTContext->GetErrorFormat()->SetMultiByteFormattedMessage(0, IMsgFormat::$encode_type, @[错误信息1],@[错误信息2]);
```

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
- **适用类型**: 函数,原子函数

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
- **适用类型**: 函数,原子函数

```
\[报错返回\]\[[错误号]\]\[{[参数列表]}\]
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
   @error_no   = ERR_EXEC_BUSIPACK_ISNULL;
   hs_snprintf(@error_info,CNST_ERRORINFO_LEN,  "%s","解包错误（无法获取解包器）");
   goto svr_end;
}
lpIUFTContext->nErrorNo = [解包器]->Open([clob字段],[clob长度]);
if ( lpIUFTContext->nErrorNo != 0)
{  
   @error_no   = ERR_EXEC_BUSIPACK_ISNULL;
   hs_snprintf(@error_info,CNST_ERRORINFO_LEN,  "%s","解包错误（无法获取解包器）");
   goto svr_end;
}
else if (  [解包器]->GetColCount() < 0)
{   
   @error_no   =  ERR_PACKRESULE_ISNULL;
   hs_snprintf(@error_info,CNST_ERRORINFO_LEN,  "%s","解包错误（行列不匹配）");
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
\[获取序列号\]\[CNST_SERIALTYPE_CANCEL_SERIAL_NO\]\[@serial_no_x\]
hs_snprintf(@[标准字段], 11, "%02d%08d", @partition_no, @serial_no_x);
```

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
- **适用类型**: 函数,服务,原子函数

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
- **适用类型**: 函数,服务,原子服务,原子函数

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

### 错误信息重置

- **参数**: `[原始错误号][原始错误信息][错误类型][重置错误信息][冲销流水号]`
- **适用类型**: 函数,原子函数

```
// 用于远程调用错误回冲时处理错误信息
hs_snprintf(@error_info, sizeof(@error_info), "%s | %s：%d-%s %s\r\n", @[原始错误信息], [错误类型],
lpIUFTContext->nErrorNo, [重置错误信息], @[冲销流水号]);
lpIUFTContext->nErrorNo = @[原始错误号];
lpIUFTContext->GetErrorFormat()->Format(ERR_SECUUFT_USER_DEFINE_ERROR, @error_info);
hs_strncpy(@[原始错误信息], lpIUFTContext->GetErrorFormat()->GetUTF8Message(), sizeof(@[原始错误信息])-1);
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

### 错误信息重置

- **参数**: `[原始错误号][原始错误信息][错误类型][重置错误信息][冲销流水号]`
- **适用类型**: 函数,原子函数

```
// 用于远程调用错误回冲时处理错误信息
hs_snprintf(@error_info, sizeof(@error_info), "%s | %s：%d-%s %s\r\n", @[原始错误信息], [错误类型],
lpIUFTContext->nErrorNo, [重置错误信息], @[冲销流水号]);
lpIUFTContext->nErrorNo = @[原始错误号];
lpIUFTContext->GetErrorFormat()->Format(ERR_SECUUFT_USER_DEFINE_ERROR, @error_info);
hs_strncpy(@[原始错误信息], lpIUFTContext->GetErrorFormat()->GetUTF8Message(), sizeof(@[原始错误信息])-1);
```

### 直接返回

- **适用类型**: 函数,原子函数

```
goto svr_end;
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
iRaiseError = 1;
lpIUFTContext->nErrorNo =  [错误号];
lpIUFTContext->GetErrorFormat()->Format([错误号], [参数信息]);
lpIUFTContext->SetErrorFileFuncInfo(__FILE__, __LINE__, __func__);
goto svr_end;
```

### 重置参数错误信息

- **参数**: `[错误号][错误信息1][错误信息2]`
- **适用类型**: 函数,服务,原子服务,原子函数

```
lpIUFTContext->nErrorNo = [错误号];
lpIUFTContext->GetErrorFormat()->SetMultiByteFormattedMessage(0, IMsgFormat::$encode_type, @[错误信息1],@[错误信息2]);
```

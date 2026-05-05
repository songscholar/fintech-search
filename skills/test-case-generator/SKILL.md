---
name: test-case-generator
description: 根据测试用例文档生成XML格式的测试用例。当用户要求生成测试用例、生成XML测试用例、根据功能号或接口名生成测试用例时使用。支持按功能号(如250294)、接口名称(如ETF申购、可转债转股)或业务类型检索。
---

# 测试用例生成器

根据测试用例文档生成标准XML格式的测试用例。

## 测试用例存储位置

测试用例存储在 `./test-cases/` 目录，每个接口一个 `.md` 文件。
文件命名格式：`{功能号}_{序号}.md`

## 使用方式

用户可以通过以下方式触发：
- "帮我生成功能号250294的测试用例"
- "生成可转债转股接口的测试用例"
- "帮我生成ETF申购的测试用例XML"
- "根据功能号339800生成测试用例"

## 工作流程

### 1. 检索测试用例

根据用户输入的关键词，使用以下方式查找：

**按功能号查找**：
```bash
grep -l "250294" ./test-cases/*.md
```

**按关键词查找**：
```bash
grep -l "可转债" ./test-cases/*.md
```

### 2. 读取测试用例文件

使用 `read` 工具读取匹配的文件内容，提取：
- 功能号（`**功能号**: xxx`）
- 接口描述（`**接口描述**: xxx`）
- 参数值列表

### 3. 生成XML输出

按照以下格式生成：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TEST_PACK node="">
    <Test>
        <sub id="{功能号}" block="1" livetime="5000" pri="8" pack_ver="1" note="{接口描述}" msg_cntr="0">
			<route esb_name="" esb_no="" neighbor="" plugin="" system="" sub_system="" branch=""/>
			<inparams>
				<in name="{参数名}" value="{参数值}"/>
				...
			</inparams>
		</sub>
    </Test>
</TEST_PACK>
```

## 生成规则

1. `id` 取自测试用例的功能号
2. `note` 取自接口描述
3. `<inparams>` 内容取自示例中的参数值
4. 每个参数生成一个 `<in name="xxx" value="yyy"/>` 标签
5. 固定属性 `block="1" livetime="5000" pri="8" pack_ver="1" msg_cntr="0"` 不需要修改
6. `<route>` 标签属性保持为空
7. **重要**：如果参数值为 `None`，必须替换为空字符串 `""`

## 示例

**用户输入**：帮我生成功能号250294的测试用例

**处理步骤**：
1. 执行 `grep -l "功能号: 250294" /root/.openclaw/workspace/memory/test-cases/*.md` 找到文件
2. 读取文件内容
3. 提取功能号、接口描述、参数值
4. 生成XML

**输出**：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<TEST_PACK node="">
    <Test>
        <sub id="250294" block="1" livetime="5000" pri="8" pack_ver="1" note="LS_证券交易_可转债转股(回售)委托_t2" msg_cntr="0">
			<route esb_name="" esb_no="" neighbor="" plugin="" system="" sub_system="" branch=""/>
			<inparams>
				<in name="op_password" value="1"/>
				<in name="op_entrust_way" value="4"/>
				<in name="entrust_prop" value="vard_entrust_prop"/>
				<in name="entrust_bs" value="2"/>
				<in name="entrust_price" value="vard_entrust_price"/>
				<in name="op_branch_no" value="vard_op_branch_no"/>
				<in name="batch_no" value="0"/>
				<in name="audit_action" value="0"/>
				<in name="fund_account" value="vard_fund_account"/>
				<in name="operator_no" value="8888"/>
				<in name="exchange_type" value="9"/>
				<in name="stock_account" value="vard_stock_account"/>
				<in name="entrust_amount" value="vard_entrust_amount"/>
				<in name="op_station" value="vard_op_station"/>
				<in name="user_type" value="1"/>
				<in name="branch_no" value="vard_branch_no"/>
				<in name="op_remark" value=""/>
				<in name="function_id" value="250294"/>
				<in name="stock_code" value="vard_stock_code"/>
				<in name="menu_id" value="303322"/>
				<in name="stb_stock_property" value="00"/>
				<in name="entrust_type" value="0"/>
			</inparams>
		</sub>
    </Test>
</TEST_PACK>
```

## 多个匹配结果的处理

如果检索到多个匹配的测试用例：
1. 列出所有匹配项供用户选择
2. 或者默认使用第一个匹配项

## 注意事项

- XML格式必须严格按要求生成，不要修改固定属性
- 参数名和参数值直接从测试用例文件中提取
- 如果用户指定某个示例，使用指定的示例参数值
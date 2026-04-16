---
name: uses-codebase-multi-index
description: Use when answering complex questions about the USES/UFT codebase that require querying multiple indexes (code, metadata, table structures). This skill enables multi-turn orchestration where the LLM can first query code, then discover and query related metadata and table information as needed.
---

# USES Codebase Multi-Index Query Skill

Use this skill for complex questions about the USES/UFT codebase that require information from multiple sources.

## Default Index Paths

- **Code Index**: `/Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_index.db`
- **Metadata Index**: `/Users/songzuoqiang/Documents/agent/condex/codes/examples/business_code_metadata_index.db`
- **Table Structure Index**: `/Users/songzuoqiang/Documents/agent/condex/codes/examples/business_table_index.db`

## Available Tools

### 1. `answer_codebase`
Use this first to get the initial code answer.

**Parameters**:
- `db_path`: Code index database path (optional, uses default)
- `question`: The user's question
- `evidence_limit`: Number of evidence blocks (default: 6)
- `context_window`: Context window size (default: 2)
- `related_limit`: Related items limit (default: 3)

### 2. `query_metadata`
Use this when you discover constants, configs, or error numbers that need explanation.

**Parameters**:
- `db_path`: Metadata index database path (optional, uses default)
- `query`: Keyword to search (e.g., "3674", "ERR_SECU", "CNST_FUNCID")
- `limit`: Maximum hits (default: 10)

### 3. `query_table`
Use this when you discover table names that need structure information.

**Parameters**:
- `db_path`: Table index database path (optional, uses default)
- `query`: Table name to search (e.g., "usps_stkcode", "uses_xxx")
- `limit`: Maximum hits (default: 10)

## Multi-Turn Workflow

### Step 1: Query Code First
Always start with `answer_codebase` to understand the code implementation.

### Step 2: Analyze the Result
From the code answer, identify:
- **Configuration switches**: Names starting with char_config_, int_config_, str_config_, etc. (e.g., "str_config_3588", "int_config_1234", "char_config_5678")
- **Table names**: Names starting with uses_, usps_, uact_, stb_, ufx_, udp_, etc.
- **Table operations**: Statements with pattern `[宏定义][表名字/sql语句][执行结果]` (e.g., `[查询表][uses_stkcode][查询成功]`)
- **Constant names**: Names starting with CNST_, ERR_, etc.
- **Error reports**: Statements with pattern `[业务报错返回][ERR_xxx]` (e.g., `[业务报错返回][ERR_USER_TABLERECORD_NOTEXISTS]`)

### Step 3: Query Metadata
If you found configuration switches or constants:
- Use `query_metadata` with the switch/constant name
- Extract: Chinese name, description, possible values

### Step 4: Query Table Structure
If you found table names:
- Use `query_table` with the table name
- Extract: Fields, indexes, Chinese name

### Step 5: Repeat as Needed
Continue querying until you have sufficient information.

### Step 6: Provide Final Answer
Integrate all information from:
- Code logic and implementation
- Configuration explanations
- Table structure details
- Constant/error definitions

## Example Workflow

**User Question**: "333002这个功能是怎么处理资金的？"

**Turn 1**:
```
Tool: answer_codebase
Question: "333002这个功能是怎么处理资金的？"
```

**Analyze Result**: Discover table "usps_stkcode" and config "3674" in the code.

**Turn 2**:
```
Tool: query_metadata
Query: "3674"
```

**Turn 3**:
```
Tool: query_table
Query: "usps_stkcode"
```

**Turn 4**:
```
Final Answer: Integrate all information...
```

## Response Guidelines

1. **Always use the tools** when you need more information
2. **Don't guess** - if you see a table name or config, query it
3. **Be thorough** - query everything that seems relevant
4. **Cite sources** - mention which tool provided which information
5. **Structure clearly** - organize the final answer logically

## When to Use Which Tool

| Need | Tool |
|------|------|
| Code implementation | answer_codebase |
| Constant/config explanation | query_metadata |
| Error number explanation | query_metadata |
| Table structure | query_table |

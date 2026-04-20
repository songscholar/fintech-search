from __future__ import annotations

import re


READ_ACTIONS = {"获取记录", "获取字段", "遍历记录开始", "遍历记录池开始", "记录为空", "记录不为空"}
WRITE_ACTIONS = {"插入记录", "修改记录", "清空记录池", "数据回库"}
COMPONENT_ACTIONS = {"获取组件", "插入组件", "尾部插入组件", "遍历组件开始", "遍历组件结束", "组件大小"}

VECTOR_SIMILARITY_THRESHOLD = 0.05
RESPONSE_SCHEMA_VERSION = "1.0"
DEFAULT_TOP_K = (1, 3, 5, 10)
TRACE_SCHEMA_VERSION = "1.0"
TRACE_PRODUCER = "uses_indexer"

JSON_RPC_VERSION = "2.0"
MCP_PROTOCOL_VERSION = "2025-11-25"
EXIT_LABEL_NAMES = {"svr_end"}

TABLE_TOKEN_PREFIXES = ("uses_", "reload_", "upbs_", "usps_", "uact_", "stb_", "ufx_", "udp_")
TABLE_INTENT_KEYWORDS = ("表", "sql", "数据库", "查询", "读取", "select", "from", "join", "update", "delete", "insert", "merge")
WRITE_INTENT_KEYWORDS = ("更新", "修改", "删除", "清空", "写入", "update", "delete", "insert", "merge")
READ_INTENT_KEYWORDS = ("查询", "读取", "获取", "select", "from", "join")
VARIABLE_INTENT_KEYWORDS = ("变量", "赋值", "写入", "读取", "参数", "字段")
CALL_CHAIN_INTENT_KEYWORDS = ("调用链", "被谁调用", "谁调用", "调用", "链路", "上游", "下游")
FAILURE_INTENT_KEYWORDS = ("失败", "报错", "异常", "exception", "when_others", "goto", "svr_end", "退出", "错误")
PROCEDURE_INTENT_KEYWORDS = ("过程", "函数", "服务", "接口", "原子", "方法")
METADATA_INTENT_KEYWORDS = ("metadata", "元数据", "字典", "常量", "错误码", "topic别名", "topic", "组件", "内存表")
TOPIC_INTENT_KEYWORDS = ("topic", "消息", "发布", "mc", "消息中心", "主题")
SQL_WRITE_HINTS = (" update ", " delete ", " insert ", " merge ", "writes_table", "清空记录池", "修改记录", "插入记录")
SQL_READ_HINTS = (" select ", " from ", " join ", "reads_table", "获取记录", "获取字段")
FAILURE_MATCH_HINTS = ("失败", "报错", "异常", "exception", "when_others", "svr_end", "goto", "处理失败", "业务报错返回")
GENERIC_QUERY_TERMS = {
    "逻辑",
    "代码",
    "流程",
    "实现",
    "位置",
    "地方",
    "相关",
    "问题",
    "功能",
    "模块",
    "方法",
}
FOCUS_EXCLUDED_QUERY_TERMS = frozenset(
    {
        *GENERIC_QUERY_TERMS,
        "过程",
        "函数",
        "服务",
        "接口",
        "原子",
        "调用",
        "调用链",
        "被谁调用",
        "谁调用",
        "上游",
        "下游",
        "读取",
        "查询",
        "获取",
        "更新",
        "修改",
        "删除",
        "写入",
        "变量",
        "赋值",
        "参数",
        "字段",
        "表",
        "数据库",
        "sql",
        "failure",
        "error",
    }
)
QUERY_TOKEN_RE = re.compile(r"[\u4e00-\u9fff]+|[A-Za-z0-9_]+")
QUERY_PROCEDURE_RE = re.compile(r"\b(?:AF|LF|LS|RS|AS)_[A-Za-z0-9_]+\b")
QUERY_VARIABLE_RE = re.compile(r"@[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?")
CHINESE_QUERY_SPLIT_RE = re.compile(r"(?:被谁调用|谁调用|在哪里|在哪儿|哪里|哪些|哪个|谁|什么|如何|怎么|是否|能否|可以|请问|一下|调用|流程|的|了|在|是|和|与|及|或|并|把|将|从|到|为|对|按|里)")
TABLE_WITH_INDEX_RE = re.compile(r"^(?P<table>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<index>[^)]+)\)$")

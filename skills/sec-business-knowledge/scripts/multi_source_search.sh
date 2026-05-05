#!/bin/bash
# Multi-source search for securities business knowledge
# Usage: ./multi_source_search.sh <keyword> [business_type]
#
# Example:
#   ./multi_source_search.sh "新股申购" "股票"
#   ./multi_source_search.sh "ETF申赎" "基金"

set -e

KEYWORD="$1"
BUSINESS_TYPE="${2:-}"
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
KNOWLEDGE_DIR="/home/ubuntu/business_file"

if [ -z "$KEYWORD" ]; then
    echo "Usage: $0 <keyword> [business_type]" >&2
    exit 1
fi

echo "========================================"
echo "证券业务知识库 - 多来源综合查询"
echo "关键词: $KEYWORD"
echo "========================================"
echo ""

# ============================================
# 来源1：本地业务文档
# ============================================
echo "【来源1】本地业务文档"
echo "---"

# 搜索文件名匹配
echo "📄 匹配的文档："
ls "$KNOWLEDGE_DIR" 2>/dev/null | grep -i "$KEYWORD" | head -10 || echo "  （无匹配）"
echo ""

# 搜索文档内容（通过文件名推断）
echo "📋 相关业务文档："
case "$KEYWORD" in
    *申购*|*新股*|*打新*)
        echo "  - UF3.0_证券交易_新股&新债申购业务流程说明.docx"
        ;;
    *ETF*|*申赎*)
        echo "  - UF3.0_证券交易_ETF业务设计说明.docx"
        ;;
    *港股通*|*港股*)
        echo "  - UF3.0_证券交易_港股通业务设计说明.docx"
        ;;
    *科创*|*科创板*)
        echo "  - UF3.0_证券交易_科创板业务设计说明.docx"
        ;;
    *创业板*)
        echo "  - UF3.0_证券交易_科创板业务设计说明.docx（参考）"
        ;;
    *可转债*|*可交债*)
        echo "  - UF3.0_证券交易_可转&可交债业务设计说明.docx"
        ;;
    *大宗*)
        echo "  - UF3.0_证券交易_大宗交易业务说明.docx"
        ;;
    *融资融券*|*融资*|*融券*)
        echo "  - UF3.0_证券交易_融资行权业务设计说明.docx"
        ;;
    *质押*|*回购*)
        echo "  - UF3.0_证券交易_股票质押式回购业务设计说明.docx"
        echo "  - UF3.0_证券交易_质押回购业务设计说明.docx"
        echo "  - UF3.0_证券交易_报价回购业务设计说明.docx"
        ;;
    *三板*|*股转*|*新三板*)
        echo "  - UF3.0_证券交易_股转交易业务设计说明.docx"
        ;;
    *债券*)
        echo "  - UF3.0_证券交易_上海债券现券业务设计说明.docx"
        echo "  - UF3.0_证券交易_深圳债券现券业务设计说明.docx"
        ;;
    *分红*|*股息*)
        echo "  - UF3.0_证券交易_股息红利差异化扣税业务设计说明.docx"
        ;;
    *)
        echo "  请使用 search_knowledge.sh 进行详细搜索"
        ;;
esac
echo ""

# ============================================
# 来源2：交易所官方文档
# ============================================
echo "【来源2】交易所官方文档"
echo "---"

# 根据关键词推荐交易所
case "$KEYWORD" in
    *科创*|*上证*|*沪市*)
        echo "🏢 上海证券交易所 (sse.com.cn)"
        echo "  规则页面: https://www.sse.com.cn/lawandrules/"
        echo "  搜索命令: web_search \"site:sse.com.cn $KEYWORD 规则\""
        ;;
    *创业*|*深证*|*深市*)
        echo "🏢 深圳证券交易所 (szse.cn)"
        echo "  规则页面: https://www.szse.cn/lawrules/"
        echo "  搜索命令: web_search \"site:szse.cn $KEYWORD 规则\""
        ;;
    *北交所*|*新三板*|*三板*)
        echo "🏢 北京证券交易所 (bse.cn)"
        echo "  规则页面: https://www.bse.cn/nq/business_rules.html"
        echo "  搜索命令: web_search \"site:bse.cn $KEYWORD 规则\""
        ;;
    *结算*|*登记*|*账户*)
        echo "🏢 中国证券登记结算有限公司 (chinaclear.cn)"
        echo "  规则页面: http://www.chinaclear.cn/zdjs/ggfzyw/home.shtml"
        echo "  搜索命令: web_search \"site:chinaclear.cn $KEYWORD\""
        ;;
    *)
        echo "🏢 推荐查询："
        echo "  上海证券交易所: web_search \"site:sse.com.cn $KEYWORD\""
        echo "  深圳证券交易所: web_search \"site:szse.cn $KEYWORD\""
        echo "  中国结算: web_search \"site:chinaclear.cn $KEYWORD\""
        ;;
esac
echo ""

# ============================================
# 来源3：权威网站
# ============================================
echo "【来源3】权威网站"
echo "---"

echo "🏛️ 监管机构："
echo "  证监会: web_search \"site:csrc.gov.cn $KEYWORD\""
echo "  证券业协会: web_search \"site:sac.net.cn $KEYWORD\""
echo ""

# ============================================
# 来源4：网络检索
# ============================================
echo "【来源4】网络检索"
echo "---"

echo "🔍 通用搜索："
echo "  web_search \"$KEYWORD 证券业务\""
echo "  web_search \"$KEYWORD 业务流程\""
echo ""

# ============================================
# 查询建议
# ============================================
echo "========================================"
echo "📌 查询建议"
echo "========================================"
echo ""
echo "1. 优先查看本地文档获取详细流程"
echo "2. 访问交易所官网确认最新规则"
echo "3. 综合多个来源给出完整答案"
echo ""
echo "执行示例："
echo "  # 提取本地文档"
echo "  ~/.openclaw/workspace/skills/sec-business-knowledge/scripts/extract_docx.sh \"文档路径\""
echo ""
echo "  # 查询交易所官网"
echo "  web_fetch \"https://www.sse.com.cn/lawandrules/\""
echo ""
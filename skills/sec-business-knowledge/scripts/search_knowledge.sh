#!/bin/bash
# Search across all knowledge documents
# Usage: ./search_knowledge.sh <keyword>

set -e

KEYWORD="$1"
KNOWLEDGE_DIR="/home/ubuntu/business_file"

if [ -z "$KEYWORD" ]; then
    echo "Usage: $0 <keyword>" >&2
    exit 1
fi

echo "=== 搜索文件名匹配 ==="
ls "$KNOWLEDGE_DIR" 2>/dev/null | grep -i "$KEYWORD" || echo "无匹配"

echo ""
echo "=== 搜索 Markdown 文件内容 ==="
find "$KNOWLEDGE_DIR" -name "*.md" -type f 2>/dev/null | while read -r f; do
    if grep -l -i "$KEYWORD" "$f" 2>/dev/null; then
        echo "--- $f ---"
        grep -i "$KEYWORD" "$f" -A 3 -B 3 2>/dev/null | head -20
        echo ""
    fi
done

echo ""
echo "=== 搜索 Word 文档 ==="
# Get script directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

find "$KNOWLEDGE_DIR" -name "*.docx" -o -name "*.doc" 2>/dev/null | while read -r f; do
    if "$SCRIPT_DIR/extract_docx.sh" "$f" 2>/dev/null | grep -q -i "$KEYWORD"; then
        echo "匹配: $(basename "$f")"
    fi
done
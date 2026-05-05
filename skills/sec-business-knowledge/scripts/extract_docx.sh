#!/bin/bash
# Extract text from docx files for searching
# Usage: ./extract_docx.sh <file.docx>

set -e

DOCX_FILE="$1"

if [ -z "$DOCX_FILE" ]; then
    echo "Usage: $0 <file.docx>" >&2
    exit 1
fi

if [ ! -f "$DOCX_FILE" ]; then
    echo "Error: File not found: $DOCX_FILE" >&2
    exit 1
fi

# Try multiple methods for extraction
# Method 1: pandoc (preferred)
if command -v pandoc &> /dev/null; then
    pandoc -f docx -t plain "$DOCX_FILE" 2>/dev/null
    exit 0
fi

# Method 2: unzip + xmllint (parse document.xml)
if command -v unzip &> /dev/null; then
    TMPDIR=$(mktemp -d)
    trap "rm -rf $TMPDIR" EXIT
    
    unzip -q -o "$DOCX_FILE" -d "$TMPDIR" 2>/dev/null || true
    
    if [ -f "$TMPDIR/word/document.xml" ]; then
        # Extract text between tags
        if command -v xmllint &> /dev/null; then
            xmllint --xpath '//text()' "$TMPDIR/word/document.xml" 2>/dev/null | \
                sed 's/<[^>]*>//g' | \
                tr -s ' \n' ' '
        else
            # Fallback: just strip XML tags with sed
            cat "$TMPDIR/word/document.xml" | \
                sed 's/<[^>]*>//g' | \
                tr -s ' \n' ' '
        fi
    fi
    exit 0
fi

# Method 3: python-docx
if command -v python3 &> /dev/null; then
    python3 -c "
from docx import Document
import sys

try:
    doc = Document('$DOCX_FILE')
    for para in doc.paragraphs:
        print(para.text)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                print(cell.text)
except Exception as e:
    print(f'Error: {e}', file=sys.stderr)
    sys.exit(1)
" 2>/dev/null
    exit 0
fi

echo "Error: No docx extraction tool available. Install pandoc, unzip, or python3-docx." >&2
exit 1
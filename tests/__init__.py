"""Test package marker for intra-test imports."""

import os

# 阻止 bootstrap_env() 加载项目 .env，确保测试使用干净的 embedder 环境
os.environ["USES_INDEXER_ENV_FILE"] = "/dev/null"

# 清除外部 embedding 环境变量
for key in [
    "OPENAI_EMBEDDING_KEY",
    "OPENAI_EMBEDDING_URL",
    "OPENAI_EMBEDDING_NAME",
    "OPENAI_EMBEDDING_DIMENSIONS",
    "OPENAI_EMBEDDING_BATCH_SIZE",
    "OPENAI_EMBEDDING_TIMEOUT",
    "USES_INDEXER_EMBEDDING_API_KEY",
    "USES_INDEXER_EMBEDDING_BASE_URL",
    "USES_INDEXER_EMBEDDING_MODEL",
    "USES_INDEXER_EMBEDDING_DIMENSIONS",
    "USES_INDEXER_EMBEDDING_BATCH_SIZE",
    "USES_INDEXER_EMBEDDING_TIMEOUT",
    "USES_INDEXER_FORCE_LOCAL_EMBEDDER",
]:
    os.environ.pop(key, None)

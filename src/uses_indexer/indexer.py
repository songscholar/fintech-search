from __future__ import annotations

import os
from pathlib import Path

from .constants import (
    COMPONENT_ACTIONS,
    EXIT_LABEL_NAMES,
    READ_ACTIONS,
    WRITE_ACTIONS,
)
from .embeddings import (
    Embedder,
    create_embedder_from_env,
)
from .context_fetch import ContextFetchService
from .db_summary import DbSummaryService
from .evidence import EvidenceService
from .index_build import IndexBuildService
from .index_write import IndexWriteService
from .parser import UftDslParser
from .retrieval import RetrievalService
from .schema import SCHEMA_SQL

class SQLiteIndexer:
    SCHEMA_SQL = SCHEMA_SQL
    READ_ACTIONS = READ_ACTIONS
    WRITE_ACTIONS = WRITE_ACTIONS
    COMPONENT_ACTIONS = COMPONENT_ACTIONS
    EXIT_LABEL_NAMES = EXIT_LABEL_NAMES

    def __init__(
        self,
        parser: UftDslParser | None = None,
        embedder: Embedder | None = None,
    ) -> None:
        self.parser = parser or UftDslParser()
        self.embedder = embedder or create_embedder_from_env()
        self._vector_cache: dict[tuple[str, int, int, str, str], list[dict[str, object]]] = {}
        self._index_build_service = IndexBuildService(self)
        self._retrieval_service = RetrievalService(self)
        self._evidence_service = EvidenceService(self)
        self._context_fetch_service = ContextFetchService(self)
        self._index_write_service = IndexWriteService(self)
        self._db_summary_service = DbSummaryService(self)

    def build_index(
        self,
        source_root: str | Path,
        db_path: str | Path,
        *,
        resume_vectors: bool = False,
        incremental: bool = False,
        index_type: str = "all",
        skip_vectors: bool = False,
        progress: bool = False,
    ) -> dict[str, object]:
        return self._index_build_service.build_index(
            source_root,
            db_path,
            resume_vectors=resume_vectors,
            incremental=incremental,
            index_type=index_type,
            skip_vectors=skip_vectors,
            progress=progress,
        )

    def resume_chunk_vectors(self, source_root: str | Path, db_path: str | Path, index_type: str = "all") -> dict[str, object]:
        return self._index_build_service.resume_chunk_vectors(source_root, db_path, index_type=index_type)

    def summarize_db(self, db_path: str | Path) -> dict[str, object]:
        return self._db_summary_service.summarize_db(db_path)

    def query_index(self, db_path: str | Path, query: str, limit: int = 20, *, debug: bool = False, expand_downstream: bool = False) -> dict[str, object]:
        return self._retrieval_service.query_index(db_path, query, limit=limit, debug=debug, expand_downstream=expand_downstream)

    def assemble_evidence(
        self,
        db_path: str | Path,
        query: str,
        limit: int = 6,
        context_window: int = 2,
        related_limit: int = 3,
        *,
        debug: bool = False,
    ) -> dict[str, object]:
        return self._evidence_service.assemble_evidence(
            db_path,
            query,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
            debug=debug,
        )



from __future__ import annotations


SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

CREATE TABLE IF NOT EXISTS metadata (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS files (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  path TEXT NOT NULL UNIQUE,
  file_name TEXT NOT NULL,
  unit_kind TEXT NOT NULL,
  prefix TEXT NOT NULL,
  name TEXT NOT NULL,
  chinese_name TEXT,
  object_id TEXT,
  code_line_count INTEGER NOT NULL DEFAULT 0,
  attributes_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS procedures (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL UNIQUE,
  name TEXT NOT NULL,
  prefix TEXT NOT NULL,
  unit_kind TEXT NOT NULL,
  chinese_name TEXT,
  object_id TEXT,
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS histories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  seq INTEGER NOT NULL,
  modified_date TEXT,
  version TEXT,
  order_number TEXT,
  modified_by TEXT,
  modified TEXT,
  extra_attributes_json TEXT NOT NULL DEFAULT '{}',
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS params (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  seq INTEGER NOT NULL,
  category TEXT NOT NULL,
  param_id TEXT NOT NULL,
  uuid TEXT,
  param_type TEXT,
  type_name TEXT,
  name TEXT,
  comments TEXT,
  default_value TEXT,
  flags TEXT,
  extra_attributes_json TEXT NOT NULL DEFAULT '{}',
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS statements (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  seq INTEGER NOT NULL,
  kind TEXT NOT NULL,
  line_start INTEGER NOT NULL,
  line_end INTEGER NOT NULL,
  raw TEXT NOT NULL,
  tag TEXT,
  name TEXT,
  condition TEXT,
  target TEXT,
  groups_json TEXT NOT NULL DEFAULT '[]',
  arguments_json TEXT NOT NULL DEFAULT '[]',
  reads_json TEXT NOT NULL DEFAULT '[]',
  writes_json TEXT NOT NULL DEFAULT '[]',
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS actions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  statement_id INTEGER NOT NULL UNIQUE,
  seq INTEGER NOT NULL,
  kind TEXT NOT NULL,
  tag TEXT,
  action_name TEXT,
  target_name TEXT,
  target_kind TEXT,
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE,
  FOREIGN KEY(statement_id) REFERENCES statements(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS variable_refs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  statement_id INTEGER NOT NULL,
  var_name TEXT NOT NULL,
  access_type TEXT NOT NULL,
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE,
  FOREIGN KEY(statement_id) REFERENCES statements(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS edges (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  statement_id INTEGER,
  edge_type TEXT NOT NULL,
  source_name TEXT NOT NULL,
  target_name TEXT NOT NULL,
  target_kind TEXT NOT NULL,
  detail_json TEXT NOT NULL DEFAULT '{}',
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE,
  FOREIGN KEY(statement_id) REFERENCES statements(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS chunks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  seq INTEGER NOT NULL,
  chunk_type TEXT NOT NULL,
  chunk_role TEXT NOT NULL DEFAULT 'general',
  line_start INTEGER NOT NULL,
  line_end INTEGER NOT NULL,
  statement_start_seq INTEGER NOT NULL,
  statement_end_seq INTEGER NOT NULL,
  statement_count INTEGER NOT NULL,
  anchor_kinds_json TEXT NOT NULL DEFAULT '[]',
  action_names_json TEXT NOT NULL DEFAULT '[]',
  target_names_json TEXT NOT NULL DEFAULT '[]',
  variable_names_json TEXT NOT NULL DEFAULT '[]',
  chunk_features_json TEXT NOT NULL DEFAULT '{}',
  embedding_text TEXT NOT NULL DEFAULT '',
  content TEXT NOT NULL,
  summary_text TEXT NOT NULL,
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS chunk_vectors (
  chunk_id INTEGER PRIMARY KEY,
  provider TEXT NOT NULL,
  model TEXT NOT NULL,
  dimension INTEGER NOT NULL,
  vector_json TEXT NOT NULL,
  FOREIGN KEY(chunk_id) REFERENCES chunks(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS blocks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  seq INTEGER NOT NULL,
  block_type TEXT NOT NULL,
  anchor_name TEXT NOT NULL,
  line_start INTEGER NOT NULL,
  line_end INTEGER NOT NULL,
  statement_start_seq INTEGER NOT NULL,
  statement_end_seq INTEGER NOT NULL,
  statement_count INTEGER NOT NULL,
  anchor_statement_id INTEGER,
  summary_text TEXT NOT NULL,
  excerpt TEXT NOT NULL,
  action_names_json TEXT NOT NULL DEFAULT '[]',
  target_names_json TEXT NOT NULL DEFAULT '[]',
  table_names_json TEXT NOT NULL DEFAULT '[]',
  variable_names_json TEXT NOT NULL DEFAULT '[]',
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE,
  FOREIGN KEY(anchor_statement_id) REFERENCES statements(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS procedure_features (
  procedure_id INTEGER PRIMARY KEY,
  file_id INTEGER NOT NULL,
  procedure_name TEXT NOT NULL,
  summary_text TEXT NOT NULL,
  actions_json TEXT NOT NULL DEFAULT '[]',
  outgoing_calls_json TEXT NOT NULL DEFAULT '[]',
  incoming_callers_json TEXT NOT NULL DEFAULT '[]',
  read_tables_json TEXT NOT NULL DEFAULT '[]',
  write_tables_json TEXT NOT NULL DEFAULT '[]',
  mc_topics_json TEXT NOT NULL DEFAULT '[]',
  metadata_refs_json TEXT NOT NULL DEFAULT '[]',
  variable_reads_json TEXT NOT NULL DEFAULT '[]',
  variable_writes_json TEXT NOT NULL DEFAULT '[]',
  feature_flags_json TEXT NOT NULL DEFAULT '{}',
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE,
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS block_edges (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  block_id INTEGER NOT NULL,
  edge_type TEXT NOT NULL,
  target_name TEXT NOT NULL,
  target_kind TEXT NOT NULL,
  detail_json TEXT NOT NULL DEFAULT '{}',
  FOREIGN KEY(block_id) REFERENCES blocks(id) ON DELETE CASCADE
);

CREATE VIRTUAL TABLE IF NOT EXISTS procedures_fts USING fts5(
  name,
  chinese_name,
  object_id,
  path,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS statements_fts USING fts5(
  raw,
  name,
  condition,
  target,
  procedure_name,
  file_path,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS actions_fts USING fts5(
  action_name,
  target_name,
  procedure_name,
  file_path,
  raw,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS edges_fts USING fts5(
  edge_type,
  source_name,
  target_name,
  target_kind,
  procedure_name,
  file_path,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
  chunk_type,
  chunk_role,
  procedure_name,
  file_path,
  summary_text,
  content,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS procedure_features_fts USING fts5(
  procedure_name,
  summary_text,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS blocks_fts USING fts5(
  block_type,
  anchor_name,
  procedure_name,
  file_path,
  summary_text,
  excerpt,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE INDEX IF NOT EXISTS idx_files_prefix ON files(prefix);
CREATE INDEX IF NOT EXISTS idx_files_unit_kind ON files(unit_kind);
CREATE INDEX IF NOT EXISTS idx_procedures_name ON procedures(name);
CREATE INDEX IF NOT EXISTS idx_params_param_id ON params(param_id);
CREATE INDEX IF NOT EXISTS idx_statements_kind ON statements(kind);
CREATE INDEX IF NOT EXISTS idx_statements_name ON statements(name);
CREATE INDEX IF NOT EXISTS idx_actions_action_name ON actions(action_name);
CREATE INDEX IF NOT EXISTS idx_variable_refs_name ON variable_refs(var_name);
CREATE INDEX IF NOT EXISTS idx_edges_target_name ON edges(target_name);
CREATE INDEX IF NOT EXISTS idx_edges_edge_type ON edges(edge_type);
CREATE INDEX IF NOT EXISTS idx_chunks_procedure_seq ON chunks(procedure_id, seq);
CREATE INDEX IF NOT EXISTS idx_chunk_vectors_provider ON chunk_vectors(provider, model);
CREATE INDEX IF NOT EXISTS idx_blocks_procedure_seq ON blocks(procedure_id, seq);
CREATE INDEX IF NOT EXISTS idx_blocks_type ON blocks(block_type);
CREATE INDEX IF NOT EXISTS idx_procedure_features_file_id ON procedure_features(file_id);
CREATE INDEX IF NOT EXISTS idx_block_edges_block ON block_edges(block_id);
CREATE INDEX IF NOT EXISTS idx_block_edges_type ON block_edges(edge_type);
"""

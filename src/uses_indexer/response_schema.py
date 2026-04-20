from __future__ import annotations


RESPONSE_SCHEMA_VERSION = "1.0"


def apply_response_envelope(payload: dict[str, object], *, kind: str) -> dict[str, object]:
    response = dict(payload)
    response["response_schema"] = f"uses_indexer.response.{kind}"
    response["response_version"] = RESPONSE_SCHEMA_VERSION
    response["response_kind"] = kind
    return response

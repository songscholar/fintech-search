from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class QaPolicy:
    evidence_limit: int = 6
    context_window: int = 2
    related_limit: int = 3


@dataclass(frozen=True, slots=True)
class AnswerExecutionPolicy:
    allow_draft_fallback: bool = True


@dataclass(frozen=True, slots=True)
class PromptProfileConfig:
    guidance: str
    max_evidence_blocks: int
    max_context_chars: int


@dataclass(frozen=True, slots=True)
class AnswerStrategyConfig:
    profiles: dict[str, PromptProfileConfig] = field(
        default_factory=lambda: {
            "call_chain": PromptProfileConfig(
                guidance="重点解释调用入口、调用方向、主候选链路和可能的上游/下游过程。",
                max_evidence_blocks=5,
                max_context_chars=10000,
            ),
            "table_sql": PromptProfileConfig(
                guidance="重点解释表访问、读写方向、SQL 语义和关联过程。",
                max_evidence_blocks=6,
                max_context_chars=12000,
            ),
            "default": PromptProfileConfig(
                guidance="先给结论，再给证据和不确定点，避免展开与问题无关的背景。",
                max_evidence_blocks=6,
                max_context_chars=12000,
            ),
        }
    )

    def profile(self, name: str) -> PromptProfileConfig:
        return self.profiles[name]

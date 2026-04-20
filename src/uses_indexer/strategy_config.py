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
    answer_sections: tuple[str, ...] = ("结论", "证据", "推断", "不确定点")


@dataclass(frozen=True, slots=True)
class AnswerStrategyConfig:
    profiles: dict[str, PromptProfileConfig] = field(
        default_factory=lambda: {
            "call_chain": PromptProfileConfig(
                guidance="重点解释调用入口、调用方向、主候选链路和可能的上游/下游过程。",
                max_evidence_blocks=5,
                max_context_chars=10000,
                answer_sections=("结论", "主调用链", "关键证据", "不确定点"),
            ),
            "table_sql": PromptProfileConfig(
                guidance="重点解释表访问、读写方向、SQL 语义和关联过程。",
                max_evidence_blocks=6,
                max_context_chars=12000,
                answer_sections=("结论", "表访问", "关键证据", "不确定点"),
            ),
            "failure_flow": PromptProfileConfig(
                guidance="重点解释失败处理入口、异常块、goto/exit 控制流和报错语句。",
                max_evidence_blocks=5,
                max_context_chars=9000,
                answer_sections=("结论", "失败处理路径", "关键证据", "不确定点"),
            ),
            "variable_flow": PromptProfileConfig(
                guidance="重点解释变量在哪里赋值、读取或透传，以及相关调用链。",
                max_evidence_blocks=5,
                max_context_chars=9000,
                answer_sections=("结论", "变量流向", "关键证据", "不确定点"),
            ),
            "metadata": PromptProfileConfig(
                guidance="重点解释 metadata 定义、映射关系、别名和值域，不展开无关实现。",
                max_evidence_blocks=4,
                max_context_chars=8000,
                answer_sections=("结论", "元数据关系", "关键证据", "不确定点"),
            ),
            "topic": PromptProfileConfig(
                guidance="重点解释 topic 名称、发布方、别名和条件字段。",
                max_evidence_blocks=4,
                max_context_chars=8000,
                answer_sections=("结论", "主题关系", "关键证据", "不确定点"),
            ),
            "procedure_lookup": PromptProfileConfig(
                guidance="重点解释实现位置、主过程和关联候选，不要展开过多背景。",
                max_evidence_blocks=5,
                max_context_chars=9000,
                answer_sections=("结论", "实现位置", "关键证据", "不确定点"),
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

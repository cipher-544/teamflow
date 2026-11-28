import operator
from typing import Annotated, TypedDict, Literal, Optional
from pydantic import BaseModel, Field

# Allowed values
Status = Literal["ok", "missing", "conflict"]
Decision = Literal["refund", "partial_refund", "replace", "reject",
                   "escalate", "ask_info", "ship_missing_item"]


class ToolCall(BaseModel):
    """One call to a simulated tool."""
    tool: str
    args: dict
    ok: bool
    output: Optional[dict] = None
    error: Optional[str] = None
    ms: float = 0


class AgentOutput(BaseModel):
    """What every agent returns."""
    agent: str                      # e.g. "shipping_analyst"
    finding: str                    # one-sentence conclusion
    evidence: list[dict] = Field(default_factory=list)  # tool outputs used
    confidence: float = 0.0         # 0 to 1
    status: Status = "ok"


class Recommendation(BaseModel):
    """Final answer from the resolution reviewer."""
    decision: Decision
    reason: str
    evidence_refs: list[str] = Field(default_factory=list)
    unresolved: list[str] = Field(default_factory=list)
    needs_human: bool = True        # always pending human approval


class CaseState(TypedDict, total=False):
    """Shared state passed between all agents."""
    case_id: str
    complaint: str
    order_id: Optional[str]
    order: Optional[dict]
    # operator.add = parallel agents APPEND instead of overwriting
    outputs: Annotated[list[AgentOutput], operator.add]
    tool_calls: Annotated[list[ToolCall], operator.add]
    errors: Annotated[list[str], operator.add]
    recommendation: Optional[Recommendation]
    verified: Optional[bool]
    mode: str
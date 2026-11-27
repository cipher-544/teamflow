from typing import Literal
from pydantic import BaseModel, Field


class ShippingFindings(BaseModel):
    order_id: str
    delivery_status: Literal["delivered", "in_transit", "lost", "unknown"]
    matches_customer_claim: bool
    evidence: list[str] = Field(default_factory=list)
    issues: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)


class PolicyFindings(BaseModel):
    order_id: str
    refund_allowed: bool
    rule_applied: str
    evidence: list[str] = Field(default_factory=list)
    issues: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)


class OrderFindings(BaseModel):
    order_id: str
    items_ordered: list[str] = Field(default_factory=list)
    order_date: str
    total_amount: float
    evidence: list[str] = Field(default_factory=list)
    issues: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)


class ResolutionRecommendation(BaseModel):
    order_id: str
    resolution: Literal["refund", "replacement", "escalate", "reject"]
    reasoning: str
    supporting_evidence: list[str] = Field(default_factory=list)
    unresolved_conditions: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)


class VerificationResult(BaseModel):
    order_id: str
    approved: bool
    problems_found: list[str] = Field(default_factory=list)
    suggested_resolution: str | None = None
    confidence: float = Field(ge=0.0, le=1.0)
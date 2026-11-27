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
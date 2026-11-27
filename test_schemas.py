from agents.schemas import ShippingFindings

result = ShippingFindings(
    order_id="A123",
    delivery_status="delivered",
    matches_customer_claim=False,
    evidence=["Carrier marked delivered on Nov 20"],
    confidence=0.8,
)
print(result)
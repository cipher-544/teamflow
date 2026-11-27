import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "orders.json"

with open(DATA_FILE, encoding="utf-8") as f:
    ORDERS = json.load(f)


def get_order(order_id: str) -> dict:
    if order_id not in ORDERS:
        return {
            "ok": False,
            "error": {
                "type": "not_found",
                "message": f"Order {order_id} not found",
            },
        }
    return {"ok": True, "data": ORDERS[order_id]}
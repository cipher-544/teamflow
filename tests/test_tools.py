from tools.get_order import get_order


def test_get_order_found():
    result = get_order("ORD-1001")
    assert result["ok"] is True
    assert result["data"]["customer_id"] == "C-501"


def test_get_order_not_found():
    result = get_order("ORD-9999")
    assert result["ok"] is False
    assert result["error"]["type"] == "not_found"
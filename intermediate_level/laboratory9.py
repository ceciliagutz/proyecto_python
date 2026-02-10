from typing import Dict, List


def calculate_order_total(items: List[Dict]) -> float:
    total = 0.0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

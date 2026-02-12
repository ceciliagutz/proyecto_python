import json
from pathlib import Path

ORDERS_FILE = Path(__file__).parent / "orders17.json"

if not ORDERS_FILE.exists():
    ORDERS_FILE.write_text(
        json.dumps([{"id": 1, "name": "Order A"}, {"id": 2, "name": "Order B"}])
    )


def load_orders():
    with open(ORDERS_FILE, "r") as f:
        return json.load(f)


def save_orders(orders):
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=2)


def get_orders():
    return load_orders()


def add_order(name: str):
    orders = load_orders()
    new_id = max([o["id"] for o in orders], default=0) + 1
    new_order = {"id": new_id, "name": name}
    orders.append(new_order)
    save_orders(orders)
    return new_order


def delete_order(order_id: int):
    orders = load_orders()
    new_orders = [o for o in orders if o["id"] != order_id]
    if len(new_orders) == len(orders):
        return False
    save_orders(new_orders)
    return True

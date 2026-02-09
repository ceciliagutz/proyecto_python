from dataclasses import dataclass
from typing import List

from pydantic import BaseModel


# -------Dataclasses---------
@dataclass
class OrderItem:
    name: str
    price: float
    quantity: int

    def total(self) -> float:
        return self.price * self.quantity


@dataclass
class Order:
    items: List[OrderItem]

    def total_price(self) -> float:
        return sum(item.total() for item in self.items)


# -----------input/out---------
class OrderItemIn(BaseModel):
    name: str
    price: float
    quantity: int


class OrderIn(BaseModel):
    items: List[OrderItemIn]


class OrderOut(BaseModel):
    total: float


# ------Conversion logic-----


def convert_to_order(order_in: OrderIn) -> Order:
    items = [
        OrderItem(
            name=item.name,
            price=item.price,
            quantity=item.quantity,
        )
        for item in order_in.items
    ]
    return Order(items=items)


if __name__ == "__main__":
    order_in = OrderIn(
        items=[
            OrderItemIn(name="Laptop", price=12000, quantity=1),
            OrderItemIn(name="Keyboard", price=600, quantity=2),
        ]
    )

    order = convert_to_order(order_in)
    total = order.total_price()
    order_out = OrderOut(total=total)

    print("Orden total:", order_out.total)

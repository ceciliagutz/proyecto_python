# Modulo. Arquitectura Hexagonal (puertos y Adaptadores)
# Caso de uso CreateOrder
from .domain import Order
from .ports import NotificationService, OrderRepository


class CreateOrder:
    def __init__(self, repo: OrderRepository, notifier: NotificationService):
        self.repository = repo
        self.notifier = notifier

    def execute(self, order_id: int, customer_name: str, items: list[dict]):
        order = Order(order_id=order_id, customer_name=customer_name, items=items)
        self.repository.save(order)
        self.notifier.notify(order)
        return order

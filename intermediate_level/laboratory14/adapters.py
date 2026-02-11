# Modulo. Arquitectura Hexagonal (puertos y Adaptadores)
# Implementaciones de repositorio u notificación

from .domain import Order
from .ports import NotificationService, OrderRepository


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.storage = []

    def save(self, order: Order) -> None:
        self.storage.append(order)


class MockNotificationService(NotificationService):
    def notify(self, order: Order) -> None:
        print(f"Notification sent for order{order.order_id}")

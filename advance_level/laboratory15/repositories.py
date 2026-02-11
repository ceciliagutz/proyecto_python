#Modulo. Arquitectura Limpia
#Ports and repositories in memory

from abc import ABC, abstractmethod
from .domain import Order

#Port
class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        pass
#In-memory implementation
class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.storage = []
    def save(self, order: Order) -> None:
        self.storage.append(order)
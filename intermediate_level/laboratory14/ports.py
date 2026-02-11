# Modulo. Arquitectura Hexagonal (puertos y Adaptadores)
# Interfaces / Protocolos

from abc import ABC, abstractmethod

from .domain import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        pass


class NotificationService(ABC):
    @abstractmethod
    def notify(self, order: Order) -> None:
        pass

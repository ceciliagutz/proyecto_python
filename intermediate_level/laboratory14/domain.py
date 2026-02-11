# Entidades y logica de dominio
# Modulo. Arquitectura Hexagonal (puertos y Adaptadores)

from dataclasses import dataclass


@dataclass
class Order:
    order_id: int
    customer_name: str
    items: list[dict]

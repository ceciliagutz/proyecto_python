#Modulo. Arquitectura Limpia
#Entities
from dataclasses import dataclass

@dataclass
class Order:
    order_id: int
    customer_name:str
    items: list[dict]


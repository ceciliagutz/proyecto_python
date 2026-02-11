#Modulo. Arquitectura Limpia
# Use Case
from .domain import Order
from .repositories import OrderRepository
from .presenters import OrderPresenter

class CreateOrder:
    def __init__(self, repo: OrderRepository, presenter: OrderPresenter):
        self.repo = repo
        self.presenter = presenter
    def execute(self, order_id: int, customer_name: str, items: list[dict]) -> dict:
        order = Order(order_id= order_id, customer_name=customer_name, items=items)
        self.repo.save(order)
        return self.presenter.present(order)
    
# Modulo. Arquitectura Hexagonal (puertos y Adaptadores)
# Test_laboratory 14

from intermediate_level.laboratory14.adapters import (
    InMemoryOrderRepository,
    MockNotificationService,
)
from intermediate_level.laboratory14.usecases import CreateOrder


def test_create_order():
    repo = InMemoryOrderRepository()
    notifier = MockNotificationService()
    usecase = CreateOrder(repo, notifier)

    order = usecase.execute(
        order_id=1,
        customer_name="Cecilia",
        items=[{"product": "Album ARIRANG", "quantity": 1}],
    )

    assert order.order_id == 1
    assert order.customer_name == "Cecilia"
    assert repo.storage[0] == order

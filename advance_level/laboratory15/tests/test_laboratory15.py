#Modulo. Arquitectura Limpia
#test Unit

from advance_level.laboratory15.domain import Order
from advance_level.laboratory15.repositories import InMemoryOrderRepository
from advance_level.laboratory15.presenters import OrderPresenter
from advance_level.laboratory15.usecases import CreateOrder

def test_create_order():
    repo = InMemoryOrderRepository()
    presenter = OrderPresenter()
    usecase = CreateOrder(repo, presenter)
    result = usecase.execute(
        order_id=1,
        customer_name="Cecilia",
        items=[{"product": "Album ARIRANG", "quantity": 1}]
    )

    #Validations
    assert result["order_id"]==1
    assert result["customer_name"]=="Cecilia"
    assert repo.storage[0].order_id==1
    
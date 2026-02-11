#Modulo. Arquitectura Limpia
#Presentation/ departure


from .domain import Order

class OrderPresenter:
    def present(self, order: Order) -> dict:
        return{
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "items": order.items
        }

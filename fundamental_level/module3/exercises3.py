# MODULO OBJETOS Y MODELOS DE DATOS

from dataclasses import dataclass

# ---Basic class with dunder methods---


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"


# --------------Inheritance------------


class DigitalProduct(Product):
    def __init__(self, name: str, price: float, file_size: float):
        super().__init__(name, price)
        self.file_size = file_size


# ------------Composition-----------


class Order:
    def __init__(self, products: list[Product]):
        self.products = products

    def total_price(self) -> float:
        total: float = 0.0
        for product in self.products:
            total += product.price
        return total


# -----------Dataclass-----------------


@dataclass
class OrderItem:
    name: str
    price: float
    quantity: int

    def total(self) -> float:
        return self.price * self.quantity


# -------Test section----------


if __name__ == "__main__":
    p1 = Product("Laptop", 12000)
    p2 = Product("Keyboard", 600)

    print(p1)
    print(p2)

    dp = DigitalProduct("Ebook", 150, 7)
    print(dp)

    order = Order([p1, p2])
    print("Total order price:", order.total_price())

    item = OrderItem("headphones", 500, 2)
    print("Item total:", item.total())

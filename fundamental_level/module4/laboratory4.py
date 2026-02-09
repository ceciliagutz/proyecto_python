from typing import Literal, Protocol, TypedDict


# TypeDict
class Product(TypedDict):
    name: str
    price: float
    in_stock: bool


def format_product(product: Product) -> str:
    return f"{product['name']} - ${product['price']} (In stock: {product['in_stock']})"


# Literal


def get_discount(level: Literal["none", "silver", "gold"]) -> float:
    if level == "silver":
        return 0.1
    elif level == "gold":
        return 0.2
    return 0.0


# Protocol
class Notifier(Protocol):
    def send(self, message: str) -> str: ...


class EmailNotifier:
    def send(self, message: str) -> str:
        return f"Email sent: {message}"


def notify_user(notifier: Notifier, message: str) -> str:
    return notifier.send(message)


# Test

if __name__ == "__main__":
    product: Product = {"name": "Laptop", "price": 16000, "in_stock": True}
    print(format_product(product))

    print(get_discount("gold"))

    email = EmailNotifier()
    print(notify_user(email, "Your order has been shipped :)"))

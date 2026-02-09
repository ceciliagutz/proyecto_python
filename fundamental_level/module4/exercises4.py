# Modulo. Tipado estátivo opcional y calidad
from typing import Literal, Protocol, TypedDict, Union


# Basic type hints
def add(a: int, b: int) -> int:
    return a + b


# Union types
def to_string(value: Union[int, float, str]) -> str:
    return str(value)


# Literal
def get_status_message(status: Literal["success", "error", "loading"]) -> str:
    if status == "success":
        return "Operation completed"
    elif status == "error":
        return " Something went wrong"
    else:
        return "Please wait"


# TypeDict
class User(TypedDict):
    name: str
    age: int


def describe_user(user: User) -> str:
    return f"Name: {user['name']}, Age: {user['age']}"


# Protocol


class Printable(Protocol):
    def print(self) -> str: ...


class Report:
    def print(self) -> str:
        return "Printing report..."


def process_printable(item: Printable) -> str:
    return item.print()


# Test

if __name__ == "__main__":
    print(add(2, 3))
    print(to_string(11.11))
    print(get_status_message("success"))

    user = {"name": "Cecilia", "age": 22}
    print(describe_user(user))

    report = Report()
    print(process_printable(report))

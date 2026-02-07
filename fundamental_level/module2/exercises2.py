import time
from contextlib import contextmanager

# simple function


def greeting(name):
    print("Hi,", name)


greeting("Cecilia")

# return function


def sum(a, b):
    return a + b


result = sum(7, 8)
print("The result is ", result)

# named arguments


def present(name, age):
    print(f"{name} is {age} years old")


present(age=24, name="Cecilia")

# *args


def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
        return total
    print("Total sum: ", sum_all(2, 8, 5, 1))


# **kwargs


def show_data(**data):
    for key, value in data.items():
        print(key, ":", value)


show_data(name="Cecilia", age=24, city="CDMX")

# Lambda


def square(x):
    return x * x


print("Square of 5:", square(5))

# List comprehension

numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]

print("Squares:", squares)

# Generator


def count_up_to(n):
    counter = 1
    while counter <= n:
        yield counter
        counter += 1


for number in count_up_to(3):
    print("Generator:", number)

# Simple decorator


def greeting_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")

    return wrapper


@greeting_decorator
def say_hi():
    print("Hi")


say_hi()

# Context manager


@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print("Execution time:", end - start)


with timer():
    print("Running something ...")
    time.sleep(1)

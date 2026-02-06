# Variables and types

name = "Cecilia Gutierrez"
age = 24
average = 80
is_programmer = True

print(name)
print(age)
print(average)
print(is_programmer)

# List
numbers = [11, 21, 18]
print(numbers)

# Dict
person = {"name": "Cecilia Gutierrez", "age": 25}
print(person["name"])

# If
age = 17
if age >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# For
for number in numbers:
    print("Number:", number)

# Try-except

try:
    number = int("abc")
    print(number)
except ValueError:
    print("Error: is not a number")


# While

counter = 0
while counter < 3:
    print("Counter:", counter)
    counter += 1

# Pattern matching (match- case)
user_type = "customer"

match user_type:
    case "admin":
        print("Full access")
    case "customer":
        print("Limited access")
    case _:
        print("Unknown access")

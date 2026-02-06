import json

archivo = "fundamental_level/module1/data1.json"

try:
    with open(archivo, "r", encoding="utf-8") as f:
        employees = json.load(f)

    # filter adults

    adults = [e for e in employees if e["age"] >= 18]
    print("Adult employees:\n")
    total_salaries = 0

    for e in adults:
        print(f"{e['name']} - {e['position']} - ${e['salary']}")
        total_salaries += e["salary"]

    # Calculate average salary
    if adults:
        average = total_salaries / len(adults)
        print("\nAverage salary:", average)

except FileNotFoundError:
    print("Error: The file doesn't exist.")

except json.JSONDecodeError:
    print("Error: The file JSON it is poorly formed")

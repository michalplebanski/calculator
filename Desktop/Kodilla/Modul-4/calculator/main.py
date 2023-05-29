from multiprocessing.sharedctypes import Value


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div 
}

def validate(op, a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Błąd! Argumenty powinny być liczbami!")
        exit(1)

    if op not in operations:
        print("Błąd! Zła operacja!")
        exit(1)

    return op, a, b

def get_data():
    op = input("Wybierz działanie: +, -, *, /")
    a = input("Podaj pierwszą liczbę: ")
    b = input("Podaj drugą liczbę: ")

    return op, a, b

def calculator():
    op, a, b = get_data()
    op, a, b = validate(op, a, b)
    operacja = operations[op]
    result = operacja(a, b)
    print(f"Rezultat to {result}")

if __name__ == "__main__":
    calculator()
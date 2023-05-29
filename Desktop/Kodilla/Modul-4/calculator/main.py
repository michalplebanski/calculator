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
import logging

logging.basicConfig(level=logging.DEBUG)

def calculator(action, number1, number2):
    if action == 1:
        logging.debug(f"Dodaję: {number1}, {number2}")
        return number1 + number2
    elif action == 2:
        logging.debug(f"Odejmuję: {number1}, {number2}")
        return number1 - number2
    elif action == 3:
        logging.debug(f"Mnozę: {number1}, {number2}")
        return number1 * number2
    elif action == 4:
        logging.debug(f"Dzielę: {number1}, {number2}")
        return number1 / number2

if __name__ == '__main__':
    logging.debug("Podaj działania, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    action = int(input())
    if action not in [1, 2, 3, 4, 5, 6]:
        logging.debug("Podano złe działanie!")
        exit(1)
    number1 = int(input("Podaj pierwszą liczbę: "))
    number2 = int(input("Podaj drugą liczbę: "))
    result = calculator(action, number1, number2)
    print(result)
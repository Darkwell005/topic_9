print('Программа "Конвертер валют"')

while True:
    print("\nВыберите операцию (0 для выхода):\n"
          "1. Конвертировать рубли в доллары\n"
          "2. Конвертировать доллары в рубли")

    operation: str = input("Введите номер операции: ")
    if not operation.isdigit():
        print("Введите числовое значение (номер операции)")
    elif operation == "0":
        print("До свидания!")
        break
    elif operation not in '12':
        print("Неверный выбор операции. Попробуйте ещё раз.")
        continue

    rate_hint: str = "Введите курс доллара к рублю: "
    quantity_hint: str = "Введите количество рублей: "
    currency_sign: str = "USD"

    if operation == "2":
        rate_hint: str = "Введите курс доллара к рублю: "
        quantity_hint: str = "Введите количество долларов: "
        currency_sign: str = "RUB"

    exchange_rate: float = float(input(rate_hint))
    quantity: float = float(input(quantity_hint))

    print(f"Вы получите {exchange_rate * quantity:05.2f} {currency_sign}")

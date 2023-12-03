while True:
    print('Программа "Конвертер валют"\n')

    print("Выберите операцию (0 для выхода):\n"
          "1. Конвертировать рубли в доллары\n"
          "2. Конвертировать доллары в рубли")
    operation: str = (input("Введите номер операции: "))
    if not operation.isnumeric():
        print("Введите числовое значение (номер операции)")
    elif ((operation != "0")
          and (operation != "1")
          and (operation != "2")):
        print("Неверный выбор операции. Попробуйте ещё раз.")
    elif operation == "0":
        print("До свидания!")
        break
    elif operation == "1":
        exchange_rate = float(input("Введите курс доллара к рублю: "))
        quantity = float(input("Введите количество рублей: "))
        print(f"Вы получите {exchange_rate * quantity:05.2f} USD\n")
    elif operation == "2":
        exchange_rate: float = float(input("Введите курс доллара к рублю: "))
        quantity: float = float(input("Введите количество рублей: "))
        print(f"Вы получите {exchange_rate * quantity:05.2f} RUB\n")

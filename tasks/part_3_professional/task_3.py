discount: int = int(input())
price: list[str] = input().split()

goods: str = "Товар"
price_hint: str = "Цена"
title: str = "Название"
discount_amount_hint: str = "Сумма скидки"
new_price_hint: str = "Новая цена"

if (discount <= 0) or (discount >= 100):
    print("Размер скидки должен "
          "быть больше 0 и не "
          "должен превышать 100")
else:
    print(f"{title:<15} "
          f"{price_hint:<10} "
          f"{discount_amount_hint:<15} "
          f"{new_price_hint:<10}")

    for index, cost in enumerate(price, start=1):
        cost: float = float(cost)
        discount_amount: float = cost * (discount / 100)
        new_price: float = cost - discount_amount

        # Вывод таблицы
        product = f"Товар {index} "
        print(f"{product:<15} "
              f"{cost:<10.2f} "
              f"{discount_amount:<15.2f} "
              f"{new_price:<10.2f}")

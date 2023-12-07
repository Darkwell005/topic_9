discount = int(input())
price = input().split()

commodity = "Товар"
price_hint = "Цена"
title = "Название"
discount_amount_hint = "Сумма скидки"
new_price_hint = "Новая цена"

if (discount <= 0) or (discount >= 100):
    print("Размер скидки должен "
          "быть больше 0 и не "
          "должен превышать 100")
else:
    print(f"{title:<15} "
          f"{price_hint:<10} "
          f"{discount_amount_hint:<15} "
          f"{new_price_hint:<10}")

    product_count = 1
    for item in price:
        num = float(item)
        discount_amount = num * (discount / 100)

        # Вывод таблицы
        print(f"Товар {product_count} "
              f"{discount_amount:.2f} ")

        product_count += 1

age: list = input().split()

children_2years: str = "Дети до 2-х лет"
children: str = "Дети от 3-х до 12 лет"
adult: str = "Взрослые"
pensioner: str = "Пенсионеры"

children_2years_count: int = 0
children_count: int = 0
adults_count: int = 0
pensioner_count: int = 0

price: int = 0
for i in age:
    i = int(i)
    if 0 < i <= 2:
        children_2years_count += 1
    elif 3 <= i <= 12:
        children_count += 1
        price += 1055

    elif i >= 65:
        pensioner_count += 1
        price += 1449
    else:
        adults_count += 1
        price += 2099

print(f"{children_2years:<20}"
      f"{children:<25}"
      f"{adult:<20}"
      f"{pensioner:<20}")

print(f"{children_2years_count:<20}"
      f"{children_count:<25}"
      f"{adults_count:<20}"
      f"{pensioner_count:<20}\n")

print(f"Общая стоимость билетов: {price:,}₽")

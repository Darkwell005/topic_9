ages: list[str] = input(
    "Введите возрасты посетителей через пробел: "
).split()

children_2_years: str = "Дети до 2-х лет"
children: str = "Дети от 3-х до 12 лет"
adult: str = "Взрослые"
pensioner: str = "Пенсионеры"

CHILD_UNTIL_12_YO_PRICE: int = 1055
ADULT_PRICE: int = 2099
SENIOR_PRICE = 1449

children_2_years_count: int = 0
children_count: int = 0
adults_count: int = 0
pensioner_count: int = 0

price: int = 0
for age in ages:
    age = int(age)
    if 0 < age <= 2:
        children_2_years_count += 1
    elif 3 <= age <= 12:
        children_count += 1
        price += CHILD_UNTIL_12_YO_PRICE
    elif 12 < age < 65:
        adults_count += 1
        price += ADULT_PRICE
    elif age >= 65:
        pensioner_count += 1
        price += SENIOR_PRICE

table_template: str = "{:<20}{:<25}{:<20}{:<20}"
print(table_template.format(children_2_years,
                            children,
                            adult,
                            pensioner))
print(table_template.format(children_2_years_count,
                            children_count,
                            adults_count,
                            pensioner_count))

print(f"\nОбщая стоимость билетов: {price:,}₽")

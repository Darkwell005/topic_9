names: list[str] = []
max_name = 0
i = 1
while True:
    full_name: str = input().strip()
    if full_name.lower() == "end":
        break

    last_name, first_name, patronymic = full_name.split()

    result = (f'{i:0>2} | {last_name.title()} '
              f'{first_name[0].upper()}'
              f'.{patronymic[0].upper()}.')

    names.append(result)
    # Добавлять в список номер строки|, ФИО

    i += 1
    if len(last_name) > 0:
        max_name = len(last_name)
        
hint = "ФИО"
print(f"{hint:^{max_name}}")
for name in names:
    print(name)

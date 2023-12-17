names: list[str] = []
last_name_max_len: int = 0
i: int = 1
while True:
    full_name: str = input().strip()
    if full_name.lower() == "end":
        break

    last_name, first_name, patronymic = full_name.split()
    length: int = len(last_name)
    if length > last_name_max_len:
        last_name_max_len = length

    result: str = (f'{i:0>2} | {last_name.title()} '
                   f'{first_name[0].upper()}'
                   f'.{patronymic[0].upper()}.')
    names.append(result)
    i += 1

table_num: str = "№"
table_fio: str = "ФИО"
print(f"{table_num:^3}{table_fio:^{last_name_max_len}}")

for name in names:
    print(name)

# Option 2
# print(*names, sep='\n')

# Option 3
# res: str = "\n".join(names)
# print(res)

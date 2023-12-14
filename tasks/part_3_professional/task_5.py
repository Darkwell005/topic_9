names: list[str, ...] = []
i = 1
while True:
    full_name: str = input().strip()
    if full_name.lower() == "end":
        break
    else:
        names.append(full_name)
    # Добавлять в список номер строки|, ФИО

    i += 1

print(" № ФИО")
for name in names:
    ...

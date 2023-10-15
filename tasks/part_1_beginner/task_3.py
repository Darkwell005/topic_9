line: str = input()
k = ""

for item in line:
    if item == " ":
        k += item
        print(k)


# Нужна переменная, чтобы определить,
# были ли пробельные символы в начале строки

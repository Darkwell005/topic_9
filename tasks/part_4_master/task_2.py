# Например: 77.88.21.8.
# 77 * 256^3 + 88 * 256^2 +
# 21 * 256^1 + 8 * 256^0 =
# 1297618184.
line: list = input().split(".")
num: int = 256
degree: int = 3

result: int = 0
# TODO: Цикл можно упростить, если избавиться от переменной degree
for item in line:
    item = int(item)
    result += item * (num ** degree)
    degree -= 1
print(result)



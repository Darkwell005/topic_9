line = input()
symbol = input()

line = line.lower()

if symbol in line:
    print(line.count(symbol))
else:
    print(False)

# TODO: Ошибка в следующих тестовых данных
"""
everyTHing yoU Can IMaGine is rEAl
I
False - тут должно быть 4, а не False
"""

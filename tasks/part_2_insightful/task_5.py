user: str = input()

vowels: str = 'aeyuoiAEYIUOауеыоэяиюАУЕЫОЭЯИЮ'
symbol: str = "?" * len(vowels)

# Метод maketrans возвращает словарь
x: dict = user.maketrans(vowels, symbol)
print(user.translate(x).strip())

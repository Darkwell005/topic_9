user: str = input()
vowels: str = 'aeyuoiAEYIUOауеыоэяиюАУЕЫОЭЯИЮ'
symbol: str = "?" * len(vowels)
x = user.maketrans(vowels, symbol)
print(user.translate(x).strip())

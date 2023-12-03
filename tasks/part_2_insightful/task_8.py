names: list = input().split()

vowels: str = "ауеыоэяию"

max_vowels: int = -1
result: list = []

for name in names:
    count_vowels = 0
    for letter in name.lower():
        if letter in vowels:
            count_vowels += 1

    if max_vowels < count_vowels:
        result.clear()
        result.append(name)
        max_vowels = count_vowels
    elif max_vowels == count_vowels:
        result.append(name)

for word in result:
    print(word.capitalize())

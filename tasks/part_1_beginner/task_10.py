ALPHABETS: dict = {
    "vowels": ("aeiouAEIOU"
               "аеиёоуыэюяАЕЁИОУЫЭЮЯ"),
    "consonants": ("bdcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
                   "бвгджзйклмнпрстцфчьжхъщшБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"),
}

word: str = input()

# 1. Здесь лучше использовать счетчик, вместо создания новой строки
set_vowels: str = ""
set_consonants: str = ""

for item in word:
    if item in ALPHABETS["vowels"]:
        set_vowels += item

    # 2. Лишняя проверка if, исправьте пожалуйста на соответствующий оператор
    if item in ALPHABETS["consonants"]:
        set_consonants += item

# 3. Как все исправите, здесь нужно будет вывести только значение счетчиков
print(len(set_vowels), len(set_consonants), sep="\n")

# В целом хорошая работа! Молодцы!

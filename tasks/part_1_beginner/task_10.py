ALPHABETS: dict = {
    "vowels": ("aeiouAEIOU"
               "аеиёоуыэюяАЕЁИОУЫЭЮЯ"),
    "consonants": ("bdcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
                   "бвгджзйклмнпрстцфчьжхъщшБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"),
}

count_vowels: int = 0
count_consonants: int = 0

for item in input():
    if item in ALPHABETS["vowels"]:
        count_vowels += 1

    elif item in ALPHABETS["consonants"]:
        count_consonants += 1

print(count_vowels, count_consonants, sep="\n")

ALPHABETS: dict = {
    "vowels": ("aeiou"
                  "AEIOU"
                  "аеиёоуыэюя"
                  "АЕЁИОУЫЭЮЯ"),
    "consonants": ("bdcdfghjklmnpqrstvwxyz"
                   "BCDFGHJKLMNPQRSTVWXYZ"
                   "бвгджзйклмнпрстцфчьжхъщш"
                   "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"),
}
word: str = input()
set_vowels = ""
set_consonants = ""
for item in word:
    if item in ALPHABETS["vowels"]:
        set_vowels += item
    if item in ALPHABETS["consonants"]:
        set_consonants += item
print(len(set_vowels), len(set_consonants), sep="\n")

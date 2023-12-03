word: str = input()
vowels: str = "АУЕЫОЭЯИЁЮауеыоёэяиюAEUIOaeuio"
count_vowel: int = 0
for item in word:
    if item in vowels:
        count_vowel += 1
attitude: float = count_vowel / (len(word)) * 100
print(f"Отношение гласных: {attitude:05.2f}%")

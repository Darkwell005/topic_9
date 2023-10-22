word: str = input()
symbol: str = input()
for i in range(len(word)):
    if word[-1] == i:
        print(word[i] + symbol)


let: str = input()
word: str = input()
if word not in let:
    print(-1)
else:
    print(let.index(word))

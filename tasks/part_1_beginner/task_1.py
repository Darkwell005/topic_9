word: str = input()

line: str = ""
for char in word:
    # print(id(line))  # каждый раз создается новая строка
    if char not in line:
        line = line + char
print(line)

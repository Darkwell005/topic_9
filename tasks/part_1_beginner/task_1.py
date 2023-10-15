word: str = input()
line = ""
for char in word:
    if char not in line:
        line = line + char
print(line)


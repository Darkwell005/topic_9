word: str = input()
line = ""
for item in word:
    if item > line:
        line = item
print(ord(line), line, sep="\n")

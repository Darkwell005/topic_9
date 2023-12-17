words: list = input().split()
f = ""
for word in words:
    if len(word) >= 5:
        print(word[::-1], end=" ")
words = input().split()
f = ""
for word in words:
    if len(word) >= 5:
        f += word[::-1]
print(f)

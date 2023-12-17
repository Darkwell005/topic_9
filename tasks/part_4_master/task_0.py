words: list = input().split()

for i in range(len(words)):
    if len(words[i]) >= 5:
        words[i] = words[i][::-1]

print(*words)
print(' '.join(words))


# Option 2
# for i, word in enumerate(words):
#     if len(word) >= 5:
#         words[i] = word[::-1]
#
# print(*words)
# print(' '.join(words))

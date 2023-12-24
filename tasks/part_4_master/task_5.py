line = input().strip()
flag = True
for i in line:
    if i.isupper() and flag:
        flag = False
    elif i.isupper():
        line = line.replace(i, "_" + i.lower())

print(line.lower())

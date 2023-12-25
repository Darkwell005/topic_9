line = input().strip()
out_line: str = line[0].lower()
for i in line[1:]:
    if not i.isupper():
        out_line += i
    elif i.isupper():
        out_line += "_" + i

print(out_line.lower())

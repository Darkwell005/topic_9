line: str = input().strip()

out_line: str = line[0].lower()
for i in line[1:]:
    if i.isupper():
        out_line += "_"
    out_line += i

print(out_line.lower())

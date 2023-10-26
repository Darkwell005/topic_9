line: str = input()

out_line: str = ""
is_printed: bool = False

for item in line:
    if is_printed or item != " ":
        is_printed = True
        out_line += item
        print(out_line)

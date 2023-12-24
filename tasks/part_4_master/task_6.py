line: str = input()

flag: bool = True
unique_chars: str = ""
for item in line:
    if item not in unique_chars:
        unique_chars += item
    else:
        flag = False
print(flag)

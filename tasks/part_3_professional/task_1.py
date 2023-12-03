line: str = input()

char_count: int = len(line) + 10  # Количество символов вокруг строки
print(f"{line:~^{char_count}}")

line: str = input().lower()

encrypt: str = ''
step: int = 13
start_alpa: int = 97
end_alpha: int = 122
letters_count: int = 26
for char in line:
    if char.isalpha():
        encrypt += chr(
            end_alpha - (ord(char) - start_alpa + step) % letters_count
        )
    elif char.isspace():
        encrypt += char

print(encrypt)

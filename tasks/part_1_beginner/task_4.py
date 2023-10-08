line: str = input()

zero_char_code = 48
nine_char_code = 57
# Нужна ещё одна переменная, чтобы определить,
# были ли цифровые символы в строке или нет

for char in line:
    if zero_char_code <= ord(char) <= nine_char_code:
        print(char + "₽", end=" ")

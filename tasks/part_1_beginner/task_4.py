line: str = input()

zero_char_code = 48
nine_char_code = 57
is_digit = False

for char in line:
    # Вы ещё не знаете, что это цифровой симвл в строке или нет
    if zero_char_code <= ord(char) <= nine_char_code:
        print(char + "₽", end=" ")
        is_digit = True

# Если флаг не был поднят, тогда выводим False
if not is_digit:  # is_digit != True:
    print(False)

# ----------------------------------

# №2
line: str = input()

digits = '0123456789'
is_digit = False
# И Ваш цикл

"""
A = True
B = False

A or B
A and B
not B
not A

10 if A == True else 20
10 if A else 20"""

numbers = "0123456789"

while True:
    password = input()
    if len(password) < 8:
        print("Пароль должен "
              "быть минимум 8 символов")

    if len(password) > 255:
        print("Пароль не может "
              "быть больше 255 символов")

    if password.isalpha():
        print("Пароль не должен состоять "
              "только из буквенных символов")

    elif password.isdecimal():
        print("Пароль не должен состоять только из цифр")

    # if password.startswith(tuple(numbers)):
    if password[0].isdigit():
        print("Пароль не может начинаться с цифры")

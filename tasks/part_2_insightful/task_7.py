numbers = "0123456789"
while True:
    password = input()
    if len(password) < 8:
        print("Пароль должен "
              "быть минимум 8 символов")

    elif len(password) > 255:
        print("Пароль не может "
              "быть больше 255 символов")

    elif password.isalpha():
        print("Пароль не должен состоять "
              "только из буквенных символов")

    elif password.isdecimal():
        print("Пароль не должен состоять только из цифр")
    else:
        for item in password:
            if item not in numbers:
                break
            else:
                print("Пароль не может начинаться с цифры")

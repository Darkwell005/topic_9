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

    # if password.startswith(tuple(numbers)):
    elif password[0].isdigit():
        print("Пароль не может начинаться с цифры")

    elif not password[-1].isalnum():
        print("Пароль должен заканчиваться буквой или цифрой")

    elif password.isalnum():
        print("ПРЕДУПРЕЖДЕНИЕ: Ваш пароль состоит только из букв и цифр")
        confirmation = input("Хотите добавить специальные символы?(y/N):")
        confirmation = confirmation.lower()

        if confirmation == "n":
            print("\nПароль принят!")
            break

        elif confirmation == "y":
            password = input()
            print("\nПароль принят!")
            break
    else:
        print("\nПароль принят!")
        break

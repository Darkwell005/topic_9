numbers = "0123456789"

while True:
    password = input()
    length = len(password)
    if length < 8:
        print("Пароль должен быть минимум 8 символов")

    elif length > 255:
        print("Пароль не может быть больше 255 символов")

    elif password.isalpha():
        print("Пароль не должен состоять "
              "только из буквенных символов")

    elif password.isdecimal():
        print("Пароль не должен состоять только из цифр")

    elif password[0].isdigit():
        print("Пароль не может начинаться с цифры")

    elif not password[-1].isalnum():
        print("Пароль должен заканчиваться буквой или цифрой")

    elif password.isalnum():
        print("ПРЕДУПРЕЖДЕНИЕ: Ваш пароль состоит только из букв и цифр")
        confirmation = input("Хотите добавить специальные символы?(y/N): ").lower()

        if confirmation == "n":
            print("\nПароль принят!")
            break

        elif confirmation == "y":
            continue

        print("\nПароль принят!")
        break

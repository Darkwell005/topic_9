user_input = input()

if user_input == "":  # 1. Здесь проверку можно улучшить
    print(False)
else:
    print(len(user_input.split()))

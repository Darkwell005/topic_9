line: str = input()

out_line = ""
is_printed = False

for item in line:
    # 1. Вы почти у цели, нужно дописать условие, и задача решена!
    if item != " ":  # 2. Это половина условия, ещё
        # Вы должны проверять состояние флага

        is_printed = True
        out_line += item
        print(out_line)

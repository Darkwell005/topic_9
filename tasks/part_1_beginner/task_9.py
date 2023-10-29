word: str = input()

counter: int = 0
flag: bool = False

for item in word:
    # if not flag and item != " ":
    if flag == False and item != " ":
        flag = True
        counter += 1
    elif item == " " and flag:
        flag = False

print(counter)

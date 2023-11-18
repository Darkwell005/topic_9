line = input()
count_num = 0
count_let = 0
count_space = 0
for i in line:
    if i.isnumeric():
        count_num += 1
    if i.isalpha():
        count_let += 1
    if i.isspace():
        count_space += 1
print(count_let, count_num, count_space, sep="\n")

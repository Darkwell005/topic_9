line = input()
symbol = input()
line = line.lower()
if symbol in line:
    print(line.count(symbol))
else:
    print(False)

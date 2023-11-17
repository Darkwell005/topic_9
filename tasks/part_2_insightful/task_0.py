line = input()
symbol = input()

line = line.lower()
symbol = symbol.lower()
if symbol in line:
    print(line.count(symbol))
else:
    print(False)

# Option 2
res: bool | int = line.count(symbol) if symbol in line else False
print(res)

line: str = input().title()

common: str = line.replace(" ", "")

print("camel" + common)
print("Pascal" + common)

line: list = line.lower().split()
symbol: str = "snake_" + "_".join(line)

print(symbol)

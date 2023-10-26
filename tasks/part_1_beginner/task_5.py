word: str = input()
symbol: str = input()

out_line: str = ""
# if symbol == "":

if not symbol:
    symbol = "-"
length = len(word)
for i in range(length):
    if i != length - 1 and word[i] != symbol:
        out_line += word[i] + symbol
    else:
        out_line += word[i]
print(out_line)

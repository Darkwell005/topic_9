# Например: 77.88.21.8.
# 77 * 256^3 + 88 * 256^2 +
# 21 * 256^1 + 8 * 256^0 =
# 1297618184.

# ---------------------

line: list = input().split(".")
num: int = 256

result: int = 0
for i in range(len(line)):
    result += int(line[3 - i]) * (num ** i)
print(result)

# --------------------- Option 2

bits_32: str = ""
for octet in input().split("."):
    bits_32 += bin(int(octet))[2:].zfill(8)

print(int(bits_32, 2))

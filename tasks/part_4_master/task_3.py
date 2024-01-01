num: int = int(input())
octet = bin(num)[2:].zfill(32)
left: int = 0
octet_list: list[str] = []
for i in range(8, 33, 8):
    octet_list.append(str(int(octet[left:i], 2)))
    left = i
print('.'.join(octet_list))

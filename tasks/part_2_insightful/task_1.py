user_input = input()

if not user_input:
    print(False)
else:
    print(len(user_input.split()))

# Option 2
res: bool | int = len(user_input.split()) if user_input else False
print(res)

# Option 3
if not (line := input()):
    print(False)
else:
    print(len(line.split()))

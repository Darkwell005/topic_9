line = input()
line = line.title()
line = line.replace(" ", "")
print("camel" + line)
print("Pascal" + line)
line = line.lower()
line = line.replace('', "_")
print("snake" + line) # Как решить тут ошибку
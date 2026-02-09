n = int(input('введите число n '))
all_characters = []
for _ in range(n):
    line = input('введите число ')
    all_characters.extend(line)
print(*all_characters)
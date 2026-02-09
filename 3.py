path = input('введите полное имя файла (разделитель 2 косые черты влево) ')
parts = path.split('\\')
for part in parts:
    if part:
        print(part)
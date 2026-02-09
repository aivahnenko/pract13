ip = input('Введите ваш IP-адрес: ')
parts = ip.split('.')
if len(parts) != 4:
    print("НЕТ")
else:
    for part in parts:
        if not (part.isdigit() and 0 <= int(part) <= 255):
            print("НЕТ")
            break
    else:
        print("ДА")
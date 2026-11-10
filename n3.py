total_hours = int(input("Введите общее количество часов: "))
amoebas = 1

for time in range(3, total_hours + 1, 3):
    amoebas *= 2
    print(f"Через {time} часов: {amoebas} амеб")
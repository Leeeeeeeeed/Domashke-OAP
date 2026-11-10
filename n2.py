days = int(input("Введите количество дней (S): "))
distance = 10.0
total_distance = 0.0

for day in range(1, days + 1):
    total_distance += distance
    distance *= 1.1

print(f"Суммарный путь за {days} дней: {total_distance:.2f} км")
import math

x = float(input("Введите длину палки x (м): "))
h = float(input("Введите шаг h для изменения y (м): "))
y = 2.0

while y <= 3.0 + 1e-9:
    if y > x:
        print(f"y={y:.2f}: невозможно (y > x)")
    else:
        alpha_deg = math.degrees(math.acos(y / x))
        print(f"y={y:.2f}: угол alpha = {alpha_deg:.2f} градусов")
    y += h
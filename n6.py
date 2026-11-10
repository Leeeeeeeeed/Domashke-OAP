for b in range(0, 6):
    remainder = 100 - 19 * b
    if remainder % 9 == 0:
        c = remainder // 9
        t = 100 - b - c
        if c >= 0 and t >= 0:
            print(f"Быки: {b}, Коровы: {c}, Телята: {t}")
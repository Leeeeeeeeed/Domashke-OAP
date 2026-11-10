for k in range(0, 17):
    g = 32 - 2 * k
    if g >= 0:
        print(f"Кроликов: {k}, Гусей: {g}, Всего голов: {k + g}")
A = float(input("Введите размер стипендии (A): "))
B = float(input("Введите начальные расходы (B): "))

total_expenses = 0
current_expense = B

for month in range(1, 11):
    total_expenses += current_expense
    current_expense *= 1.03

total_scholarship = A * 10
needed_money = total_expenses - total_scholarship

if needed_money > 0:
    print(f"Нужно попросить у родителей: {needed_money:.2f} руб.")
else:
    print(f"Денег хватит, останется: {abs(needed_money):.2f} руб.")
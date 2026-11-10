def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for x in range(0, 29):
    val = 2 * x**2 + 29
    if is_prime(val):
        print(f"x = {x}: {val} - простое")
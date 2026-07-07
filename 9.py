def steps(x, y):
    d = y - x

    if d == 0:
        return 0

    k = 0

    while (k + 1) * (k + 1) <= d:
        k = k + 1

    if d == k * k:
        return 2 * k - 1

    elif d <= k * k + k:
        return 2 * k

    else:
        return 2 * k + 1


x, y = map(int, input(
    "Введіть початкове та кінцеве числа x і y через пробіл:\n"
).split())

a = steps(x, y)

print("Мінімальна кількість кроків:", a)
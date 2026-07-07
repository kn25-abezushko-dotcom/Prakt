x1, y1, r1, x2, y2, r2 = map(int, input(
    "Введіть шість цілих чисел x1, y1, r1, x2, y2, r2 — координати центрів та радіуси кіл:\n"
).split())

d = (x2 - x1) ** 2 + (y2 - y1) ** 2

if x1 == x2 and y1 == y2 and r1 == r2:
    k = -1

elif d > (r1 + r2) ** 2:
    k = 0

elif d < (r1 - r2) ** 2:
    k = 0

elif d == (r1 + r2) ** 2:
    k = 1

elif d == (r1 - r2) ** 2:
    k = 1

else:
    k = 2

print("Кількість точок перетину:", k)
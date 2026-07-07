n = int(input("Введіть натуральне число n: "))

k = 0

for m in range(1, n + 1):
    if n // m == n % m:
        k = k + 1

print("Кількість рівних дільників числа", n, ":", k)
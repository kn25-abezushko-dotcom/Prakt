n = int(input("Введіть довжину послідовності n: "))

if n == 1:
    k = 2
elif n == 2:
    k = 4
elif n == 3:
    k = 7
else:
    a = 2
    b = 4
    c = 7
    for i in range(4, n + 1):
        k = (a + b + c) % 12345
        a = b
        b = c
        c = k
print("Кількість шуканих послідовностей:", k)
p = int(input("Введіть кількість розрядів: "))

if p == 1:
    print(2)

elif p == 2:
    print(4)

elif 3 <= p <= 30:
    a = 2
    b = 4

    for i in range(3, p + 1):
        c = a + b
        a = b
        b = c

    print(c)

else:
    print("Кількість розрядів повинна бути від 1 до 30")
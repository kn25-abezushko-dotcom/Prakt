x = int(input("Введіть кількість чисел: "))
if 2 <= x <= 20:
    c = []
    print("Введіть натуральні числа")

    while len(c) < x:
        a = int(input())
        c.append(a)
    y = max(c)
    while True:
        z = 0
        for i in c:
            if y%i == 0:
                z = z+1
        if z == x:
            break
        y =y+1
    print("Найменше спільне кратне:", y)
else:
    print("Кількість чисел повинна бути від 2 до 20")
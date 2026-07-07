s = input("Введіть слово: ")

n = len(s)
a = 1

for i in range(1, n + 1):
    a = a * i

p = []

for i in s:
    if i not in p:
        k = s.count(i)
        b = 1

        for j in range(1, k + 1):
            b = b * j

        a = a // b
        p.append(i)

print("Кількість анаграм:", a)
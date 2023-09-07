n = int(input())
a = 0

while a * a <= n:
    if a * a == n:
        print("Корень из", n, "равен", a)
        break
    a += 1
else:
    print("Сложно не могу")

n = input().split()
mas = [int(x) for x in n]
mas_bad = []

for i in range(1, len(mas)):
    if mas[i] - mas[i-1] != 1:
        mas_bad.append(i)

if not mas_bad:
    print("Ничего не найдено")
else:
    print("Разрывы обнаружены на индексах:", mas_bad)



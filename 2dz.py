n = int(input())
mas =[]
mas_bad=[]
a = 0
for i in range(n):
    x = int(input())
    mas.append(x)
for i in range(n-1):
    if mas[a+1]-mas[a] != 1:
        mas_bad.append(a+1)
    a+=1
if not mas_bad:
    print("Ничего не найдено")
else:
    print(mas_bad)




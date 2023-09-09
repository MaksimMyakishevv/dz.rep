def sum():
    n = int(input())
    a = ((3+(n-n%3))*(n//3))/2
    b = ((5+(n-n%5))*(n//5))/2
    c = ((15+(n-n%15))*(n//15))/2
    s = (a+b-c)
    return s
print(sum())
    


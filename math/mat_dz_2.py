a,b = int(input()),int(input())
def evclid(a, b):
    if not (isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0):
        return 0
    while b != 0:
        a, b = b, a % b
    return a
result = evclid(a, b)
print(result)